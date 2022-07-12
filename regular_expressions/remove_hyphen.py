import re

pattern="(\d\d\d)-(\d\d\d)-(\d\d\d\d)"
newpattern=r"\1\2\3"
user_input=input()
new_user_input=re.sub(pattern,newpattern,user_input)
print(new_user_input)