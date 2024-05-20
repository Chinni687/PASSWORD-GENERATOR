import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
           'v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
           'Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols  = ['!','@','#','$','%','(',')','*','^','+','-']

print( "WELCOME TO PASSWORD GENERATOR")
print("It will generate 2 passwords")
n_letters = int(input("Enter how many letters you want in your password: ")) 
n_numbers = int(input("Enter how many numbers you want in your password: ")) 
n_symbols = int(input("Enter how many symbols you want in your password: "))  

password_list1 = []  
password_list2 = []


for i in range(1,n_letters+1):
    char = random.choice(letters)
    password_list1 +=char
    password_list2 +=char
    
for i in range(1,n_numbers+1):
    char = random.choice(numbers)
    password_list1 += char
    password_list2 += char
    
for i in range(1,n_symbols+1):
    char = random.choice(symbols)
    password_list1 += char
    password_list2 += char
print(password_list1)
print(password_list2)
random.shuffle(password_list1)
random.shuffle(password_list2)
print(password_list1)
print(password_list2)
password1 = " "
password2 = " "
for char in password_list1:
    password1 += char
print(password1)
for char in password_list2:
    password2+= char
print(password2)    


  
         
         