x = [1,2,3,4,5]
print(x)
y = []

max = int(input("How many values?"))
for i in range(0,max):
    input1 = input(str(i+1) + ".) " + "Input values now: ")
    y.append(input1)
    #y.apnpend(i) = input("Input values now: ") #Cannot assign value to function, use variables instead
print(y,"\n")

#Execute selection sort(Descending)
for i in range(max-1):
    for j in range(i+1,max):
        if int(y[i]) > int(y[j]): #Convert to int because list is string type
            temp = int(y[j]) #If int is not specified, list will be sorted according to 1st digit
            y[j] = int(y[i])
            y[i] = int(temp)
print("Descending order:")
print(y,"\n")

#Execute selection sort(Ascending)
for i in range(max-1):
    for j in range(i+1,max):
        if int(y[i]) < int(y[j]): #Convert to int because list is string type
            temp = int(y[j]) #If int is not specified, list will be sorted according to 1st digit
            y[j] = int(y[i])
            y[i] = int(temp)
print("Ascending order:")
print(y)
