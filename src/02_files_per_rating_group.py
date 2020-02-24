"""
TODO Find files which have measures which could be related to the various star-rating-groups

"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')

PROJECT_LOCATION = "/Users/eklavya/projects/education/formalEducation/DataScience/DataScienceAssignments/HealthCare/Capstone/"

os.chdir(PROJECT_LOCATION)


# Util fuction: line seperator
def print_ln():
    print('-' * 80, '\n')


# ==================
# Data Exploration
## We need to identify the files which give measures for a particular rating group
# ==================
"""
Hospital Overall Rating

"""

hospital_general_information = pd.read_csv("./data/intermediate/Hospital_General_Information.csv", encoding='utf-8')

"""
Mortality National Comparison
"""
# Readmissions_and_Deaths_Hospital.csv

"""
Safety of care national comparison
"""

"""
Readmission national comparison
"""
# Readmissions_and_Deaths_Hospital.csv

"""
Patient experience national comparison
"""
#HOSPITAL_QUARTERLY_HAC_DOMAIN_HOSPITAL_02_26_2016.csv
#HOSPITAL_QUARTERLY_MSPB_6_DECIMALS.csv (doubt)
#Complications - Hospital.csv (doubt)
#READMISSION REDUCTION.csv
#Hvbp_hai_08_26_2016.csv
#HCAHPS - Hospital.csv
#Hvbp_hcahps_08_26_2016.csv
#hvbp_tps_08_26_2016.csv

"""
Effectiveness of care national comparison
"""
#Complications - Hospital.csv
#Healthcare Associated Infections - Hospital.csv
#READMISSION REDUCTION.csv
#Readmissions and Deaths - Hospital.csv → readmission part only
#Timely and Effective Care - Hospital
#hvbp_hcahps_08_26_2016.csv
#Hvbp_scip_08_26_2016.csv
#Ambulatory Surgical Measures-Facility.csv

"""
Timeliness of care national comparison
"""
# Timely_and_Effective_Care_Hospital.csv
## - score is in 3 variants
## - what to do with sample


"""
Efficient use of medical imaging national comparison
"""
# Outpatient_Imaging_Efficiency_Hospital.csv



# TODO Modify this for files in remaining 4 star-rating-groups
# hospital_general_information_orig = pd.read_csv("./data/raw/Hospital_Revised_FlatFiles_20161110/Provider_ID/Hospital_General_Information.csv", encoding = "ISO-8859-1")
#
# # Create a working copy
# hospital_general_information =  hospital_general_information_orig.copy()
#
# hospital_general_information.columns
#
#
# hospital_general_information.drop(['Hospital overall rating footnote',
#                                    'Mortality national comparison footnote',
#                                    'Safety of care national comparison footnote',
#                                    'Readmission national comparison footnote',
#                                    'Patient experience national comparison footnote',
#                                    'Effectiveness of care national comparison footnote',
#                                    'Timeliness of care national comparison footnote',
#                                    'Efficient use of medical imaging national comparison footnote'],
#                                   axis=1,
#                                   inplace=True)
#
# hospital_general_information.to_csv("./data/intermediate/Hospital_General_Information.csv",
#                                     encoding='utf-8')

