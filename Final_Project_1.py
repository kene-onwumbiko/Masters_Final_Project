# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:55:26 2024

@author: keneo
"""

# Import libraries
import pandas as pd





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
                                                                 value_name = "Number of Applications")

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
def get_date_jan_2019_2022(row):
    category = row["Category"]
    if category == "Home":
        row["Date"] = "Jan 2022"
    elif category == "Home.1":
        row["Date"] = "Jan 2021"
        row["Category"] = "Home"
    elif category == "Home.2":
        row["Date"] = "Jan 2020"
        row["Category"] = "Home"
    elif category == "Home.3":
        row["Date"] = "Jan 2019"
        row["Category"] = "Home"
    elif category == "Overseas":
        row["Date"] = "Jan 2022"
    elif category == "Overseas.1":
        row["Date"] = "Jan 2021"
        row["Category"] = "Overseas"
    elif category == "Overseas.2":
        row["Date"] = "Jan 2020"
        row["Category"] = "Overseas"
    elif category == "Overseas.3":
        row["Date"] = "Jan 2019"
        row["Category"] = "Overseas"
    elif category == "Unknown":
        row["Date"] = "Jan 2022"
    elif category == "Unknown.1":
        row["Date"] = "Jan 2021"
        row["Category"] = "Unknown"
    elif category == "Unknown.2":
        row["Date"] = "Jan 2020"
        row["Category"] = "Unknown"
    elif category == "Unknown.3":
        row["Date"] = "Jan 2019"
        row["Category"] = "Unknown"
    return row

# Apply the function to the January 2019-2022 applications dataset
new_jan_2019_2022_applications = new_jan_2019_2022_applications.apply(get_date_jan_2019_2022, axis = 1)





########## JANUARY 2019-2022 ACCEPTANCES DATASET ##########
# Import the January 2019-2022 acceptances dataset
jan_2019_2022_acceptances = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 31 January 2024 - 2022.xlsx",
                                          sheet_name = "Jan_2019-2022_Acceptances_2")

# Unpivot the January 2019-2022 acceptances dataset
new_jan_2019_2022_acceptances = jan_2019_2022_acceptances.melt(id_vars = id_vars, value_vars = value_vars, 
                                                               var_name = "Category", 
                                                               value_name = "Number of Acceptances")

# Apply the function to the January 2019-2022 acceptances dataset
new_jan_2019_2022_acceptances = new_jan_2019_2022_acceptances.apply(get_date_jan_2019_2022, axis = 1)

# Merge the applications and acceptance datasets
jan_2019_2022 = new_jan_2019_2022_applications.merge(new_jan_2019_2022_acceptances, on = on_values, 
                                                     how = "outer")





########## JANUARY 2020-2023 APPLICATIONS DATASET ##########
# Import the January 2020-2023 applications dataset
jan_2020_2023_applications = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 31 January 2024 - 2023.xlsx",
                                           sheet_name = "Jan_2020-2023_Applications_2")

# Fill the missing cell with "Enterprise and Entrepreneurship"
jan_2020_2023_applications = jan_2020_2023_applications.fillna("Enterprise and Entrepreneurship")

# Unpivot the January 2020-2023 applications dataset
new_jan_2020_2023_applications = jan_2020_2023_applications.melt(id_vars = id_vars, value_vars = value_vars, 
                                                                 var_name = "Category", 
                                                                 value_name = "Number of Applications")

# Create a function to get the Date based on "Category" and also modify "Category"
def get_date_jan_2020_2023(row):
    category = row["Category"]
    if category == "Home":
        row["Date"] = "Jan 2023"
    elif category == "Home.1":
        row["Date"] = "Jan 2022"
        row["Category"] = "Home"
    elif category == "Home.2":
        row["Date"] = "Jan 2021"
        row["Category"] = "Home"
    elif category == "Home.3":
        row["Date"] = "Jan 2020"
        row["Category"] = "Home"
    elif category == "Overseas":
        row["Date"] = "Jan 2023"
    elif category == "Overseas.1":
        row["Date"] = "Jan 2022"
        row["Category"] = "Overseas"
    elif category == "Overseas.2":
        row["Date"] = "Jan 2021"
        row["Category"] = "Overseas"
    elif category == "Overseas.3":
        row["Date"] = "Jan 2020"
        row["Category"] = "Overseas"
    elif category == "Unknown":
        row["Date"] = "Jan 2023"
    elif category == "Unknown.1":
        row["Date"] = "Jan 2022"
        row["Category"] = "Unknown"
    elif category == "Unknown.2":
        row["Date"] = "Jan 2021"
        row["Category"] = "Unknown"
    elif category == "Unknown.3":
        row["Date"] = "Jan 2020"
        row["Category"] = "Unknown"
    return row

# Apply the function to the January 2020-2023 applications dataset
new_jan_2020_2023_applications = new_jan_2020_2023_applications.apply(get_date_jan_2020_2023, axis = 1)





########## JANUARY 2020-2023 ACCEPTANCES DATASET ##########
# Import the January 2020-2023 acceptances dataset
jan_2020_2023_acceptances = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 31 January 2024 - 2023.xlsx",
                                          sheet_name = "Jan_2020-2023_Acceptances_2")

# Fill the missing cell with "Enterprise and Entrepreneurship"
jan_2020_2023_acceptances = jan_2020_2023_acceptances.fillna("Enterprise and Entrepreneurship")

# Unpivot the January 2020-2023 acceptances dataset
new_jan_2020_2023_acceptances = jan_2020_2023_acceptances.melt(id_vars = id_vars, value_vars = value_vars, 
                                                               var_name = "Category", 
                                                               value_name = "Number of Acceptances")

# Apply the function to the January 2020-2023 acceptances dataset
new_jan_2020_2023_acceptances = new_jan_2020_2023_acceptances.apply(get_date_jan_2020_2023, axis = 1)

# Merge the applications and acceptance datasets
jan_2020_2023 = new_jan_2020_2023_applications.merge(new_jan_2020_2023_acceptances, on = on_values, 
                                                     how = "outer")




########## GET ALL THE REGISTRATION RECORDS ##########
# Extract all the registration records for the datasets
sep_2019_registrations = sep_2017_2020_applications.iloc[:, :5]
# Rename the "Registrations for 2019" column to "Registrations"
sep_2019_registrations.rename(columns = {"Registrations for 2019": "Registrations"}, inplace = True)
# Add a Date column and fill it with 2019
sep_2019_registrations["Date"] = "Sep 2019"

sep_2020_registrations = sep_2018_2021_applications.iloc[:, :5]
# Rename the "Registrations for 2020" column to "Registrations"
sep_2020_registrations.rename(columns = {"Registrations for 2020": "Registrations"}, inplace = True)
# Add a Date column and fill it with 2020
sep_2020_registrations["Date"] = "Sep 2020"

sep_2021_registrations = sep_2019_2022_applications.iloc[:, :5]
# Rename the "Registrations for 2021" column to "Registrations"
sep_2021_registrations.rename(columns = {"Registrations for 2021": "Registrations"}, inplace = True)
# Add a Date column and fill it with 2021
sep_2021_registrations["Date"] = "Sep 2021"

sep_2022_registrations = sep_2020_2023_applications.iloc[:, :5]
# Rename the "Registrations for 2022" column to "Registrations"
sep_2022_registrations.rename(columns = {"Registrations for 2022": "Registrations"}, inplace = True)
# Add a Date column and fill it with 2022
sep_2022_registrations["Date"] = "Sep 2022"

jan_2019_registrations = jan_2017_2020_applications.iloc[:, :5]
# Rename the "Registrations for 2019" column to "Registrations"
jan_2019_registrations.rename(columns = {"Registrations for 2019": "Registrations"}, inplace = True)
# Add a Date column and fill it with 2019
jan_2019_registrations["Date"] = "Jan 2019"

jan_2020_registrations = jan_2018_2021_applications.iloc[:, :5]
# Rename the "Registrations for 2020" column to "Registrations"
jan_2020_registrations.rename(columns = {"Registrations for 2020": "Registrations"}, inplace = True)
# Add a Date column and fill it with 2020
jan_2020_registrations["Date"] = "Jan 2020"

jan_2021_registrations = jan_2019_2022_applications.iloc[:, :5]
# Rename the "Registrations for 2021" column to "Registrations"
jan_2021_registrations.rename(columns = {"Registrations for 2021": "Registrations"}, inplace = True)
# Add a Date column and fill it with 2021
jan_2021_registrations["Date"] = "Jan 2021"

jan_2022_registrations = jan_2020_2023_applications.iloc[:, :5]
# Rename the "Registrations for 2022" column to "Registrations"
jan_2022_registrations.rename(columns = {"Registrations for 2022": "Registrations"}, inplace = True)
# Add a Date column and fill it with 2022
jan_2022_registrations["Date"] = "Jan 2022"

# Merge all the registration records
on_values_2 = ["Campus", "Group", "School / Department", "Level", "Registrations", "Date"]
final_registrations = sep_2022_registrations.merge(sep_2021_registrations, on = on_values_2, how = "outer")

final_registrations = final_registrations.merge(sep_2020_registrations, on = on_values_2, how = "outer")

final_registrations = final_registrations.merge(sep_2019_registrations, on = on_values_2, how = "outer")

final_registrations = final_registrations.merge(jan_2022_registrations, on = on_values_2, how = "outer")

final_registrations = final_registrations.merge(jan_2021_registrations, on = on_values_2, how = "outer")

final_registrations = final_registrations.merge(jan_2020_registrations, on = on_values_2, how = "outer")

final_registrations = final_registrations.merge(jan_2019_registrations, on = on_values_2, how = "outer")

# Change the date format
# final_registrations["Date"] = pd.to_datetime(final_registrations["Date"]).dt.date





# # Merge all the final application and acceptance records
on_values_3 = ["Campus", "Group", "School / Department", "Level", "Category", "Number of Applications", "Date", "Number of Acceptances"]

# final_records = pd.merge_ordered(sep_2020_2023, sep_2019_2022, on = on_values_2, how = "outer")

# final_records = final_records.merge(sep_2018_2021, on = on_values_2, how = "outer")

# final_records = final_records.merge(sep_2017_2020, on = on_values_2, how = "outer")

# final_records = final_records.merge(jan_2020_2023, on = on_values_2, how = "outer")

# final_records = final_records.merge(jan_2019_2022, on = on_values_2, how = "outer")

# final_records = final_records.merge(jan_2018_2021, on = on_values_2, how = "outer")

# final_records = final_records.merge(jan_2017_2020, on = on_values_2, how = "outer")

# Change the date format
# final_records["Date"] = pd.to_datetime(final_records["Date"]).dt.date





##########

sep_levels_2020_2023 = sep_2020_2023_applications.iloc[:, :4]

jan_levels_2020_2023 = jan_2020_2023_applications.iloc[:, :4]

new_sep_2017_2020 = sep_2017_2020[sep_2017_2020["Date"] != "Sep 2020"]
sep_2017_2023 = sep_2020_2023.merge(new_sep_2017_2020, on = on_values_3, how = "left")

# on_values_3 = ["Campus", "Group", "School / Department", "Level"]
# levels = sep_levels_2020_2023.merge(sep_levels_2019_2022, on = on_values_3, how = "outer")
# levels = levels.merge(sep_levels_2018_2021, on = on_values_3, how = "outer")
# levels = levels.merge(sep_levels_2017_2020, on = on_values_3, how = "outer")
# levels = levels.merge(jan_levels_2020_2023, on = on_values_3, how = "outer")
# levels = levels.merge(jan_levels_2019_2022, on = on_values_3, how = "outer")
# levels = levels.merge(jan_levels_2018_2021, on = on_values_3, how = "outer")
# levels = levels.merge(jan_levels_2017_2020, on = on_values_3, how = "outer")





