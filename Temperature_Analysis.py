#!/usr/bin/env python
# coding: utf-8

# #  Importing Panda

# In[20]:


import os
import pandas as pd


# # Uploading excel files and converting them to csv

# In[21]:


# defining the folder where all the Excel files are stored
folder_path = "D:/downloads folder/Downloads/weather analysis/temperatures"

# Looping through all the files in the specified folder
for filename in os.listdir(folder_path):
    
    # Checking if the current file is an Excel file (.xlsx or .xls)
    if filename.endswith('.xlsx') or filename.endswith('.xls'):
        
        # Creating the full file path by joining the folder path with the filename
        filepath = os.path.join(folder_path, filename)
        
        # Reading the Excel file into a pandas DataFrame
        df = pd.read_excel(filepath)
        
        # Creating a new filename by replacing the file extension with .csv
        new_filename = filename.rsplit('.', 1)[0] + '.csv'
        
        # Saving the DataFrame as a CSV file in the same folder
        df.to_csv(os.path.join(folder_path, new_filename), index=False)


# # Loading csv files

# In[22]:


# Defining a function to load all CSV files from a given folder and combine them into one DataFrame
def load_all_data(folder_path):
    # Creating an empty list to store individual DataFrames
    all_data = []

    # Looing through each file in the folder, sorted by filename
    for filename in sorted(os.listdir(folder_path)):
        
        # Checking if the file has a .csv extension
        if filename.endswith('.csv'):
            
            # Creating the full path to the file
            filepath = os.path.join(folder_path, filename)
            
            # Reading the CSV file into a DataFrame
            df = pd.read_csv(filepath)
            
            # Extracting the year from the filename 
            df['Year'] = filename[-8:-4]
            
            # Appending the DataFrame to the list
            all_data.append(df)

    # Concatenating all DataFrames into one and reset the index
    return pd.concat(all_data, ignore_index=True)


# # Average temperatures for each season across all years

# In[13]:


# Defining a function to calculate average temperatures for each season
def calculate_seasonal_averages(df):
    
    # Dictionary that defines which months belong to which season
    seasons = {
        'Summer': ['December', 'January', 'February'],
        'Autumn': ['March', 'April', 'May'],
        'Winter': ['June', 'July', 'August'],
        'Spring': ['September', 'October', 'November']
    }

    # Dictionary to store the average temperature result for each season
    results = {}

    # Looping through each season and its corresponding months
    for season, months in seasons.items():
        
        # Filtering out months that are not present in the DataFrame columns
        valid_months = [m for m in months if m in df.columns]
        
        # Calculating the average temperature for the valid months by stacking and taking the mean
        results[season] = df[valid_months].stack().mean()

    # Printing the average temperature for each season, formatted to two decimal places
    for season, avg in results.items():
        print(f"{season}: {avg:.2f} °C")


# In[23]:


df = load_all_data(folder_path)  # Loading all the CSV data into a single DataFrame
calculate_seasonal_averages(df)  # Calculating and print average temperatures for each season


# # Station/stations have the largest temperature range

# In[24]:


# Defining a function to find the stations with the largest temperature range
def find_largest_temp_range(df):
    
    # Finding the maximum temperature for each row (station/year) across all months
    df['MaxTemp'] = df.loc[:, 'January':'December'].max(axis=1)
    
    # Finding the minimum temperature for each row (station/year) across all months
    df['MinTemp'] = df.loc[:, 'January':'December'].min(axis=1)
    
    # Calculating the temperature range for each row
    df['Range'] = df['MaxTemp'] - df['MinTemp']
    
    # Finding the highest temperature range in the dataset
    max_range = df['Range'].max()
    
    # Getting the name(s) of station(s) that have this maximum temperature range
    stations = df[df['Range'] == max_range]['STATION_NAME'].unique()
    
    # Printing the largest temperature range and the corresponding station(s)
    print(f"Largest temperature range: {max_range:.2f} °C")
    print("Station(s):", ", ".join(stations))
    
    # Writing the result to a text file
    with open("largest_temp_range_station.txt", "w") as f:
        f.write(f"Largest temperature range: {max_range:.2f} °C\n")
        for station in stations:
            f.write(f"{station}\n")

# Calling the function using your combined dataset
find_largest_temp_range(df)


# # Finding the warmest and coolest station/stations

# In[25]:


# Defining a function to find the warmest and coolest stations based on average temperatures
def find_warmest_and_coolest(df):

    # Calculating the average (mean) temperature across all months for each row (station/year)
    df['MeanTemp'] = df.loc[:, 'January':'December'].mean(axis=1)

    # Grouping the data by station name and calculate the average of the mean temperatures for each station
    station_avg = df.groupby('STATION_NAME')['MeanTemp'].mean()

    # Finding the maximum and minimum average temperatures
    max_avg = station_avg.max()
    min_avg = station_avg.min()

    # Getting the station(s) with the highest average temperature
    warmest = station_avg[station_avg == max_avg]

    # Getting the station(s) with the lowest average temperature
    coolest = station_avg[station_avg == min_avg]

    # Printing the warmest station(s)
    print("Warmest Station(s):")
    for name, temp in warmest.items():
        print(f"{name} - {temp:.2f} °C")

    # Printing the coolest station(s)
    print("\nCoolest Station(s):")
    for name, temp in coolest.items():
        print(f"{name} - {temp:.2f} °C")

    # Saving the results to a text file
    with open("warmest_and_coolest_station.txt", "w") as f:
        f.write("Warmest Station(s):\n")
        for name, temp in warmest.items():
            f.write(f"{name} - {temp:.2f} °C\n")
        f.write("\nCoolest Station(s):\n")
        for name, temp in coolest.items():
            f.write(f"{name} - {temp:.2f} °C\n")

# Calling the function with the loaded temperature data
find_warmest_and_coolest(df)


# In[ ]:




