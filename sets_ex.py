#Sets is a data structure that only stores UNIQUE values, duplicates will be removed
a = set()
a.add(1)
print(a)
a.add(2)
a.add(70)
a.add(2)
print a

b = set()
c = []

input_max = input("How many numbers? ")
for i in range(0,input_max):
    value = raw_input(str(i+1) + " .) " + "Input values: ")
    c.append(value)
for i in c: #Cannot use "range(0,input_max)" because zero will be added to unique values in set
    b.add(i)

print("Removing duplicates!")
print(b)
