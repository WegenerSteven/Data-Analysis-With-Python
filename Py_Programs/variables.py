#Variables are essential containers for storing data,and python makes easy to work with since you don't have declare them explicitly.
#Variables are names that hold values that you can use later in your code,In python, you create variables by assigning a value to it using the "=" operator.
#Key points to take home are -No need to declare the type integer,string before hand
#-variable names should be descriptive eg, age, temprature_data
#-Rules for naming start with a letter or underscore can include numbers, no spaces case sensitve.
#The main datatypes are integers, float, strings,booleans,lists, dictionaries
#These is comment

#Integers in Python
#Explanation: They are whole numbers(that's no decimals) they are usefull for counts, indices, or any data that does not need fractional precision
num_rows = 13
print("Number of rows in database:" , num_rows)
age = 22
print("I am ,", age , "years old.")

#Floats
#Floats are numbers with decimals like 3.14, -0.23 they are essential for measure, percentages or requiring precision
average_score = 85.5
print("The average score is :", average_score)
average_salary = 89000.00
print("Your average salary is Ksh.",average_salary)

#Strings
#Strings are sequences of characters(text) enclosed in single('') or double("") quotes. They are used for labels, categories, or textual data
dataset_name = 'Sales Data 2025'
print(dataset_name)
title = "Upskill Data Analytics"
print("We are learning on: ", title)

#Booleans
#Boleans represent True and False
is_complete = False
print("Is Data Processing Complete .", is_complete)
like_dataanalytics = True
print("Do you like Data Analytics", like_dataanalytics)

#Lists in python
#They are perfect for storing a small dataset or subset of values to analyze
#Lists are ordered, mutable(changeable) collections of items, enclosed in the square brackets[].they can hold mixed data type and are widely used in data science for storing sequence like rows or columns
data_points = [23, 45, 67,12]
print("The points collected: ", data_points)


#Dictionaries in Python
#They are unordered collection of key value pairs enclosed in curly braces{}.They are great for structured data where you need to look up values by a key  like mini database
student_record = {"name": "Alex", "grade": 78, "passed": True}
print("Student Info: ", student_record)


#Assigning and reassigning Variables
#You can assign a value to a variable with = and reassign it later.Python will update the variables value dynamically.
temprature = 25.5
print("Initial temparature is:", temprature)
temprature = 26.0
print("Updated temprature is:", temprature)

#Type Checking and conversion
#You can check the variable type with type() and convert between types eg integer to float. This is handy when the data types do not match your needs
price = 10
print("Data type price..", type(price))
price_float = float(price)
print("Price as float, ", price_float, "Type", type(price_float))

#Mini exercise
#Create variables for a dataset's name(string), row  count(integer), and average value(integer)
#Solution
dataset_nem = "SalesData"
row_count = 3
average_value =25.0
sample_data = [10, 30, 20]
print(f"Dataset, {dataset_nem} has  {row_count} rows with {average_value}")
print("Sample data", sample_data)