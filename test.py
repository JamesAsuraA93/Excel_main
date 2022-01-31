import pandas as pd
#
df = pd.DataFrame(
      [['6c, 9d, 9s', 7, 10],
       [5, 8, 11],
       [6, 9, '6c, 9d, 9s'],
       ['6c, 9d, 9s', 9, 13]],
      index=[1, 2, 3, 4],
      columns=['a', 'b', 'c'])
# if col a is '6c, 9d, 9s' replace tp '5' else pass
df['a'].replace(to_replace='6c, 9d, 9s', value=5, inplace=True)
print(df)

#
# # print(df)
#
# # new DF with only same value : 5 in column 'a'
# df_new = df[df['a'] == '6c, 9d, 9s']
# print(df_new)
#
# # count number of rows with same value : 5 in column 'a'
# # print(df_new.shape[0])  # 2 rows
# #
# # # create DF with count of rows with same value : 5 in column 'a'
# # df_count = pd.DataFrame(df[df['a'] == 5].groupby('a').size(),columns=['count'])
# # print(df_count)
#
# # writer = pd.ExcelWriter('test2.xlsx', engine='xlsxwriter')
# # df.to_excel(writer, sheet_name='Statics', index=False)
# # writer.save()
# #
# # writer1 = pd.ExcelWriter('test3.xlsx', engine='xlsxwriter')
# # df_count.to_excel(writer1, sheet_name='Statics', index=False)
# # writer1.save()
#
#
#
#
#
# test = 'Tc,9h,Qs'
# print('2c' in test)
# print('Tc' in test)

#