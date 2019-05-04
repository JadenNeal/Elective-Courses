import numpy as np
import h5py


def cat_data_loader():
    train_dataset = h5py.File('./cats_and_dogs/datasets/train_set.h5', "r")
    x_train = np.array(train_dataset["train_set_x"][:])  # train set features
    y_train = np.array(train_dataset["train_set_y"][:])  # train set labels
    y_train = y_train.reshape((y_train.shape[0], 1))

    test_dataset = h5py.File('./cats_and_dogs/datasets/test_set.h5', "r")
    x_test = np.array(test_dataset["test_set_x"][:])     # test set features
    y_test = np.array(test_dataset["test_set_y"][:])     # test set labels
    y_test = y_test.reshape((y_test.shape[0], 1))
    return (x_train, y_train), (x_test, y_test)
