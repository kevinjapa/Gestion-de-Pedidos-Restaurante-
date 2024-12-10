from multiprocessing import Lock

class Inventario:
    def __init__(self):
        self.stock = {"item1": 10, "item2": 5, "item3": 20}
        self.lock = Lock()

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
