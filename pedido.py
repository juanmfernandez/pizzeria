import datetime
from detallePedido import DetallePedido
from variedadPizza import  VariedadPizza
from pizza import  Pizza
listadoPizzas = [{'id':'1', 'nombre' : 'Napolitana', 'ingredientes' : 'tomate, queso mozarella, masa, salsa'},{'id':'2', 'nombre' : 'fugazzeta', 'ingredientes' : 'cebolla, queso, masa, salsa'},{'id':'3', 'nombre' : 'Peperoni', 'ingredientes' : 'tomate, queso mozarella, chorizzo, masa, salsa'},{'id':'4', 'nombre' : '4 Quesos', 'ingredientes' : 'mozarella, parmesano, crema, cheddar, masa, salsa'}]

class Pedido(object):
	"""docstring for Pedido"""
	def __init__(self, fechaHoraCreacion, fechaHoraEntrega, nombreCliente, numero, detallePedido=[], total=[]):
		self.fechaHoraCreacion = datetime.datetime.now()
		self.fechaHoraEntrega = fechaHoraEntrega
		self.nombreCliente = nombreCliente
		self.numero = numero
		self.detallePedido = detallePedido
		self.total = total

	def calcTotalPedido(self):
		suma = 0
		for linea in self.detallePedido:
			suma+=linea.calcularSubtotal()
		self.total = suma
		return self.total
	def pedidos_por_periodo(self, fechaInit, fechaFin):
		"""listar pedidos de un periodo determinado"""
		pass

	def agregar_detalle_pedido(self, lista_pizzas=[]):
		"""metodo para agragar una linea del pedido
		1 - crear instancia de Detalle Pedido, preguntando cual es la pizza, que desea(listar las pizas que hay)
		2- llamar al metodo calcular precio de la piza
		2 - agregarlo a self.detalle_pedido
		"""
		print('antes de listadoMenu')
		listadoMenu = VariedadPizza(listadoPizzas)
		print(listadoMenu.imprimirLista())
		variedad = int(input("Elija la variedad según código: "))
		elegida = listadoMenu.getVariedadById(variedad)

		print("Tipo de cocción: [1]piedra->+5% -- [2]molde->+3% -- [3]parrilla->+1%")
		tipo = input("Elija el tipo de cocción: ")
		if(tipo == '1'):
			tipo = 'piedra'
		elif(tipo == '2'):
			tipo = 'molde'
		elif(tipo == '3'):
			tipo = 'parrilla'
		else:
			print('Codigo incorrecto')
		print("Tamaño: [1]8 porciones->+0% -- [2]10 porciones->+10% -- [3]12 porciones->+15%")
		tamanio = input("Elija el tamaño: ")
		if(tamanio == '1'):
			tamanio = 'chica'
		elif(tamanio == '2'):
			tamanio = 'mediana'
		elif(tamanio == '3'):
			tamanio = 'grande'
		else:
			print('Codigo incorrecto')
		miPizza = Pizza("Muza", 250, tipo, elegida, tamanio)
		lista_pizzas.append(miPizza)

		eldetalle= DetallePedido(len(lista_pizzas), lista_pizzas)
		print("Subtotal: ", eldetalle.calcularSubtotal())
		seguir = input('Desea seguir pidiendo pizzas??: ')
		if(seguir=='1'):
			return False
		return True
		#eldetalle = DetallePedido(10, lista_pizzas, calcular)