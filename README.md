# BioNLP
> Useful functiosn for DL with bio seqs


This file will become your README and also the index of your documentation.

## Install

`pip install your_project_name`

## How to use

Fill me in please! Don't forget code examples:

```python
dna_dict = gen_dna_vocab(kmer=1)
```

```python
synthetic_data = generate_Seqs_Exp_Dataset(50,10,30)
synthetic_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Seqs</th>
      <th>Exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>CGAACGCTACTA</td>
      <td>0.7373034730804604</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CCGGAAGCATTCATTAGTGAGTT</td>
      <td>-1.88195416047714</td>
    </tr>
    <tr>
      <th>2</th>
      <td>AGCAGCGCAGTGTACCCCCT</td>
      <td>0.09558584614212201</td>
    </tr>
    <tr>
      <th>3</th>
      <td>TTCAAAACCTTT</td>
      <td>0.9047737703778639</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ATCAGAGCCTCAAGAAGACGAGTCATTT</td>
      <td>-0.20030463613388197</td>
    </tr>
    <tr>
      <th>5</th>
      <td>CTCTCAGATGCACAGTTCTGAACCTA</td>
      <td>1.232823897326797</td>
    </tr>
    <tr>
      <th>6</th>
      <td>GTGCTCACTTCA</td>
      <td>0.580879943065253</td>
    </tr>
    <tr>
      <th>7</th>
      <td>CCTAGTACGCG</td>
      <td>-0.03059702971281039</td>
    </tr>
    <tr>
      <th>8</th>
      <td>GAGGCCGCGACACTCTG</td>
      <td>0.6719352703583051</td>
    </tr>
    <tr>
      <th>9</th>
      <td>CCCATTCTTGTGGATTACAGCCAACCGG</td>
      <td>-0.15376504153111467</td>
    </tr>
    <tr>
      <th>10</th>
      <td>GGGTGTTAGTGGGTATTGACAGT</td>
      <td>1.968838976400091</td>
    </tr>
    <tr>
      <th>11</th>
      <td>GTCGCCAGCAGCTGATCCATG</td>
      <td>1.2184714174654492</td>
    </tr>
    <tr>
      <th>12</th>
      <td>TTAGGTGAACATAGTGAAGCCC</td>
      <td>-1.4001210002187108</td>
    </tr>
    <tr>
      <th>13</th>
      <td>TTTCCCCACTCGACCG</td>
      <td>-0.8610513771598288</td>
    </tr>
    <tr>
      <th>14</th>
      <td>ATCCCGCCCCGACTCATATACTT</td>
      <td>-0.7794051526741257</td>
    </tr>
    <tr>
      <th>15</th>
      <td>AGGCACTGAAGAGCCGGCAA</td>
      <td>0.60671057345695</td>
    </tr>
    <tr>
      <th>16</th>
      <td>TAGTGGCAAAAGT</td>
      <td>0.5333276056854838</td>
    </tr>
    <tr>
      <th>17</th>
      <td>AGTTATCGGATGGACTACAAT</td>
      <td>0.08086178663246339</td>
    </tr>
    <tr>
      <th>18</th>
      <td>ATTTCCACGTAGCCAGCCGTG</td>
      <td>0.26551040371816315</td>
    </tr>
    <tr>
      <th>19</th>
      <td>TCATAATCCGCACCGGAGG</td>
      <td>0.5179465300990544</td>
    </tr>
    <tr>
      <th>20</th>
      <td>CGCATGTTAAATCTGATATTCCTC</td>
      <td>-0.0413082252787</td>
    </tr>
    <tr>
      <th>21</th>
      <td>GATCAATATAAAGCGCCTCCGAAG</td>
      <td>-1.2656701039776628</td>
    </tr>
    <tr>
      <th>22</th>
      <td>GAGGCTAGCGCTCCTAAGTATCCAGTCGG</td>
      <td>0.39151121240550324</td>
    </tr>
    <tr>
      <th>23</th>
      <td>GTGTGATCGCTCTGTGAGCATTTTCA</td>
      <td>1.2183617172966104</td>
    </tr>
    <tr>
      <th>24</th>
      <td>CTCCATCGCATCTATGACCTA</td>
      <td>-2.6613604493474945</td>
    </tr>
    <tr>
      <th>25</th>
      <td>CATTTCCTATATCCTATGA</td>
      <td>0.29111009816776945</td>
    </tr>
    <tr>
      <th>26</th>
      <td>CCAAATTACGTCTTCTTGAGCCC</td>
      <td>0.8227903725318689</td>
    </tr>
    <tr>
      <th>27</th>
      <td>CCCGAGGTCCGTTGAATGCACTG</td>
      <td>-0.921389921646768</td>
    </tr>
    <tr>
      <th>28</th>
      <td>AGTACCCGACGATAGACCCGTCCGTG</td>
      <td>-0.1313494905631385</td>
    </tr>
    <tr>
      <th>29</th>
      <td>TCTTACTCAGAGTATGGCC</td>
      <td>0.46579649820093777</td>
    </tr>
    <tr>
      <th>30</th>
      <td>TCTCCAACGCTACGTGCGCCCCTACAGAG</td>
      <td>-0.2562556116320983</td>
    </tr>
    <tr>
      <th>31</th>
      <td>CCTCTATGCGATCCTGAG</td>
      <td>1.682111582590814</td>
    </tr>
    <tr>
      <th>32</th>
      <td>TGTGTCCGCG</td>
      <td>-0.0856188441514632</td>
    </tr>
    <tr>
      <th>33</th>
      <td>GACCGGAACGAAGGT</td>
      <td>-0.010491381140232951</td>
    </tr>
    <tr>
      <th>34</th>
      <td>CCTCCCCGTCAGTTGGGGAGATTT</td>
      <td>1.2036985172008714</td>
    </tr>
    <tr>
      <th>35</th>
      <td>AGTGGGCGGATT</td>
      <td>0.009898081860903154</td>
    </tr>
    <tr>
      <th>36</th>
      <td>CTACATAGGCTGAGCTTAACTGGACTT</td>
      <td>-0.3689032953539045</td>
    </tr>
    <tr>
      <th>37</th>
      <td>TTGGAAACTAGATAGCCG</td>
      <td>-0.26357701157900915</td>
    </tr>
    <tr>
      <th>38</th>
      <td>CAATCAGCTCCCGCGATCCTCG</td>
      <td>-0.9830154676926086</td>
    </tr>
    <tr>
      <th>39</th>
      <td>GAATGTGAAAGCCGCCAAACATAG</td>
      <td>0.12393623313992741</td>
    </tr>
    <tr>
      <th>40</th>
      <td>CACGTGGGCAGA</td>
      <td>0.8641308332723732</td>
    </tr>
    <tr>
      <th>41</th>
      <td>AGCCTTTTGAATTGTTAATGCGCATGGGA</td>
      <td>2.949504686277576</td>
    </tr>
    <tr>
      <th>42</th>
      <td>GAGAAATGAAACCCCTTTTTGCC</td>
      <td>-0.4407761914357316</td>
    </tr>
    <tr>
      <th>43</th>
      <td>CACGTCAAAGTGATTTAAGACAAAC</td>
      <td>0.10846407697493915</td>
    </tr>
    <tr>
      <th>44</th>
      <td>ATCCTTTGAGCTCGTCC</td>
      <td>-1.1845969767021456</td>
    </tr>
    <tr>
      <th>45</th>
      <td>ATGGACAAATGG</td>
      <td>-0.010689489415148207</td>
    </tr>
    <tr>
      <th>46</th>
      <td>CCCATCAATCCTCATCAGAT</td>
      <td>-0.8537340320560226</td>
    </tr>
    <tr>
      <th>47</th>
      <td>GGCCGGTTTGAAGC</td>
      <td>-0.4086225907015212</td>
    </tr>
    <tr>
      <th>48</th>
      <td>CCTAAAGATC</td>
      <td>0.6123665565181334</td>
    </tr>
    <tr>
      <th>49</th>
      <td>TCTGCTGTCA</td>
      <td>0.2618775641966456</td>
    </tr>
  </tbody>
</table>
</div>



```python
synthetic_data.Exp = synthetic_data.Exp.astype(float)
```

```python
DnaDataset(synthetic_data)
```




    <bionlp.core.DnaDataset at 0x7f993b437580>



```python
#retreive single data point ; One hot encoded + target value 
DnaDataset(synthetic_data).__getitem__(4)
```




    (tensor([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
              0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
             [1., 0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 1., 1., 0., 1., 1., 0., 1.,
              0., 0., 1., 0., 0., 0., 1., 0., 0., 0., 0.],
             [0., 1., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0.,
              0., 0., 0., 0., 1., 0., 0., 1., 1., 1., 0.],
             [0., 0., 1., 0., 0., 0., 0., 1., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0.,
              1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
             [0., 0., 0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0.,
              0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
             [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
              0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]]),
     tensor(-0.2003))


