import re



def password_strength():
    '''Check ur Password'''
    password = input("Enter a password : ")
    if len(password) < 9:
        print("Bad Password --> Add more characters")
    else:
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower = 'abcdefghijklmnopqrstuvwxyz'
        special = '~`!@#$%^&*)_-+={[]}|'
        number = '0123456789'
        x = re.findall("[~,`,!,@,#,$,%,^,&,*,),_,-,+,=,{,[,],},|,]", password)
        y = re.findall("[0123456789]", password)
        z = re.findall("[a-zA-Z]", password)
        if x and y and z:
            print("Strong Password")
        elif (x and y) or (y and z) or (z and x):
            print("Good Password")
        elif x or y or z:
            print("Mid Password")
        else:
            print("Bad Password")

password_strength()


 