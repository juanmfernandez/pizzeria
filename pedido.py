import datetime
import DetallePedido
class Pedido(object):
	"""docstring for Pedido"""
	def __init__(self, fechaHoraCreacion, fechaHoraEntrega, nombreCliente, numero, detallePedido=[], total=[]):
		self.fechaHoraCreacion = datetime.now()
		self.fechaHoraEntrega = fechaHoraEntrega
		self.nombreCliente = nombreCliente
		self.numero = numero
		self.detallePedido = detallePedido
		self.total = total

	def calcTotalPedido(self):
		suma = 0
		for linea in detallePedido:
			suma+=linea.subtotal
		self.total = suma
	def pedidos_por_periodo(self, fechaInit, fechaFin):
		"""listar pedidos de un periodo determinado"""
		pass

	def agregar_detalle_pedido(self, lista_pizzas):
		#1 crear instancia de DatallePedido preguntar cual es a pizza q desea (listar)
		#2 calcular el precio de la pizza con el metodo calcularPrecio()
		#3 agregarlo a self.detallePedido
		eldetalle = DetallePedido(10, lista_pizzas[0], calcular)
		pass
	def obtenerDetallesPedido():
		pass
	def setEstado():
		pass
	def terminar():
		pass
