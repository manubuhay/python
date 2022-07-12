import re

pattern="[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net|ph)"
user_input=input()
if(re.search(pattern,user_input)):
    print("Valid email")
else:
    print("Invalid email")