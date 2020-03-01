import os

os.chdir(
    "/Users/eklavya/projects/education/formalEducation/DataScience/DataScienceAssignments/HealthCare/Capstone/src/")

print(os.listdir("./"))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
sns.set_style('whitegrid')
sns.set_context('paper')


# ==================================================================
# ==================================================================

# Util function: line seperator
def print_ln():
    print('-' * 80, '\n')


# Function to create a subset of the dataframe
def subset(dataframe, col_name, col_names_list):
    return dataframe.loc[dataframe[col_name].isin(col_names_list)]


def func_numeric(df, col_name):
    df[col_name] = df[col_name].astype(float)
    return df


def func_rename(df):
    old_col_names = df.columns.to_list()
    new_col_names = []
    for a_col_name in old_col_names:
        col_name = a_col_name + "_score"
        new_col_names.append(col_name)

    name_pairs = dict(zip(old_col_names, new_col_names))
    df = df.rename(columns=name_pairs)
    return df


def negative_zscore(dataframe):
    df = dataframe.copy()
    cols = list(df.columns)
    for col in cols:
        df[col] = - (df[col] - df[col].mean()) / df[col].std(ddof=0)
    return df


def positive_zscore(dataframe):
    df = dataframe.copy()
    cols = list(df.columns)
    for col in cols:
        df[col] = (df[col] - df[col].mean()) / df[col].std(ddof=0)
    return df


def subset_by_iqr(df, column, whisker_width=0):
    # Calculate Q1, Q2 and IQR
    q1 = df[column].quantile(0.00125)
    q3 = df[column].quantile(0.99875)
    iqr = q3 - q1
    # Apply filter with respect to IQR, including optional whiskers
    filter = (df[column] >= q1 - whisker_width * iqr) & (df[column] <= q3 + whisker_width * iqr)
    return df.loc[filter][column]


def treat_outliers(dataframe):
    df = dataframe.copy()
    cols = list(df.columns)
    for col in cols:
        df[col] = subset_by_iqr(df, col)
    return df


# ==================================================================
# ==================================================================


read_rawdata = pd.read_csv("Readmissions and Deaths - Hospital.csv",
                           encoding="ISO-8859-1",
                           na_values=["Not Available", "Not Applicable"])

read_rawdata.shape

read_rawdata.head(10)
read_rawdata.info()

read_rawdata['Score'].unique()
read_meas_list = ["READM_30_AMI", "READM_30_CABG", "READM_30_COPD", "READM_30_HF", "READM_30_HIP_KNEE",
                  "READM_30_HOSP_WIDE", "READM_30_PN", "READM_30_STK"]
read_meas_list

read_hosp = read_rawdata.iloc[:, 0:8]
read_hosp.head(5)

read_hosp = read_hosp.drop_duplicates(keep='first')
read_hosp

read_meas = read_rawdata.iloc[:, [0, 9, 12]]
read_meas

print_ln()
read_meas.info()

print_ln()
read_meas.dtypes

read_meas['Score'] = read_meas['Score'].astype(float)
read_meas.dtypes

print_ln()
read_meas

# read_meas['Measure ID'].unique()
# print_ln()
# len(read_meas['Measure ID'].unique())

read_meas = read_meas.loc[read_meas['Measure ID'].isin(read_meas_list)]
read_meas

read_meas_score = read_meas.pivot(index='Provider ID', columns='Measure ID', values='Score')
print_ln()
read_meas_score.columns
print_ln()
read_meas_score
print_ln()
read_meas_score.dtypes
print_ln()
read_meas_score.info()

read_meas_score = func_rename(read_meas_score)
read_meas_score
print_ln()

np.nansum(read_meas_score['READM_30_AMI_score'].unique())

readmission = negative_zscore(read_meas_score)
print_ln()
readmission

readmission = treat_outliers(readmission)
readmission

readmission.to_csv("cleaned_readmission_data_py.csv")

read_master = pd.merge(read_hosp, readmission, on="Provider ID")
read_master.info()
print_ln()
read_master.head()
read_master.to_csv("read_master_data_py.csv")

# ==================================================================
# ==================================================================


mort_rawdata1 = read_rawdata
mort_rawdata1.shape
print_ln()

mort_rawdata2 = pd.read_csv("Complications - Hospital.csv",
                            encoding="ISO-8859-1",
                            na_values=["Not Available", "Not Applicable"])
mort_rawdata2.shape
print_ln()

mort_rawdata2.columns
mort_rawdata2.columns
print_ln()

mort_rawdata1.columns == mort_rawdata2.columns
mort_rawdata = pd.concat([mort_rawdata1, mort_rawdata2])
mort_rawdata.shape
print_ln()

mort_rawdata
mort_meas_list = ["MORT_30_AMI", "MORT_30_CABG", "MORT_30_COPD", "MORT_30_HF", "MORT_30_PN", "MORT_30_STK",
                  "PSI_4_SURG_COMP"]
