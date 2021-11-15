import random, string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

if __name__=="__main__":
    # x=randomword(5)
    # print(x)
    letters=string.ascii_letters
    new_str="".join(random.choice(letters) for i in range(0,5))
    print(new_str)