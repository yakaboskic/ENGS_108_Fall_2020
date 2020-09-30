import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
import argparse
import math
import tqdm
import pickle

def process_cyrillic_images(folder, pixel_size=(36,36), save_filename=None):
    '''
    Accepts the folder where the cyrillic data is saved so that each subfolders are cyrillic characters and the subfolders contents are the examples of those characters.

    Will output a numpy array with first column an integer label of the character and subsequent columns a numerical 784 dimensional 
    vector corresponding the the examples greyscale numerical values. Will also output a map detailing cyrillic characters to integer labels.
    '''
    map_ = {}
    data = []
    for idx, subfold in enumerate(tqdm.tqdm(os.listdir(folder), desc='Processing characters', leave=False)):
        if os.path.isdir(os.path.join(folder, subfold)):
            map_[idx] = subfold
            #-- Wa have found cyrillic character folder so let's extract all example data
            for img_name in os.listdir(os.path.join(folder, subfold)):
                if img_name.endswith('.png'):
                    img_path = os.path.join(folder, subfold, img_name)
                    img_array = np.array(Image.open(img_path).resize(pixel_size))
                    img_array = img_array[:,:,3].flatten()
                    img_array = np.insert(img_array, 0, idx)
                    data.append(img_array)

    data = np.array(data)

    if save_filename is not None:
        with open(save_filename, 'wb') as f_:
            pickle.dump((data, map_), f_)

    return data, map_


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str, help='Path to Cyrillic PNG data.')
    parser.add_argument('--s', type=str, default=None, help='Save file name')
    parser.add_argument('--p', type=int, default=36, help='Pixel dimensions of images.')
    args = parser.parse_args()

    X, map_ = process_cyrillic_images(
            args.f,
            pixel_size=(args.p, args.p),
            save_filename=args.s
            )
    '''
    # Some Testing Code. Plots a random image.

    import random
    rand_idx = random.randint(0, X.shape[0])
    r = X[rand_idx, 1:]
    plt.imshow(r.reshape((36,36)), cmap='Greys')
    plt.show()
    '''
