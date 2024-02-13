import random

character= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
a = int(input("cuantos caracteres quieres que tenga tu contraseña"))
for i in range (a):
    x= random.choice(character)
    password += x
print (password)
