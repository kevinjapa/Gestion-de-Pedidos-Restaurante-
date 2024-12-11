import multiprocessing

class Inventario(multiprocessing.Process):
    def __init__(self, stock):
        super().__init__()
        self.stock = stock
        self.lock = multiprocessing.Lock()

    

    def actualizar_inventario(self, item, cantidad):
        """Reduce el stock del inventario."""
        with self.lock:
            if self.stock.get(item, 0) >= cantidad:
                self.stock[item] -= cantidad
                return True
            return False

    def consultar_inventario(self):
        """Devuelve el estado actual del inventario."""
        with self.lock:
            return dict(self.stock)
