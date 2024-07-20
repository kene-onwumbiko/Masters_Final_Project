# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:55:26 2024

@author: keneo
"""

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot


# Import the applications dataset
sep_2020_applications = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 30 October  2023 - 2020.xlsx",
                                      sheet_name = "Sheet2_New_Applications_2")

# Unpivot the applications dataset
id_vars = ["Campus", "Group", "School / Department", "Level"]
value_vars = ["Home", "Overseas", "Unknown", "Home.1", "Overseas.1", "Unknown.1", "Home.2", 
              "Overseas.2", "Unknown.2", "Home.3", "Overseas.3", "Unknown.3"]

new_sep_2020_applications = sep_2020_applications.melt(id_vars = id_vars, value_vars = value_vars, 
                                                        var_name = "Category", 
                                                        value_name = "Number of Applicants")

# Create a function to get the Date based on "Category" and also modify "Category"
def modify_date_category(row):
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

# Apply the function to the applications dataset
new_sep_2020_applications = new_sep_2020_applications.apply(modify_date_category, axis = 1)


# Import the acceptance dataset
sep_2020_acceptance = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 30 October  2023 - 2020.xlsx",
                                    sheet_name = "Sheet2_New_Acceptance_2")

# Unpivot the acceptance dataset
new_sep_2020_acceptance = sep_2020_acceptance.melt(id_vars = id_vars, value_vars = value_vars, 
                                                    var_name = "Category", 
                                                    value_name = "Number of Acceptances")

# Apply the function to the acceptance dataset
new_sep_2020_acceptance = new_sep_2020_acceptance.apply(modify_date_category, axis = 1)

# Merge the applications and acceptance datasets
on_values = ["Campus", "Group", "School / Department", "Level", "Category", "Date"]
sep_2020 = new_sep_2020_applications.merge(new_sep_2020_acceptance, on = on_values, how = "outer")





# Filter all Undergraduate data
sep_2020_undergrad = sep_2020[sep_2020["Level"] == "Undergraduate"]

# Filter all School of Computing data from the Undergraduate data
sep_2020_undergrad_computing = sep_2020_undergrad[sep_2020_undergrad["School / Department"] == "School of Computing"]














