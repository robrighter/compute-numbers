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

if __name__ == '__main__':
    unittest.main()



#value = c.divide(1,2323)
#print("Value is: "+ value['value'])
#if(value['repeat']):
#	print("Decimal repeats with value: "+value['repeat_value'])
	 
#print('\n')
