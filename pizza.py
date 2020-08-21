# from tipo import tipo
# from variedadPizza import VariedadPizza
# from tamanioPizza import TamanioPizza
class Pizza:
	"""docstring for Pizza o Pizeria"""
	mediana = 0.1
	grande = 0.15
	piedra = 0.05
	molde = 0.03
	parrilla = 0.01
	def __init__(self, nombre, precio_base, tipo, variedad, tamanio):
		self.nombre = nombre
		self.precio_base = precio_base
		self.tipo = tipo
		self.variedad = variedad
		self.tamanio = tamanio

	def __str__(self):
		return f"Nombre:\t {self.nombre}\n" \
		f"Precio:\t {self.precio_base}\n" \
		f"Tipo:\t {self.tipo}\n" \
		f"Variedad:\t {self.variedad}\n"  \
		f"Tamaño:\t {self.tamanio}\n" 

	def calcularPrecio(self):
		"""metodo para calcular el precio por tipo y tamanio"""
		precio = self.precio_base
		if (self.tipo == "piedra" and self.tamanio == "chica"):
			precio += (precio * 0.05)
		elif(self.tipo == "piedra" and self.tamanio == "mediana"):
			precio += (precio * 0.05) + (precio * 0.1)
		elif(self.tipo == "piedra" and self.tamanio == "grande"):
			precio += (precio * 0.05) + (precio * 0.15)
		elif(self.tipo == "molde" and self.tamanio == "chica"):
			precio += (precio * 0.03)
		elif(self.tipo == "molde" and self.tamanio == "mediana"):
			precio += (precio * 0.03) + (precio * 0.1)
		elif(self.tipo == "molde" and self.tamanio == "grande"):
			precio += (precio * 0.03) + (precio * 0.15)
		elif(self.tipo == "parrilla" and self.tamanio == "chica"):
			precio += (precio * 0.01)
		elif(self.tipo == "parrilla" and self.tamanio == "mediana"):
			precio += (precio * 0.01) + (precio * 0.1)
		elif(self.tipo == "parrilla" and self.tamanio == "grande"):
			precio += (precio * 0.01) + (precio * 0.15)
		return precio
	
#muza = Pizza("Muza", 250, "piedra", "muzarella", "chica")

#print(muza)