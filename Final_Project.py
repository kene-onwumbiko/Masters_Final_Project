# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:55:26 2024

@author: keneo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import the data
sep_2020 = pd.read_excel(r"C:\Users\keneo\Downloads\Data and Software\Overview_FullData_For_4_Academic_Years - 30 October  2023 - 2020.xlsx",
                         sheet_name = "Sheet2_New_Applications_2")

# Unpivot the DataFrame
id_vars = ["Campus", "Group", "School / Department", "Level"]
value_vars = ["Home", "Overseas", "Unknown", "Home.1", "Overseas.1", "Unknown.1", "Home.2", 
              "Overseas.2", "Unknown.2", "Home.3", "Overseas.3", "Unknown.3"]

unpivoted_sep_2020 = sep_2020.melt(id_vars=id_vars, value_vars=value_vars, 
                                   var_name='Category', value_name='Number of Students')

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

# Apply the function to the "unpivoted_sep_2020"
unpivoted_sep_2020 = unpivoted_sep_2020.apply(modify_date_category, axis = 1)