mort_meas_list
print_ln()

mort_hosp = mort_rawdata.iloc[:, 0:8]

mort_hosp = mort_hosp.drop_duplicates(keep='first')
mort_hosp
print_ln()

mort_hosp.dtypes

mort_meas = mort_rawdata.iloc[:, [0, 9, 12]]
mort_meas.dtypes
print_ln()
mort_meas

mort_meas = mort_meas.loc[mort_meas['Measure ID'].isin(mort_meas_list)]
mort_meas
print_ln()

mort_meas.dtypes
print_ln()

mort_meas = func_numeric(mort_meas, 'Score')
mort_meas.dtypes
print_ln()

mort_meas_score = mort_meas.pivot(index='Provider ID', columns='Measure ID', values='Score')
mort_meas_score
print_ln()

mort_meas_score = func_rename(mort_meas_score)
mort_meas_score
print_ln()

mort_meas_score.columns
print_ln()
mort_meas_score
print_ln()
mort_meas_score.dtypes
print_ln()
mort_meas_score.info()

mortality = mort_meas_score
mortality
print_ln()

mortality = negative_zscore(mortality)
mortality
print_ln()

mortality = treat_outliers(mortality)
mortality
print_ln()
mortality.to_csv("cleaned_mortality_data_py.csv")

mort_master = pd.merge(mort_hosp, mortality, on="Provider ID")
mort_master.info()
print_ln()
mort_master.head()
mort_master.to_csv("mort_master_data_py.csv")

# ==================================================================
# ==================================================================


safe_rawdata1 = mort_rawdata
safe_rawdata1
print_ln()

safe_rawdata2 = pd.read_csv("Healthcare Associated Infections - Hospital.csv", encoding="ISO-8859-1",
                            na_values=["Not Available", "Not Applicable"])
safe_rawdata2
print_ln()
safe_rawdata1 = safe_rawdata1.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 9, 12]]
safe_rawdata1.columns
print_ln()
safe_rawdata1
print_ln()

safe_rawdata2 = safe_rawdata2.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 9, 11]]
safe_rawdata2.columns
print_ln()
safe_rawdata2
print_ln()

safe_rawdata1.columns == safe_rawdata2.columns

safe_rawdata = pd.concat([safe_rawdata1, safe_rawdata2])
safe_meas_list = ["HAI_1_SIR", "HAI_2_SIR", "HAI_3_SIR", "HAI_4_SIR", "HAI_5_SIR", "HAI_6_SIR", "COMP_HIP_KNEE",
                  "PSI_90_SAFETY"]
safe_hosp = safe_rawdata.iloc[:, 0:8]
safe_hosp = safe_hosp.drop_duplicates(keep='first')
safe_hosp
print_ln()
safe_hosp.dtypes

safe_rawdata.columns
print_ln()

safe_meas = safe_rawdata.iloc[:, [0, 8, 9]]
safe_meas
print_ln()

safe_meas = safe_meas.loc[safe_meas['Measure ID'].isin(safe_meas_list)]
safe_meas
safe_meas.dtypes
print_ln()

safe_meas = func_numeric(safe_meas, 'Score')
safe_meas.dtypes
print_ln()

safe_meas_score = safe_meas.pivot(index='Provider ID', columns='Measure ID', values='Score')
safe_meas_score
print_ln()

safe_meas_score = func_rename(safe_meas_score)
safe_meas_score
print_ln()

safety = safe_meas_score
safety
print_ln()

safety = negative_zscore(safety)
safety
print_ln()

safety = treat_outliers(safety)
safety
print_ln()
safety.to_csv("cleaned_safety_data_py.csv")

safe_master = pd.merge(mort_hosp, safety, on="Provider ID")
safe_master
print_ln()
safe_master.to_csv("safe_master_data_py.csv")

# ==================================================================
# ==================================================================


expe_rawdata = pd.read_csv("HCAHPS - Hospital.csv", encoding="ISO-8859-1",
                           na_values=["Not Available", "Not Applicable"])
expe_rawdata
expe_rawdata.columns
print_ln()

expe_new_col_names = {"HCAHPS Question": "Measure Name",
                      "HCAHPS Measure ID": "Measure ID",
                      "HCAHPS Linear Mean Value": "Score"}

expe_rawdata = expe_rawdata.rename(columns=expe_new_col_names)
expe_rawdata.columns
print_ln()

expe_meas_list = ["H_CLEAN_LINEAR_SCORE", "H_COMP_1_LINEAR_SCORE", "H_COMP_2_LINEAR_SCORE", "H_COMP_3_LINEAR_SCORE",
                  "H_COMP_4_LINEAR_SCORE", "H_COMP_5_LINEAR_SCORE", "H_COMP_6_LINEAR_SCORE", "H_COMP_7_LINEAR_SCORE",
                  "H_HSP_RATING_LINEAR_SCORE", "H_QUIET_LINEAR_SCORE", "H_RECMND_LINEAR_SCORE"]

