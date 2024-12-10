class Pedido:
    def __init__(self, pedido_id, items):
        self.pedido_id = pedido_id
        self.items = items
        self.estado = "pendiente"  # Puede ser "pendiente", "en preparación", o "completado"
    
    def __repr__(self):
        return f"Pedido({self.pedido_id}, {self.items}, {self.estado})"
