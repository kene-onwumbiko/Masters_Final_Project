# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:55:26 2024

@author: keneo
"""

# Import libraries
import pandas as pd


# on_values_2 = ["Campus", "Group", "School / Department", "Level", "Category", "Number of Applications", "Date", "Number of Acceptances"]
# data = sep_2020_2023.merge(sep_2019_2022, on = on_values_2, how = "outer")

# # Correct the date format
# sep_2019_2022["Date"] = pd.to_datetime(sep_2019_2022["Date"]).dt.date





########## SEPTEMBER 2017-2020 APPLICATIONS DATASET ##########
# Import the September 2017-2020 applications dataset
sep_2017_2020_applications = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 30 October  2023 - 2020.xlsx",
                                           sheet_name = "Sep_2017-2020_Applications_2")

# Unpivot the September 2017-2020 applications dataset
id_vars = ["Campus", "Group", "School / Department", "Level"]
value_vars = ["Home", "Overseas", "Unknown", "Home.1", "Overseas.1", "Unknown.1", "Home.2", 
              "Overseas.2", "Unknown.2", "Home.3", "Overseas.3", "Unknown.3"]

new_sep_2017_2020_applications = sep_2017_2020_applications.melt(id_vars = id_vars, value_vars = value_vars, 
                                                                 var_name = "Category", 
                                                                 value_name = "Number of Applicantions")

# Create a function to get the Date based on "Category" and also modify "Category"
def get_date_sep_2017_2020(row):
    category = row["Category"]
    if category == "Home":
        row["Date"] = "Sep 2020"
    elif category == "Home.1":
        row["Date"] = "Sep 2019"
        row["Category"] = "Home"
    elif category == "Home.2":
        row["Date"] = "Sep 2018"
        row["Category"] = "Home"
    elif category == "Home.3":
        row["Date"] = "Sep 2017"
        row["Category"] = "Home"
    elif category == "Overseas":
        row["Date"] = "Sep 2020"
    elif category == "Overseas.1":
        row["Date"] = "Sep 2019"
        row["Category"] = "Overseas"
    elif category == "Overseas.2":
        row["Date"] = "Sep 2018"
        row["Category"] = "Overseas"
    elif category == "Overseas.3":
        row["Date"] = "Sep 2017"
        row["Category"] = "Overseas"
    elif category == "Unknown":
        row["Date"] = "Sep 2020"
    elif category == "Unknown.1":
        row["Date"] = "Sep 2019"
        row["Category"] = "Unknown"
    elif category == "Unknown.2":
        row["Date"] = "Sep 2018"
        row["Category"] = "Unknown"
    elif category == "Unknown.3":
        row["Date"] = "Sep 2017"
        row["Category"] = "Unknown"
    return row

# Apply the function to the September 2017-2020 applications dataset
new_sep_2017_2020_applications = new_sep_2017_2020_applications.apply(get_date_sep_2017_2020, axis = 1)





########## SEPTEMBER 2017-2020 ACCEPTANCES DATASET ##########
# Import the September 2017-2020 acceptances dataset
sep_2017_2020_acceptances = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 30 October  2023 - 2020.xlsx",
                                          sheet_name = "Sep_2017-2020_Acceptances_2")

# Unpivot the September 2017-2020 acceptances dataset
new_sep_2017_2020_acceptances = sep_2017_2020_acceptances.melt(id_vars = id_vars, value_vars = value_vars, 
                                                               var_name = "Category", 
                                                               value_name = "Number of Acceptances")

# Apply the function to the September 2017-2020 acceptances dataset
new_sep_2017_2020_acceptances = new_sep_2017_2020_acceptances.apply(get_date_sep_2017_2020, axis = 1)

# Merge the applications and acceptance datasets
on_values = ["Campus", "Group", "School / Department", "Level", "Category", "Date"]
sep_2017_2020 = new_sep_2017_2020_applications.merge(new_sep_2017_2020_acceptances, on = on_values, 
                                                     how = "outer")





########## SEPTEMBER 2018-2021 APPLICATIONS DATASET ##########
# Import the September 2018-2021 applications dataset
sep_2018_2021_applications = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 30 October 2023 - 2021.xlsx",
                                           sheet_name = "Sep_2018-2021_Applications_2")

# Unpivot the September 2018-2021 applications dataset
new_sep_2018_2021_applications = sep_2018_2021_applications.melt(id_vars = id_vars, value_vars = value_vars, 
                                                                 var_name = "Category", 
                                                                 value_name = "Number of Applications")

# Create a function to get the Date based on "Category" and also modify "Category"
def get_date_sep_2018_2021(row):
    category = row["Category"]
    if category == "Home":
        row["Date"] = "Sep 2021"
    elif category == "Home.1":
        row["Date"] = "Sep 2020"
        row["Category"] = "Home"
    elif category == "Home.2":
        row["Date"] = "Sep 2019"
        row["Category"] = "Home"
    elif category == "Home.3":
        row["Date"] = "Sep 2018"
        row["Category"] = "Home"
    elif category == "Overseas":
        row["Date"] = "Sep 2021"
    elif category == "Overseas.1":
        row["Date"] = "Sep 2020"
        row["Category"] = "Overseas"
    elif category == "Overseas.2":
        row["Date"] = "Sep 2019"
        row["Category"] = "Overseas"
    elif category == "Overseas.3":
        row["Date"] = "Sep 2018"
        row["Category"] = "Overseas"
    elif category == "Unknown":
        row["Date"] = "Sep 2021"
    elif category == "Unknown.1":
        row["Date"] = "Sep 2020"
        row["Category"] = "Unknown"
    elif category == "Unknown.2":
        row["Date"] = "Sep 2019"
        row["Category"] = "Unknown"
    elif category == "Unknown.3":
        row["Date"] = "Sep 2018"
        row["Category"] = "Unknown"
    return row

# Apply the function to the September 2018-2021 applications dataset
new_sep_2018_2021_applications = new_sep_2018_2021_applications.apply(get_date_sep_2018_2021, axis = 1)





########## SEPTEMBER 2018-2021 ACCEPTANCES DATASET ##########
# Import the September 2018-2021 acceptances dataset
sep_2018_2021_acceptances = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 30 October 2023 - 2021.xlsx",
                                          sheet_name = "Sep_2018-2021_Acceptances_2")

# Unpivot the September 2018-2021 acceptances dataset
new_sep_2018_2021_acceptances = sep_2018_2021_acceptances.melt(id_vars = id_vars, value_vars = value_vars, 
                                                               var_name = "Category", 
                                                               value_name = "Number of Acceptances")

# Apply the function to the September 2018-2021 acceptances dataset
new_sep_2018_2021_acceptances = new_sep_2018_2021_acceptances.apply(get_date_sep_2018_2021, axis = 1)

# Merge the applications and acceptance datasets
sep_2018_2021 = new_sep_2018_2021_applications.merge(new_sep_2018_2021_acceptances, on = on_values, 
                                                     how = "outer")





########## SEPTEMBER 2019-2022 APPLICATIONS DATASET ##########
# Import the September 2019-2022 applications dataset
sep_2019_2022_applications = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 30 October 2023 - 2022.xlsx",
                                           sheet_name = "Sep_2019-2022_Applications_2")

# Unpivot the September 2019-2022 applications dataset
new_sep_2019_2022_applications = sep_2019_2022_applications.melt(id_vars = id_vars, value_vars = value_vars, 
                                                                 var_name = "Category", 
                                                                 value_name = "Number of Applications")

# Create a function to get the Date based on "Category" and also modify "Category"
def get_date_sep_2019_2022(row):
    category = row["Category"]
    if category == "Home":
        row["Date"] = "Sep 2022"
    elif category == "Home.1":
        row["Date"] = "Sep 2021"
        row["Category"] = "Home"
    elif category == "Home.2":
        row["Date"] = "Sep 2020"
        row["Category"] = "Home"
    elif category == "Home.3":
        row["Date"] = "Sep 2019"
        row["Category"] = "Home"
    elif category == "Overseas":
        row["Date"] = "Sep 2022"
    elif category == "Overseas.1":
        row["Date"] = "Sep 2021"
        row["Category"] = "Overseas"
    elif category == "Overseas.2":
        row["Date"] = "Sep 2020"
        row["Category"] = "Overseas"
    elif category == "Overseas.3":
        row["Date"] = "Sep 2019"
        row["Category"] = "Overseas"
    elif category == "Unknown":
        row["Date"] = "Sep 2022"
    elif category == "Unknown.1":
        row["Date"] = "Sep 2021"
        row["Category"] = "Unknown"
    elif category == "Unknown.2":
        row["Date"] = "Sep 2020"
        row["Category"] = "Unknown"
    elif category == "Unknown.3":
        row["Date"] = "Sep 2019"
        row["Category"] = "Unknown"
    return row

# Apply the function to the September 2019-2022 applications dataset
new_sep_2019_2022_applications = new_sep_2019_2022_applications.apply(get_date_sep_2019_2022, axis = 1)





########## SEPTEMBER 2019-2022 ACCEPTANCES DATASET ##########
# Import the September 2019-2022 acceptances dataset
sep_2019_2022_acceptances = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 30 October 2023 - 2022.xlsx",
                                          sheet_name = "Sep_2019-2022_Acceptances_2")

# Unpivot the September 2019-2022 acceptances dataset
new_sep_2019_2022_acceptances = sep_2019_2022_acceptances.melt(id_vars = id_vars, value_vars = value_vars, 
                                                               var_name = "Category", 
                                                               value_name = "Number of Acceptances")

# Apply the function to the September 2019-2022 acceptances dataset
new_sep_2019_2022_acceptances = new_sep_2019_2022_acceptances.apply(get_date_sep_2019_2022, axis = 1)

# Merge the applications and acceptance datasets
sep_2019_2022 = new_sep_2019_2022_applications.merge(new_sep_2019_2022_acceptances, on = on_values, 
                                                     how = "outer")





########## SEPTEMBER 2020-2023 APPLICATIONS DATASET ##########
# Import the September 2020-2023 applications dataset
sep_2020_2023_applications = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 30 October 2023 - 2023.xlsx",
                                           sheet_name = "Sep_2020-2023_Applications_2")

# Unpivot the September 2020-2023 applications dataset
new_sep_2020_2023_applications = sep_2020_2023_applications.melt(id_vars = id_vars, value_vars = value_vars, 
                                                                 var_name = "Category", 
                                                                 value_name = "Number of Applications")

# Create a function to get the Date based on "Category" and also modify "Category"
def get_date_sep_2020_2023(row):
    category = row["Category"]
    if category == "Home":
        row["Date"] = "Sep 2023"
    elif category == "Home.1":
        row["Date"] = "Sep 2022"
        row["Category"] = "Home"
    elif category == "Home.2":
        row["Date"] = "Sep 2021"
        row["Category"] = "Home"
    elif category == "Home.3":
        row["Date"] = "Sep 2020"
        row["Category"] = "Home"
    elif category == "Overseas":
        row["Date"] = "Sep 2023"
    elif category == "Overseas.1":
        row["Date"] = "Sep 2022"
        row["Category"] = "Overseas"
    elif category == "Overseas.2":
        row["Date"] = "Sep 2021"
        row["Category"] = "Overseas"
    elif category == "Overseas.3":
        row["Date"] = "Sep 2020"
        row["Category"] = "Overseas"
    elif category == "Unknown":
        row["Date"] = "Sep 2023"
    elif category == "Unknown.1":
        row["Date"] = "Sep 2022"
        row["Category"] = "Unknown"
    elif category == "Unknown.2":
        row["Date"] = "Sep 2021"
        row["Category"] = "Unknown"
    elif category == "Unknown.3":
        row["Date"] = "Sep 2020"
        row["Category"] = "Unknown"
    return row

# Apply the function to the September 2020-2023 applications dataset
new_sep_2020_2023_applications = new_sep_2020_2023_applications.apply(get_date_sep_2020_2023, axis = 1)





########## SEPTEMBER 2020-2023 ACCEPTANCES DATASET ##########
# Import the September 2020-2023 acceptances dataset
sep_2020_2023_acceptances = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 30 October 2023 - 2023.xlsx",
                                          sheet_name = "Sep_2020-2023_Acceptances_2")

# Unpivot the September 2020-2023 acceptances dataset
new_sep_2020_2023_acceptances = sep_2020_2023_acceptances.melt(id_vars = id_vars, value_vars = value_vars, 
                                                               var_name = "Category", 
                                                               value_name = "Number of Acceptances")

# Apply the function to the September 2020-2023 acceptances dataset
new_sep_2020_2023_acceptances = new_sep_2020_2023_acceptances.apply(get_date_sep_2020_2023, axis = 1)

# Merge the applications and acceptance datasets
sep_2020_2023 = new_sep_2020_2023_applications.merge(new_sep_2020_2023_acceptances, on = on_values, 
                                                     how = "outer")





########## JANUARY 2017-2020 APPLICATIONS DATASET ##########
# Import the January 2017-2020 applications dataset
jan_2017_2020_applications = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 31 January 2023 - 2020.xlsx",
                                           sheet_name = "Jan_2017-2020_Applications_2")

# Unpivot the January 2017-2020 applications dataset
new_jan_2017_2020_applications = jan_2017_2020_applications.melt(id_vars = id_vars, value_vars = value_vars, 
                                                                 var_name = "Category", 
                                                                 value_name = "Number of Applications")

# Create a function to get the Date based on "Category" and also modify "Category"
def get_date_jan_2017_2020(row):
    category = row["Category"]
    if category == "Home":
        row["Date"] = "Jan 2020"
    elif category == "Home.1":
        row["Date"] = "Jan 2019"
        row["Category"] = "Home"
    elif category == "Home.2":
        row["Date"] = "Jan 2018"
        row["Category"] = "Home"
    elif category == "Home.3":
        row["Date"] = "Jan 2017"
        row["Category"] = "Home"
    elif category == "Overseas":
        row["Date"] = "Jan 2020"
    elif category == "Overseas.1":
        row["Date"] = "Jan 2019"
        row["Category"] = "Overseas"
    elif category == "Overseas.2":
        row["Date"] = "Jan 2018"
        row["Category"] = "Overseas"
    elif category == "Overseas.3":
        row["Date"] = "Jan 2017"
        row["Category"] = "Overseas"
    elif category == "Unknown":
        row["Date"] = "Jan 2020"
    elif category == "Unknown.1":
        row["Date"] = "Jan 2019"
        row["Category"] = "Unknown"
    elif category == "Unknown.2":
        row["Date"] = "Jan 2018"
        row["Category"] = "Unknown"
    elif category == "Unknown.3":
        row["Date"] = "Jan 2017"
        row["Category"] = "Unknown"
    return row

# Apply the function to the January 2017-2020 applications dataset
new_jan_2017_2020_applications = new_jan_2017_2020_applications.apply(get_date_jan_2017_2020, axis = 1)





########## JANUARY 2017-2020 ACCEPTANCES DATASET ##########
# Import the January 2017-2020 acceptances dataset
jan_2017_2020_acceptances = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 31 January 2023 - 2020.xlsx",
                                          sheet_name = "Jan_2017-2020_Acceptances_2")

# Unpivot the January 2017-2020 acceptances dataset
new_jan_2017_2020_acceptances = jan_2017_2020_acceptances.melt(id_vars = id_vars, value_vars = value_vars, 
                                                               var_name = "Category", 
                                                               value_name = "Number of Acceptances")

# Apply the function to the January 2017-2020 acceptances dataset
new_jan_2017_2020_acceptances = new_jan_2017_2020_acceptances.apply(get_date_jan_2017_2020, axis = 1)

# Merge the applications and acceptance datasets
jan_2017_2020 = new_jan_2017_2020_applications.merge(new_jan_2017_2020_acceptances, on = on_values, 
                                                     how = "outer")





########## JANUARY 2018-2021 APPLICATIONS DATASET ##########
# Import the January 2018-2021 applications dataset
jan_2018_2021_applications = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 31 January 2024 - 2021.xlsx",
                                           sheet_name = "Jan_2018-2021_Applications_2")

# Unpivot the January 2018-2021 applications dataset
new_jan_2018_2021_applications = jan_2018_2021_applications.melt(id_vars = id_vars, value_vars = value_vars, 
                                                                 var_name = "Category", 
                                                                 value_name = "Number of Applications")

# Create a function to get the Date based on "Category" and also modify "Category"
def get_date_jan_2018_2021(row):
    category = row["Category"]
    if category == "Home":
        row["Date"] = "Jan 2021"
    elif category == "Home.1":
        row["Date"] = "Jan 2020"
        row["Category"] = "Home"
    elif category == "Home.2":
        row["Date"] = "Jan 2019"
        row["Category"] = "Home"
    elif category == "Home.3":
        row["Date"] = "Jan 2018"
        row["Category"] = "Home"
    elif category == "Overseas":
        row["Date"] = "Jan 2021"
    elif category == "Overseas.1":
        row["Date"] = "Jan 2020"
        row["Category"] = "Overseas"
    elif category == "Overseas.2":
        row["Date"] = "Jan 2019"
        row["Category"] = "Overseas"
    elif category == "Overseas.3":
        row["Date"] = "Jan 2018"
        row["Category"] = "Overseas"
    elif category == "Unknown":
        row["Date"] = "Jan 2021"
    elif category == "Unknown.1":
        row["Date"] = "Jan 2020"
        row["Category"] = "Unknown"
    elif category == "Unknown.2":
        row["Date"] = "Jan 2019"
        row["Category"] = "Unknown"
    elif category == "Unknown.3":
        row["Date"] = "Jan 2018"
        row["Category"] = "Unknown"
    return row

# Apply the function to the January 2018-2021 applications dataset
new_jan_2018_2021_applications = new_jan_2018_2021_applications.apply(get_date_jan_2018_2021, axis = 1)





########## JANUARY 2018-2021 ACCEPTANCES DATASET ##########
# Import the January 2018-2021 acceptances dataset
jan_2018_2021_acceptances = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 31 January 2024 - 2021.xlsx",
                                          sheet_name = "Jan_2018-2021_Acceptances_2")

# Unpivot the January 2018-2021 acceptances dataset
new_jan_2018_2021_acceptances = jan_2018_2021_acceptances.melt(id_vars = id_vars, value_vars = value_vars, 
                                                               var_name = "Category", 
                                                               value_name = "Number of Acceptances")

# Apply the function to the January 2018-2021 acceptances dataset
new_jan_2018_2021_acceptances = new_jan_2018_2021_acceptances.apply(get_date_jan_2018_2021, axis = 1)

# Merge the applications and acceptance datasets
jan_2018_2021 = new_jan_2018_2021_applications.merge(new_jan_2018_2021_acceptances, on = on_values, 
                                                     how = "outer")





########## JANUARY 2019-2022 APPLICATIONS DATASET ##########
# Import the January 2019-2022 applications dataset
jan_2019_2022_applications = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 31 January 2024 - 2022.xlsx",
                                           sheet_name = "Jan_2019-2022_Applications_2")

# Unpivot the January 2019-2022 applications dataset
new_jan_2019_2022_applications = jan_2019_2022_applications.melt(id_vars = id_vars, value_vars = value_vars, 
                                                                 var_name = "Category", 
                                                                 value_name = "Number of Applications")

# Create a function to get the Date based on "Category" and also modify "Category"
def get_date_jan_2018_2021(row):
    category = row["Category"]
    if category == "Home":
        row["Date"] = "Jan 2021"
    elif category == "Home.1":
        row["Date"] = "Jan 2020"
        row["Category"] = "Home"
    elif category == "Home.2":
        row["Date"] = "Jan 2019"
        row["Category"] = "Home"
    elif category == "Home.3":
        row["Date"] = "Jan 2018"
        row["Category"] = "Home"
    elif category == "Overseas":
        row["Date"] = "Jan 2021"
    elif category == "Overseas.1":
        row["Date"] = "Jan 2020"
        row["Category"] = "Overseas"
    elif category == "Overseas.2":
        row["Date"] = "Jan 2019"
        row["Category"] = "Overseas"
    elif category == "Overseas.3":
        row["Date"] = "Jan 2018"
        row["Category"] = "Overseas"
    elif category == "Unknown":
        row["Date"] = "Jan 2021"
    elif category == "Unknown.1":
        row["Date"] = "Jan 2020"
        row["Category"] = "Unknown"
    elif category == "Unknown.2":
        row["Date"] = "Jan 2019"
        row["Category"] = "Unknown"
    elif category == "Unknown.3":
        row["Date"] = "Jan 2018"
        row["Category"] = "Unknown"
    return row

# Apply the function to the January 2018-2021 applications dataset
new_jan_2018_2021_applications = new_jan_2018_2021_applications.apply(get_date_jan_2018_2021, axis = 1)





########## JANUARY 2018-2021 ACCEPTANCES DATASET ##########
# Import the January 2018-2021 acceptances dataset
jan_2018_2021_acceptances = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 31 January 2024 - 2021.xlsx",
                                          sheet_name = "Jan_2018-2021_Acceptances_2")

# Unpivot the January 2018-2021 acceptances dataset
new_jan_2018_2021_acceptances = jan_2018_2021_acceptances.melt(id_vars = id_vars, value_vars = value_vars, 
                                                               var_name = "Category", 
                                                               value_name = "Number of Acceptances")

# Apply the function to the January 2018-2021 acceptances dataset
new_jan_2018_2021_acceptances = new_jan_2018_2021_acceptances.apply(get_date_jan_2018_2021, axis = 1)

# Merge the applications and acceptance datasets
jan_2018_2021 = new_jan_2018_2021_applications.merge(new_jan_2018_2021_acceptances, on = on_values, 
                                                     how = "outer")











