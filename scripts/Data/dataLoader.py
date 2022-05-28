import os
import pandas as pd
import pickle
import numpy as np
import random
from utils import helperFunctions
from datetime import datetime, timedelta,date
from dateutil.parser import parse

class DataProcessor:
    def __init__(self,configfile):
        self.config = configfile

    def dataLoader(self):
        inputPath = self.config["inputData"]
        dataFrame = pd.read_csv(inputPath,encoding = "ISO-8859-1")
        return dataFrame
    def dateParser(self):
        postDetails = self.dataLoader()
        postDetails['Parse_date'] = postDetails[self.config["order_date"]].apply(lambda x: parse(x))
        postDetails['Weekday'] = postDetails['Parse_date'].apply(lambda x: x.weekday())
        postDetails['Day'] = postDetails['Parse_date'].apply(lambda x: x.strftime("%A"))
        postDetails['Month'] = postDetails['Parse_date'].apply(lambda x: x.strftime("%B"))
        postDetails['Year'] = postDetails['Parse_date'].apply(lambda x: x.strftime("%Y"))
        postDetails['year_month'] = postDetails['Year'] + "_" +postDetails['Month']

        return postDetails





