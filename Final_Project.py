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





# Filter all Undergraduate data
sep_2020_undergrad = sep_2020[sep_2020["Level"] == "Undergraduate"]

# Filter all School of Computing data from the Undergraduate data
sep_2020_undergrad_computing = sep_2020_undergrad[sep_2020_undergrad["School / Department"] == "School of Computing"]





# Create a dictionary to store the continent names.
# This dictionary is used to get the map of each continent.
continents = {"World": "world",
              "Asia": "asia",
              "Africa": "africa",
              "Europe": "europe",
              "North America": "north america",
              "South America": "south america"}

# Labels for policies.
# These lists are used to label the y axis of the policy line graph.
school_closing = ["No measures", "Recommend closing", "Require localised closing", "Require all closing"]
stay_at_home = ["No measures", "Recommend stay home", "Stay home with some exception", "Stay home with minimum exception"]

# Define a function to create the bubble map.
def create_bubble_map(map_covid_data, scope, data_input):
    fig = px.scatter_geo(map_covid_data,
                         locations = "CountryCode",
                         color = "Continent_Name",
                         hover_name = "CountryName",
                         size = data_input,
                         size_max = 50,
                         animation_frame = "Date",
                         projection = "equirectangular",
                         opacity = 0.6,
                         title = f"COVID-19 {data_input} in {scope}",
                         color_discrete_sequence = px.colors.qualitative.T10)
    
    # Update geos for the scope.
    fig.update_geos(projection_type = "equirectangular", 
                    scope = continents[scope], 
                    showcountries = True)
    return fig

# Define a function to create the choropleth map.
def create_choropleth_map(map_covid_data, scope, policy):
    fig = px.choropleth(map_covid_data,
                        locations = "CountryCode",
                        color = policy,
                        hover_name = "CountryName",
                        animation_frame = "Date",
                        projection = "equirectangular",
                        title = f"{policy} policy in {scope}",
                        color_continuous_scale = px.colors.sequential.Plasma)
    
    # Update geos for the scope.
    fig.update_geos(projection_type = "equirectangular", 
                    scope = continents[scope], 
                    showcountries = True)
    return fig

# Define a function to create the line graph.
def create_line_graph(map_covid_data, data_input, policy):
    
    # Filter the top five countries as of 20th May 2020 for confirmed cases.
    top_5_countries = map_covid_data[map_covid_data["Date"] == pd.Timestamp("2020-05-20").date()].drop_duplicates(subset = map_covid_data.columns[0:8]).nlargest(5, "ConfirmedCases")["CountryName"].unique()
    filtered_top_5_countries = map_covid_data[map_covid_data["CountryName"].isin(top_5_countries)]

    if data_input:
        
        # Line graph for data input
        fig = px.line(filtered_top_5_countries, 
                      x = "Date", 
                      y = data_input, 
                      color = "CountryName", 
                      title = f"COVID-19 {data_input} in the top five countries")
    else:
        
        # Line graph for policy
        fig = px.line(filtered_top_5_countries,
                      x = "Date", 
                      y = policy, 
                      color = "CountryName", 
                      title = f"{policy} policy in the top five countries")
        
        # Set ticktext for each policy.
        if policy == "School closing":
            ticktext = school_closing
        elif policy == "Stay at home requirements":
            ticktext = stay_at_home
        else:
            ticktext = []
        
        # Update layout for the line gragh
        fig.update_layout(yaxis_title = f"{policy} policy level",
                          yaxis = dict(
                              tickmode = "array",
                              tickvals = [0, 1, 2, 3],
                              ticktext = ticktext,
                              tickfont = dict(size = 10))
                          )
    return fig




