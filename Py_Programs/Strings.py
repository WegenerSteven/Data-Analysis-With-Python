#Strings are used for labels, categories or text data in data science.While strings don't "calculate" like numbers you can manipulate them with key few words
#(+) Conacatenation joins strings together
#(*)Repetition Repeats a string multiple number of times
#String methods(not operators but useful).Like .upper() .lower(), .strip()

dataset_prefix = "Sales"
year = "2025"
file_name = dataset_prefix + " " + year
repated_border = "_" * 10
column_name = "price"
cleaned_column = column_name.strip()
print(dataset_prefix)
print("File Name: ", file_name)
print("Border: ", repated_border)
print("Cleaned Column: ", cleaned_column)