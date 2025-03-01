for letter in 'Python':
    print('Current Letter :', letter)
for fruits in ['banana', 'apple', 'mango']:
    print('Current Fruit :', fruits)
print('Good Bye!')

#For loop using range() function
for num in range(5):
    print(num)
    print("range(start,stop)")
for num in range(1,5):
    print(num)
for num in range(1,6,2):
    print(num)

#For loop iterating by sequence index
dict = {'011':'New Delhi','022':'Mumbai','033':'Kolkata'}
for key in dict:
    print(dict[key])
for key,value in dict.items():
    print(key,value)
for val in dict.values():
    print(val)
for key in dict.keys():
    print(key)

#Else with for loop
count = 0
for count in range(10):
    print("Hello World ",count)
else:
    print("End of for loop")
    print("Good Bye!")