#1. Arithmetic Operations
#These operations handle numerical data (integers, floats) and are fundamental for calculations in data science, like computing averages or scaling values.
#Key Operations:
#(Addition): Adds numbers.
#(Subtraction): Subtracts numbers.
#(Multiplication): Multiplies numbers.
#(Division): Divides numbers (returns a float).
#(Floor Division): Divides and rounds down to the nearest integer.
#(Modulus): Returns the remainder of division.
#(Exponentiation): Raises a number to a power.

sales = [100, 200, 300]
total_sales = sales[0] + sales[1] + sales[2]
average_sales = total_sales / 3
squared_diff = (sales[0] - average_sales) **2
print("The sales are", sales)
print("Total sales", total_sales)
print("Average sales:", average_sales)
print("Squared difference of the first value: ", squared_diff)

#Comparison operations
#Comparison operations evaluate relationships between values and return booleans (True or False). They’re essential for filtering or decision-making in data science.
#== (Equal to): Checks if two values are equal.
#!= (Not equal to): Checks if two values are different.
#< (Less than), > (Greater than).
#<= (Less than or equal to), >= (Greater than or equal to).

temprature = 25.5
threshold =20.0
is_above_threshold =temprature > threshold
is_exact = temprature == 25.5
not_exact = temprature != 25.5
print("Above Thresholdd", is_above_threshold)
print("Exactly 25.5 : ", is_exact)
print("Not Exact :", not_exact)

#Logical Operations
#Logical operations combine booleans to create more complex conditions, often used in control flow or filtering.
#and: True if both conditions are True.
#or: True if at least one condition is True.
#not: Inverts a boolean (True becomes False, and vice versa).

value = 150
is_high = value > 100
is_positive= value > 0
is_outlier = is_high and is_positive
is_edge_case = is_high or (value < -100)
print("Is Outlier", is_outlier)
print("Is Edge Case", is_edge_case)

#List-Specific Operations
#Since lists are so central to data science, let’s touch on basic operations you can perform on them. While some involve methods (like .append()), there are also operators for lists.
#Key Operations:
#+ (Concatenation): Combines two lists.
#* (Repetition): Repeats a list.
#in (Membership): Checks if an item is in the list.
#Indexing/Slicing: Access specific elements (e.g., list[0] or list[1:3]).

data_a = [10, 20]
data_b = [30, 40]
combined_data = data_a + data_b  # Concatenation
repeated_data = [0] * 3  # Repetition
is_present = 20 in combined_data  # Membership
first_value = combined_data[0]  # Indexing
subset = combined_data[1:3]  # Slicing
print("Combined Data:", combined_data)
print("Repeated Data:", repeated_data)
print("Is 20 Present?", is_present)
print("First Value:", first_value)
print("Subset:", subset)

