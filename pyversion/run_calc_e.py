from compute.exact import Compute

#>>> c.count_leading_zeros(1,c.factorial(7000))
#23877

c = Compute()

n=7000


def create_number_file_generator(thefile):
	while 1:
		char = thefile.read(1)
		if not char:
			break
		if char != '\n':
			yield(str(char))

def test_e_partial_sum(n):
	gen = c.e_partial_sum(n)
	efile = open('../data/e-2-million.txt', 'r')
	filegen = create_number_file_generator(efile)
	print("\nCalculating and verifing digits...")
	for i in range(0, 23877):
		if(str(next(filegen)) != next(gen)):
			print("\n")
			print("############# NOT SUCCESSFUL ########################")
			print("      Found Mismatched digit at " + str(i) )
			print("#####################################################")
			break
		if(i%100 == 0):
			print(str(i)+", ",end='')
		if(i%1000 == 0):
			print("\n")
	gen.close()
	efile.close()
	print('\n')
		
test_e_partial_sum(n)

