# Problem 1: Loading and Displaying Data
# In this problem, we will:
# 1. Load the CSV file cars.csv into a Pandas DataFrame named 'cars'.
#    - We use pd.read_csv() to load the file into a DataFrame named cars. The file should be located in the default user folder or the same directory as the notebook.
# 2. Display the first five rows and the last five rows of the DataFrame using Pandas functions.
#    - We use cars.head() to display the first five rows and cars.tail() to display the last five rows of the DataFrame. These functions are useful for getting a quick overview of the data.

# Importing the pandas library
import pandas as pd

# Loading the corresponding cars.csv file given into a data frame named 'cars' using pandas
cars = pd.read_csv('cars.csv') 

# Calling the variable 'cars' to output the values
print(cars)

# Displaying the first five rows of the resulting 'cars' DataFrame 
print("First Five Rows:")

# Using the function 'cars.head()' to display the first five rows
print(cars.head())

# Displaying the first ten rows of the resulting 'cars' DataFrame by specifying a value
print("First Ten Rows:")
print(cars.head(10))

# Displaying the last five rows of the resulting 'cars' DataFrame
print("\nLast Five Rows:")

# Using the function 'cars.tail()' to display the last five rows
print(cars.tail())

# Displaying the last ten rows of the resulting 'cars' DataFrame by specifying a value
print("\nLast Ten rows:")
print(cars.tail(10))

# Displaying the first fifty rows of the resulting 'cars' DataFrame
print("First 50 Rows:")

# Specifying a value more than the information stored in the 'cars.csv' will still display all values
print(cars.head(50))