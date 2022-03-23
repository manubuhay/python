mylist=[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
#        0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#      -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:step]
print(mylist[0])
print(mylist[5])
print(mylist[-10])

#From 0 to 5, prints 0-4 because end value is 5(it doesnt include 5)
print(mylist[0:5])
#To include 5, do this
print(mylist[0:6])
#3 to 7
print(mylist[3:8])
#Include negative,
print(mylist[-7:8])
print(mylist[-7:-2])
#Starting point to last value in list, since :9 is non inclusive
print(mylist[1:])

#Enter list
print(mylist[:])
###Step
#2 to 8, with a step of 2
print(mylist[2:-1:2])
#Empty because step is -1
print(mylist[2:-1:-1])
#Reverse order printing, 9 to 3
print(mylist[-1:2:-1])
#8 to 2
print(mylist[-2:1:-1])
#8 to 2 with step 2
print(mylist[-2:1:-2])
#Reverse print entire list
print(mylist[::-1])

###String slicing

sample_url="http://site.url"
print(sample_url)
#Reverse the URL
print(sample_url[::-1])
#Get top level domain, prints ".url",(l=-1,r=-2,u=-3 and .=-4)
print(sample_url[-4:])
#Print URL without http://
print(sample_url[7:])
#Print URL without http:// and the top level domain(.com)
print(sample_url[7:-4])
