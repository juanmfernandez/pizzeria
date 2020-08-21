from pizza import Pizza
from cliente import Cliente
from pedido import Pedido
from datetime import timedelta
import datetime
import time
class Pizeria:
	"""docstring for Pizeria"""
	def __init__(self, pedidos=[], pizzas=[], clientes=[]):
		self.pedidos=pedidos
		self.pizzas=pizzas
		self.clientes=clientes
	def cargarCliente(self):
		cliente = Cliente("Juanchy Ferna","584755411","Siempre Viva 123")
		return cliente

	def cargarPedido(self):
		#micliente = cargarCliente()
		micliente = 'Juanchy'
		#print("timedelta: ",datetime.datetime.now()+timedelta(minutes=15))
		pedido = Pedido(1, micliente, datetime.datetime.now(), datetime.datetime.now()+timedelta(minutes=15))
		while True:
			pedido.agregar_detalle_pedido(self.pizzas)
			print(pedido.calcTotalPedido())
	
	def cargarPizza(self):
		pass


foo = True
while foo == True:
	pizzasLocas = Pizeria()
	pizzasLocas.cargarPedido()
	seguir = input('Desea seguir pidiendo pizzas??: ')
	if(seguir=='1'):
		foo = False
		#pedido = cargarPedido()

from datetime import datetime
import time
dt = datetime.now()
timestamp = time.mktime(dt.timetuple()) + dt.microsecond/1e6