from multiprocessing import Process
from models.pedido import Pedido
from controllers.gestorPedido import GestorPedidos
from models.inventario import Inventario

def recibir_pedidos(gestor_pedidos):
    """Proceso para generar pedidos simulados."""
    pedidos = [
        Pedido(1, {"item1": 2, "item2": 1}),
        Pedido(2, {"item3": 5}),
        Pedido(3, {"item1": 1, "item3": 2}),
    ]
    for pedido in pedidos:
        gestor_pedidos.recibir_pedido(pedido)

def preparar_pedidos(gestor_pedidos, inventario):
    """Proceso para preparar pedidos."""
    while not gestor_pedidos.cola_pedidos.empty():
        pedido = gestor_pedidos.procesar_pedido()
        if pedido:
            for item, cantidad in pedido.items.items():
                if not inventario.actualizar_inventario(item, cantidad):
                    pedido.estado = "no procesado"
                    break
            else:
                pedido.estado = "completado"
            print(f"Pedido {pedido.pedido_id}: {pedido.estado}")

if __name__ == "__main__":
    gestor_pedidos = GestorPedidos()
    inventario = Inventario()

    # Crear procesos
    proceso_recepcion = Process(target=recibir_pedidos, args=(gestor_pedidos,))
    proceso_preparacion = Process(target=preparar_pedidos, args=(gestor_pedidos, inventario))

    # Iniciar procesos
    proceso_recepcion.start()
    proceso_recepcion.join()

    proceso_preparacion.start()
    proceso_preparacion.join()

    # Reporte final
    print("Estado final del inventario:", inventario.consultar_inventario())
