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
	question = input("Calculator written in Python, choose your action (+,-,*,/) ?")
	if(question != '+' and question != '-' and question != '*' and question != '/'):
		print("Pagtarung oi.")
	else:
		num1 = int(input("Enter 1st number: "))
		num2 = int(input("Enter 2nd number: "))
		if(question == '-'):
			print(subtract(num1, num2))
		elif(question == '*'):
			print(multiply(num1, num2))
		elif(question == '/'):
			print(divide(num1, num2))
		else:
			print(add(num1, num2))
main()