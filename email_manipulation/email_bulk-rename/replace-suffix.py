import csv

email_list = list(open('email.csv'))
print("-----Old list-----")
for i in range(len(email_list)):
    print(email_list[i].strip('\n'))
print("-----New list-----")
for x in range(len(email_list)):
    email_list[x]=email_list[x].replace("abc.com","xyz.com")
    print(email_list[x].strip('\n'))
    with open('new-suffix.csv', 'a') as newfile:
        newfile.write(email_list[x])