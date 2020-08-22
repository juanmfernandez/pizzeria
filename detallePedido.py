class DetallePedido(object):
	"""docstring for DetallePedido"""
	def __init__(self, cant, pizza, subtotal=0):
		self.cant = cant
		self.pizza = pizza
		self.subtotal = subtotal

	def calcularSubtotal(self):
		"""metodo para calcular subtotal en base a la cantidad y el prcio de la pizza
		1 - preguntar tipo y tamño desea
		2 - return del precio
		test de ramas dev en git
		testteo de ramas en dev para Git
		"""
		for p in self.pizza:
			self.subtotal += p.calcularPrecio()
		return self.subtotal


	def agregar(self):
		pass
		