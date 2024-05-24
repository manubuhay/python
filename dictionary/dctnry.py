d = {}
e = dict()

#d["ct1"] = "1.1.1.62"

d = {"ct1": "192.168.1.1", "ct2": "192.168.1.2"}
d["ct3"] = "192.168.1.3"
#print(d["ct1"])
#print(d["ct2"])

for i in d:
    print(i)
    print(d[i])


#Input and output values into a dictionary
index = input("Input index: ")
kypr = input("Input keypair: ")
e = {index: kypr}
print("Index and keypair is: ")
print(e)
