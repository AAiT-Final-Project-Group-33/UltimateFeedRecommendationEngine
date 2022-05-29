from pickle import load
from pickle import dump
import numpy as np


def save_clean_data(data,filename):
    dump(data,open(filename,'wb'))
    print('Saved: %s' % filename)

def load_files(filename):
    return load(open(filename,'rb'))






