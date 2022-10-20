from compute.exact import Compute

import unittest
c = Compute()


def create_number_file_generator(thefile):
	while 1:
		char = thefile.read(1)
		if not char:
			break
		if char != '\n':
			yield(str(char))

class TestComputeMethods(unittest.TestCase):

	def test_divide_generator(self):
		gen = c.divide_generator(1,2323)
		actual = "0.0004304778303917348256564786913473956091261300043047783039173482565647869134739560912613000430477830391734825656478691347395609126130004304778303917348256564786913473956091261300043047783039173482565647869134739560912613000430477830391734825656478691347395609126130004304778303917348256564786913473956091261300043047783039173482565647869134739560912613000430477830391734825656478691347395609126130004304778303917348256564786913473956091261300043047783039173482565647869134739560912613000430477830391734825656478691347395609126130004304778303917348256564786913473956091261300043047783039173482565647869134739560912613000430477830391734825656478691347395609126130004304778303917348256564786913473956091261300043047783039173482565647869134739560912613000430477830391734825656478691347395609126130004304778303917348256564786913473956091261300043047783039173482565647869134739560912613000430477830391734825656478691347395609126130004304778303917348256564786913473956091261300043047783039173482565647869134739560912613000430477830391734825656478691347395609126130004304778303917348256564786913473956091261300043047783039173482565647869134739560912613000430477830391734825656478691347395609126130004304778303917348256564786913473956091261300043047783039173482565647869134739560912613000430477830391734825656478691347395609126130004304778303917348256564786913473956091261300043047783039173482565647869134739560912613000430477830391734825656478691347395609126130004304778303917348256564786913473956091261300043047783039173482565647869134739560912613000430477830391734825656478691347395609126130004304778303917348256564786913473956091261300043047783039173482565647869134739560912613000430477830391734825656478691347395609126130004304778303917348256564786913473956091261300043047783039173482565647869134739560912613000430477830391734825656478691347395609126130004304778303917348256564786913473956091261300043047783039173482565647869134739560912613000430477830391734825656478691347395609126130004304778303917348256564786913473956091261300043047783039173482565647869134739560912613000430477830391734825656478691347395609126130004304778303917348256564786913473956091261300043047783039173482565647869134739560912613000430477830391734825656478691347395609126130004304778303917348256564786913473956091261300043047783039173482565647869134739"
		for i in range(0, len(actual)):
			self.assertEqual(str(actual[i]), next(gen))
		gen.close()
		
		gen = c.divide_generator(1,4)
		actual = "0.25\n"
		for i in range(0, len(actual)):
			self.assertEqual(str(actual[i]), next(gen))
		gen.close()
		
		gen = c.divide_generator(1,3)
		actual = "0.3333333333333333"
		for i in range(0, len(actual)):
			self.assertEqual(str(actual[i]), next(gen))
		gen.close()
		
		gen = c.divide_generator(9,3)
		actual = "3\n"
		for i in range(0, len(actual)):
			self.assertEqual(str(actual[i]), next(gen))
		gen.close()
		
		gen = c.divide_generator(10,3)
		actual = "3.3333333333333333"
		for i in range(0, len(actual)):
			self.assertEqual(str(actual[i]), next(gen))
		gen.close()
		
		gen = c.divide_generator(780,288)
		actual = "2.708333333333333333333333333"
		for i in range(0, len(actual)):
			self.assertEqual(str(actual[i]), next(gen))
		gen.close()
		
		gen = c.divide_generator(18099969098565397826764800000,6658606584104736522240000000)
		actual = "2.7182818"
		for i in range(0, len(actual)):
			self.assertEqual(str(actual[i]), next(gen))
		gen.close()

	def test_factorial(self):
		self.assertEqual(c.factorial(0), 1)
		self.assertEqual(c.factorial(1), 1)
		self.assertEqual(c.factorial(2), 2)
		self.assertEqual(c.factorial(3), 6)
		self.assertEqual(c.factorial(4), 24)
		self.assertEqual(c.factorial(5), 120)
		self.assertEqual(c.factorial(9), 362880)

	def test_count_leading_zeros(self):
		self.assertEqual(c.count_leading_zeros(1,1000), 2)
		self.assertEqual(c.count_leading_zeros(1,100), 1)
		self.assertEqual(c.count_leading_zeros(1,c.factorial(1200)), 3175)
		self.assertEqual(c.count_leading_zeros(1,c.factorial(1000)), 2567)
		self.assertEqual(c.count_leading_zeros(18099969098565397826764800000,6658606584104736522240000000), 0)

	def test_reduce_fraction(self):
		self.assertEqual(c.reduce_fraction(2, 6), {"numerator":1, "denominator":3})
		self.assertEqual(c.reduce_fraction(1, 5), {"numerator":1, "denominator":5})
		self.assertEqual(c.reduce_fraction(8, 4), {"numerator":2, "denominator":1})
		self.assertEqual(c.reduce_fraction(14, 49), {"numerator":2, "denominator":7})
		self.assertEqual(c.reduce_fraction(8, 24), {"numerator":1, "denominator":3})
	
	def test_add_rational(self):
		self.assertEqual(c.add_rational((1,3),(1,3)), (6,9))
		self.assertEqual(c.add_rational((2,3),(1,3)), (9,9))
		self.assertEqual(c.add_rational((1,2),(2,4)), (8,8))
	
	def test_determine_if_repeating_fraction(self):
		self.assertEqual(c.determine_if_repeating_fraction(1,3), {"is_repeating": True, "max_nonrepeat": 0, "max_repeat": 2 })
		self.assertEqual(c.determine_if_repeating_fraction(1,4), {"is_repeating": False})
		self.assertEqual(c.determine_if_repeating_fraction(780,288), {"is_repeating": True, "max_nonrepeat": 3, "max_repeat": 23 })
		self.assertEqual(c.determine_if_repeating_fraction(1,2323), {"is_repeating": True, "max_nonrepeat": 0, "max_repeat": 2322 })	
		
	def test_e_partial_sum(self):
		pass
		#gen = c.e_partial_sum(1000)
		#efile = open('../data/e-2-million.txt', 'r')
		#filegen = create_number_file_generator(efile)
		#for i in range(0, 2567):
		#	self.assertEqual(str(next(filegen)), next(gen))
		#gen.close()
		#efile.close()
		
	def test_e_partial_sum_v2(self):
		pass
		#result = c.e_partial_sum_v2(100)
		#r = (result[0]/result[1])+1
		#self.assertEqual(r, 2.7182818284590455)
		
	def test_e_recusive(self):
		result = c.e_recusive(10)
		r = str((result[0]/result[1])+1)
		self.assertEqual(r[0:6], "2.7182")
		

if __name__ == '__main__':
    unittest.main()
