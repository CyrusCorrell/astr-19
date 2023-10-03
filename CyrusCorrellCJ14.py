class animal: #defines and creates animal class with arms, legs, eyes, tails, and fur components
	def __init__(self,armlen,leglen,eye,tail,fur):
		self.armlen= armlen
		self.leglen= leglen
		self.eye= eye
		self.tail=tail
		self.fur=fur

def converttobool(inp): #bandaid fix to turn 'true' strings into the boolean True
	if str(inp)=="y" or str(inp)=="yes" or str(inp)=="Y" or str(inp)=="Yes":
		return True
	else: 
		return False

def createanimal(): #creates an animal object off input
	a = float(input("How long are the arms? "))
	b = float(input("How long are the legs? "))
	c = int(input("How many eyes? "))
	d = input("Does it have a tail? ")
	e = input("Does it have fur? ")

	output= animal(a,b,c,converttobool(d),converttobool(e))
	print("\n\n=====Animal stats!======\n\nArm length: "+str(output.armlen)+"\nLeg Length: "+str(output.leglen)+"\nNumber Of Eyes: "+ str(output.eye)+"\nTail: "+str(output.tail)+"\nFurry: "+str(output.fur))


#run it!
def main():
	createanimal()
if __name__ == '__main__':
	main()
