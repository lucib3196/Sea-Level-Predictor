import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')
  
  # Sets up x and y variable using data from DataFrame
  x = df['Year']
  y= df["CSIRO Adjusted Sea Level"]
  # Using linregress to find values such as slope, y-int ect.
  res = linregress(x,y)

  # Creates new Dataframe from the original which appends dates up to 2050
  df2 = df.copy()
  for i in range(2014,2051):
      df2 = df2.append({'Year': i},ignore_index=True)
    
  # Using the values from x and y to plot a line of best fit
  x_1 = df2['Year']
  y_1 = res.slope*x_1 + res.intercept # y is essentially in the form y=mx+b

  # Use a new Dataframe to filter values from 2000-2013 and will be used to find new slope and y intercept 
  new_df = df[df['Year']>=2000]
  x_new = new_df['Year']
  y_new = new_df["CSIRO Adjusted Sea Level"]
  res_2 = linregress(x_new,y_new)

  # Uses the appeneded dataframe to create a new line of best fit
  new_df2 = df2[df2['Year']>=2000]
  x_3 = new_df2['Year']
  y_3 = res_2.slope*x_3 + res_2.intercept 
  
  
  fig, ax = plt.subplots(figsize=(15,10))
  # Scatter Plot
  plt.scatter(x=x, y=y, label = 'Original Data')
  # Line of Best Fit 1, using all the data points
  plt.plot(x_1,y_1, label='Best Fit 1')
  # Line of Best Fit 2, only using data from 2000-2013
  plt.plot(x_3,y_3, label='Best Fit 2')
  
  plt.legend() # Shows Legend

  # Basic Plot Formating 
  plt.xlabel("Year") 
  plt.ylabel("Sea Level (inches)")
  plt.title("Rise in Sea Level")
  plt.xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
  
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()

draw_plot()