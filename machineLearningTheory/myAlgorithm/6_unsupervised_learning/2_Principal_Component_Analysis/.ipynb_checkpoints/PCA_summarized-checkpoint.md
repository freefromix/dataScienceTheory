# PCA summarized

```
        Mouse1	Mouse2	Mouse3	Mouse4	Mouse5	Mouse6
Gene1	10      11	    8	    3	    2.0	    1
Gene2	6       4	    5	    3	    2.8	    1
```

## How PCA works

### Mean

We calculate the mean of each row.

```python
gene1mean = df.loc['Gene1'].mean()
gene2mean = df.loc['Gene2'].mean()
```

![](img/1.png)

We recenter all rows value by substracting the mean.

```python
dfcentered=df.copy()
dfcentered.loc['Gene1'] = df.loc['Gene1']-gene1mean
dfcentered.loc['Gene2'] = df.loc['Gene2']-gene2mean
```

Recentered data becomes:

![](img/2.png)