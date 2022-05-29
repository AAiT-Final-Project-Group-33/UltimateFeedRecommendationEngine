import argparse
import pandas as pd
from utils import Conf,helperFunctions
from Data import DataProcessor
from processes import rfmMaker,rlLearn,rlRecomend
import os.path
from pymongo import MongoClient


ap = argparse.ArgumentParser()
ap.add_argument('-c','--conf',required=True,help='Path to the configuration file')
args = vars(ap.parse_args())


conf = Conf(args['conf'])

print("[INFO] loading the raw files")
dl = DataProcessor(conf)


if os.path.exists(conf["postDetails"]):
    print("[INFO] Loading post details from pickle file")
    
    postDetails = helperFunctions.load_files(conf["postDetails"])
else:
    print("[INFO] Creating post details from csv file")
    
    postDetails = dl.gvCreator()
    
    rfm = rfmMaker(postDetails,conf)
    postDetails = rfm.segmenter()
    
    

