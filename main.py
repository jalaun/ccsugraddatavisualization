import pandas as pd
import matplotlib.pyplot as plt

# Data for Black or African American students
black_students = {
    "Year": [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
    "Graduation Rate (%)": [21, 20, 17, 21, 26, 13, 16, 16, None, None, None]  # for None, the data is not available yet
}

# Data for White students
white_students = {
    "Year": [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
    "Graduation Rate (%)": [29, 34, 30, 33, 33, 33, 30, 32, None, None, None]
}

# Data for Hispanic students
hispanic_students = {
    "Year": [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
    "Graduation Rate (%)": [21, 26, 19, 22, 25, 20, 17, 20, None, None, None]
}

df_black = pd.DataFrame(black_students)
df_white = pd.DataFrame(white_students)
df_hispanic = pd.DataFrame(hispanic_students)

#matplotlib library used to create a new figure for plotting with the specified size
#figure will be 12 inches wide and 6 inches tall
plt.figure(figsize=(12, 6))
#.plot draws a line plot. marker = o means each data point will be marked with a circle
plt.plot(df_black["Year"], df_black["Graduation Rate (%)"], marker='o', color='black', label='Black Students')
plt.plot(df_white["Year"], df_white["Graduation Rate (%)"], marker='o', color='yellow', label='White Students')
plt.plot(df_hispanic["Year"], df_hispanic["Graduation Rate (%)"], marker='o', color='red', label='Hispanic Students')

plt.title("4-Year Graduation Rates by Race (2012-2022)")
plt.xlabel("Year")
plt.ylabel("Graduation Rate (%)")
plt.legend()
plt.grid(True)
plt.show()
