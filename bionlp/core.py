# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['gen_dna_vocab', 'pred_vs_truth', 'raw2token', 'token2hot', 'hot2token', 'prep_seqs', 'DnaDataset',
           'StepByStep', 'generate_Seqs_Exp_Dataset']

# Cell
from itertools import product
import numpy as np
import torch
import torch.nn.functional as F
import pandas as pd

# Cell
def gen_dna_vocab(frameshift=True, kmer=1, letters='ATCGN'):
    """ Makes a dictionary for mapping a raw sequence
    to one hot encoding
    """
    token_list  = []
    if frameshift:
        letters = 'X' + letters
    for i in [''.join(c) for c in product(letters, repeat=kmer)]:
        if (i[0] == 'X') and (i[kmer-1] == 'X'):
            pass
        else:
            token_list.append(i)

    mapping = {}
    idx = 1
    for letter in token_list:
        if letter not in mapping:
            mapping[letter] = idx
            idx+=1

    return mapping

# Cell
def pred_vs_truth(model,dataloader):
    """
    takes a trained model and runs predictions over the
    given dataloader.

    plots hist of the ground truths vs predictions

        """

    import numpy as np
    import matplotlib.pyplot as plt
    truths = []
    preds =  []
    for i in range(len(dataloader)):
        batch = next(iter(dataloader))
        preds.append(model.predict(batch[0]))
        truths.append(batch[1])

    array_pred = []
    for i in preds:
        for x in i:
            array_pred.append(x)

    flat_preds = np.array(array_pred).flatten()

    truth_pred = []
    for i in truths:
        for x in i:
            truth_pred.append(np.array(x))
    flat_truth = np.array(truth_pred)


    #figures

    x_low = flat_truth.min()*-(1.1*flat_truth.min())

    figure = plt.figure(figsize=(10,5))
    plt.subplot(1, 2, 2)

    plt.hist(flat_truth, bins=20, color = 'blue', label='Truths',alpha=.5,
             range=(flat_truth.min()*-(1.5*flat_truth.min()),flat_truth.max()*1.5))
    plt.hist(flat_preds, bins=20, color = 'red', label='Preds', alpha=.5)
    plt.legend(['Truth','Pred'])


    r2 = round(np.corrcoef(flat_truth,flat_preds)[0][1],2)

    m, b = np. polyfit(flat_truth, flat_preds, 1)# m = slope, b = intercept.


    plt.subplot(1, 2, 1)
    plt.scatter(flat_truth,flat_preds)
    plt.plot(flat_truth, 1*flat_truth, c='blue', linewidth=1 )
    plt.plot(flat_truth, m*flat_truth + b, c = 'red', linewidth = 1)
    plt.xlabel('truth values')
    plt.ylabel('pred values')
    plt.text(flat_truth.min(),flat_truth.max()*1.3, f'R2 = {str(r2)} \n y = {round(m,2)}x + {round(b,2)}', color='red',fontweight='heavy')
    plt.xlim(x_low,flat_truth.max()*1.5)
    plt.ylim(x_low,flat_truth.max()*1.5)

    plt.show()

    return figure

# Cell

def raw2token(seq):
    dna_dict = gen_dna_vocab()
    return [dna_dict[x] for x in seq]

def token2hot(seq, max_length):
    N = max_length - len(seq)
    x = np.pad(seq, (0, N), 'constant')
    x = F.one_hot(torch.tensor(x),num_classes=6)
    return x

def hot2token(seq):
    """ one-hot to tokens

    input:single sequence

    e.g. [[0 0 1 0], [0 0 0 1] , [0 1 0 0]] -> [2 3 1]
    """
    return [np.argmax(i) for i in np.array(seq)]

def prep_seqs(seq, max_length=10):
    """
    takes in a raw seq 'ATTATA' -> one hot encodes to specified max_len
      """
    x = raw2token(seq)
    x = token2hot(x, max_length)
    return x

