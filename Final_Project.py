# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:55:26 2024

@author: keneo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotly.offline import plot
import plotly.express as px

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





# # Create an array of unique dates
# dates = sep_2020["Date"].unique()

# # Calculate the width of each bar
# bar_width = 0.3

# # Positions for the bars
# positions1 = dates - bar_width/2
# positions2 = dates + bar_width/2

# Filter the dataset to get the Home and Overseas categories
home = sep_2020[sep_2020["Category"] == "Home"]
overseas = sep_2020[sep_2020["Category"] == "Overseas"]

# Plot the Barchart
plt.figure(figsize = (20, 10))
plt.suptitle("Number of Applications VS Number of Acceptances")

# Applications Barchart
plt.subplot(1, 2, 1)
bar_1 = plt.bar(home["Date"] - 0.3/2,
               home["Number of Applicants"],
               width = 0.3,
               label = "Home")

bar_2 = plt.bar(overseas["Date"] + 0.3/2,
               overseas["Number of Applicants"],
               width = 0.3,
               label = "Overseas")

plt.xlabel("Date")
plt.ylabel("Number of Applicants")
plt.title("Number of Applications by Date")
plt.legend()

# Acceptance Barchart
plt.subplot(1, 2, 2)
bar_3 = plt.bar(home["Date"] - 0.3/2,
               home["Number of Acceptances"],
               width = 0.3,
               label = "Home")

bar_4 = plt.bar(overseas["Date"] + 0.3/2,
               overseas["Number of Acceptances"],
               width = 0.3,
               label = "Overseas")

plt.xlabel("Date")
plt.ylabel("Number of Acceptances")
plt.title("Number of Acceptances by Date")
plt.legend()
plt.show()


# fig = px.bar(sep_2020, x = "Date", y = "Number of Acceptances", color = "Category", barmode = "group")
# fig.show(renderer="png")









