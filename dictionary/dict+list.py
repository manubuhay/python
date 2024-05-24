# company={
#     "name":"john smith",
#     "designation":"IT",
#     "age":35,
#     "location":(12.34567,-98.7654)
# }
# # print(company["name"])
# # print(company["location"])
# position = company.get("designation",None )
# print(position)

companylist=[
    {
    "name":"john smith",
    "designation":"IT",
    "age":25,
    "location":(12.34567,-98.7654)
    },
    {
    "name":"jane doe",
    "designation":"HR",
    "age":25,
    "location":(32.34567,-87.7654)
    },
    {
    "name":"mark smith",
    "designation":"CEO",
    "age":45,
    "location":(32.34567,-87.7654)
    },
    {
    "name":"jack sparrow",
    "designation":"Accountant",
    "age":30,
    "location":(42.34567,-77.7654)
    }
            ]

# print(companylist[2]["designation"])
# print(companylist[1]["location"])
# print(companylist[0]["age"])

# print(companylist)
for x in range(len(companylist)): # x must be int to hold index of list companylist, use "len" method to get length of companylist
    for y in companylist[x]: 
        if companylist[x][y] == 25: # print records that have 25 as age
            print(companylist[x])

for a in range(len(companylist)):
    for b in companylist[a]:
        if "location" in b: # if location exists as key pair, print dictionary record
            print(companylist[a][b])
        
    
