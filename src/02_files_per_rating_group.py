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

hospital_general_information = pd.read_csv("./data/final/Hospital_General_Information.csv", encoding='utf-8')

"""
Mortality National Comparison
"""

"""
Safety of care national comparison
"""

"""
Readmission national comparison
"""

"""
Patient experience national comparison
"""

"""
Effectiveness of care national comparison
"""

"""
Timeliness of care national comparison
"""

"""
Efficient use of medical imaging national comparison
"""




