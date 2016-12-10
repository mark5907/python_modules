import pandas as pd
import numpy as np 
import matplotlib.pylab as plt


def carol(df, x, y, ax=None):
    if ax is not None:
        plt.sca(ax)
    plt.plot( df.sort_values(by=x)['y'].cumsum().values )
    # plt.xlabel(x)
    # plt.ylabel(y)
    # plt.title( 'n={}'.format(len(ef) ) )

    # n = len(ef)
    # step = n/6
    # tick_range = range(0, n, step)
    # tick_label = ['{:.2f}'.format(v) for v in ef.loc[tick_range, x]]
    # plt.xticks(tick_range, tick_label)


def group_scatter(df, x, y):
    pass