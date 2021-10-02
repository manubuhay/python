#Swap 1st and last character of string length greater than 1
def front_back(str):
  if len(str) > 1:
    #strt = str[0]
    #end = str[-1]
    swapped = str[-1] + str[1:-1] + str[0]
    return swapped
  return str

string = raw_input("Input string: ")
#string1 = front_back("Hello")
swapped = front_back(string)
print(swapped)
