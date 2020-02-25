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
#Structural_Measures_Hospital.csv

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
# Readmissions and Deaths - Hospital.csv → readmission part only using the Start date & End date measures (maybe)



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

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# ### Patient Experience

# In[90]:


## 1


# In[91]:


Complications_Hospital_orig = pd.read_csv("Complications_Hospital.csv", encoding = "ISO-8859-1")


# In[92]:


Complications_Hospital =  Complications_Hospital_orig.copy()


# In[93]:


Complications_Hospital.columns


# In[94]:


Complications_Hospital.drop(['Hospital Name',
                                    'Address',
                                    'City',
                                    'State',
                                    'ZIP Code',
                                    'County Name',
                                    'Phone Number',
                                    'Measure Name', 'Compared to National','Denominator','Lower Estimate','Higher Estimate'
                                  ,'Footnote'],
                                   axis=1,
                                  inplace=True)


# In[95]:


Complications_Hospital.to_csv("./intermediate/group_05_patient_experience_national_comparison/Complications_Hospital.csv",
                                   encoding='utf-8')


# In[96]:


## 2


# In[97]:


HCAHPS_Hospital_orig = pd.read_csv("./raw/Hospital_Revised_FlatFiles_20161110/Provider_ID/HCAHPS_Hospital.csv", encoding = "ISO-8859-1")


# In[98]:


HCAHPS_Hospital =  HCAHPS_Hospital_orig.copy()


# In[99]:


HCAHPS_Hospital.columns


# In[100]:


HCAHPS_Hospital.drop(['Hospital Name',
                                    'Address',
                                    'City',
                                    'State',
                                    'ZIP Code',
                                    'County Name','HCAHPS Answer Percent',
       'HCAHPS Answer Percent Footnote',
                                    'Phone Number',
                                    'HCAHPS Question', 'HCAHPS Answer Description','Patient Survey Star Rating Footnote','Number of Completed Surveys', 'Number of Completed Surveys Footnote',
       'Survey Response Rate Percent', 'Survey Response Rate Percent Footnote'
       ],
                                   axis=1,
                                  inplace=True)


# In[101]:


HCAHPS_Hospital.to_csv("./intermediate/group_05_patient_experience_national_comparison/HCAHPS_Hospital.csv",
                                   encoding='utf-8')


# In[102]:


## 3


# In[103]:


HOSPITAL_QUARTERLY_HAC_DOMAIN_HOSPITAL_02_26_2016_orig = pd.read_csv("./raw/Hospital_Revised_FlatFiles_20161110/Both_MeasureID_ And_ProviderID/HOSPITAL_QUARTERLY_HAC_DOMAIN_HOSPITAL_02_26_2016.csv", encoding = "ISO-8859-1")


# In[104]:


HOSPITAL_QUARTERLY_HAC_DOMAIN_HOSPITAL_02_26_2016 =  HOSPITAL_QUARTERLY_HAC_DOMAIN_HOSPITAL_02_26_2016_orig.copy()


# In[105]:


HOSPITAL_QUARTERLY_HAC_DOMAIN_HOSPITAL_02_26_2016.columns


# In[106]:


HOSPITAL_QUARTERLY_HAC_DOMAIN_HOSPITAL_02_26_2016.drop(['Hospital_Name',
                                    'State',
                                    'Fiscal Year',
                                    'Domain_1_Score_Footnote', 'Domain_1_Start_Date',
       'Domain_1_End_Date','AHRQ_PSI_90_Score_Footnote', 'Domain_2_Score_Footnote','CLABSI_Score_Footnote', 'CAUTI_Score_Footnote',
     'SSI_Score_Footnote', 'Domain_2_Start_Date',
       'Domain_2_End_Date','Total_HAC_Score_Footnote'],
                                   axis=1,
                                  inplace=True)


# In[107]:


HOSPITAL_QUARTERLY_HAC_DOMAIN_HOSPITAL_02_26_2016.to_csv("./intermediate/group_05_patient_experience_national_comparison/HOSPITAL_QUARTERLY_HAC_DOMAIN_HOSPITAL_02_26_2016.csv",
                                   encoding='utf-8')


# In[108]:


## 4


# In[109]:


hvbp_hai_08_26_2016_orig = pd.read_csv("./raw/Hospital_Revised_FlatFiles_20161110/Provider_ID/hvbp_hai_08_26_2016.csv", encoding = "ISO-8859-1")


# In[110]:


hvbp_hai_08_26_2016 =  hvbp_hai_08_26_2016_orig.copy()


# In[111]:


hvbp_hai_08_26_2016.columns


# In[112]:


