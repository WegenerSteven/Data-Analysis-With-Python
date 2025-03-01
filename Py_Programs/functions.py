#A function is a named block of code that performs a specific task and can be reused throughout your program. Think of it like a recipe: you define the steps once, then call it whenever you need it. In Python, you define functions with the def keyword, and they can take inputs (parameters), process them, and return results.
#Why Use Functions in Data Science?
#Reusability: Write once, use multiple times (e.g., a function to clean data).
#Modularity: Break complex tasks into smaller, manageable pieces.
#Readability: Descriptive function names (e.g., calculate_mean) make code self-explanatory.
#Debugging: Isolate errors to specific functions rather than sprawling scripts.

#def: Keyword to define a function.
#function_name: Name of the function (use descriptive, lowercase names with underscores, e.g., calculate_mean).
#parameters: Inputs (optional; can have none or many).
#return: Sends a result back to the caller (optional; if omitted, the function returns None).

def say_hello():
    print("Hello, Data Scientist!")
say_hello()
#Functions with Parameters
#Parameters allow you to pass data into a function to process. You can have as many parameters as needed, and they act like variables inside the function.
def square(number):
    result = number ** 2
    return result
# Call the function
value = 5
squared_value = square(value)
print(f"Square of {value} is {squared_value}")
