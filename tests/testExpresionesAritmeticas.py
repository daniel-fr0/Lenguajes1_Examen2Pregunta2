import io
import unittest
from unittest.mock import patch
from src.expresionesAritmeticas import main

class TestExpresionesAritmeticas(unittest.TestCase):

	def testExit(self):
		with patch('builtins.input', side_effect=['SALIR']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[1], 'Bienvenido al programa de expresiones aritméticas prefijas y postfijas')

	def testEvalPre(self):
		with patch('builtins.input', side_effect=['EVAL PRE + * + 3 4 5 7', 'salir']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[-1], '42')

	def testEvalPost(self):
		with patch('builtins.input', side_effect=['EVAL POST 8 3 - 8 4 4 + * +', 'salir']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[-1], '69')

	def testMostrarPre(self):
		with patch('builtins.input', side_effect=['MOSTRAR PRE + * + 3 4 5 7', 'salir']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[-1], '(3 + 4) * 5 + 7')

	def testMostrarPost(self):
		with patch('builtins.input', side_effect=['MOSTRAR POST 8 3 - 8 4 4 + * +', 'salir']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[-1], '8 - 3 + 8 * (4 + 4)')

	def testInvalidExpression(self):
		with patch('builtins.input', side_effect=['EVAL PRE + * + 3 4 5 7 8', 'salir']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[-1], 'Expresión inválida')

	def testInvalidExpression2(self):
		with patch('builtins.input', side_effect=['EVAL PRE + * +34578', 'salir']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[-1], 'Expresión inválida')

	def testUnrecognizedCommand(self):
		with patch('builtins.input', side_effect=['evaluar 1 + 1', 'salir']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[-1], 'Comando no reconocido')

	def testInvalidEval(self):
		with patch('builtins.input', side_effect=['eval 1 + 1', 'salir']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[-2], 'Uso del comando EVAL: EVAL <orden> <expresión>')
				self.assertEqual(output[-1], 'Ordenes disponibles: POST, PRE')

	def testInvalidMostrar(self):
		with patch('builtins.input', side_effect=['mostrar 1 + 1', 'salir']):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				self.assertEqual(output[-2], 'Uso del comando MOSTRAR: MOSTRAR <orden> <expresión>')
				self.assertEqual(output[-1], 'Ordenes disponibles: POST, PRE')

	def testMultipleCommands(self):
		commands = [
			'EVAL PRE + * + 3 4 5 7',
			'EVAL POST 8 3 - 8 4 4 + * +',
			'MOSTRAR PRE + * + 3 4 5 7',
			'MOSTRAR POST 8 3 - 8 4 4 + * +',
			'SALIR'
		]
		results = [
			'42',
			'69',
			'(3 + 4) * 5 + 7',
			'8 - 3 + 8 * (4 + 4)'
		]
		with patch('builtins.input', side_effect=commands):
			with patch('sys.stdout', new_callable=io.StringIO) as fakeStdout:
				main()
				output = fakeStdout.getvalue().strip().split('\n')
				for i in range(len(results)):
					self.assertEqual(output[i-len(results)], results[i])

if __name__ == '__main__':
	unittest.main()