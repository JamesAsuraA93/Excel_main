import random as rd
import pandas as pd


def sent_card(card_name, start, stats, NO):
    if start > 11:
        start = (start % 12) + 4
    for i in range(len(stats)):
        if i == 8:
            break
        current = rd.sample(card_name, stats[start])
        stats[start] = str(current).removeprefix('[').removesuffix(']').replace("'", "")
        for card in current:
            card_name.remove(card)
        if start == 11:
            start = 4
        else:
            start += 1
    for i in range(3):
        current = rd.sample(card_name, stats[i + 1])
        stats[i + 1] = str(current).removeprefix('[').removesuffix(']').replace("'", "")
        for card in current:
            card_name.remove(card)
    stats[0] = NO
    return stats



def Data_Frame_Real(rows, start_with, list_stats, df):
    control = ['Ac', 'Ad', 'Ah', 'As', '2c', '2d', '2h', '2s', '3c', '3d', '3h', '3s', '4c', '4d', '4h', '4s', '5c',
               '5d', '5h', '5s', '6c', '6d', '6h', '6s', '7c', '7d', '7h', '7s', '8c', '8d', '8h', '8s', '9c', '9d',
               '9h', '9s', 'Tc', 'Td', 'Th', 'Ts', 'Jc', 'Jd', 'Jh', 'Js', 'Kc', 'Kd', 'Kh', 'Ks', 'Qc', 'Qd', 'Qh',
               'Qs']
    if rows >= 10000:
        cut = 1000
        light = rows // cut
        walk = 0
        list_df = []
        for i in range(light):
            for j in range(cut):
                current = walk
                # print(current)
                current %= 8
                # print(walk)
                prepare_deck = sent_card(control, start_with + current, list_stats, walk + 1)
                control = ['Ac', 'Ad', 'Ah', 'As', '2c', '2d', '2h', '2s', '3c', '3d', '3h', '3s', '4c', '4d', '4h',
                           '4s', '5c',
                           '5d', '5h', '5s', '6c', '6d', '6h', '6s', '7c', '7d', '7h', '7s', '8c', '8d', '8h', '8s',
                           '9c', '9d',
                           '9h', '9s', 'Tc', 'Td', 'Th', 'Ts', 'Jc', 'Jd', 'Jh', 'Js', 'Kc', 'Kd', 'Kh', 'Ks', 'Qc',
                           'Qd', 'Qh',
                           'Qs']
                list_stats = ['NO', 3, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]
                df.loc[walk] = prepare_deck
                print(walk+1)
                walk += 1
            list_df.append(df)
            df = pd.DataFrame(
            columns=('NO.', 'Flop(3)', 'Turn(1)', 'River(1)', 'Small blind(2)', 'Big blind(2)', 'Under the gun(UTG)(2)',
                     'Under the gun(UTG)+1(2)', 'Middle position (MP)(2)', 'Middle position (MP)+1(2)', 'Cut off(2)',
                     'Button(2)'))

        df_main = pd.concat(list_df)
        return df_main

    else:
        for j in range(rows):
            current = j
            current %= 8
            prepare_deck = sent_card(control, start_with + current, list_stats, j + 1)
            control = ['Ac', 'Ad', 'Ah', 'As', '2c', '2d', '2h', '2s', '3c', '3d', '3h', '3s', '4c', '4d', '4h', '4s', '5c',
                   '5d', '5h', '5s', '6c', '6d', '6h', '6s', '7c', '7d', '7h', '7s', '8c', '8d', '8h', '8s', '9c', '9d',
                   '9h', '9s', 'Tc', 'Td', 'Th', 'Ts', 'Jc', 'Jd', 'Jh', 'Js', 'Kc', 'Kd', 'Kh', 'Ks', 'Qc', 'Qd', 'Qh',
                   'Qs']
            list_stats = ['NO', 3, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]
            print(j+1)
            df.loc[j] = prepare_deck

        return df


def sent_card_test(card_name, start, stats, NO):
    if start > 11:
        start = (start % 12) + 4
    for i in range(len(stats)):
        if i == 8:
            break
        stats[start] = card_name[0]
        card_name.remove(card_name[0])
        if start == 11:
            start = 4
        else:
            start += 1
    for i in range(3):
        stats[i + 1] = card_name[0]
        card_name.remove(card_name[0])
    stats[0] = NO
    return stats


def Data_Frame_Test(rows, start_with, list_stats, df):
    control = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    for j in range(rows):
        current = j
        current %= 8
        prepare_deck = sent_card_test(control, start_with + current, list_stats, j + 1)
        control = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        list_stats = ['NO', 3, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]
        print(j+1)
        df.loc[j] = prepare_deck
    return df


def main_process(name, rows=20, start_with=4, Mode=1):
    # read
    try:
        df = pd.read_excel(r'file_create/' + name + '.xlsx')
    except:
        df = pd.DataFrame(
            columns=['NO.', 'Flop(3)', 'Turn(1)', 'River(1)', 'Small blind(2)', 'Big blind(2)', 'Under the gun(UTG)(2)',
                     'Under the gun(UTG)+1(2)', 'Middle position (MP)(2)', 'Middle position (MP)+1(2)', 'Cut off(2)',
                     'Button(2)'])
        writer = pd.ExcelWriter('file_create/'+name + '.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Statics', index=False)
        writer.save()

    list_stats = ['NO', 3, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]  # 12 Columns

    # write
    if Mode == 1:
        df = Data_Frame_Real(rows, start_with, list_stats, df)
    elif Mode == 0:
        df = Data_Frame_Test(rows, start_with, list_stats, df)
    writer = pd.ExcelWriter('file_create/'+name + '.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Statics', index=False)
    writer.save()
    print('Done!')

