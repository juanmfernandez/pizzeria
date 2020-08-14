class VariedadPizza(object):
	"""docstring for VariedadPizza"""
	def __init__(self, ingredientes, nombre):
		self.ingredientes = ingredientes
		self.nombre = nombre

	def __str__(self):
		return f"Nombre:\t {self.nombre}\n"  \
		f"Ingredientes:\t {self.ingredientes}\n" 