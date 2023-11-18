import unittest
from src.Postfix import Postfix

class TestPostfix(unittest.TestCase):

	def testEvalSimple(self):
		self.assertEqual(Postfix("1 2 +").value, 3)

	def testMostrarSimple(self):
		self.assertEqual(Postfix("1 2 +").infix, "1 + 2")

	def testEvalComplex(self):
		self.assertEqual(Postfix("8 3 - 8 4 4 + * +").value, 69)

	def testMostrarComplex(self):
		self.assertEqual(Postfix("8 3 - 8 4 4 + * +").infix, "8 - 3 + 8 * (4 + 4)")

	def testEvalComplex2(self):
		self.assertEqual(Postfix("10 2 3 * - 6 2 / +").value, 7)

	def testMostrarComplex2(self):
		self.assertEqual(Postfix("10 2 3 * - 6 2 / +").infix, "10 - 2 * 3 + 6 / 2")

	def testEvalComplex3(self):
		self.assertEqual(Postfix("3 2 + 4 * 10 3 + 2 / 5 - -").value, 19)

	def testMostrarComplex3(self):
		self.assertEqual(Postfix("3 2 + 4 * 10 3 + 2 / 5 - -").infix, "(3 + 2) * 4 - ((10 + 3) / 2 - 5)")

	def testInvalidExpression(self):
		with self.assertRaises(Exception):
			Postfix("1 2 + +")

if __name__ == '__main__':
	unittest.main()
