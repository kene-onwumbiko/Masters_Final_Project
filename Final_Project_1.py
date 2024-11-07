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





########## GET THE FINAL RECORDS FOR APPLICATIONS AND ACCEPTANCES ##########
# Extract the levels for the 2020-2023 datasets
sep_levels_2020_2023 = sep_2020_2023.iloc[:, :4]
jan_levels_2020_2023 = jan_2020_2023.iloc[:, :4]

# Merge the extracted levels with the 2017-2020 datasets
on_values_2 = ["Campus", "Group", "School / Department", "Level"]
new_sep_2017_2020 = sep_levels_2020_2023.merge(sep_2017_2020, on = on_values_2, how = "left").drop_duplicates().dropna().sort_values(by = ["Date", "Group"], ascending = False)
new_jan_2017_2020 = jan_levels_2020_2023.merge(jan_2017_2020, on = on_values_2, how = "left").drop_duplicates().dropna().sort_values(by = ["Date", "Group"], ascending = False)

# Delete the rows with "Date" column = "Sep 2020"
sep_2017_2019 = new_sep_2017_2020[new_sep_2017_2020["Date"] != "Sep 2020"]
jan_2017_2019 = new_jan_2017_2020[new_jan_2017_2020["Date"] != "Sep 2020"]

# Merge the newly derived 2017-2019 datasets with the 2020-2023 datasets
on_values_3 = ["Campus", "Group", "School / Department", "Level", "Category", "Number of Applications", "Date", "Number of Acceptances"]
sep_2017_2023 = sep_2020_2023.merge(sep_2017_2019, on = on_values_3, how = "outer")
jan_2017_2023 = jan_2020_2023.merge(jan_2017_2019, on = on_values_3, how = "outer")

# Merge the newly derived September and January 2017-2023 datasets
final_records = sep_2017_2023.merge(jan_2017_2023, on = on_values_3, how = "outer").sort_values(by = ["Date", "Category"], ascending = [False, True])

# Change the Date format
final_records["Date"] = pd.to_datetime(final_records["Date"]).dt.to_period('M')

# Save to a CSV file
final_records.to_csv(r'final_records.csv', index = False)





########## GET ALL THE REGISTRATION RECORDS ##########
# Import the remaining applications datasets
# September 2018-2021
sep_2018_2021_applications = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 30 October 2023 - 2021.xlsx",
                                           sheet_name = "Sep_2018-2021_Applications_2")

# September 2019-2022
sep_2019_2022_applications = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 30 October 2023 - 2022.xlsx",
                                           sheet_name = "Sep_2019-2022_Applications_2")

# January 2018-2021
jan_2018_2021_applications = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 31 January 2024 - 2021.xlsx",
                                           sheet_name = "Jan_2018-2021_Applications_2")

# January 2019-2022
jan_2019_2022_applications = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 31 January 2024 - 2022.xlsx",
                                           sheet_name = "Jan_2019-2022_Applications_2")

# Extract all the registration records for the applications datasets
# September 2017-2020
sep_2019_registrations = sep_2017_2020_applications.iloc[:, :5]
# Rename the "Registrations for 2019" column to "Registrations"
sep_2019_registrations.rename(columns = {"Registrations for 2019": "Registrations for Sep 2019"}, inplace = True)
# # Add a Date column and fill it with 2019
# sep_2019_registrations["Date"] = "Sep 2019"

# September 2018-2021
sep_2020_registrations = sep_2018_2021_applications.iloc[:, :5]
# Rename the "Registrations for 2020" column to "Registrations"
sep_2020_registrations.rename(columns = {"Registrations for 2020": "Registrations for Sep 2020"}, inplace = True)
# # Add a Date column and fill it with 2020
# sep_2020_registrations["Date"] = "Sep 2020"

# September 2019-2022
sep_2021_registrations = sep_2019_2022_applications.iloc[:, :5]
# Rename the "Registrations for 2021" column to "Registrations"
sep_2021_registrations.rename(columns = {"Registrations for 2021": "Registrations for Sep 2021"}, inplace = True)
# # Add a Date column and fill it with 2021
# sep_2021_registrations["Date"] = "Sep 2021"

# September 2020-2023
sep_2022_registrations = sep_2020_2023_applications.iloc[:, :5]
# Rename the "Registrations for 2022" column to "Registrations"
sep_2022_registrations.rename(columns = {"Registrations for 2022": "Registrations for Sep 2022"}, inplace = True)
# # Add a Date column and fill it with 2022
# sep_2022_registrations["Date"] = "Sep 2022"

# January 2017-2020
jan_2019_registrations = jan_2017_2020_applications.iloc[:, :5]
# Rename the "Registrations for 2019" column to "Registrations"
jan_2019_registrations.rename(columns = {"Registrations for 2019": "Registrations for Jan 2019"}, inplace = True)
# # Add a Date column and fill it with 2019
# jan_2019_registrations["Date"] = "Jan 2019"

# January 2018-2021
jan_2020_registrations = jan_2018_2021_applications.iloc[:, :5]
# Rename the "Registrations for 2020" column to "Registrations"
jan_2020_registrations.rename(columns = {"Registrations for 2020": "Registrations for Jan 2020"}, inplace = True)
# # Add a Date column and fill it with 2020
# jan_2020_registrations["Date"] = "Jan 2020"

# January 2019-2022
jan_2021_registrations = jan_2019_2022_applications.iloc[:, :5]
# Rename the "Registrations for 2021" column to "Registrations"
jan_2021_registrations.rename(columns = {"Registrations for 2021": "Registrations for Jan 2021"}, inplace = True)
# # Add a Date column and fill it with 2021
# jan_2021_registrations["Date"] = "Jan 2021"

# January 2020-2023
jan_2022_registrations = jan_2020_2023_applications.iloc[:, :5]
# Rename the "Registrations for 2022" column to "Registrations"
jan_2022_registrations.rename(columns = {"Registrations for 2022": "Registrations for Jan 2022"}, inplace = True)
# # Add a Date column and fill it with 2022
# jan_2022_registrations["Date"] = "Jan 2022"

# Extract the levels for the 2022 registrations datasets
sep_levels_registrations = sep_2022_registrations.iloc[:, :4]
jan_levels_registrations = jan_2022_registrations.iloc[:, :4]

# Merge the extracted levels with the extracted registration datasets
sep_registrations = sep_levels_registrations.merge(sep_2022_registrations, on = on_values_2, how = "left")
sep_registrations = sep_registrations.merge(sep_2021_registrations, on = on_values_2, how = "left")
sep_registrations = sep_registrations.merge(sep_2020_registrations, on = on_values_2, how = "left")
sep_registrations = sep_registrations.merge(sep_2019_registrations, on = on_values_2, how = "left")

jan_registrations = jan_levels_registrations.merge(jan_2022_registrations, on = on_values_2, how = "left")
jan_registrations = jan_registrations.merge(jan_2021_registrations, on = on_values_2, how = "left")
jan_registrations = jan_registrations.merge(jan_2020_registrations, on = on_values_2, how = "left")
jan_registrations = jan_registrations.merge(jan_2019_registrations, on = on_values_2, how = "left")

# Merge the final September and January datasets
final_registrations = sep_registrations.merge(jan_registrations, on = on_values_2, how = "outer").sort_values(by = ["Group", "School / Department"], ascending = [False, True])

# Fill the missing values with -1
final_registrations = final_registrations.fillna(-1)

# Save to a CSV file
final_registrations.to_csv(r'final_registrations.csv', index = False)










