#Swap 1st and last character of string length greater than 1
def front_back(str):
  if len(str) > 1:
    strt = str[0]
    end = str[-1]
    swapped = end + str[1:-1] + strt
    return swapped
  return str

string1 = front_back("Hello")
print(string1)
