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


def process_raw_csv(input_csv_name, output_csv_group_name, columns_to_be_dropped, replace_with_nan=""):
    # compute the output file name
    input_csv_location = "./data/raw/Hospital_Revised_FlatFiles_20161110/" + input_csv_name
    output_csv_location = "./data/intermediate/" + output_csv_group_name + "/" + input_csv_name

    # copy df and drop columns
    orig_df = pd.read_csv(input_csv_location, encoding="ISO-8859-1")
    temp_df = orig_df.copy()
    temp_df.drop(columns_to_be_dropped, axis=1, inplace=True)

    # process nan values
    if replace_with_nan != "":
        temp_df.replace(replace_with_nan, np.nan)

    # output the new csv
    temp_df.to_csv(output_csv_location, encoding='utf-8')

    # return the temp_df for further processing
    return temp_df


process_raw_csv(input_csv_name="Hospital_General_Information.csv",
                output_csv_group_name="group_05_patient_experience_national_comparison",
                columns_to_be_dropped=['ZIP Code',
                                       'County Name',
                                       'State',
                                       'City',
                                       'Phone Number',
                                       'Address',
                                       'Hospital Name',
                                       'Hospital Ownership',  # NOTE maybe imporantant
                                       'Hospital overall rating footnote',
                                       'Mortality national comparison footnote',
                                       'Safety of care national comparison footnote',
                                       'Readmission national comparison footnote',
                                       'Patient experience national comparison footnote',
                                       'Effectiveness of care national comparison footnote',
                                       'Timeliness of care national comparison footnote',
                                       'Efficient use of medical imaging national comparison footnote'],
                replace_with_nan="Not Available")

hospital_general_information_orig = pd.read_csv(
    "./data/raw/Hospital_Revised_FlatFiles_20161110/Provider_ID/Hospital_General_Information.csv",
    encoding="ISO-8859-1")

# Create a working copy
hospital_general_information = hospital_general_information_orig.copy()

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

hospital_general_information = hospital_general_information.replace('Not Available', np.nan)

hospital_general_information.shape

# TODO encode the Below/Same/Above values
hospital_general_information.to_csv("./data/intermediate/Hospital_General_Information.csv",
                                    encoding='utf-8')

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
# HOSPITAL_QUARTERLY_HAC_DOMAIN_HOSPITAL_02_26_2016.csv
# HOSPITAL_QUARTERLY_MSPB_6_DECIMALS.csv (doubt)
# Complications - Hospital.csv (doubt)
# READMISSION REDUCTION.csv
# Hvbp_hai_08_26_2016.csv
# HCAHPS - Hospital.csv
# Hvbp_hcahps_08_26_2016.csv
# hvbp_tps_08_26_2016.csv
# Structural_Measures_Hospital.csv

"""
Effectiveness of care national comparison
"""
# Complications - Hospital.csv
# Healthcare Associated Infections - Hospital.csv
# READMISSION REDUCTION.csv
# Readmissions and Deaths - Hospital.csv → readmission part only
# Timely and Effective Care - Hospital
# hvbp_hcahps_08_26_2016.csv
# Hvbp_scip_08_26_2016.csv
# Ambulatory Surgical Measures-Facility.csv

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


# ### Patient Experience

Complications_Hospital_orig = pd.read_csv("Complications_Hospital.csv", encoding="ISO-8859-1")

Complications_Hospital = Complications_Hospital_orig.copy()

Complications_Hospital.columns

Complications_Hospital.drop(['Hospital Name',
                             'Address',
                             'City',
                             'State',
                             'ZIP Code',
                             'County Name',
                             'Phone Number',
                             'Measure Name', 'Compared to National', 'Denominator', 'Lower Estimate', 'Higher Estimate'
                                , 'Footnote'],
                            axis=1,
                            inplace=True)

Complications_Hospital.to_csv(
    "./intermediate/group_05_patient_experience_national_comparison/Complications_Hospital.csv",
    encoding='utf-8')

HCAHPS_Hospital_orig = pd.read_csv("./raw/Hospital_Revised_FlatFiles_20161110/Provider_ID/HCAHPS_Hospital.csv",
                                   encoding="ISO-8859-1")

HCAHPS_Hospital = HCAHPS_Hospital_orig.copy()



HCAHPS_Hospital.columns



HCAHPS_Hospital.drop(['Hospital Name',
                      'Address',
                      'City',
                      'State',
                      'ZIP Code',
                      'County Name', 'HCAHPS Answer Percent',
                      'HCAHPS Answer Percent Footnote',
                      'Phone Number',
                      'HCAHPS Question', 'HCAHPS Answer Description', 'Patient Survey Star Rating Footnote',
                      'Number of Completed Surveys', 'Number of Completed Surveys Footnote',
                      'Survey Response Rate Percent', 'Survey Response Rate Percent Footnote'
                      ],
                     axis=1,
                     inplace=True)



