import random
import six.moves.cPickle as pickle

def get_cv_index(index_length, cv_num, fileout):
    '''split data in to cross validation list
    '''
    cv_index_res = []
    for i in range(cv_num):
        cv_index_res.append([])
    for i in range(index_length):
        index = random.randint(0, cv_num-1)
        cv_index_res[index].append(i)
    for i in range(cv_num):
        length = len(cv_index_res[i])
        print "cv index %d, has %d instances"%(i, length)
    pickle.dump(cv_index_res, open(fileout, 'wb'))

def save_model(model, filename):
    pickle.dump(model, open(filename, 'wb'))


if __name__ == '__main__':
    #test split cv data function
    get_cv_index(1000, 10, 'cv_index.test')


