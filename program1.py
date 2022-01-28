
def add(n1, n2):
	return n1 + n2


def subtract(n1, n2):
	return n1 - n2


def multiply(n1, n2):
	return n1 * n2


def divide(n1, n2):
	return n1 / n2

print("Please select operation -\n" \
		"1. Add\n" \
		"2. Subtract\n" \
		"3. Multiply\n" \
		"4. Divide\n")



select = int(input("Select operations form 1, 2, 3, 4 :"))

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

if select == 1:
	print(" Answer is = ",add(num_1, num_2))

elif select == 2:
	print(" Answer is = ",subtract(num_1, num_2))

elif select == 3:
	print(" Answer is = ", multiply(num_1, num_2))

elif select == 4:
	print(" Answer is = ",divide(num_1, num_2))
else:
	print("Invalid input")