HCAHPS_Hospital.to_csv("./intermediate/group_05_patient_experience_national_comparison/HCAHPS_Hospital.csv",
                       encoding='utf-8')

HOSPITAL_QUARTERLY_HAC_DOMAIN_HOSPITAL_02_26_2016_orig = pd.read_csv(
    "./raw/Hospital_Revised_FlatFiles_20161110/Both_MeasureID_ And_ProviderID/HOSPITAL_QUARTERLY_HAC_DOMAIN_HOSPITAL_02_26_2016.csv",
    encoding="ISO-8859-1")

HOSPITAL_QUARTERLY_HAC_DOMAIN_HOSPITAL_02_26_2016 = HOSPITAL_QUARTERLY_HAC_DOMAIN_HOSPITAL_02_26_2016_orig.copy()



HOSPITAL_QUARTERLY_HAC_DOMAIN_HOSPITAL_02_26_2016.columns



HOSPITAL_QUARTERLY_HAC_DOMAIN_HOSPITAL_02_26_2016.drop(['Hospital_Name',
                                                        'State',
                                                        'Fiscal Year',
                                                        'Domain_1_Score_Footnote', 'Domain_1_Start_Date',
                                                        'Domain_1_End_Date', 'AHRQ_PSI_90_Score_Footnote',
                                                        'Domain_2_Score_Footnote', 'CLABSI_Score_Footnote',
                                                        'CAUTI_Score_Footnote',
                                                        'SSI_Score_Footnote', 'Domain_2_Start_Date',
                                                        'Domain_2_End_Date', 'Total_HAC_Score_Footnote'],
                                                       axis=1,
                                                       inplace=True)

HOSPITAL_QUARTERLY_HAC_DOMAIN_HOSPITAL_02_26_2016.to_csv(
    "./intermediate/group_05_patient_experience_national_comparison/HOSPITAL_QUARTERLY_HAC_DOMAIN_HOSPITAL_02_26_2016.csv",
    encoding='utf-8')

hvbp_hai_08_26_2016_orig = pd.read_csv("./raw/Hospital_Revised_FlatFiles_20161110/Provider_ID/hvbp_hai_08_26_2016.csv",
                                       encoding="ISO-8859-1")

hvbp_hai_08_26_2016 = hvbp_hai_08_26_2016_orig.copy()



hvbp_hai_08_26_2016.columns



hvbp_hai_08_26_2016.drop(['Hospital Name',
                          'Address',
                          'City',
                          'State',
                          'Zip Code',
                          'County Name', 'SCIP-Inf-2 Achievement Points', 'SCIP-Inf-2 Improvement Points',
                          'SCIP-Inf-2 Measure Score',
                          'SCIP-Inf-3 Achievement Points', 'SCIP-Inf-3 Improvement Points',
                          'SCIP-Inf-3 Measure Score', 'SCIP-Inf-9 Measure Score',
                          'SCIP-Inf-9 Achievement Points', 'SCIP-Inf-9 Improvement Points'],
                         axis=1,
                         inplace=True)



hvbp_hai_08_26_2016.columns



hvbp_hai_08_26_2016.to_csv("./intermediate/group_05_patient_experience_national_comparison/hvbp_hai_08_26_2016.csv",
                           encoding='utf-8')

hvbp_hcahps_08_26_2016_orig = pd.read_csv(
    "./raw/Hospital_Revised_FlatFiles_20161110/Provider_ID/hvbp_hcahps_08_26_2016.csv", encoding="ISO-8859-1")

hvbp_hcahps_08_26_2016 = hvbp_hcahps_08_26_2016_orig.copy()



hvbp_hcahps_08_26_2016.columns



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



hvbp_hcahps_08_26_2016.columns

hvbp_hcahps_08_26_2016.to_csv(
    "./intermediate/group_05_patient_experience_national_comparison/hvbp_hcahps_08_26_2016.csv",
    encoding='utf-8')

hvbp_tps_08_26_2016_orig = pd.read_csv("./raw/Hospital_Revised_FlatFiles_20161110/Provider_ID/hvbp_tps_08_26_2016.csv",
                                       encoding="ISO-8859-1")

hvbp_tps_08_26_2016 = hvbp_tps_08_26_2016_orig.copy()



hvbp_tps_08_26_2016.columns


