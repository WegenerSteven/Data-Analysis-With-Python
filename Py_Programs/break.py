#Loop control statements
#Break = Terminates the loop statement
#Continue = Causes the loop to skip the
#Pass = Commands code to execute

#Break
for letter in 'Python':
    if letter == 'h':
        break
    print("Current Letter :", letter)
var = 10
while var > 0:
    print("Current variable value :",var)
    var = var -1
    if var == 5:
        break
    print("Good Bye!")
id = [1,2,3,4,5,]
print(id)
x = int(input("Enter A Number"))
for i in range(len(id)):
    if x == id[i]:
        break
    if i < len(id)-1:
        print(x, 'Found at position :',i+1)
    else:
        print(x, 'Not found in the list.')

