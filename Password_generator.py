import random
import string
letters=string.ascii_letters
numbers=string.digits
punctuation=string.punctuation
char_pool=letters+numbers+punctuation

while True:
    N_digits=input("Choose the length of your new password: ")
    if N_digits.isdigit():
        N_digits=int(N_digits)
        if N_digits<6:
         print("Password length must be at least 6 characters. ")
        if N_digits>=6:
         break
    else:
        print("Please enter a valid number. ")

password=""
for i in range(N_digits):
 digit=random.choice(char_pool)

 password=password+digit
print(f"Your password is {password}. ")
