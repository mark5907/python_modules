import pandas as pd
import numpy as np 
import matplotlib.pylab as plt


def carol(x, y, ax=None):

    df = pd.DataFrame( {'x': x, 'y':y} )
    df = df[df['x'].notnull()].copy()

    df = df.sort_values(by='x').reset_index(drop=True)

    if ax is not None:
        plt.sca(ax)
    plt.plot( df['y'].cumsum() )

    n = len(df)
    steps = n/6
    xtick_label = df['x'].tolist()[::steps]
    xtick_label = ['{:.2f}'.format(v) for v in xtick_label]
    plt.xticks(range(0, n, steps), xtick_label)


def group_scatter(x, y, bins=50, ax=None):
    df = pd.DataFrame( {'x': x, 'y':y} )
    df = df[df['x'].notnull()].copy()

    df['x_cut'] = pd.qcut(df['x'], bins, labels=False)
    ef = df.groupby('x_cut')['y'].mean()
    if ax is not None:
        plt.sca(ax)
    plt.scatter(ef.index, ef.values)
