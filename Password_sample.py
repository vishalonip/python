# generate a password with length "passlen" with no duplicate characters in the password
import random

x = "abcdefghijklmnopqrstuvwxyz"
y = "01234567890"
z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t = "!@#$%^&*()?"
passlen = int(input("Enter the random password length (less than 20): " ))
while passlen >=20:
    print("Please enter less than 20")
    break
else:
    b=int(passlen/4)
    c=int(passlen - 3*b)
    password = (random.sample(x,b) + random.sample(y,b) + random.sample(z,b) + random.sample(t,c))
    print("".join(password))