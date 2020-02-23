import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')

os.chdir(
    "/Users/eklavya/projects/education/formalEducation/DataScience/DataScienceAssignments/HealthCare/Capstone/")


# Util fuction: line seperator
def print_ln():
    print('-' * 80, '\n')


# ==================
# Data Exploration
# ==================

"""
We start our analysis with the Hospital_General_Information.csv in mind.

"""

hospital_general_information_orig = pd.read_csv("./data/raw/Hospital_Revised_FlatFiles_20161110/Provider_ID/Hospital_General_Information.csv", encoding = "ISO-8859-1")

# Create a working copy
hospital_general_information =  hospital_general_information_orig.copy()

hospital_general_information.head()


hospital_general_information.drop(['Hospital overall rating footnote',
                                   'Mortality national comparison footnote',
                                   'Safety of care national comparison footnote',
                                   'Readmission national comparison footnote',
                                   'Patient experience national comparison footnote',
                                   'Effectiveness of care national comparison footnote',
                                   'Timeliness of care national comparison footnote',
                                   'Efficient use of medical imaging national comparison footnote'],
                                  axis=1,
                                  inplace=True)


hospital_general_information.columns

hospital_general_information =  hospital_general_information.replace('Not Available', np.nan)

hospital_general_information.shape

hospital_general_information.to_csv("./data/final/Hospital_General_Information.csv",
                                    encoding='utf-8')


columns_with_missing_data = round(100 * (hospital_general_information.isnull().sum() / len(hospital_general_information.index)), 2)
columns_with_missing_data_above_30 = columns_with_missing_data[columns_with_missing_data > 30]
columns_with_missing_data_above_30

columns_with_missing_data_above_30.plot(kind='bar')
plt.show()

