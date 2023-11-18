import unittest
from src.Prefix import Prefix

class TestPrefix(unittest.TestCase):

	def testEvalSimple(self):
		self.assertEqual(Prefix("+ 1 2").value, 3)

	def testMostrarSimple(self):
		self.assertEqual(Prefix("+ 1 2").infix, "1 + 2")

	def testEvalComplex(self):
		self.assertEqual(Prefix("+ * + 3 4 5 7").value, 42)

	def testMostrarComplex(self):
		self.assertEqual(Prefix("+ * + 3 4 5 7").infix, "(3 + 4) * 5 + 7")

	def testEvalComplex2(self):
		self.assertEqual(Prefix("+ - 10 * 2 3 / 6 2").value, 7)

	def testMostrarComplex2(self):
		self.assertEqual(Prefix("+ - 10 * 2 3 / 6 2").infix, "10 - 2 * 3 + 6 / 2")

	def testEvalComplex3(self):
		self.assertEqual(Prefix("- * + 3 2 4 - / + 10 3 2 5").value, 19)

	def testMostrarComplex3(self):
		self.assertEqual(Prefix("- * + 3 2 4 - / + 10 3 2 5").infix, "(3 + 2) * 4 - ((10 + 3) / 2 - 5)")

if __name__ == '__main__':
	unittest.main()