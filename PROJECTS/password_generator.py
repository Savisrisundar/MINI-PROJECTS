import random
print("Welcome to your password generator")
chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
num=int(input("Enter the number of password to be generated:"))
length=int(input("Enter the length of the password:"))
print("Here are your password!")
for pwd in range(num):
    password=''
    for i in range(length):
        password+=random.choice(chars)
    print(pwd,password)
    
        