expe_hosp = expe_rawdata.iloc[:, 0:8]
expe_hosp
print_ln()
expe_hosp.dtypes

expe_hosp = expe_hosp.drop_duplicates(keep='first')
expe_hosp
print_ln()
expe_hosp.dtypes

expe_meas = expe_rawdata.iloc[:, [0, 8, 15]]
expe_meas
print_ln()

expe_meas = expe_meas.loc[expe_meas['Measure ID'].isin(expe_meas_list)]
expe_meas
expe_meas.dtypes
print_ln()

expe_meas = func_numeric(expe_meas, 'Score')
expe_meas.dtypes
print_ln()

expe_meas_score = expe_meas.pivot(index='Provider ID', columns='Measure ID', values='Score')
expe_meas_score.dtypes
expe_meas_score
print_ln()

expe_meas_score = func_rename(expe_meas_score)
expe_meas_score
print_ln()

experience = expe_meas_score
experience
print_ln()

experience = positive_zscore(experience)
experience
print_ln()

experience = treat_outliers(experience)
experience
print_ln()
experience.to_csv("cleaned_experience_data_py.csv")

expe_master = pd.merge(expe_hosp, experience, on="Provider ID")
expe_master
print_ln()
expe_master.to_csv("expe_master_data_py.csv")

# ==================================================================
# ==================================================================


medi_rawdata = pd.read_csv("Outpatient Imaging Efficiency - Hospital.csv", encoding="ISO-8859-1",
                           na_values=["Not Available", "Not Applicable"])

medi_meas_list = ["OP_10", "OP_11", "OP_13", "OP_14", "OP_8"]

medi_hosp = medi_rawdata.iloc[:, 0:8]
medi_hosp
print_ln()
medi_hosp.dtypes

medi_hosp = medi_hosp.drop_duplicates(keep='first')
medi_hosp
print_ln()
medi_hosp.dtypes

medi_meas = medi_rawdata.iloc[:, [0, 8, 10]]
medi_meas
print_ln()

medi_meas = subset(medi_meas, 'Measure ID', medi_meas_list)
medi_meas
medi_meas.dtypes
print_ln()

medi_meas = func_numeric(medi_meas, 'Score')
medi_meas.dtypes
print_ln()

medi_meas_score = medi_meas.pivot(index='Provider ID', columns='Measure ID', values='Score')
medi_meas_score
print_ln()

medi_meas_score = func_rename(medi_meas_score)
medi_meas_score
print_ln()

medical = medi_meas_score
medical
print_ln()

medical = negative_zscore(medical)
medical
print_ln()

medical = treat_outliers(medical)
medical
print_ln()
medical.to_csv("cleaned_medical_data_py.csv")

medi_master = pd.merge(medi_hosp, medical, on="Provider ID")
medi_master
print_ln()
medi_master.to_csv("medi_master_data_py.csv")

# ==================================================================
# ==================================================================

time_rawdata = pd.read_csv("Timely and Effective Care - Hospital.csv", encoding="ISO-8859-1",
                           na_values=["Not Available", "Not Applicable"])
time_rawdata
print_ln()

time_meas_list = ["ED_1b", "ED_2b", "OP_18b", "OP_20", "OP_21", "OP_3b", "OP_5"]

time_hosp = time_rawdata.iloc[:, 0:8]
time_hosp
print_ln()
time_hosp.dtypes

time_hosp = time_hosp.drop_duplicates(keep='first')
time_hosp
print_ln()
time_hosp.dtypes

time_meas = time_rawdata.iloc[:, [0, 9, 11]]
time_meas
print_ln()

time_meas = subset(time_meas, 'Measure ID', time_meas_list)
time_meas
time_meas.dtypes
print_ln()

time_meas = func_numeric(time_meas, 'Score')
time_meas.dtypes
print_ln()

time_meas_score = time_meas.pivot(index='Provider ID', columns='Measure ID', values='Score')
time_meas_score
print_ln()

time_meas_score = func_rename(time_meas_score)
time_meas_score
print_ln()

timeliness = time_meas_score
timeliness
print_ln()

timeliness = negative_zscore(timeliness)
timeliness
print_ln()

timeliness = treat_outliers(timeliness)
timeliness
print_ln()
timeliness.to_csv("cleaned_timeliness_data_py.csv")

time_master = pd.merge(time_hosp, timeliness, on="Provider ID")
time_master
print_ln()
time_master.to_csv("time_master_data_py.csv")

# ==================================================================
# ==================================================================

effe_rawdata = time_rawdata
effe_rawdata
print_ln()

