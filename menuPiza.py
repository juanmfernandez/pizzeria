from pizza import Pizza
import Cliente, Pedido
import datetime
class Pizeria:
	"""docstring for Pizeria"""
	def __init__(self, arg):
		self.arg = arg

	def cargarPedido(self):
		micliente = cargarCliente()
		pedido = Pedido(1, micliente, datetime.now(), datetime.now()+timedelta(minutes=15))
		while True:
			mipedido.agregar_detalle_pedido(self.pizzas)
		mipedido.calcularTotal()
	
	def cargarPizza(self):
		pass
	def cargarCliente(self):
		cliente = Cliente("Juanchy Ferna","584755411","Siempre Viva 123")
		return cliente

	while True:
		pedido = cargarPedido()