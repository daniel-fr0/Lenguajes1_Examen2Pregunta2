class Prefix():
	def __init__(self, expr):
		self.expr = expr
		self._evaluate()

	def _evaluate(self):
		stack = []
		for i in reversed(self.expr.split(" ")):
			if i.isdigit():
				stack.append(i)
			else:
				a = stack.pop()
				b = stack.pop()

				# Si son mas de dos terminos que se van a multiplicar o dividir, se ponen entre parentesis
				if i in "*/" and (len(a.split("+")) > 1 or len(a.split("-")) > 1):
					a = f"({a})"

				# Tambien si se restan dos o mas terminos, se ponen entre parentesis
				if i in "*/-" and (len(b.split("-")) > 1 or len(b.split("+")) > 1):
					b = f"({b})"

				stack.append(f"{a} {i} {b}")

		self.infix = stack.pop()
		self.value = eval(self.infix.replace("/", "//"))

		if len(stack) > 0:
			raise Exception("Expresión inválida")

	def __str__(self):
		return f"(pre): {self.expr}"

	def __repr__(self):
		return self.__str__()