import re

pattern = re.compile(r"[a-zA-Z#@$0-9]{8,}\d")
password = input("Enter your password : ")
x = pattern.fullmatch(password)
if(x):
    print("Password Accepted")
else:
    print("Invalid password")