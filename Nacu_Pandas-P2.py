# Problem 2: Extracting Specific Data using Subsetting, Slicing, and Indexing
# In this problem, we will extract specific information from the cars DataFrame, such as:
# 1. Display the first five rows with only odd-numbered columns.
#    - 'iloc[:5, ::2]' is used to subset the DataFrame. Here, :5 selects the first five rows, and ::2 selects only odd-numbered columns (i.e., 1st, 3rd, 5th columns).
# 2. Find the row that contains the 'Mazda RX4' model.
#    - Boolean indexing (i.e., cars['Model'] == 'Mazda RX4') is used to find the row where the 'Model' column equals 'Mazda RX4'.
# 3. Determine how many cylinders the 'Camaro Z28' has.
#    - Boolean indexing is used again to find the 'Camaro Z28' row, then we select the 'cyl' column to display the number of cylinders.
# 4. Find the number of cylinders and the gear type for the models 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic'.
#    - isin() is used to filter rows for these specific car models, and then we select the 'Model', 'cyl', and 'gear' columns to display the desired data.

# Expected Output
#    - Odd-numbered columns for the first five rows using 'cars.iloc[:5, ::2]' will show columns like 1st, 3rd, and 5th.
#    - The row where the 'Mazda RX4' model is located will be returned when using either Boolean indexing or the '.query()' function.
#    - For the 'Camaro Z28', the number of cylinders will be shown.
#    - The number of cylinders and gear type for 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic' will display only relevant columns (i.e., 'Model', 'cyl', 'gear') for those models.

# Importing the pandas library
import pandas as pd

# Loading the 'cars.csv' file into a DataFrame again (continuing from problem 1)
cars = pd.read_csv('cars.csv')

# Displaying the first five rows with odd-numbered columns (columns 1, 3, 5, 7...)
print("\nFirst Five Rows With Odd-Numbered Columns:")

# Using slicing to select odd-numbered columns wherein ::2 selects every second column
print(cars.iloc[:5, ::2])

# Displaying the row that contains the 'Model' of 'Mazda RX4'
print("\nRow for the Car Model 'Mazda RX4':")

# Using Boolean indexing to filter the row for 'Mazda RX4'
print(cars[cars['Model'] == 'Mazda RX4'])

# Alternative method: Displaying the row for 'Mazda RX4' using query()
# The .query() function is a simple and readable way to filter rows based on conditions
print("\nRow for the Car Model 'Mazda RX4' (using .query()):")
print(cars.query('Model == "Mazda RX4"'))

# Displaying the number of cylinders ('cyl') of the car model 'Camaro Z28'
print("\nNumber of Cylinders for 'Camaro Z28':")
print(cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']])

# Alternative method: Finding the number of cylinders for 'Camaro Z28' using .loc[]
# The .loc[] function is used for label-based indexing, which is more intuitive for selecting specific data points
print("\nNumber of Cylinders for 'Camaro Z28' (direct value):")
print(cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0])

# Displaying the number of cylinders ('cyl') and gear type ('gear') of the car models 'Mazda RX4 Wag', 'Ford Pantera L' and 'Honda Civic'
print("\nCylinders and Gear Type for 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic':")

# Using the .isin() function to find rows that match specific models, and selecting relevant columns
subset_models = cars[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic'])]
print(subset_models[['Model', 'cyl', 'gear']])