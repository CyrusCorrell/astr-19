def sumation(): #sumation of two float inputs
	x = input("X: ")
	y = input("Y: ")

	z = str(float(x)+float(y)) 
	print("Sum is: "+z)

def diff(): #difference of two int inputs
	x = input("X: ")
	y = input("Y: ")

	z = str(int(y)-int(x)) 
	print("Difference is: "+z)

def product(): #product of float and int inputs
	x = input("X: ")
	y = input("Y: ")

	z = str(float(x)*int(y)) #Turns str x into float into str again
	print("Product is: "+z)

def main():
	sumation()
	diff()
	product()
	print("\nHave a lovely day!")

if __name__ == '__main__':
	main()