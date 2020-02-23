"""
TODO Find files which have measures which could be related to the various star-rating-groups

"""

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
# HCAHPS_Hospital.csv
# hvbp_hcahps_08_26_2016.csv
"""
Effectiveness of care national comparison
"""

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



