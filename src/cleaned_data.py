import os
os.chdir("/Users/eklavya/projects/education/formalEducation/DataScience/DataScienceAssignments/HealthCare/Capstone/src/")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.neighbors import NearestNeighbors
from random import sample
from numpy.random import uniform
from math import isnan

from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


import warnings
warnings.filterwarnings('ignore')
sns.set_style('whitegrid')
sns.set_context('paper')

def print_ln():
    print('-' * 80, '\n')



# PCA on a group of measures

effe_master = pd.read_csv("effe_master_data_py.csv").drop(['Unnamed: 0'], axis= 1).set_index('Provider ID')
effe_master.info()

print_ln()

eff = effe_master.drop(effe_master.iloc[:, 0:7], axis=1)
eff.columns



eff = eff.dropna(thresh= 3)

eff.to_csv("eff_data_py.csv")

eff.info()


eff = eff.apply(lambda x: x.fillna(x.median()), axis=0)
eff



## With Incremental PCA

from sklearn.decomposition import IncrementalPCA, PCA
pca = IncrementalPCA()
eff_pca = pca.fit_transform(eff)
eff_pca = pd.DataFrame(eff_pca, columns=eff.columns)
eff_pca.index = eff.index
eff_pca


pca.explained_variance_ratio_


eff_pca_weights = pd.DataFrame(pca.components_, columns=eff.columns)
eff_pca_weights




eff_measure_weight = eff_pca.mean(axis=1)
eff_measure_weight


eff_scores = pd.DataFrame({'effe' : eff_measure_weight})
eff_scores


def function_group_score(numeric_df, score_name):
    df = numeric_df.dropna(thresh= 3)
    imputed_df = df.apply(lambda x: x.fillna(x.median()), axis=0)
    pca = IncrementalPCA()
    df_pca = pca.fit_transform(imputed_df)
    df_pca = pd.DataFrame(df_pca, columns= df.columns)
    df_pca.index = df.index
    df_with_weight = df_pca.mean(axis=1)
    df_scores = pd.DataFrame({score_name : df_with_weight})
    return df_scores


effe_master = pd.read_csv("effe_master_data_py.csv").drop(['Unnamed: 0'], axis= 1).set_index('Provider ID')
eff = effe_master.drop(effe_master.iloc[:, 0:7], axis=1)

effectiveness_scores = function_group_score(eff, 'effe_score')
effectiveness_scores



df = pd.read_csv("read_master_data_py.csv").drop(['Unnamed: 0'], axis= 1).set_index('Provider ID')
df.columns
print_ln()

num_df = df.drop(df.iloc[:, 0:7], axis=1)
num_df.columns
print_ln()

readmission_scores = function_group_score(num_df, 'radm_score')
readmission_scores


df = pd.read_csv("mort_master_data_py.csv").drop(['Unnamed: 0'], axis= 1).set_index('Provider ID')
df.columns
print_ln()

num_df = df.drop(df.iloc[:, 0:7], axis=1)
num_df.columns
print_ln()

mortality_scores = function_group_score(num_df, 'mort_score')
mortality_scores


df = pd.read_csv("safe_master_data_py.csv").drop(['Unnamed: 0'], axis= 1).set_index('Provider ID')
df.columns
print_ln()

num_df = df.drop(df.iloc[:, 0:7], axis=1)
num_df.columns
print_ln()

safety_scores = function_group_score(num_df, 'safety_score')
safety_scores



df = pd.read_csv("expe_master_data_py.csv").drop(['Unnamed: 0'], axis= 1).set_index('Provider ID')
df.columns
print_ln()

num_df = df.drop(df.iloc[:, 0:7], axis=1)
num_df.columns
print_ln()

experience_scores = function_group_score(num_df, 'expe_score')
experience_scores



df = pd.read_csv("medi_master_data_py.csv").drop(['Unnamed: 0'], axis= 1).set_index('Provider ID')
df.columns
print_ln()

num_df = df.drop(df.iloc[:, 0:7], axis=1)
num_df.columns
print_ln()

medical_scores = function_group_score(num_df, 'medi_score')
medical_scores





df = pd.read_csv("time_master_data_py.csv").drop(['Unnamed: 0'], axis= 1).set_index('Provider ID')
df.columns
print_ln()

num_df = df.drop(df.iloc[:, 0:7], axis=1)
num_df.columns
print_ln()

timeliness_scores = function_group_score(num_df, 'time_score')
timeliness_scores

merge1= pd.merge(readmission_scores, mortality_scores, on= 'Provider ID')
merge2= pd.merge(merge1, safety_scores, on= 'Provider ID')
merge3= pd.merge(merge2, experience_scores, on= 'Provider ID')
merge4= pd.merge(merge3, medical_scores, on= 'Provider ID')
merge5= pd.merge(merge4, timeliness_scores, on= 'Provider ID')
merge6= pd.merge(merge5, effectiveness_scores, on= 'Provider ID')
group_scores = merge6
group_scores



group_scores['final_score'] = group_scores.mean(axis=1)
final_score = group_scores
final_score.to_csv("final_score.csv")



#group_scores['final_score'].describe()








