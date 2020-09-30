from sklearn.datasets import make_blobs, make_classification
from sklearn.model_selection import train_test_split
import pickle
import argparse
import matplotlib.pyplot as plt
import random

def makeClustersDataset(n_samples, n_features, centers, filename='synth_cluster.pk'):
    ''' Returns an array of samples that form m blobs.'''
    X, _ = make_blobs(n_samples=n_samples,
            n_features=n_features,
            centers=centers,
            center_box=(-10, 10),
            cluster_std=[random.random() for _ in range(centers)],
            )

    with open(filename, 'wb') as f_:
        pickle.dump(obj=X, file=f_)

    return X

def makeExplosionsEarthquakeDataset(n_samples, n_features, split=True, filename='explosions.pk'):
    X, y = make_classification(n_samples=n_samples,
            n_features=n_features)

    if split:
        X_train_valid, X_test, y_train_valid, y_test = train_test_split(X, y, test_size=.3)
        X_train, X_valid, y_train, y_valid = train_test_split(X_train_valid, y_train_valid, test_size=.1)

        data = ((X_train, y_train), (X_valid, y_valid), (X_test, y_test))
    else:
        data = (X, y)

    with open(filename, 'wb') as f_:
        pickle.dump(data)

    return data

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', type=str, help='Dataset to generate. Options: "synth", "explosions".'), 
    parser.add_argument('-s', default=100, type=int, help='Number of samples to generate')
    parser.add_argument('-p', default=2, type=int, help='Number of features')
    parser.add_argument('--f', default=None, type=str, help='Filename to save.')
    parser.add_argument('--c', default=20, type=int, help='Number of centers.')

    args = parser.parse_args()

    if args.d == 'synth':
        X = makeClustersDataset(args.s, args.p, args.c, args.f)
    elif args.d == 'explosions':
        train, _, _ = makeExplosionsEarthquakeDataset(args.s, args.p)
    plt.scatter(X[:,0], X[:,1])
    plt.show()
