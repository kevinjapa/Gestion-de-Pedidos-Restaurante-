import multiprocessing

class GestorPedidos(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def recibir_pedido(self, pedido):
        """Agrega un pedido a la cola."""
        # self.cola_pedidos.put(pedido)
        self.queue.put(pedido)

    def procesar_pedido(self):
        """Extrae un pedido de la cola para procesarlo."""
        if not self.queue.empty():
            pedido = self.queue.get()
            pedido.estado = "en preparación"
            return pedido
        return None
