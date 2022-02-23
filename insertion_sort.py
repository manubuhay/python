MAX=9
a=[]
for i in range(MAX):
    input1=int(input("Enter values: "))
    a.append(input1)
print(a,"\n")

for i in range(1,MAX):
    temp=a[i]
    j=i-1
    while temp<a[j] and j>=0:
        a[j+1]=a[j]
        j=j-1
    a[j+1]=temp
print("Resulting list is ",a)