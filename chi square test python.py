import pandas as pd
import scipy

df = pd.DataFrame({'a' : ['b', 'b','a', 'a' , 'a', 'a', 'a', 'a' , 'a', 'a','a','a', 'b', 'b', 'b', 'b', 'b', 'a','a','a', 'b', 'b', 'b', 
                          'b', 'b', 'b', 'b', 'a', 'a'],
                   'b' : ['c','c', 'c','c', 'c', 'c',   'c', 'c', 'c',     'd' , 'd'  , 'd' , 'd' , 'd', 'd',        
                    'c', 'd', 'c', 'd', 'c', 'd', 'c', 'd', 'c', 'd', 'c', 'd', 'c', 'd']})
# crosstab
pd.crosstab(df['a'], df['b'])
# we get meanings row1 = [10, 5], row2 = [6, 8]
table = [ [ 10, 5 ], [ 6, 8 ] ]
chisq, prob, df, expected = scipy.stats.chi2_contingency( table )
# chisq - empirical meaning
# prob - probability
# df - degrees of freedom
# expected - expected meanings
output = "test Statistics: {}\ndegrees of freedom: {}\np-value: {}\n"
print(output.format( chi2, df, prob))
print(expected)
