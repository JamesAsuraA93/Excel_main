import pandas as pd


def write_file(df, name):
    writer = pd.ExcelWriter(name + '_counted' + '.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Statics', index=True)
    writer.save()


def process(df,tag):
    new_count = pd.pivot_table(df, values='NO.',index='Flop(3)', columns=tag, aggfunc='count', fill_value=0)
    return new_count


def main(name):
    print('Reading file...')
    df = pd.read_excel(name + '.xlsx')
    print('Processing...')
    new_df1 = process(df, 'Turn(1)')
    new_df2 = process(df, 'River(1)')
    print('Writing file...')
    write_file(new_df1, name + "_Turn")
    write_file(new_df2, name + "_River")
    print('Done!')
