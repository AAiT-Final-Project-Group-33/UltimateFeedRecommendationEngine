import sys
import pandas as pd
import lifetimes
from sklearn.cluster import KMeans
from utils import helperFunctions



class rfmMaker:
    def __init__(self,postDetails,conf):
        self.postDetails = postDetails
        self.conf = conf

    def rfmMatrix(self):
        # Converting data to RFM format
        RfmAgeTrain = lifetimes.utils.summary_data_from_transaction_data(self.postDetails, self.conf['post_id'], 'Parse_date','Entity')
        # Reset the index
        RfmAgeTrain = RfmAgeTrain.reset_index()
        return RfmAgeTrain

    # Function for ordering cluster numbers

    def order_cluster(self,cluster_field_name, target_field_name, data, ascending):
        data_new = data.groupby(cluster_field_name)[target_field_name].mean().reset_index()
        data_new = data_new.sort_values(by=target_field_name, ascending=ascending).reset_index(drop=True)
        data_new['index'] = data_new.index
        data_final = pd.merge(data, data_new[[cluster_field_name, 'index']], on=cluster_field_name)
        data_final = data_final.drop([cluster_field_name], axis=1)
        data_final = data_final.rename(columns={'index': cluster_field_name})
        return data_final


    def clusterSorter(self,target_field_name,RfmAgeTrain, ascending):
        nclust = self.conf['nclust']
        user_variable = RfmAgeTrain[['UserID', target_field_name]]
        kmeans = KMeans(n_clusters=nclust)
        kmeans.fit(user_variable[[target_field_name]])
        cluster_field_name = target_field_name + 'Cluster'
        user_variable[cluster_field_name] = kmeans.predict(user_variable[[target_field_name]])
        user_variable.sort_values(by=target_field_name, ascending=ascending).reset_index(drop=True)
        user_variable = self.order_cluster(cluster_field_name, target_field_name, user_variable, ascending)
        return user_variable




