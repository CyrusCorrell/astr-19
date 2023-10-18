import numpy as np 
import sys

def sinslicer(n): #returns an array between 0 and 2pi with passed slices
	pi=np.pi
	slices = np.sin(np.linspace(0,2*pi,n))
	return slices

def makeatable(data): #prints a table from passed data
	x = np.linspace(0,2*np.pi,1000)
	print("Data:\nX:\t  Sin(x):")

	for y in range(1000):
		print(f'{x[y]:.4f} || {data[y]:.4f}')

def main():
	sindata=sinslicer(1000) #make an array with sin(x) from 0 -> 2pi with 1000 values
	makeatable(sindata)

if __name__ == '__main__':
	main() 
