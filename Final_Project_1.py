# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:55:26 2024

@author: keneo
"""

# Import libraries
import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import dash
# from dash import html, dcc, Input, Output
# import plotly.express as px
# import plotly.graph_objects as go
# from plotly.offline import plot





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
def modify_date_category_2017_2020(row):
    category = row["Category"]
    if category == "Home":
        row["Date"] = 2020
    elif category == "Home.1":
        row["Date"] = 2019
        row["Category"] = "Home"
    elif category == "Home.2":
        row["Date"] = 2018
        row["Category"] = "Home"
    elif category == "Home.3":
        row["Date"] = 2017
        row["Category"] = "Home"
    elif category == "Overseas":
        row["Date"] = 2020
    elif category == "Overseas.1":
        row["Date"] = 2019
        row["Category"] = "Overseas"
    elif category == "Overseas.2":
        row["Date"] = 2018
        row["Category"] = "Overseas"
    elif category == "Overseas.3":
        row["Date"] = 2017
        row["Category"] = "Overseas"
    elif category == "Unknown":
        row["Date"] = 2020
    elif category == "Unknown.1":
        row["Date"] = 2019
        row["Category"] = "Unknown"
    elif category == "Unknown.2":
        row["Date"] = 2018
        row["Category"] = "Unknown"
    elif category == "Unknown.3":
        row["Date"] = 2017
        row["Category"] = "Unknown"
    return row

# Apply the function to the September 2017-2020 applications dataset
new_sep_2017_2020_applications = new_sep_2017_2020_applications.apply(modify_date_category_2017_2020, 
                                                                      axis = 1)





########## SEPTEMBER 2017-2020 ACCEPTANCES DATASET ##########
# Import the September 2017-2020 acceptances dataset
sep_2017_2020_acceptances = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 30 October  2023 - 2020.xlsx",
                                          sheet_name = "Sep_2017-2020_Acceptances_2")

# Unpivot the September 2017-2020 acceptances dataset
new_sep_2017_2020_acceptances = sep_2017_2020_acceptances.melt(id_vars = id_vars, value_vars = value_vars, 
                                                               var_name = "Category", 
                                                               value_name = "Number of Acceptances")

# Apply the function to the September 2017-2020 acceptances dataset
new_sep_2017_2020_acceptances = new_sep_2017_2020_acceptances.apply(modify_date_category_2017_2020, 
                                                                    axis = 1)

# Merge the applications and acceptance datasets
on_values = ["Campus", "Group", "School / Department", "Level", "Category", "Date"]
sep_2017_2020 = new_sep_2017_2020_applications.merge(new_sep_2017_2020_acceptances, on = on_values, 
                                                     how = "outer")





########## SEPTEMBER 2018-2021 APPLICATIONS DATASET ##########
# Import the September 2018-2021 applications dataset
sep_2018_2021_applications = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 30 October 2023 - 2021.xlsx",
                                           sheet_name = "Sep_2018-2021_Acceptances_2")

# Unpivot the September 2018-2021 applications dataset
new_sep_2018_2021_applications = sep_2018_2021_applications.melt(id_vars = id_vars, value_vars = value_vars, 
                                                                 var_name = "Category", 
                                                                 value_name = "Number of Applications")

# Create a function to get the Date based on "Category" and also modify "Category"
def modify_date_category_2018_2021(row):
    category = row["Category"]
    if category == "Home":
        row["Date"] = 2021
    elif category == "Home.1":
        row["Date"] = 2020
        row["Category"] = "Home"
    elif category == "Home.2":
        row["Date"] = 2019
        row["Category"] = "Home"
    elif category == "Home.3":
        row["Date"] = 2018
        row["Category"] = "Home"
    elif category == "Overseas":
        row["Date"] = 2021
    elif category == "Overseas.1":
        row["Date"] = 2020
        row["Category"] = "Overseas"
    elif category == "Overseas.2":
        row["Date"] = 2019
        row["Category"] = "Overseas"
    elif category == "Overseas.3":
        row["Date"] = 2018
        row["Category"] = "Overseas"
    elif category == "Unknown":
        row["Date"] = 2021
    elif category == "Unknown.1":
        row["Date"] = 2020
        row["Category"] = "Unknown"
    elif category == "Unknown.2":
        row["Date"] = 2019
        row["Category"] = "Unknown"
    elif category == "Unknown.3":
        row["Date"] = 2018
        row["Category"] = "Unknown"
    return row

# Apply the function to the September 2018-2021 applications dataset
new_sep_2018_2021_applications = new_sep_2018_2021_applications.apply(modify_date_category_2018_2021, 
                                                                      axis = 1)