hvbp_hai_08_26_2016.drop(['Hospital Name',
                                    'Address',
                                    'City',
                                    'State',
                                    'Zip Code',
                                    'County Name','SCIP-Inf-2 Achievement Points', 'SCIP-Inf-2 Improvement Points',
       'SCIP-Inf-2 Measure Score',
       'SCIP-Inf-3 Achievement Points', 'SCIP-Inf-3 Improvement Points',
       'SCIP-Inf-3 Measure Score','SCIP-Inf-9 Measure Score',
       'SCIP-Inf-9 Achievement Points', 'SCIP-Inf-9 Improvement Points'],
                                   axis=1,
                                  inplace=True)


# In[113]:


hvbp_hai_08_26_2016.columns


# In[114]:


hvbp_hai_08_26_2016.to_csv("./intermediate/group_05_patient_experience_national_comparison/hvbp_hai_08_26_2016.csv",
                                   encoding='utf-8')


# In[115]:


## 5


# In[116]:


hvbp_hcahps_08_26_2016_orig = pd.read_csv("./raw/Hospital_Revised_FlatFiles_20161110/Provider_ID/hvbp_hcahps_08_26_2016.csv", encoding = "ISO-8859-1")


# In[117]:


hvbp_hcahps_08_26_2016 =  hvbp_hcahps_08_26_2016_orig.copy()


# In[118]:


hvbp_hcahps_08_26_2016.columns


# In[119]:


hvbp_hcahps_08_26_2016.drop(['Hospital Name',
                                    'Address',
                                    'City',
                                    'State',
                                    'ZIP Code',
                                    'County Name',
                                    'Communication with Nurses Achievement Points',
       'Communication with Nurses Improvement Points',
       'Communication with Doctors Achievement Points',
       'Communication with Doctors Improvement Points',
       'Responsiveness of Hospital Staff Achievement Points',
       'Responsiveness of Hospital Staff Improvement Points',
       'Pain Management Achievement Points',
       'Pain Management Improvement Points', 
       'Communication about Medicines Achievement Points',
       'Communication about Medicines Improvement Points',
       'Cleanliness and Quietness of Hospital Environment Achievement Points',
       'Cleanliness and Quietness of Hospital Environment Improvement Points',
       'Discharge Information Achievement Points',
       'Discharge Information Improvement Points',
       'Overall Rating of Hospital Achievement Points',
       'Overall Rating of Hospital Improvement Points'],
                                   axis=1,
                                  inplace=True)


# In[120]:


hvbp_hcahps_08_26_2016.columns


# In[121]:


hvbp_hcahps_08_26_2016.to_csv("./intermediate/group_05_patient_experience_national_comparison/hvbp_hcahps_08_26_2016.csv",
                                   encoding='utf-8')


# In[122]:


## 6


# In[123]:


hvbp_tps_08_26_2016_orig =  pd.read_csv("./raw/Hospital_Revised_FlatFiles_20161110/Provider_ID/hvbp_tps_08_26_2016.csv", encoding = "ISO-8859-1")


# In[124]:


hvbp_tps_08_26_2016 =  hvbp_tps_08_26_2016_orig.copy()


# In[125]:


hvbp_tps_08_26_2016.columns


# In[126]:


hvbp_tps_08_26_2016.drop(['Hospital Name',
                                    'Address',
                                    'City',
                                    'State',
                                    'Zip Code',
                                    'County Name','Unweighted Normalized Clinical Process of Care Domain Score',
       'Unweighted Patient Experience of Care Domain Score',
       'Unweighted Normalized Outcome Domain Score',
       'Weighted Outcome Domain Score',
       'Unweighted Normalized Efficiency Domain Score'],
                                   axis=1,
                                  inplace=True)


# In[127]:


hvbp_tps_08_26_2016.columns


# In[128]:


hvbp_tps_08_26_2016.to_csv("./intermediate/group_05_patient_experience_national_comparison/hvbp_tps_08_26_2016.csv",
                                   encoding='utf-8')


# In[129]:


## 7


# In[130]:


Readmissions_and_Deaths_Hospital_orig =  pd.read_csv("./raw/Hospital_Revised_FlatFiles_20161110/Both_MeasureID_ And_ProviderID/Readmissions_and_Deaths_Hospital.csv", encoding = "ISO-8859-1")


# In[131]:


Readmissions_and_Deaths_Hospital =  Readmissions_and_Deaths_Hospital_orig.copy()


# In[132]:


Readmissions_and_Deaths_Hospital.columns


# In[133]:


Readmissions_and_Deaths_Hospital.drop(['Hospital Name',
                                    'Address',
                                    'City',
                                    'State',
                                    'ZIP Code','Phone Number','Measure Name','Compared to National', 'Denominator',
                                    'County Name',
       'Lower Estimate',
       'Higher Estimate', 'Footnote'],
                                   axis=1,
                                  inplace=True)


# In[134]:


Readmissions_and_Deaths_Hospital.columns


# In[135]:


Readmissions_and_Deaths_Hospital.to_csv("./intermediate/group_05_patient_experience_national_comparison/Readmissions_and_Deaths_Hospital.csv",
                                   encoding='utf-8')


# In[4]:


Structural_Measures_Hospital_orig =  pd.read_csv("./raw/Hospital_Revised_FlatFiles_20161110/Both_MeasureID_ And_ProviderID/Structural_Measures_Hospital.csv", encoding = "ISO-8859-1")


# In[5]:


Structural_Measures_Hospital =  Structural_Measures_Hospital_orig.copy()


# In[6]:


Structural_Measures_Hospital.columns


# In[7]:


Structural_Measures_Hospital.drop(['Hospital Name',
                                    'Address',
                                    'City',
                                    'State',
                                    'ZIP Code', 'County Name','Phone Number','Measure Name',
                                    'County Name', 'Footnote','Measure Start Date',
       'Measure End Date'],
                                   axis=1,
                                  inplace=True)


# In[8]:


Structural_Measures_Hospital.to_csv("./intermediate/group_05_patient_experience_national_comparison/Structural_Measures_Hospital.csv",
                                   encoding='utf-8')


# ### Effectiveness Of Care

# In[136]:


## 1 


# In[137]:


Healthcare_Associated_Infections_Hospital_orig =  pd.read_csv("./raw/Hospital_Revised_FlatFiles_20161110/Both_MeasureID_ And_ProviderID/Healthcare_Associated_Infections_Hospital.csv", encoding = "ISO-8859-1")


# In[138]:


Healthcare_Associated_Infections_Hospital =  Healthcare_Associated_Infections_Hospital_orig.copy()


# In[139]:


Healthcare_Associated_Infections_Hospital.columns


# In[140]:


Healthcare_Associated_Infections_Hospital.drop(['Hospital Name',
                                    'Address',
                                    'City',
                                    'State',
                                    'ZIP Code','Phone Number','Measure Name','Compared to National',
                                    'County Name',
     'Footnote'],
                                   axis=1,
                                  inplace=True)


# In[141]:


Healthcare_Associated_Infections_Hospital.columns


# In[142]:


Healthcare_Associated_Infections_Hospital.to_csv("./intermediate/group_06_effectiveness_of_care_national_comparison/Healthcare_Associated_Infections_Hospital.csv",
                                   encoding='utf-8')


# In[143]:


## 2


# In[144]:


Ambulatory_Surgical_Measures_Facility_orig =  pd.read_csv("./raw/Hospital_Revised_FlatFiles_20161110/Provider_ID/Ambulatory_Surgical_Measures_Facility.csv", encoding = "ISO-8859-1")


# In[145]:


Ambulatory_Surgical_Measures_Facility =  Ambulatory_Surgical_Measures_Facility_orig.copy()


# In[146]:


Ambulatory_Surgical_Measures_Facility.columns


# In[147]:


Ambulatory_Surgical_Measures_Facility.drop(['ASC_Name',
                                    'City',
                                    'State',
                                    'ZIP_Code','Year', 'ASC1_Footnote', 
       'ASC2_Footnote', 'ASC3_Footnote',
        'ASC4_Footnote', 
       'ASC5_Footnote', 'ASC6_Footnote',
       'ASC_7_Volume', 'ASC_7_Gastrointestinal', 'ASC_7_Eye',
       'ASC_7_Musculoskeletal', 'ASC_7_Skin', 'ASC_7_Genitourinary',
       'ASC_7_Multi_System', 'ASC_7_Nervous_System', 'ASC_7_Respiratory',
       'ASC7_Footnote', 'ASC_6_7_Encounter_Start_Date',
       'ASC_6_7_Encounter_End_Date', 'ASC8_Footnote',
       'ASC_8_Encounter_Date', 'ASC9_Footnote',
       'ASC10_Footnote', 'ASC_9_10_Encounter_Start_Date',
       'ASC_9_10_Encounter_End_Date'],
                                   axis=1,
                                  inplace=True)


# In[148]:


Ambulatory_Surgical_Measures_Facility.to_csv("./intermediate/group_06_effectiveness_of_care_national_comparison/Ambulatory_Surgical_Measures_Facility.csv",
                                   encoding='utf-8')


# In[149]:


## 3 


# In[150]:


hvbp_scip_08_26_2016_orig =  pd.read_csv("./raw/Hospital_Revised_FlatFiles_20161110/Provider_ID/hvbp_scip_08_26_2016.csv", encoding = "ISO-8859-1")


# In[151]:


hvbp_scip_08_26_2016 =  hvbp_scip_08_26_2016_orig.copy()


# In[152]:


hvbp_scip_08_26_2016.columns


# In[153]:


hvbp_scip_08_26_2016.drop(['Hospital Name','Address',
                                    'City',
                                    'State',
                                    'ZIP Code','County Name',  'SCIP-Card-2 Performance Rate',
       'SCIP-Card-2 Achievement Points', 'SCIP-Card-2 Improvement Points',
    'SCIP-VTE-2 Performance Rate',
       'SCIP-VTE-2 Achievement Points', 'SCIP-VTE-2 Improvement Points',],
                                   axis=1,
                                  inplace=True)


# In[154]:


hvbp_scip_08_26_2016.columns


# In[155]:


hvbp_scip_08_26_2016.to_csv("./intermediate/group_06_effectiveness_of_care_national_comparison/hvbp_scip_08_26_2016.csv",
                                   encoding='utf-8')


# In[156]:


## 4 


# In[157]:


READMISSION_REDUCTION_orig =  pd.read_csv("./raw/Hospital_Revised_FlatFiles_20161110/Both_MeasureID_ And_ProviderID/READMISSION_REDUCTION.csv", encoding = "ISO-8859-1")


# In[158]:


READMISSION_REDUCTION =  READMISSION_REDUCTION_orig.copy()


# In[159]:


READMISSION_REDUCTION.columns


# In[160]:


READMISSION_REDUCTION.drop(['Hospital Name',
                                    'State',
                                  'Footnote'],
                                   axis=1,
                                  inplace=True)


# In[161]:


READMISSION_REDUCTION.to_csv("./intermediate/group_06_effectiveness_of_care_national_comparison/READMISSION_REDUCTION.csv",
                                   encoding='utf-8')


# In[162]:


## 5


# In[163]:


Readmissions_and_Deaths_Hospital_orig =  pd.read_csv("./raw/Hospital_Revised_FlatFiles_20161110/Both_MeasureID_ And_ProviderID/Readmissions_and_Deaths_Hospital.csv", encoding = "ISO-8859-1")


# In[164]:


Readmissions_and_Deaths_Hospital =  Readmissions_and_Deaths_Hospital_orig.copy()


# In[165]:


Readmissions_and_Deaths_Hospital.columns


# In[166]:


Readmissions_and_Deaths_Hospital.drop(['Hospital Name', 'Address', 'City', 'State', 'ZIP Code',
       'County Name', 'Phone Number', 'Measure Name',
      'Denominator','Lower Estimate',
       'Higher Estimate', 'Footnote'],
                                   axis=1,
                                  inplace=True)


# In[167]:


Readmissions_and_Deaths_Hospital.to_csv("./intermediate/group_06_effectiveness_of_care_national_comparison/Readmissions_and_Deaths_Hospital.csv",
                                   encoding='utf-8')


# In[168]:


## 6 


# In[169]:


Timely_and_Effective_Care_Hospital_orig =  pd.read_csv("./raw/Hospital_Revised_FlatFiles_20161110/Both_MeasureID_ And_ProviderID/Timely_and_Effective_Care_Hospital.csv", encoding = "ISO-8859-1")


# In[170]:


Timely_and_Effective_Care_Hospital =  Timely_and_Effective_Care_Hospital_orig.copy()


# In[171]:


Timely_and_Effective_Care_Hospital.columns


# In[172]:


Timely_and_Effective_Care_Hospital.drop(['Hospital Name', 'Address', 'City', 'State', 'ZIP Code',
       'County Name', 'Phone Number',
       'Measure Name','Footnote'],
                                   axis=1,
                                  inplace=True)


# In[173]:


Timely_and_Effective_Care_Hospital.to_csv("./intermediate/group_06_effectiveness_of_care_national_comparison/Timely_and_Effective_Care_Hospital.csv",
                                   encoding='utf-8')


# ### Use Of Medical Imaging

# In[174]:


Outpatient_Imaging_Efficiency_Hospital =  pd.read_csv("./raw/Hospital_Revised_FlatFiles_20161110/Both_MeasureID_ And_ProviderID/Outpatient_Imaging_Efficiency_Hospital.csv", encoding = "ISO-8859-1")


# In[175]:


Outpatient_Imaging_Efficiency_Hospital =  Outpatient_Imaging_Efficiency_Hospital.copy()


# In[176]:


Outpatient_Imaging_Efficiency_Hospital.columns


# In[177]:


Outpatient_Imaging_Efficiency_Hospital.drop(['Hospital Name', 'Address', 'City', 'State', 'ZIP Code',
       'County Name', 'Phone Number',
       'Measure Name','Footnote'],
                                   axis=1,
                                  inplace=True)


# In[178]:


Outpatient_Imaging_Efficiency_Hospital.to_csv("./intermediate/group_08_efficient_use_of_medical_imaging_national_comparison/Outpatient_Imaging_Efficiency_Hospital.csv",
                                   encoding='utf-8')


# In[ ]:



