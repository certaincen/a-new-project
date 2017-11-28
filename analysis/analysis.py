import numpy as np
import matplotlib.pyplot as plt
import six.moves.cPickle as pickle

def plot_bar_data(x, y, xlabel, ylabel, title):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.bar(x, y)
    plt.show()


def plot_data(x, y, xlabel, ylabel, title, log_flag=False):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if log_flag:
        plt.loglog(x, y)
    else:
        plt.plot(x, y)
    plt.show()


def cal_price_distribution(price_array, xlabel='price interval', ylabel='count', title='price distribution'):
    mean_price = np.mean(price_array)
    var = np.var(price_array)
    std = np.std(price_array)
    print "mean price %f, std %f, var %f"%(mean_price, std, var)
    dis_dict = {}
    for price in price_array:
        index = int(price / 5)
        if index not in dis_dict:
            dis_dict[index] = 0
        dis_dict[index] += 1
    plot_data(dis_dict.keys(), dis_dict.values(), xlabel, ylabel, title, True)

def cal_condition_id_distribution(condition_id_array):
    title = 'condition distribution'
    xlabel = 'condition id'
    ylabel = 'count'
    dis_dict = {}
    for c_id in condition_id_array:
        if c_id not in dis_dict:
            dis_dict[c_id] = 0
        dis_dict[c_id] += 1
    print dis_dict
    #plot_data(dis_dict.keys(), dis_dict.values(), xlabel, ylabel, title)
    plot_bar_data(np.array(dis_dict.keys(),dtype=int), dis_dict.values(), xlabel, ylabel, title)

def build_category_tree(category_tree, category_list):
    category_name = category_list[0]
    if len(category_list) == 1:
        if category_name not in category_tree:
            category_tree[category_name] = 0
        category_tree[category_name] += 1
        return category_tree
    if category_name not in category_tree:
        category_tree[category_name] = {}
    category_tree[category_name] = build_category_tree(category_tree[category_name], category_list[1:])
    return category_tree


def show_hierarchical_category(itemlist, deep):
    if not itemlist:
        return
    cate_list = []
    count = 0
    for item in itemlist:
        count += len(item.keys())
        for sub_category in item.values():
            if isinstance(sub_category, dict):
                cate_list.append(sub_category)
    print "deep %d has %d categorys"%(deep, count)
    show_hierarchical_category(cate_list, deep+1)


def analysis_category(category_name_array):
    category_tree = {}
    for category_name in category_name_array:
        category_list = category_name.split('/')
        #print category_list
        category_tree = build_category_tree(category_tree, category_list)
        #print category_tree
    pickle.dump(category_tree, open('../input/category_tree.pkl', 'wb'))
    print category_tree['Women'].keys()
    show_hierarchical_category([category_tree], 1)



def run(filename):
    price_array = []
    condition_id_array = []
    category_name_array = []
    condition_price_dict = {}
    with open(filename, 'r') as fin:
        content = fin.read().strip().split('\n')
        for line in content[1:]:
            items = line.split('\t')
            price = float(items[5])
            condition_id = items[2]
            category_name = items[3]
            if condition_id not in condition_price_dict:
                condition_price_dict[condition_id] = []
            condition_price_dict[condition_id].append(price)
            #condition_id_array.append(condition_id)
            #price_array.append(price)
            #category_name_array.append(category_name)
    #price_array = np.array(price_array)
    #cal_price_distribution(price_array)
    #cal_condition_id_distribution(condition_id_array)
    #analysis_category(category_name_array)
    for condition_id, price_array in condition_price_dict.iteritems():
        title = "condition %s, price distribution"%condition_id
        price_array = np.array(price_array)
        print title
        cal_price_distribution(price_array, title=title)



if __name__ == '__main__':
    filename = '../dataset/train.tsv'
    run(filename)
