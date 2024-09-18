# **EXPERIMENT 3 - PYTHON DATA ANALYSIS (PANDAS)**

This repository contains code and solutions for two problems that demonstrate data manipulation and analysis using the Pandas library in Python. The experiment focuses on loading data, displaying specific rows, and extracting relevant information using indexing, slicing, and Boolean operations.

---

## PROBLEM 1: LOADING AND DISPLAYING DATA
Load a CSV file (`cars.csv`) into a Pandas DataFrame named `cars`. Display the first five and last five rows of the dataset to get an overview of the data.
  
- **Functions Used**:  
  - `pd.read_csv()` to load the data.  
  - `cars.head()` to display the first rows.  
  - `cars.tail()` to display the last rows.
  
- **Expected Output**:  
  The first five rows, the last five rows, and a few other slices (10, 50 rows) of the dataset will be displayed.

### Code Line Breakdown:

1. **Function used**: `import pandas as pd`  
   **Description**: This imports the Pandas library, which is essential for loading and manipulating the data in a DataFrame.

2. **Function used**: `cars = pd.read_csv('cars.csv')`  
   **Description**: This line loads the `cars.csv` file into a Pandas DataFrame named `cars`.

3. **Function used**: `cars`  
   **Description**: Outputs the entire DataFrame, useful for viewing the loaded data.

4. **Function used**: `print("First Five Rows:")`  
   **Description**: Prints a label indicating that the following output shows the first five rows.

5. **Function used**: `cars.head()`  
   **Description**: Displays the first five rows of the DataFrame. This is useful for a quick preview of the dataset.

6. **Function used**: `print("First Ten Rows:")`  
   **Description**: Prints a label indicating that the following output shows the first ten rows.

7. **Function used**: `cars.head(10)`  
   **Description**: Displays the first ten rows of the DataFrame by specifying 10 as the argument for `head()`.

8. **Function used**: `print("\nLast Five Rows:")`  
   **Description**: Prints a label indicating that the following output shows the last five rows.

9. **Function used**: `cars.tail()`  
   **Description**: Displays the last five rows of the DataFrame using the `tail()` function.

10. **Function used**: `print("\nLast Ten rows:")`  
    **Description**: Prints a label indicating that the following output shows the last ten rows.

11. **Function used**: `cars.tail(10)`  
    **Description**: Displays the last ten rows of the DataFrame by specifying 10 as the argument for `tail()`.

12. **Function used**: `print("First 50 Rows:")`  
    **Description**: Prints a label indicating that the following output shows the first fifty rows.

13. **Function used**: `cars.head(50)`  
    **Description**: Displays the first fifty rows of the DataFrame by specifying 50 as the argument for `head()`.

### Conclusion:

This part of the experiment involves loading the `cars.csv` dataset and getting an overview of its contents by displaying specific subsets of the data. We use `head()` and `tail()` to display rows from the top and bottom of the DataFrame, which helps to quickly understand the dataset's structure.

---

## PROBLEM 2: EXTRACTING SPECIFIC DATA USING SUBSETTING, SLICING, AND INDEXING
Extract specific information from the `cars` DataFrame, such as displaying only odd-numbered columns, finding specific rows, and extracting certain columns for particular car models.

- **Functions Used**:  
  - `iloc[]` for slicing rows and columns.  
  - Boolean indexing (`cars['Model'] == 'Mazda RX4'`) to locate specific rows.  
  - `.loc[]` and `.isin()` for selecting and filtering data.
  
- **Expected Output**:  
  Subsets of data for odd-numbered columns, specific rows for car models, and selected columns (like `cyl` and `gear`) for particular models.

### Code Line Breakdown:

1. **Function used**: `import pandas as pd`  
   **Description**: This imports the Pandas library, required for data manipulation and analysis.

2. **Function used**: `cars = pd.read_csv('cars.csv')`  
   **Description**: Loads the `cars.csv` file into a DataFrame named `cars`.

3. **Function used**: `print("\nFirst Five Rows With Odd-Numbered Columns:")`  
   **Description**: Prints a label indicating that the following output shows the first five rows with only odd-numbered columns.

4. **Function used**: `cars.iloc[:5, ::2]`  
   **Description**: Displays the first five rows of the DataFrame, but only the odd-numbered columns (1st, 3rd, 5th, etc.) using slicing with `iloc[]`.

5. **Function used**: `print("\nRow for the Car Model 'Mazda RX4':")`  
   **Description**: Prints a label indicating that the following output will show the row for the 'Mazda RX4' model.

6. **Function used**: `cars[cars['Model'] == 'Mazda RX4']`  
   **Description**: Uses Boolean indexing to filter and display the row for the 'Mazda RX4' model.

7. **Function used**: `print("\nRow for the Car Model 'Mazda RX4':")`  
   **Description**: Prints a label indicating an alternative method to show the row for 'Mazda RX4' using `.query()`.

8. **Function used**: `cars.query('Model == "Mazda RX4"')`  
   **Description**: Uses the `.query()` function to filter and display the row for the 'Mazda RX4' model, providing a more readable alternative to Boolean indexing.

9. **Function used**: `print("\nNumber of Cylinders for 'Camaro Z28':")`  
   **Description**: Prints a label indicating that the following output will show the number of cylinders for 'Camaro Z28'.

10. **Function used**: `cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']]`  
    **Description**: Uses `.loc[]` to filter the row for 'Camaro Z28' and display the 'Model' and 'cyl' columns, showing the number of cylinders.

11. **Function used**: `print("\nNumber of Cylinders for 'Camaro Z28':")`  
    **Description**: Prints a label indicating that the following output will show the number of cylinders for 'Camaro Z28' using a different method.

12. **Function used**: `cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0]`  
    **Description**: Retrieves the exact number of cylinders for 'Camaro Z28' by accessing the `cyl` column and extracting the value directly.

13. **Function used**: `print("\nCylinders and Gear Type for 'Mazda RX4 Wag', 'Ford Pantera L' and 'Honda Civic':")`  
    **Description**: Prints a label indicating that the following output will show the number of cylinders and gear type for specific car models.

14. **Function used**: `subset_models = cars[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic'])]`  
    **Description**: Uses `.isin()` to filter and select rows for the car models 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic'.

15. **Function used**: `subset_models[['Model', 'cyl', 'gear']]`  
    **Description**: Displays the 'Model', 'cyl', and 'gear' columns for the filtered car models.

### Conclusion:

In Problem 2, we utilize various subsetting techniques such as slicing, Boolean indexing, and the `.isin()` method to extract specific data from the DataFrame. This problem demonstrates how to efficiently filter and retrieve relevant columns and rows based on certain conditions.

---

###### Author: **Francesca Ellaiza R. Nacu**
