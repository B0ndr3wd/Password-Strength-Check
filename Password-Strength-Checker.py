import re

def password_strength():
    '''Check ur Password'''
    password = input("Enter a password : ")
    if len(password) < 8:
        print("Bad Password --> Add more characters")
    else:
        x = re.findall(r"[~`!@#$%^&*()_\-+=\[\]{}|]", password)
        y = re.findall(r"[0123456789]", password)
        z = re.findall(r"[a-zA-Z]", password)
        if x and y and z:
            print("Strong Password")
        elif (x and y) or (y and z) or (z and x):
            print("Mid Password")
        else:
            print("Bad Password")

password_strength()


 