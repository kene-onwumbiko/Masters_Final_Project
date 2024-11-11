# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 17:09:09 2024

@author: keneo
"""

# Import libraries
import pandas as pd





# Import the final_records dataset
final_records = pd.read_csv(r"C:\Users\keneo\OneDrive\Desktop\Github Projects\Masters_Final_Project\final_records.csv")

# Import the final_registrations dataset
final_registrations = pd.read_csv(r"C:\Users\keneo\OneDrive\Desktop\Github Projects\Masters_Final_Project\final_registrations.csv")

# Drop rows with the specified dates in the final_records dataset
dates_to_drop = ["Sep 2023", "Sep 2018", "Sep 2017", "Jan 2023", "Jan 2018", "Jan 2017"]
final_records = final_records[~final_records["Date"].isin(dates_to_drop)]












