from compute.exact import Compute

#>>> c.count_leading_zeros(1,c.factorial(7000))
#23877

c = Compute()

n=1000000


#calcuate the digit goal from n
digit_goal= c.count_leading_zeros(1,c.factorial(n))-100
print("Calculating e to "+str(digit_goal)+" decimal places.")



def create_number_file_generator(thefile):
	while 1:
		char = thefile.read(1)
		if not char:
			break
		if char != '\n':
			yield(str(char))

def print_success_or_fail(was_successful, digit):
	print("\n")
	print("########################################################")
	if(was_successful):
		print("      SUCCESS! Computed e to digit " + str(digit) )
	else:
		print("      FAILURE! Found Mismatched digit at " + str(digit) )
	print("########################################################")
	print("\n")

def test_e_partial_sum(n, digit):
	gen = c.e_partial_sum_v2(n)
	efile = open('../data/e-2-million.txt', 'r')
	filegen = create_number_file_generator(efile)
	print("\nCalculating and verifing digits...")
	success = True
	for i in range(0, digit):
		if(str(next(filegen)) != next(gen)):
			success = False
			print_success_or_fail(False, i)
			break
		if(i%100 == 0):
			print(str(i)+", ",end='')
		if(i%1000 == 0):
			print("\n")
	gen.close()
	efile.close()
	if( success ):
		print_success_or_fail(True, digit)
		
test_e_partial_sum(n, digit_goal)

