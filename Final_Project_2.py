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

final_registrations = final_registrations.drop(columns = ["Month", "Year", "Main Level"])

# Group by "Campus", "Group", "School / Department", "Level", and "Category"
# Then sum the values for "Number of Acceptances" and "Number of Applications"
final_summary = final_records.groupby(
    ["Campus", "Group", "School / Department", "Level", "Date"], as_index = False
)[["Number of Applications", "Number of Acceptances"]].sum().sort_values(by = ["Group", "Date"], 
                                                                         ascending = False)

on_values = ["Campus", "Group", "School / Department", "Level", "Date"]                                                                         
final_summary = final_summary.merge(final_registrations, on = on_values, how = "left")

# index_values = ["Campus", "Group", "School / Department", "Level"]  
# data = final_summary.pivot(index = index_values, 
#                            columns = "Date", values = ["Number of Acceptances", "Number of Registrations"])

# Group by "School / Department" and calculate the total for "Number of Acceptances" and "Number of Registrations"
total_summary = final_summary.groupby("School / Department", as_index=False)[
    ["Number of Acceptances", "Number of Registrations"]
].sum()




