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

# Mapping dictionary
school_department_mapping = {
    "Accounting and Finance": "001",
    "Centre for Foundation Studies": "002",
    "Economics and International Studies": "003",
    "English and Digital Media": "004",
    "Enterprise and Entrepreneurship": "005",
    "History and History of Art": "006",
    "London": "007",
    "Management": "008",
    "Modern Foreign Languages": "009",
    "School of Computing": "010",
    "School of Education": "011",
    "School of Law": "012",
    "School of Postgraduate Medicine": "013",
    "School of Psychology": "014",
    "School of UG Medicine": "015"
}

# Function to modify School / Department
def modify_school_department(row):
    school_department = row["School / Department"]
    if school_department in school_department_mapping:
        row["School / Department"] = school_department_mapping[school_department]
    return row

# Apply the function to the "sep_2020" DataFrame
new_sep_2020_applications = new_sep_2020_applications.apply(modify_school_department, axis=1)

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





# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("University Admissions Dashboard"),
    
    # Dropdown for filtering by Group
    html.Label("Select Group:"),
    dcc.Dropdown(
        id='group-filter',
        options=[{'label': group, 'value': group} for group in sep_2020['Group'].unique()],
        value=sep_2020['Group'].unique()[0]
    ),
    
    # Dropdown for filtering by School / Department
    html.Label("Select School / Department:"),
    dcc.Dropdown(
        id='school-filter',
        options=[{'label': school, 'value': school} for school in sep_2020['School / Department'].unique()],
        value=sep_2020['School / Department'].unique()[0]
    ),
    
    # Dropdown for filtering by Level
    html.Label("Select Level:"),
    dcc.Dropdown(
        id='level-filter',
        options=[{'label': level, 'value': level} for level in sep_2020['Level'].unique()],
        value=sep_2020['Level'].unique()[0]
    ),
    
    # Dropdown for filtering by Category
    html.Label("Select Category:"),
    dcc.Dropdown(
        id='category-filter',
        options=[{'label': category, 'value': category} for category in sep_2020['Category'].unique()],
        value=sep_2020['Category'].unique()[0]
    ),
    
    # Line graph
    dcc.Graph(id='line-graph')
])

# Callback to update the graph based on selected filters
@app.callback(
    Output('line-graph', 'figure'),
    [Input('group-filter', 'value'),
     Input('school-filter', 'value'),
     Input('level-filter', 'value'),
     Input('category-filter', 'value')]
)
def update_graph(selected_group, selected_school, selected_level, selected_category):
    filtered_df = sep_2020[
        (sep_2020['Group'] == selected_group) &
        (sep_2020['School / Department'] == selected_school) &
        (sep_2020['Level'] == selected_level) &
        (sep_2020['Category'] == selected_category)
    ]
    
    trace1 = go.Scatter(
        x=filtered_df['Date'],
        y=filtered_df['Number of Applicants'],
        mode='lines+markers',
        name='Number of Applicants'
    )
    
    trace2 = go.Scatter(
        x=filtered_df['Date'],
        y=filtered_df['Number of Acceptances'],
        mode='lines+markers',
        name='Number of Acceptances'
    )
    
    return {
        'data': [trace1, trace2],
        'layout': go.Layout(
            title='Number of Applicants and Acceptances Over Time',
            xaxis={'title': 'Date'},
            yaxis={'title': 'Count'},
            hovermode='closest'
        )
    }

# Run the server
app.run_server(debug = True, port = 8050, use_reloader = False)