effe_meas_list = ["CAC_3", "IMM_2", "IMM_3_OP_27_FAC_ADHPCT", "OP_22", "OP_23", "OP_29", "OP_30", "OP_4", "PC_01",
                  "STK_4", "STK_5", "STK_6", "STK_8", "VTE_1", "VTE_2", "VTE_3", "VTE_5", "VTE_6"]

effe_hosp = effe_rawdata.iloc[:, 0:8]
effe_hosp
print_ln()
effe_hosp.dtypes

effe_hosp = effe_hosp.drop_duplicates(keep='first')
effe_hosp
print_ln()
effe_hosp.dtypes

effe_meas = effe_rawdata.iloc[:, [0, 9, 11]]
effe_meas
print_ln()

effe_meas = subset(effe_meas, 'Measure ID', effe_meas_list)
effe_meas
effe_meas.dtypes
print_ln()

effe_meas = func_numeric(effe_meas, 'Score')
effe_meas.dtypes
print_ln()

effe_meas_score = effe_meas.pivot(index='Provider ID', columns='Measure ID', values='Score')
effe_meas_score
print_ln()

effe_meas_score = func_rename(effe_meas_score)
effe_meas_score
print_ln()

effectiveness = effe_meas_score
effectiveness
print_ln()

positive_measures = [0, 1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16]
effectiveness.iloc[:, positive_measures] = positive_zscore(effectiveness.iloc[:, positive_measures])
effectiveness.iloc[:, positive_measures].columns
print_ln()

negative_measures = [3, 8, 17]
effectiveness.iloc[:, negative_measures] = negative_zscore(effectiveness.iloc[:, negative_measures])
effectiveness.iloc[:, negative_measures].columns
print_ln()

effectiveness = treat_outliers(effectiveness)
effectiveness
print_ln()
effectiveness.to_csv("cleaned_effectiveness_data_py.csv")

effe_master = pd.merge(effe_hosp, effectiveness, on="Provider ID")
effe_master
print_ln()
effe_master.to_csv("effe_master_data_py.csv")

# ==================================================================
# ==================================================================


merge1 = pd.merge(read_master, mort_master)
merge2 = pd.merge(merge1, safe_master)
merge3 = pd.merge(merge2, expe_master)
merge4 = pd.merge(merge3, medi_master)
merge5 = pd.merge(merge4, time_master)
merge6 = pd.merge(merge5, effe_master)

print(merge6.columns.to_list)
print_ln()

merge6
print_ln()

master_data_x = merge6

master_data_x.to_csv("cleaned_master_data_x_py.csv")

master_data_x = master_data_x.drop_duplicates(keep='first')
master_data_x
print_ln()

master_data_x.isnull().sum()

columns_with_missing_data = round(100 * (master_data_x.isnull().sum() / len(master_data_x.index)), 2)
columns_with_missing_data[columns_with_missing_data > 30].plot(kind='bar')
plt.show()

np.sum(master_data_x.isnull().sum().to_list())
print_ln()

master_data_x

hospital_ratings = pd.read_csv("Hospital General Information.csv", encoding="ISO-8859-1",
                               na_values=["Not Available", "Not Applicable"])
hospital_ratings.columns
print_ln()
hospital_ratings
print_ln()

master_data_y = hospital_ratings

hospital_ratings[['Hospital overall rating']].isnull().sum()

master_data_y = master_data_y.iloc[:, [0, 12]]
master_data_y.columns
print_ln()

master_data = pd.merge(master_data_x, master_data_y, on="Provider ID")
master_data
print_ln()

master_data_without_na = master_data[master_data['Hospital overall rating'].notnull()]
master_data_without_na
print_ln()

master_data_without_na

master_data_with_na = master_data[~master_data['Hospital overall rating'].notnull()]
master_data_with_na
print_ln()

np.sum(master_data_without_na.isnull().sum().to_list())

columns_with_missing_data = round(100 * (master_data_without_na.isnull().sum() / len(master_data_without_na.index)), 2)

output = columns_with_missing_data[columns_with_missing_data < 50]
output = list(output.to_dict().keys())
print_ln()

master_data_without_na = master_data_without_na[output]
master_data_without_na

# Impute only relevant numerical columns
master_data_without_na.iloc[:, 8:] = master_data_without_na.iloc[:, 8:].apply(lambda x: x.fillna(x.median()), axis=0)

master_data_without_na

master_data_without_na.isnull().sum()

master_data_without_na = master_data_without_na.drop(master_data_without_na.iloc[:, 1:8], axis=1)
master_data_without_na['Hospital overall rating'], factors_hospital_overall_rating = pd.factorize(
    master_data_without_na['Hospital overall rating'])
cleaned_master_data = master_data_without_na
cleaned_master_data
print_ln()

cleaned_master_data.to_csv("cleaned_master_data_py.csv")
