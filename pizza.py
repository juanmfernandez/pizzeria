from tipoPizza import TipoPizza
from variedadPizza import VariedadPizza
from tamanioPizza import TamanioPizza
class Pizza:
	"""docstring for Pizza o Pizeria"""
	mediana = 0.1
	grande = 0.15
	piedra = 0.05
	molde = 0.03
	parrilla = 0.01
	def __init__(self, nombre, precio, tipoPizza, variedad, tamanio):
		self.nombre = nombre
		self.precio = precio
		self.tipoPizza = tipoPizza
		self.variedad = variedad
		self.tamanio = tamanio

	def __str__(self):
		return f"Nombre:\t {self.nombre}\n" \
		f"Precio:\t {self.precio}\n" \
		f"Tipo:\t {self.tipoPizza}\n" \
		f"Variedad:\t {self.variedad}\n"  \
		f"Tamaño:\t {self.tamanio}\n" 

	def calcularPrecio(self):
		"""metodo para calcular el precio por tipo y tamanio"""
		pass
		
#muza = Pizza("Muza", 250, "piedra", "muzarella", 10)

#print(muza)