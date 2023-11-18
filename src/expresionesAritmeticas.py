from .Postfix import Postfix
from .Prefix import Prefix


def main():
	print("-------------------------------------------------------------------------------------------------------")
	print("Bienvenido al programa de evaluacion de expresiones aritméticas")
	print("\nIMPORTANTE: Las expresiones deben estar separadas por espacios, ")
	print("solo se aceptan numeros enteros y las operaciones +, -, * y /\n")
	print("Comandos disponibles:")
	print("EVAL <orden> <expresión> - Evalúa la expresión del orden indicado (POST o PRE)")
	print("MOSTRAR <orden> <expresión> - Muestra la expresión del orden indicado (POST o PRE) con notacion infija")
	print("SALIR - Sale del programa")
	print("-------------------------------------------------------------------------------------------------------\n")

	while True:
		entrada = input(">>> ").upper().strip().split(" ")

		match entrada:
			case ["SALIR"]:
				break

			case ["EVAL", "POST", *expr]:
				try:
					expr = ' '.join(expr)
					print(Postfix(expr).value)
				except Exception as e:
					print("Expresión inválida")

			case ["EVAL", "PRE", *expr]:
				try:
					expr = ' '.join(expr)
					print(Prefix(expr).value)
				except Exception as e:
					print("Expresión inválida")

			case ["MOSTRAR", "PRE", *expr]:
				try:
					expr = ' '.join(expr)
					print(Prefix(expr).infix)
				except Exception as e:
					print("Expresión inválida")

			case ["MOSTRAR", "POST", *expr]:
				try:
					expr = ' '.join(expr)
					print(Postfix(expr).infix)
				except Exception as e:
					print("Expresión inválida")

			case ["EVAL", *_]:
				print("Uso del comando EVAL: EVAL <orden> <expresión>")
				print("Ordenes disponibles: POST, PRE")

			case ["MOSTRAR", *_]:
				print("Uso del comando MOSTRAR: MOSTRAR <orden> <expresión>")
				print("Ordenes disponibles: POST, PRE")

			case [""]:
				pass

			case _:
				print("Comando no reconocido")


if __name__ == "__main__":
	main()