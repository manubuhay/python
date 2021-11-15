###Normal
x=123
print("Normal output:",x)

###Walrused
print("Walrused output:",x:=123)

###Normal
[x for x in range(10)]
def square(x):
    return x*x
[square(x) for x in range(10)]
#Even
[square(x) for x in range(10) if square(x)%2==0]

###Walrused
[y for x in range(10) if (y:=square(x))%2==0]

###Normal
while True:
    name=input("Enter name: ")
    if name=="exit":
        break
    print("Hello",name)

###Walrused
while(name:=input("Enter name: "))!="exit":
    print("Hello",name)