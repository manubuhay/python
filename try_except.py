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
		num1 = int(input("Gae kog numero: "))
		num2 = int(input("Gae kog ikaduha na numero: "))
		question = int(input("Bisaya ni na calculator, unsa imong ginahan buhaton (1 - Add,2 - Subtract,3 - Multiply, 4 - Divide?"))
	except:
		print("Invalid Input!")
		return #Exit program
	if(question == '2'):
		print(subtract(num1, num2))
	elif(question == '3'):
		print(multiply(num1, num2))
	elif(question == '4'):
		print(divide(num1, num2))
	else:
		print(add(num1, num2))
main()
