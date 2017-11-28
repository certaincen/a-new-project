import analysis as ana
import numpy as np
import sys

if __name__ == '__main__':
    with open('./rate.txt', 'r') as fin:
        content = fin.read().strip().split('\n\t\n')
        for index, result in enumerate(content):
            x = []
            y = []
            items = result.split('\n')
            #print items
            for line in items:
                res = line.split('\t')
                ids = int(res[0])
                value = float(res[1])
                x.append(ids)
                y.append(value)
            x_label = 'class id'
            y_label = 'log motif number rate(in_number / out_umber)'
            title = 'motif %d'%index
            #ana.plot_data(x, y, x_label, y_label, title, True)
            y = np.log(y)
            ana.plot_bar_data(x, y, x_label, y_label, title)
