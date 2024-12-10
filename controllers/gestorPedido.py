from multiprocessing import Queue

class GestorPedidos:
    def __init__(self):
        self.cola_pedidos = Queue()

    def recibir_pedido(self, pedido):
        """Agrega un pedido a la cola."""
        self.cola_pedidos.put(pedido)

    def procesar_pedido(self):
        """Extrae un pedido de la cola para procesarlo."""
        if not self.cola_pedidos.empty():
            pedido = self.cola_pedidos.get()
            pedido.estado = "en preparación"
            return pedido
        return None
