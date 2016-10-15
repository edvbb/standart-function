# file is for a standart function Kruskal-Wallis H-test
# packages
import pandas as pd
import scipy.stats 
# a dataframe
df = pd.DataFrame({'numbers':range(9), 'group':['a', 'b', 'c']*3})
# groups
groups = {}
for grp in df['group'].unique(): 
    groups[grp] = df['numbers'][df['group']==grp].values
# args
args = groups.values()
scipy.stats.kruskal(*args)
# or if you need them in an order:
args = [groups[grp] for grp in sorted(df['group'].unique())]

# if we have some columns in a dataframe we can do
df = pd.DataFrame({'a': range(9), 'b':[1,2,3,1,2,3,1,2,3], 'group':['a', 'b', 'c']*3}) 

groups = {}
res = []
for column in df[[0, 1]]:
    for grp in df['group'].unique():
        groups[grp] = df[column][df['group']==grp].values
    args = groups.values()
    g = scipy.stats.kruskal(*args)
    res.append(g)
print (res) 
