import os

os.chdir(
    "/Users/eklavya/projects/education/formalEducation/DataScience/DataScienceAssignments/HealthCare/Capstone/src/")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import cut_tree
import warnings

warnings.filterwarnings('ignore')
sns.set_style('whitegrid')
sns.set_context('paper')


# Util function: line seperator
def print_ln():
    print('-' * 80, '\n')


# split into train and test
from sklearn.model_selection import train_test_split

cleaned_master_data = pd.read_csv("cleaned_master_data_py.csv")

print_ln()

X = cleaned_master_data.loc[:, cleaned_master_data.columns != 'Hospital overall rating']
y = cleaned_master_data.loc[:, 'Hospital overall rating']

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    stratify=y,
                                                    train_size=0.7,
                                                    test_size=0.3, random_state=100)

pca = PCA(svd_solver='randomized', random_state=16)

pca.fit(X_train)

print(pca.components_)

colnames = list(X_train.columns)

pcs_df = pd.DataFrame({'PC1': pca.components_[0], \
                       'PC2': pca.components_[1], \
                       'Feature': colnames})

pcs_df.head()

explained_variance_ratio_ = np.around(pca.explained_variance_ratio_, decimals=3)
explained_variance_ratio_

fig = plt.figure(figsize=(12, 8))
plt.plot(np.cumsum(pca.explained_variance_ratio_), 'ro-', linewidth=2)
plt.title('Scree Plot')
plt.xlabel('Principle components')
plt.ylabel('variance')
plt.show()

from sklearn.decomposition import IncrementalPCA

pca_final = IncrementalPCA(n_components=2)

df_pca = pca_final.fit_transform(cleaned_master_data.drop(['Hospital overall rating'], axis=1))
df_pca.shape
