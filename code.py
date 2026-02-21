import random
letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number =['0','1','2','3','4','5','6','7','8','9']
symbols =['!','@','#','$','%','^','&','*']
print("Welcome to password generator!")
No_of_Letters = int(input("Enter your no of letters u want in your password: "))
No_of_Symbols = int(input("Enter your no of symbols u want in your password: "))
No_of_Numbers = int(input("Enter your no of numbers u want in your password: "))

# Creating a empty list for suffle in password: 
password_list =[]

for i in range (1, No_of_Letters + 1):
    var = random.choice(letters)
    password_list += var
for i in range (1, No_of_Symbols + 1):
    var = random.choice(symbols)
    password_list += var
for i in range (1,No_of_Numbers+1):
    var = random.choice(number)
    password_list += var

# it's not in a Shuffle mode so....
print("Before  shuffle   password in list format : " ,password_list)
# Shuffle the list in random ;
random.shuffle(password_list)
print("After shuffle password is in list format : " ,password_list)

# Covert the list in String;
# Create one empty list:
password =""
for char in password_list:
    password += char
  # final answer is After converting ....
print("final password is: " + password)