hvbp_tps_08_26_2016.drop(['Hospital Name',
                          'Address',
                          'City',
                          'State',
                          'Zip Code',
                          'County Name', 'Unweighted Normalized Clinical Process of Care Domain Score',
                          'Unweighted Patient Experience of Care Domain Score',
                          'Unweighted Normalized Outcome Domain Score',
                          'Weighted Outcome Domain Score',
                          'Unweighted Normalized Efficiency Domain Score'],
                         axis=1,
                         inplace=True)



hvbp_tps_08_26_2016.columns



hvbp_tps_08_26_2016.to_csv("./intermediate/group_05_patient_experience_national_comparison/hvbp_tps_08_26_2016.csv",
                           encoding='utf-8')

Readmissions_and_Deaths_Hospital_orig = pd.read_csv(
    "./raw/Hospital_Revised_FlatFiles_20161110/Both_MeasureID_ And_ProviderID/Readmissions_and_Deaths_Hospital.csv",
    encoding="ISO-8859-1")

Readmissions_and_Deaths_Hospital = Readmissions_and_Deaths_Hospital_orig.copy()


Readmissions_and_Deaths_Hospital.columns


Readmissions_and_Deaths_Hospital.drop(['Hospital Name',
                                       'Address',
                                       'City',
                                       'State',
                                       'ZIP Code', 'Phone Number', 'Measure Name', 'Compared to National',
                                       'Denominator',
                                       'County Name',
                                       'Lower Estimate',
                                       'Higher Estimate', 'Footnote'],
                                      axis=1,
                                      inplace=True)



Readmissions_and_Deaths_Hospital.columns

Readmissions_and_Deaths_Hospital.to_csv(
    "./intermediate/group_05_patient_experience_national_comparison/Readmissions_and_Deaths_Hospital.csv",
    encoding='utf-8')

Structural_Measures_Hospital_orig = pd.read_csv(
    "./raw/Hospital_Revised_FlatFiles_20161110/Both_MeasureID_ And_ProviderID/Structural_Measures_Hospital.csv",
    encoding="ISO-8859-1")

Structural_Measures_Hospital = Structural_Measures_Hospital_orig.copy()



Structural_Measures_Hospital.columns



Structural_Measures_Hospital.drop(['Hospital Name',
                                   'Address',
                                   'City',
                                   'State',
                                   'ZIP Code', 'County Name', 'Phone Number', 'Measure Name',
                                   'County Name', 'Footnote', 'Measure Start Date',
                                   'Measure End Date'],
                                  axis=1,
                                  inplace=True)

Structural_Measures_Hospital.to_csv(
    "./intermediate/group_05_patient_experience_national_comparison/Structural_Measures_Hospital.csv",
    encoding='utf-8')

# ### Effectiveness Of Care


Healthcare_Associated_Infections_Hospital_orig = pd.read_csv(
    "./raw/Hospital_Revised_FlatFiles_20161110/Both_MeasureID_ And_ProviderID/Healthcare_Associated_Infections_Hospital.csv",
    encoding="ISO-8859-1")

Healthcare_Associated_Infections_Hospital = Healthcare_Associated_Infections_Hospital_orig.copy()


Healthcare_Associated_Infections_Hospital.columns


Healthcare_Associated_Infections_Hospital.drop(['Hospital Name',
                                                'Address',
                                                'City',
                                                'State',
                                                'ZIP Code', 'Phone Number', 'Measure Name', 'Compared to National',
                                                'County Name',
                                                'Footnote'],
                                               axis=1,
                                               inplace=True)


Healthcare_Associated_Infections_Hospital.columns

Healthcare_Associated_Infections_Hospital.to_csv(
    "./intermediate/group_06_effectiveness_of_care_national_comparison/Healthcare_Associated_Infections_Hospital.csv",
    encoding='utf-8')

Ambulatory_Surgical_Measures_Facility_orig = pd.read_csv(
    "./raw/Hospital_Revised_FlatFiles_20161110/Provider_ID/Ambulatory_Surgical_Measures_Facility.csv",
    encoding="ISO-8859-1")

Ambulatory_Surgical_Measures_Facility = Ambulatory_Surgical_Measures_Facility_orig.copy()


Ambulatory_Surgical_Measures_Facility.columns

