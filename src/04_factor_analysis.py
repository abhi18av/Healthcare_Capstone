import os

os.chdir(
    "/Users/eklavya/projects/education/formalEducation/DataScience/DataScienceAssignments/HealthCare/Capstone/src/")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
sns.set_style('whitegrid')
sns.set_context('paper')


# Util function: line seperator
def print_ln():
    print('-' * 80, '\n')


# https://www.datacamp.com/community/tutorials/introduction-factor-analysis
from factor_analyzer import FactorAnalyzer

effe_master = pd.read_csv("effe_master_data_py.csv")

eff = effe_master.drop(effe_master.iloc[:, 0:9], axis=1)
eff.columns
print_ln()

eff

# effectiveness = effectiveness.drop(effectiveness.iloc[:,0],  axis = 1)


# https://stackoverflow.com/questions/27296387/difference-between-r-scale-and-sklearn-preprocessing-scale/27297618
# https://stackoverflow.com/questions/18005305/implementing-r-scale-function-in-pandas-in-python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

eff[eff.columns] = scaler.fit_transform(eff[eff.columns])
eff

eff.corr()
# sns.heatmap(eff.corr())
# plt.show()
print_ln()

eff.info()
print_ln()

# at n=20, variance drops to 19
# at n=15, variance is 35
# at n=10, variance is 39 - highest
fa = FactorAnalyzer(n_factors=10, rotation="varimax", method="ml")

fa.fit(eff)
print_ln()

# fa.loadings_

print_ln()

ev, v = fa.get_eigenvalues()

# TODO @abhi18av make this better
# We can see only for 5-factors eigenvalues are greater or close to one. It means we need to choose only 5 factors (or unobserved variables)
ev
print_ln()

# v
# print_ln()


# plt.scatter(range(1,eff.shape[1]+1),ev)
# plt.plot(range(1,eff.shape[1]+1),ev)
# plt.title('Scree Plot')
# plt.xlabel('Factors')
# plt.ylabel('Eigenvalue')
# plt.grid()
# plt.show()

print_ln()

eff_factor_variance = fa.get_factor_variance()

eff = eff.dropna(thresh=3)

eff

eff.to_csv("eff_data_py.csv")

eff = eff.apply(lambda x: x.fillna(x.median()), axis=0)
eff
