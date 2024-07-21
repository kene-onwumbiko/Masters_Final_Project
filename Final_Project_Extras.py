# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 17:09:09 2024

@author: keneo
"""

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


fig= px.scatter(sep_2020, x="Date", y="Number of Applicants",
                color="School / Department",
                size="Category", size_max=55,
                hover_name="School / Department",
                animation_frame="Date", 
                animation_group="School / Department",
                log_x=True,range_x=[100,100000], range_y=[25,90])
                # x_range and y_range to ensure that data remains visible throughout the animation
# save and open the output as html
fig.write_html('lifeExp4.html', auto_open=True)