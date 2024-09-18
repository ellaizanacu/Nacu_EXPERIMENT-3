# Problem 1: Loading and Displaying Data
# In this problem, we will:
# 1. Load the CSV file 'cars.csv' into a Pandas DataFrame named 'cars'.
#    - 'pd.read_csv()' is used to read the CSV file and load it into a DataFrame named cars. This file is expected to be located in the same directory as the notebook or in a default user folder.
# 2. Display the first five rows and the last five rows of the DataFrame using Pandas functions.
#    - 'cars.head()' displays the first five rows, while cars.tail() displays the last five rows. These functions are useful for quickly previewing the data.

# Expected Output
#    - The first five rows of the dataset, using 'cars.head()', will show the top entries to help understand the structure of the data.
#    - The first ten rows using 'cars.head(10)' will give a broader view of the top records.
#    - 'cars.tail()' will return the last five rows, useful for checking how the data ends.
#    - Similarly, 'cars.tail()' gives the last ten rows for more data at the bottom.
#    - The first 50 rows will be shown if the dataset is long enough; otherwise, it will return as many rows as the data contains.

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