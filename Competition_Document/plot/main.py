# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import os
import matplotlib.pyplot as plt

cwd = os.getcwd()
path = os.path
pjoin = path.join

for wave in range(1, 9):
    print(f'Processing Wave {wave}')
    var = pd.read_csv(pjoin(cwd, 'data', f'wave{wave}.csv'))
    # plt.hist(list(var.columns)[22:23])
    print(list(var.columns)[22])
    var[list(var.columns)[22]].value_counts().plot(kind='bar')
    plt.title("wave" f'{wave}')
    plt.savefig(f'W{wave}_2425.png', dpi=300)