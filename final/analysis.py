import numpy as np
from matplotlib import pyplot as plt
import argparse

x_train_path = '../../data_CSIE_ML/X_train/arr_0.npy'
y_train_path = '../../data_CSIE_ML/Y_train/arr_0.npy'
x_test_path  = '../../data_CSIE_ML/X_test/arr_0.npy'

def save_mean_std():
    data_train = np.load(x_train_path)
    data_test  = np.load(x_test_path)
    data = np.vstack([data_train, data_test])
    del data_train
    del data_test
    print(data.shape)
    mean_std = np.zeros((2, data.shape[1]))
    mean_std[0] = np.mean(data, 0)
    mean_std[1] = np.std(data, 0)
    print(mean_std.shape)
    np.save('mean_std.npy', mean_std)


def test():
    print('test')

if __name__ == '__main__':
    #save_mean_std(y_train_path, 'y_train_mean_std.npy')
    save_mean_std()