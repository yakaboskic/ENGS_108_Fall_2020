from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split

import pickle
import argparse
import matplotlib.pyplot as plt
import random

def makeClustersDataset(n_samples, n_features, centers, filename):
    ''' Returns an array of samples that form m blobs.'''
    X, _ = make_blobs(n_samples=n_samples,
            n_features=n_features,
            centers=centers,
            center_box=(-10, 10),
            cluster_std=[random.random() for _ in range(centers)],
            )

    X_train_valid, X_test = train_test_split(X, test_size=.2)
    X_train, X_valid = train_test_split(X, test_size=.1)

    with open(filename, 'wb') as f_:
        pickle.dump(obj=(X_train, X_valid, X_test), file=f_)

    return (X_train, X_valid, X_test)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', default=100, type=int, help='Number of samples to generate')
    parser.add_argument('-p', default=2, type=int, help='Number of features')
    parser.add_argument('-f', default='data.pk', type=str, help='Filename to save.')
    parser.add_argument('-c', default=20, type=int, help='Number of centers.')

    args = parser.parse_args()

    X_train, X_valid, X_test = makeClustersDataset(args.s, args.p, args.c, args.f)
    plt.scatter(X_train[:,0], X_train[:,1])
    plt.show()
