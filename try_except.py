#Adds numbers
def add(a, b):
    return a + b
#Subtracts numbers
def subtract(a, b):
    return a - b
#Multiplies numbers
def multiply(x, y):
    return x * y
#Divides numbers
def divide(x, y):
    return x / y

#Main function
def main():
    try:
        num1 = int(input("Enter 1st number: "))
        num2 = int(input("Enter 2nd number: "))
        question = int(input("Choose your operation( 1 - Add,2 - Subtract,3 - Multiply, 4 - Divide?)"))
    except:
        print("Invalid Input!")
        return #Exit program
    if(question == 2):
        print(subtract(num1, num2))
    elif(question == 3):
        print(multiply(num1, num2))
    elif(question == 4):
	    print(divide(num1, num2))
    elif(question == 1):
        print(add(num1,num2))
    else:
        print("Number Out Of Range!")
main()
