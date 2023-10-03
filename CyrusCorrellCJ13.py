def f(x):
	return float(x**3 + 8) #function 'f' with input x

def main():
	a = f(9) #assigns f(9) to a variable
	print("Function equals: "+str(a))
	if a > 27: #Checks if f(9)>27
		print("yay!")

if __name__ == '__main__':
	main()