# file is for a standart function Kruskal-Wallis H-test
# packages
import pandas as pd
import scipy 
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
