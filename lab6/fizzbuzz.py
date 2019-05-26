#Write a program that prints numbers from 1-100 with the following exceptions:
#For each multiple of 3 print "fizz"
#For each multiple of 5 print "buzz"
#For each multiple of 3 & 5 print "fizz and buzz"

def main():
	nums = range(1,101)
	for i in nums:
		print nums[i]
		#could also use if nums[i] % 3 is 0 and nums[i] % 5 is 0
		if nums[i] % 15 is 0:
			print "fizzbuzz"
		elif nums[i] % 3 is 0:
			print "fizz"
		elif nums[i] % 5 is 0:
			print "buzz"

if __name__=='__main__':
	main()