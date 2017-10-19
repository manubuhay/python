def add(a, b):
	return a + b
def subtract(a, b):
	return a - b
def multiply(x, y):
	return x * y
def divide(x, y):
	return x / y

def main():
	question = input("What do you want to do?")
	if(question == '+' or question == "add"):
		num1 = int(input("Enter 1st number: "))
		num2 = int(input("Enter 2nd number: "))
		result = add(num1, num2)
		print(result)
	elif(question == '-' or question == "subtract"):
		num1 = int(input("Enter 1st number: "))
		num2 = int(input("Enter 2nd number: "))
		subtract(num1, num2)
		result = subtract(num1, num2)
		print(result)
	elif(question == '*' or question == "multiply"):
		num1 = int(input("Enter 1st number: "))
		num2 = int(input("Enter 2nd number: "))
		multiply(num1, num2)
		result = multiply(num1, num2)
		print(result)
	elif(question == '/' or question == "divide"):
		num1 = int(input("Enter 1st number: "))
		num2 = int(input("Enter 2nd number: "))
		divide(num1, num2)
		result = divide(num1, num2)
		print(result)
	else:
		print("Please enter a valid operation, you fool.")
main()