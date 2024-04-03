import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

def gencoord_to_idx(coord, st, res=2000):
    if type(coord) == int:
        idx = (coord - st) // res
    elif coord[0] == 'c':
        idx = ''
    else:
        idx = (int(coord) - st) // res
    return idx


def make_matr_list(df):
    res = df.loc[0, 'end'] - df.loc[0, 'start']
    st = int(df.loc[0, 'start'])

    p1_all = [gencoord_to_idx(coord, 0, res) for coord in df['start']]
    int_chr, int_st, int_ed, score = zip(*[re.split(':|-|,', i) for i in df['info']])
    p2_all = [gencoord_to_idx(coord, 0, res) for coord in int_ed]
    score_all = np.array([int(s) for s in score])

    #     print(score_all)
    #     print(p1_all)
    #     print(p2_all)

    matr_df_all = pd.DataFrame(columns=['chr1', 'p1', 'chr2', 'p2', 'score'])
    matr_df_all['chr1'] = df['chr']
    matr_df_all['p1'] = p1_all
    matr_df_all['chr2'] = int_chr
    matr_df_all['p2'] = p2_all
    matr_df_all['score'] = score_all

    mask = matr_df_all['p2'] == ''
    matr_df = matr_df_all[~mask]

    # print(matr_df)

    return matr_df

def make_matr_chr(matr_df, chrname):
    # assert ice balance
    matr_df_chr = matr_df[matr_df['chr'] == chrname].reset_index()
    matr_list = make_matr_list(matr_df_chr)
    sz = len(matr_list)
    matr = np.zeros([2020, 2020])

    # fill matrix
    for i in range(sz):
        if 2000 < matr_list.loc[i, 'p1'] < 4000:
            if 2000 < matr_list.loc[i, 'p2'] < 4000:
                #             print(matr_DP.loc[i,'p1'], matr_DP.loc[i,'p2'])
                #             print(matr_DP.loc[i,'score'])
                matr[matr_list.loc[i, 'p1'] - 2020:matr_list.loc[i, 'p1'] - 2000,
                matr_list.loc[i, 'p2'] - 2020:matr_list.loc[i, 'p2'] - 2000] = matr_list.loc[i, 'score']

    return matr

def plot_matr(all_matr, names):
    n = len(all_matr)
    fig, axs = plt.subplots(1, n)

    for i in range(n):
        axs[i].matshow(all_matr[i])
        axs[i].set_title(names[i])
    plt.show()

    pass

