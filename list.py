x = [1,2,3,4,5]
print(x)
y = []

max = int(input("How many values?"))
for i in range(0,max):
    input1 = input(str(i+1) + ".) " + "Input values now: ")
    y.append(input1)
    #y.append(i) = input("Input values now: ") #Cannot assign value to function, use variables instead
print(y)
