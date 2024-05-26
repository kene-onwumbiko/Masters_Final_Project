# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:55:26 2024

@author: keneo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Import the dataset
sep_2020_applications = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 30 October  2023 - 2020.xlsx",
                                      sheet_name = "Sheet2_New_Applications_2")

# Unpivot the dataset
id_vars = ["Campus", "Group", "School / Department", "Level"]
value_vars = ["Home", "Overseas", "Unknown", "Home.1", "Overseas.1", "Unknown.1", "Home.2", 
              "Overseas.2", "Unknown.2", "Home.3", "Overseas.3", "Unknown.3"]

new_sep_2020_applications = sep_2020_applications.melt(id_vars = id_vars, value_vars = value_vars, 
                                                       var_name = "Category", 
                                                       value_name = "Number of Applicants")

# Create a function to determine the date based on "Category" and also modify "Category"
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

# Apply the function to the "new_sep_2020_applications"
new_sep_2020_applications = new_sep_2020_applications.apply(modify_date_category, axis = 1)


# Import the dataset
sep_2020_acceptance = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 30 October  2023 - 2020.xlsx",
                                    sheet_name = "Sheet2_New_Acceptance_2")

new_sep_2020_acceptance = sep_2020_acceptance.melt(id_vars = id_vars, value_vars = value_vars, 
                                                   var_name = "Category", 
                                                   value_name = "Number of Acceptances")

# Apply the function to the "new_sep_2020_acceptance"
new_sep_2020_acceptance = new_sep_2020_acceptance.apply(modify_date_category, axis = 1)

on_values = ["Campus", "Group", "School / Department", "Level", "Category", "Date"]
sep_2020 = new_sep_2020_applications.merge(new_sep_2020_acceptance, on = on_values, how = "outer")

# Plot linechat
plt.figure(figsize = (15, 10))
# plt.plot(sep_2020["Date"], sep_2020["Number of Applicants"], "-g")
# plt.plot(sep_2020["Date"], sep_2020["Number of Acceptances"], "-r")
# plt.plot("Date", "Number of Applicants", data = sep_2020, marker = "o", 
#          markerfacecolor = "darkgreen", color = "green", linewidth = 2)

plt.bar(sep_2020["Date"], sep_2020["Number of Applicants"], color = "green")
plt.bar(sep_2020["Date"], sep_2020["Number of Acceptances"], color = "red")
plt.show()

fig = go.Figure()
fig = go.Figure(data = [go.Bar(x = sep_2020["Date"],y = sep_2020["Number of Applicants"])])
fig.show()













