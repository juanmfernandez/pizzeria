class TipoPizza:
	"""docstring for TipoPizza"""
	def __init__(self, descripcion, nombre):
		self.descripcion = descripcion
		self.nombre = nombre

	def __str__(self):
		return f"Nombre::\t {self.nombre}\n"  \
		f"Descripcion:\t {self.descripcion}\n" 

muza = TipoPizza("piza con queso de leche","Muzarella")
#print(muza)