"""This module load a dataset in h5"""

import numpy as np
import h5py

def load_dataset_fromh5(h5FilePathTraining, h5FilePathTest):
    """Load dataset from h5
    Args:
        h5FilePathTraining: Path to the h5 training file
        h5FilePathTest: Path to the h5 test file
    Returns:
    """

    train_dataset = h5py.File(h5FilePathTraining, "r")
    # your train set features
    train_set_x_orig = np.array(train_dataset["train_set_x"][:])
    train_set_y_orig = np.array(
        train_dataset["train_set_y"][:])  # your train set labels

    test_dataset = h5py.File(h5FilePathTest, "r")
    # your test set features
    test_set_x_orig = np.array(test_dataset["test_set_x"][:])
    test_set_y_orig = np.array(
        test_dataset["test_set_y"][:])  # your test set labels

    classes = np.array(test_dataset["list_classes"][:])  # the list of classes

    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes
