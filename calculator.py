def add(a, b):
	return a + b
def subtract(a, b):
	return a - b
def multiply(x, y):
	return x * y
def divide(x, y):
	return x / y

def main():
	question = input("Bisaya ni na calculator, unsa imong ginahan buhaton?")
	if(question == '+' or question == "dugangan"):
		num1 = int(input("Gae kog numero: "))
		num2 = int(input("Gae kog ikaduha na numero: "))
		print(add(num1, num2))
	elif(question == '-' or question == "minusan"):
		num1 = int(input("Gae kog numero: "))
		num2 = int(input("Gae kog ikaduha na numero: "))
		print(subtract(num1, num2))
	elif(question == '*' or question == "padaghanon"):
		num1 = int(input("Gae kog numero: "))
		num2 = int(input("Gae kog ikaduha na numero: "))
		print(multiply(num1, num2))
	elif(question == '/' or question == "tungaon"):
		num1 = int(input("Gae kog numero: "))
		num2 = int(input("Gae kog ikaduha na numero: "))
		print(divide(num1, num2))
	else:
		print("Pagtarung oi.")
main()