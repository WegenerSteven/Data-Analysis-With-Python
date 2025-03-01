# Loop through each letter in the word "Python"
for letter in 'Python':
    if letter == 'h':
        continue  # Skip 'h'
    print('Current Letter :', letter)

var = 10
while var > 0:
    var -= 1
    if var == 5:
        continue 
    print('Current variable value :', var)
pwd = "@#$"
while True:
    x = input("Password: ")
    if x != pwd:
        print("Enter Again")
        continue
    print("Password entered correctly")
    break