# Cell
class DnaDataset(torch.utils.data.Dataset):
    """
    takes in dataframe with ['Seqs'] and ['Exp']

    returns pytorch dataset
    """
    def __init__(self, dataframe):
        self.df = dataframe
        self.max_length = self.df.Seqs.map(len).max()
        self.df.Exp.astype(float)


    def __len__(self):
        return len(self.df)

    def __getitem__(self,idx):
        seq = self.df['Seqs'][idx]
        seq = prep_seqs(seq,self.max_length)
        seq = seq.swapaxes(0,1)
        seq = seq.float()

        target = self.df['Exp'][idx]
        target = torch.tensor(target).float()
        #target = torch.tensor(target)

        return seq, target

# Cell
import numpy as np
import datetime
import torch
import matplotlib.pyplot as plt
from torch.utils.tensorboard import SummaryWriter

plt.style.use('fivethirtyeight')

class StepByStep(object):
    def __init__(self, model, loss_fn, optimizer):
        # Here we define the attributes of our class

        # We start by storing the arguments as attributes
        # to use them later
        self.model = model
        self.loss_fn = loss_fn
        self.optimizer = optimizer
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        # Let's send the model to the specified device right away
        self.model.to(self.device)

        # These attributes are defined here, but since they are
        # not informed at the moment of creation, we keep them None
        self.train_loader = None
        self.val_loader = None
        self.writer = None

        # These attributes are going to be computed internally
        self.losses = []
        self.val_losses = []
        self.total_epochs = 0

        #MINE
        self.images = []

        # Creates the train_step function for our model,
        # loss function and optimizer
        # Note: there are NO ARGS there! It makes use of the class
        # attributes directly
        self.train_step = self._make_train_step()
        # Creates the val_step function for our model and loss
        self.val_step = self._make_val_step()

    def to(self, device):
        # This method allows the user to specify a different device
        # It sets the corresponding attribute (to be used later in
        # the mini-batches) and sends the model to the device
        self.device = device
        self.model.to(self.device)

    def set_loaders(self, train_loader, val_loader=None):
        # This method allows the user to define which train_loader (and val_loader, optionally) to use
        # Both loaders are then assigned to attributes of the class
        # So they can be referred to later
        self.train_loader = train_loader
        self.val_loader = val_loader

    def set_tensorboard(self, name, folder='runs'):
        # This method allows the user to define a SummaryWriter to interface with TensorBoard
        suffix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        self.writer = SummaryWriter('{}/{}_{}'.format(folder, name, suffix))

    def _make_train_step(self):
        # This method does not need ARGS... it can refer to
        # the attributes: self.model, self.loss_fn and self.optimizer

        # Builds function that performs a step in the train loop
        def perform_train_step(x, y):
            # Sets model to TRAIN mode
            self.model.train()

            # Step 1 - Computes our model's predicted output - forward pass
            yhat = self.model(x)
            # Step 2 - Computes the loss
            loss = self.loss_fn(yhat, y)
            # Step 3 - Computes gradients for both "a" and "b" parameters
            loss.backward()
            # Step 4 - Updates parameters using gradients and the learning rate
            self.optimizer.step()
            self.optimizer.zero_grad()

            # Returns the loss
            return loss.item()

        # Returns the function that will be called inside the train loop
        return perform_train_step

    def _make_val_step(self):
        # Builds function that performs a step in the validation loop
        def perform_val_step(x, y):
            # Sets model to EVAL mode
            self.model.eval()

            # Step 1 - Computes our model's predicted output - forward pass
            yhat = self.model(x)
            # Step 2 - Computes the loss
            loss = self.loss_fn(yhat, y)
            # There is no need to compute Steps 3 and 4, since we don't update parameters during evaluation
            return loss.item()

        return perform_val_step

    def _mini_batch(self, validation=False):
        # The mini-batch can be used with both loaders
        # The argument `validation`defines which loader and
        # corresponding step function is going to be used
        if validation:
            data_loader = self.val_loader
            step = self.val_step
        else:
            data_loader = self.train_loader
            step = self.train_step

        if data_loader is None:
            return None

        # Once the data loader and step function, this is the same
        # mini-batch loop we had before
        mini_batch_losses = []
        for x_batch, y_batch in data_loader:
            x_batch = x_batch.to(self.device)
            y_batch = y_batch.to(self.device)

            mini_batch_loss = step(x_batch, y_batch)
            mini_batch_losses.append(mini_batch_loss)

        loss = np.mean(mini_batch_losses)
        return loss

    def set_seed(self, seed=42):
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
        torch.manual_seed(seed)
        np.random.seed(seed)

    def train(self, n_epochs, seed=42):
        # To ensure reproducibility of the training process
        self.set_seed(seed)

        for epoch in range(n_epochs):
            # Keeps track of the numbers of epochs
            # by updating the corresponding attribute
            self.total_epochs += 1

            # inner loop
            # Performs training using mini-batches
            loss = self._mini_batch(validation=False)
            self.losses.append(loss)

            # VALIDATION
            # no gradients in validation!
            with torch.no_grad():
                # Performs evaluation using mini-batches
                val_loss = self._mini_batch(validation=True)



                self.val_losses.append(val_loss)

            # If a SummaryWriter has been set...
            if self.writer:
                scalars = {'training': loss}
                if val_loss is not None:
                    scalars.update({'validation': val_loss})
                # Records both losses for each epoch under the main tag "loss"
                self.writer.add_scalars(main_tag='loss',
                                        tag_scalar_dict=scalars,
                                        global_step=epoch)

        if self.writer:
            # Closes the writer
            self.writer.close()

    def save_checkpoint(self, filename):
        # Builds dictionary with all elements for resuming training
        checkpoint = {'epoch': self.total_epochs,
                      'model_state_dict': self.model.state_dict(),
                      'optimizer_state_dict': self.optimizer.state_dict(),
                      'loss': self.losses,
                      'val_loss': self.val_losses}

        torch.save(checkpoint, filename)

    def load_checkpoint(self, filename):
        # Loads dictionary
        checkpoint = torch.load(filename)

        # Restore state for model and optimizer
        self.model.load_state_dict(checkpoint['model_state_dict'])
        self.optimizer.load_state_dict(checkpoint['optimizer_state_dict'])

        self.total_epochs = checkpoint['epoch']
        self.losses = checkpoint['loss']
        self.val_losses = checkpoint['val_loss']

        self.model.train() # always use TRAIN for resuming training

    def predict(self, x):
        # Set is to evaluation mode for predictions
        self.model.eval()
        # Takes aNumpy input and make it a float tensor
        x_tensor = torch.as_tensor(x).float()
        # Send input to device and uses model for prediction
        y_hat_tensor = self.model(x_tensor.to(self.device))
        # Set it back to train mode
        self.model.train()
        # Detaches it, brings it to CPU and back to Numpy
        return y_hat_tensor.detach().cpu().numpy()

    def plot_losses(self):
        fig = plt.figure(figsize=(10, 4))
        plt.plot(self.losses, label='Training Loss', c='b')
        plt.plot(self.val_losses, label='Validation Loss', c='r')
        plt.yscale('log')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.legend()
        plt.tight_layout()
        return fig

    def add_graph(self):
        # Fetches a single mini-batch so we can use add_graph
        if self.train_loader and self.writer:
            x_sample, y_sample = next(iter(self.train_loader))
            self.writer.add_graph(self.model, x_sample.to(self.device))



# Cell
def generate_Seqs_Exp_Dataset(num_seq, low, high):
    """
    generates a DNA dataset with Expression(or whatever else) values
    nucleotides/expressions will be drawn from 2 distinct distributions

    input : num_seq -> int: number of sequences
            length_seq -> tuple(min/max length of sequences)
    """

    raw_sequences = []
    dna_dict = gen_dna_vocab()


    for i in range(num_seq):
        length_seq = np.random.randint(low=low, high=high)
        seq_instance = np.random.randint(low=1,high=5, size=(1,length_seq))
        raw_seq = "".join([list(dna_dict.keys())[x-1] for x in seq_instance[0]])
        raw_sequences.append(raw_seq)


    exp = list(np.random.randn(num_seq))

    dataframe = pd.DataFrame(np.array([raw_sequences,exp])).transpose()
    dataframe.columns = ['Seqs','Exp']

    return dataframe