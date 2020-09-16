from sklearn.datasets import make_blobs
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

    with open(filename, 'wb') as f_:
        pickle.dump(obj=X, file=f_)

    return X

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', default=100, type=int, help='Number of samples to generate')
    parser.add_argument('-p', default=2, type=int, help='Number of features')
    parser.add_argument('-f', default='data.pk', type=str, help='Filename to save.')
    parser.add_argument('-c', default=20, type=int, help='Number of centers.')

    args = parser.parse_args()

    X = makeClustersDataset(args.s, args.p, args.c, args.f)
    plt.scatter(X[:,0], X[:,1])
    plt.show()
