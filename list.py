x = [1,2,3,4,5]
print(x)
y = []

max = int(input("How many values?"))
for i in range(0,max):
    input1 = int(input(str(i+1) + ".) " + "Input values now: ")) #Convert to int because default is string type
    y.append(input1) #If int is not specified, list will be sorted according to 1st digit
    #y.append(i) = input("Input values now: ") #Cannot assign value to function, use variables instead
print(y,"\n")

#Execute selection sort(Descending)
for i in range(max-1):
    for j in range(i+1,max):
        if y[i] > y[j]:
            temp = y[j]
            y[j] = y[i]
            y[i] = temp
print("Descending order:")
print(y,"\n")

#Execute selection sort(Ascending)
for i in range(max-1):
    for j in range(i+1,max):
        if y[i] < y[j]:
            temp = y[j]
            y[j] = y[i]
            y[i] = temp
print("Descending order:")
print(y,"\n")
