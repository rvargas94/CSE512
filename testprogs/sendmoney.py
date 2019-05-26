#Program to solve the SEND MORE MONEY problem with back tracking

#letterNode will handle each letter created in the program
class letterNode:

	def __init__(self):
		self.number_assigned = 0
		self.used_numbers = []
		
	def get_number(self):
		return self.number_assigned
	
	def assign_num(self, x):
		self.number_assigned = x
		self.used_numbers.append(x)

#recursion?
def traverse_tree(letter, carry)
	#a number should be taken and assigned
	#a second number should be taken and assigned
	#answer should be check if its in the list of numbers
	#if answer is in the list of numbers then assign (only the ones place)
	#move to next column and take carry if needed 
	
	
		
#main program
def main():
	D=E=M=N=O=R=S=Y=letterNode()
	numbers_taken = [0,1,2,3,4,5,6,7,8,9]
	
	#D + E = Y
	for i in numbers_taken:
		D.assign_num(numbers_taken[i])
		numbers_taken.remove(i)
		print(D.get_number())
		print(numbers_taken)

if __name__=="__main__":
	main()
