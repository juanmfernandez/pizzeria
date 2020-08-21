listadoPizzas = [{'id':'1', 'nombre' : 'Napolitana', 'ingredientes' : 'tomate, queso mozarella, masa, salsa'},{'id':'2', 'nombre' : 'fugazzeta', 'ingredientes' : 'cebolla, queso, masa, salsa'},{'id':'3', 'nombre' : 'Peperoni', 'ingredientes' : 'tomate, queso mozarella, chorizzo, masa, salsa'},{'id':'4', 'nombre' : '4 Quesos', 'ingredientes' : 'mozarella, parmesano, crema, cheddar, masa, salsa'}]
class VariedadPizza:
	"""docstring for VariedadPizza"""
	def __init__(self, listadoPizzas=[]):
		self.listadoPizzas = listadoPizzas

	def __str__(self):
		for item in range(0,len(self.listadoPizzas)):
			return str(self.listadoPizzas[item])

	def getVariedadById(self, id):
		encontrado = False
		try:
			for item in range(0,len(self.listadoPizzas)):	
				if (self.listadoPizzas[item]['id']==str(id)):
					print(f"Codigo:\t {self.listadoPizzas[item]['id']}\n"\
						f"Nombre:\t {self.listadoPizzas[item]['nombre']}\n"\
						f"Ingredientes:\t {self.listadoPizzas[item]['ingredientes']}\n")
					encontrado = True
			if(encontrado==False):
				raise ValueError(" Codigo no encontrado => ", [id])
		except ValueError as e:
			print("Error:", e)

	def imprimirLista(self):
		for item in range(0,len(self.listadoPizzas)):
			print(f"Codigo:\t {self.listadoPizzas[item]['id']}\n"\
			f"Nombre:\t {self.listadoPizzas[item]['nombre']}\n"\
			 f"Ingredientes:\t {self.listadoPizzas[item]['ingredientes']}\n")


#nuevolistado = VariedadPizza(listadoPizzas)
#nuevolistado.imprimirLista()
#nuevolistado.getVariedadById('3')