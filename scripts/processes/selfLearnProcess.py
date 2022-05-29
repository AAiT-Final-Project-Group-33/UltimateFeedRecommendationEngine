import pandas as pd
from numpy.random import normal as GaussianDistribution
from collections import OrderedDict
from collections import Counter
import operator
from random import sample
import numpy as np
from pymongo import MongoClient
client = MongoClient(port=27017)
db = client.rlRecomendation



class rlLearn:
    def __init__(self,postDetails,conf):
        
        postDetails['Date'] = postDetails['Parse_date'].apply(lambda x: x.strftime("%d"))
        
        postDetails['Date'] = postDetails['Date'].astype('float64')
                

        rewardFull = postDetails.groupby(['Hour', 'Day', 'Entity', 'Username', conf['post_id']])[conf['prod_qnty']].agg(
            'sum').reset_index()
        
        self.postDetails = postDetails
        self.conf = conf
        self.rewardFull = rewardFull
        
        self.countDic = {}  
        self.polDic = {}  
        self.rewDic = {}  
        self.recoCountdic = {}  

    
    def uniqeVars(self):
        
        hours = list(self.rewardFull.Hour.unique())
        entities = list(self.rewardFull.Entity.unique())
        username = list(self.rewardFull.username.unique())
        days = list(self.rewardFull.Day.unique())
        return hours,entities,username,days

   