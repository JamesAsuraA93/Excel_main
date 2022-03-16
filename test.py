import pandas as pd
#
# df = pd.DataFrame(
#       [['a', 7, 10],
#        ['b', 8, 11],
#        ['b', 9, 10],
#        ['a', 9, 13]],
#       index=[1, 2, 3, 4],
#       columns=['a', 'b', 'c'])
#
# print(df)
#
#
# new_count = pd.pivot_table(df, index=['a'], columns=['b'], aggfunc='count', fill_value=0)
# print(new_count)
name = 'need'
df = pd.read_excel(name + '.xlsx')
print(df)