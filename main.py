from multiprocessing import Process, Lock, Queue, Manager
from models.pedido import Pedido
from controllers.gestorPedido import GestorPedidos
from models.inventario import Inventario

def recibir_pedidos(gestor_pedidos):
    """Proceso para generar pedidos simulados."""
    pedidos = [
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(4, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(5, {"Pollo": 5}),
        Pedido(6, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(7, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(8, {"Pollo": 5}),
        Pedido(9, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(10, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(11, {"Pollo": 5}),
        Pedido(12, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(13, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(14, {"Pollo": 5}),
        Pedido(15, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(16, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(17, {"Pollo": 5}),
        Pedido(18, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(19, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(20, {"Pollo": 5}),
        Pedido(21, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(22, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(23, {"Pollo": 5}),
        Pedido(24, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(25, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(26, {"Pollo": 5}),
        Pedido(27, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(28, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(29, {"Pollo": 5}),
        Pedido(30, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(31, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(32, {"Pollo": 5}),
        Pedido(33, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(34, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(35, {"Pollo": 5}),
        Pedido(36, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(37, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(38, {"Pollo": 5}),
        Pedido(39, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(40, {"Hamburgesas": 2, "Hot-Dog": 1}),
    ]
    for pedido in pedidos:
        gestor_pedidos.recibir_pedido(pedido)

def preparar_pedido(pedido, inventario):
    """Proceso para preparar un pedido específico."""
    for item, cantidad in pedido.items.items():
        if not inventario.actualizar_inventario(item, cantidad):
            pedido.estado = "no procesado"
            break
    else:
        pedido.estado = "completado"
    print(f"Pedido {pedido.pedido_id}: {pedido.estado}")

if __name__ == "__main__":
    manager = Manager()
    stock_inicial = manager.dict({"Pollo": 20, "Hamburgesas": 20, "Hot-Dog": 20})
    inventario = Inventario(stock_inicial)

    queue = Queue()
    gestor_pedidos = GestorPedidos(queue)

    # Crear proceso para recibir pedidos
    proceso_recepcion = Process(target=recibir_pedidos, args=(gestor_pedidos,))
    proceso_recepcion.start()
    proceso_recepcion.join()

    # Crear un proceso para cada pedido
    lista_procesos = []
    while not gestor_pedidos.queue.empty():  # Reemplazar qsize() con empty()
        pedido = gestor_pedidos.procesar_pedido()
        if pedido:
            proceso_preparacion = Process(target=preparar_pedido, args=(pedido, inventario))
            lista_procesos.append(proceso_preparacion)
            proceso_preparacion.start()

    # Esperar a que todos los procesos terminen
    for proceso in lista_procesos:
        proceso.join()

    # Reporte final
    print("Estado final del inventario:", inventario.consultar_inventario())