Ambulatory_Surgical_Measures_Facility.drop(['ASC_Name',
                                            'City',
                                            'State',
                                            'ZIP_Code', 'Year', 'ASC1_Footnote',
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

Ambulatory_Surgical_Measures_Facility.to_csv(
    "./intermediate/group_06_effectiveness_of_care_national_comparison/Ambulatory_Surgical_Measures_Facility.csv",
    encoding='utf-8')

hvbp_scip_08_26_2016_orig = pd.read_csv(
    "./raw/Hospital_Revised_FlatFiles_20161110/Provider_ID/hvbp_scip_08_26_2016.csv", encoding="ISO-8859-1")

hvbp_scip_08_26_2016 = hvbp_scip_08_26_2016_orig.copy()


hvbp_scip_08_26_2016.columns

hvbp_scip_08_26_2016.drop(['Hospital Name', 'Address',
                           'City',
                           'State',
                           'ZIP Code', 'County Name', 'SCIP-Card-2 Performance Rate',
                           'SCIP-Card-2 Achievement Points', 'SCIP-Card-2 Improvement Points',
                           'SCIP-VTE-2 Performance Rate',
                           'SCIP-VTE-2 Achievement Points', 'SCIP-VTE-2 Improvement Points', ],
                          axis=1,
                          inplace=True)


hvbp_scip_08_26_2016.columns

hvbp_scip_08_26_2016.to_csv(
    "./intermediate/group_06_effectiveness_of_care_national_comparison/hvbp_scip_08_26_2016.csv",
    encoding='utf-8')

READMISSION_REDUCTION_orig = pd.read_csv(
    "./raw/Hospital_Revised_FlatFiles_20161110/Both_MeasureID_ And_ProviderID/READMISSION_REDUCTION.csv",
    encoding="ISO-8859-1")

READMISSION_REDUCTION = READMISSION_REDUCTION_orig.copy()

READMISSION_REDUCTION.columns


READMISSION_REDUCTION.drop(['Hospital Name',
                            'State',
                            'Footnote'],
                           axis=1,
                           inplace=True)

READMISSION_REDUCTION.to_csv(
    "./intermediate/group_06_effectiveness_of_care_national_comparison/READMISSION_REDUCTION.csv",
    encoding='utf-8')

Readmissions_and_Deaths_Hospital_orig = pd.read_csv(
    "./raw/Hospital_Revised_FlatFiles_20161110/Both_MeasureID_ And_ProviderID/Readmissions_and_Deaths_Hospital.csv",
    encoding="ISO-8859-1")

Readmissions_and_Deaths_Hospital = Readmissions_and_Deaths_Hospital_orig.copy()


Readmissions_and_Deaths_Hospital.columns



Readmissions_and_Deaths_Hospital.drop(['Hospital Name', 'Address', 'City', 'State', 'ZIP Code',
                                       'County Name', 'Phone Number', 'Measure Name',
                                       'Denominator', 'Lower Estimate',
                                       'Higher Estimate', 'Footnote'],
                                      axis=1,
                                      inplace=True)

Readmissions_and_Deaths_Hospital.to_csv(
    "./intermediate/group_06_effectiveness_of_care_national_comparison/Readmissions_and_Deaths_Hospital.csv",
    encoding='utf-8')

Timely_and_Effective_Care_Hospital_orig = pd.read_csv(
    "./raw/Hospital_Revised_FlatFiles_20161110/Both_MeasureID_ And_ProviderID/Timely_and_Effective_Care_Hospital.csv",
    encoding="ISO-8859-1")

Timely_and_Effective_Care_Hospital = Timely_and_Effective_Care_Hospital_orig.copy()


Timely_and_Effective_Care_Hospital.columns


Timely_and_Effective_Care_Hospital.drop(['Hospital Name', 'Address', 'City', 'State', 'ZIP Code',
                                         'County Name', 'Phone Number',
                                         'Measure Name', 'Footnote'],
                                        axis=1,
                                        inplace=True)

Timely_and_Effective_Care_Hospital.to_csv(
    "./intermediate/group_06_effectiveness_of_care_national_comparison/Timely_and_Effective_Care_Hospital.csv",
    encoding='utf-8')

# ### Use Of Medical Imaging

Outpatient_Imaging_Efficiency_Hospital = pd.read_csv(
    "./raw/Hospital_Revised_FlatFiles_20161110/Both_MeasureID_ And_ProviderID/Outpatient_Imaging_Efficiency_Hospital.csv",
    encoding="ISO-8859-1")

Outpatient_Imaging_Efficiency_Hospital = Outpatient_Imaging_Efficiency_Hospital.copy()

Outpatient_Imaging_Efficiency_Hospital.columns


Outpatient_Imaging_Efficiency_Hospital.drop(['Hospital Name', 'Address', 'City', 'State', 'ZIP Code',
                                             'County Name', 'Phone Number',
                                             'Measure Name', 'Footnote'],
                                            axis=1,
                                            inplace=True)

Outpatient_Imaging_Efficiency_Hospital.to_csv(
    "./intermediate/group_08_efficient_use_of_medical_imaging_national_comparison/Outpatient_Imaging_Efficiency_Hospital.csv",
    encoding='utf-8')
