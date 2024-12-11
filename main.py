# from multiprocessing import Process, Lock, Queue, Manager
# from models.pedido import Pedido
# from controllers.gestorPedido import GestorPedidos
# from models.inventario import Inventario

# def recibir_pedidos(queue):
#     """Proceso para generar pedidos simulados."""
#     pedidos = [
#         Pedido(1, {"item1": 2, "item2": 1}),
#         Pedido(2, {"item3": 25}),
#         Pedido(3, {"item1": 1, "item3": 2}),
#     ]
#     for pedido in pedidos:
#         queue.put(pedido)


# def preparar_pedido(pedido, inventario):
#     """Proceso para preparar un pedido específico."""
#     for item, cantidad in pedido.items.items():
#         if not inventario.actualizar_inventario(item, cantidad):
#             pedido.estado = "no procesado"
#             break
#     else:
#         pedido.estado = "completado"
#     print(f"Pedido {pedido.pedido_id}: {pedido.estado}")

# def recibir_pedidos(queue):
#     """Proceso para generar pedidos simulados."""
#     pedidos = [
#         Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
#         Pedido(2, {"Pollo": 5}),
#         Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
#     ]
#     for pedido in pedidos:
#         queue.put(pedido)

# def preparar_pedido(pedido, inventario):
#     """Proceso para preparar un pedido específico."""
#     for item, cantidad in pedido.items.items():
#         if not inventario.actualizar_inventario(item, cantidad):
#             pedido.estado = "no procesado"
#             break
#     else:
#         pedido.estado = "completado"
#     print(f"Pedido {pedido.pedido_id}: {pedido.estado}")

# if __name__ == "__main__":
#     manager = Manager()
#     stock_inicial = manager.dict({"Pollo": 10, "Hamburgesas": 10, "Hot-Dog": 10})
#     inventario = Inventario(stock_inicial)

#     queue = Queue()

#     # Crear proceso para recibir pedidos
#     proceso_recepcion = Process(target=recibir_pedidos, args=(queue,))
#     proceso_recepcion.start()
#     proceso_recepcion.join()

#     # Crear un proceso para cada pedido
#     lista_procesos = []
#     while not queue.empty():
#         pedido = queue.get()
#         proceso_preparacion = Process(target=preparar_pedido, args=(pedido, inventario))
#         lista_procesos.append(proceso_preparacion)
#         proceso_preparacion.start()

#     # Esperar a que todos los procesos terminen
#     for proceso in lista_procesos:
#         proceso.join()

#     # Reporte final
#     print("Estado final del inventario:", inventario.consultar_inventario())




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
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        
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
    stock_inicial = manager.dict({"Pollo": 10, "Hamburgesas": 10, "Hot-Dog": 10})
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
