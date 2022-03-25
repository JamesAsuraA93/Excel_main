import pandas as pd
from threading import Thread

# class MyThread(Thread):
#
#     def __init__(self, df,name):
#         Thread.__init__(self)
#         self.name = name
#         self.df = df


    # def run(self):
    #     print("Hello " + self.name + " from " + self.name)

    # def write_file(self,df, name):
    #     writer = pd.ExcelWriter(name + '_counted' + '.xlsx', engine='xlsxwriter')
    #     df.to_excel(writer, sheet_name='Statics', index=True)
    #     writer.save()
    #
    # def process(self,df, tag):
    #     new_count = pd.pivot_table(df, values='NO.', index='Flop(3)', columns=tag, aggfunc='count', fill_value=0)
    #     return new_count
#
# thr1 = MyThread("Meteo")
# thr2 = MyThread("Danny")
#
# thr1.start()
# thr2.start()





def write_file(df, name):
    writer = pd.ExcelWriter(name + '_counted' + '.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Statics', index=True)
    writer.save()


def process(df, tag):
    new_count = pd.pivot_table(df, values='NO.', index='Flop(3)', columns=tag, aggfunc='count', fill_value=0)
    return new_count


def main(name,lst):
    df = pd.read_excel(name + '.xlsx')
    # new_df = process(df, lst_column[2])
    # write_file(new_df, name + "_" + lst_column[2])
    for item in lst:
        new_df = process(df,item)
        write_file(new_df, name + "_"+item)
        del new_df


