import numpy as np
from numpy import linalg as LA
import six.moves.cPickle as pickle
import my_util as u

def cal_MSLE(pred_y, y):
    a = np.log(pred_y+1) - np.log(y+1)
    msle = np.sqrt(np.mean(np.square(a)))
    return msle

if __name__ == '__main__':
    #test msle function
    #p = np.ma.arange(10)
    #y = np.ones(10)
    #print cal_MSLE(p, y)
