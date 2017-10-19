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
	question = input("Bisaya ni na calculator, unsa imong ginahan buhaton (+,-,*,/) ?")
	if(question != '+' and question != '-' and question != '*' and question != '/'):
		print("Pagtarung oi.")
	else:
		num1 = int(input("Gae kog numero: "))
		num2 = int(input("Gae kog ikaduha na numero: "))
		if(question == '-' or question == "minusan"):
			print(subtract(num1, num2))
		elif(question == '*' or question == "padaghanon"):
			print(multiply(num1, num2))
		elif(question == '/' or question == "tungaon"):
			print(divide(num1, num2))
		else:
			print(add(num1, num2))
main()