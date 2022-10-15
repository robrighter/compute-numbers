from compute.exact import Compute

import unittest
c = Compute()

class TestComputeMethods(unittest.TestCase):

	def test_divide(self):
		self.assertEqual(c.divide(1,2323), { 'repeat': True, 'value': '0.0004304778303917348256564786913473956091261300043047783039173482565647869134739560912613', 'repeat_value': '00043047783039173482565647869134739560912613' })
		self.assertEqual(c.divide(1,4), { 'repeat': False, 'value': '0.25'})
		self.assertEqual(c.divide(1,3), { 'repeat': True, 'value': '0.33', 'repeat_value': '3'})
		self.assertEqual(c.divide(9,3), { 'repeat': False, 'value': '3'})
		self.assertEqual(c.divide(10,3), { 'repeat': True, 'value': '3.33', 'repeat_value': '3'})
		#self.assertEqual(c.divide(780,288), { 'repeat': True, 'value': '3.33', 'repeat_value': '3'})

	def test_factorial(self):
		self.assertEqual(c.factorial(0), 1)
		self.assertEqual(c.factorial(1), 1)
		self.assertEqual(c.factorial(2), 2)
		self.assertEqual(c.factorial(3), 6)
		self.assertEqual(c.factorial(4), 24)
		self.assertEqual(c.factorial(5), 120)
		self.assertEqual(c.factorial(9), 362880)

	def test_factorial(self):
		pass
		#self.assertEqual(c.e(), "2.7182818284590452353602874713526624977572470936999595749669676277")

#2 1 = 5 1
#1 2   2 6
if __name__ == '__main__':
    unittest.main()
	#value = c.divide(780,288)
	#print("Value is: "+ value['value'])
	#if(value['repeat']):
	#	print("Decimal repeats with value: "+value['repeat_value'])
	#print('\n')
