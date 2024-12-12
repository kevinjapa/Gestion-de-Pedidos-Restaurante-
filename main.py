from multiprocessing import Process, Lock, Queue, Manager
from models.pedido import Pedido
from controllers.gestorPedido import GestorPedidos
from models.inventario import Inventario
import time

def recibir_pedidos(gestor_pedidos):
    """Proceso para generar pedidos simulados."""
    pedidos = [
        Pedido(1, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(2, {"Pollo": 5}),
        Pedido(3, {"Hamburgesas": 1, "Pollo": 2}),
        Pedido(4, {"Hamburgesas": 2, "Hot-Dog": 1}),
        Pedido(5, {"Pollo": 5}),
        # Pedido(6, {"Hamburgesas": 1, "Pollo": 2}),
        # Pedido(7, {"Hamburgesas": 2, "Hot-Dog": 4}),
        # Pedido(8, {"Pollo": 5}),
        # Pedido(9, {"Hamburgesas": 1, "Pollo": 2}),
        # Pedido(10, {"Hamburgesas": 2, "Hot-Dog": 1}),
        # Pedido(11, {"Pollo": 5}),
        # Pedido(12, {"Hamburgesas": 1, "Pollo": 2}),
        # Pedido(13, {"Hamburgesas": 2, "Hot-Dog": 7}),
        # Pedido(14, {"Pollo": 5}),
        # Pedido(15, {"Hamburgesas": 1, "Pollo": 2}),
        # Pedido(16, {"Hamburgesas": 2, "Hot-Dog": 2}),
        # Pedido(17, {"Pollo": 5}),
        # Pedido(18, {"Hamburgesas": 1, "Pollo": 2}),
        # Pedido(19, {"Hamburgesas": 2, "Hot-Dog": 3}),
        # Pedido(20, {"Pollo": 5}),
        # Pedido(21, {"Hamburgesas": 1, "Pollo": 2}),
        # Pedido(22, {"Hamburgesas": 2, "Hot-Dog": 1}),
        # Pedido(23, {"Pollo": 5}),
        # Pedido(24, {"Hamburgesas": 1, "Pollo": 2}),
        # Pedido(25, {"Hamburgesas": 2, "Hot-Dog": 2}),
        # Pedido(26, {"Pollo": 5}),
        # Pedido(27, {"Hamburgesas": 1, "Pollo": 2}),
        # Pedido(28, {"Hamburgesas": 2, "Hot-Dog": 1}),
        # Pedido(29, {"Pollo": 5}),
        # Pedido(30, {"Hamburgesas": 1, "Pollo": 2}),
        # Pedido(31, {"Hamburgesas": 2, "Hot-Dog": 5}),
        # Pedido(32, {"Pollo": 5}),
        # Pedido(33, {"Hamburgesas": 1, "Pollo": 2}),
        # Pedido(34, {"Hamburgesas": 2, "Hot-Dog": 3}),
        # Pedido(35, {"Pollo": 5}),
        # Pedido(36, {"Hamburgesas": 1, "Pollo": 2}),
        # Pedido(37, {"Hamburgesas": 2, "Hot-Dog": 3}),
        # Pedido(38, {"Pollo": 5}),
        # Pedido(39, {"Hamburgesas": 1, "Pollo": 2}),
        # Pedido(40, {"Hamburgesas": 2, "Hot-Dog": 1}),
    ]
    for pedido in pedidos:
        gestor_pedidos.recibir_pedido(pedido)

def preparar_pedido(pedido, inventario, pedidos_no_procesados, pedidos_completados):
    """Proceso de Preparacion."""
    print(f"\nPreparando pedido {pedido.pedido_id, pedido.estado }...")
    print(f"Verificando stock para el pedido {pedido.pedido_id}:\n{pedido.items}")
    print("stock disponible:")
    print(inventario.consultar_inventario())

    tiempo_estimado = 1 
    time.sleep(tiempo_estimado)

    for item, cantidad in pedido.items.items():
        if not inventario.actualizar_inventario(item, cantidad):
            pedido.estado = "no procesado"
            pedidos_no_procesados.append(pedido)
            print(f"No hay stock para completar el pedido: {pedido.pedido_id}")
            print(f"Estado pedido {pedido.pedido_id, pedido.estado}")
            return

    pedido.estado = "completado"
    pedidos_completados.append(pedido)
    print(f"Estado pedido {pedido.pedido_id, pedido.estado}")
    print("Inventario actual:")
    print(inventario.consultar_inventario())

if __name__ == "__main__":
    manager = Manager()
    stock_inicial = manager.dict({"Pollo": 10, "Hamburgesas": 15, "Hot-Dog": 20})
    inventario = Inventario(stock_inicial)
    
    queue = manager.Queue()
    gestor_pedidos = GestorPedidos(queue)
    
    pedidos_no_procesados = manager.list()  
    pedidos_completados = manager.list()

    proceso_recepcion = Process(target=recibir_pedidos, args=(gestor_pedidos,))
    # proceso_recepcion.daemon = True
    proceso_recepcion.start()
    proceso_recepcion.join()

    lista_procesos = []
    while not queue.empty():
        pedido = gestor_pedidos.procesar_pedido()
        if pedido:
            proceso_preparacion = Process(target=preparar_pedido, args=(pedido, inventario, pedidos_no_procesados,pedidos_completados))
            lista_procesos.append(proceso_preparacion)

    # Iniciar y unir procesos de preparación
    for proceso in lista_procesos:
        proceso.start()

    for proceso in lista_procesos:
        proceso.join()

    
    print("------------------------------------ Reporte Final ------------------------------------")
    print("          Pedidos completados: ")
    pnc = 0
    pc=0
    for pedido in pedidos_completados:
        print(f"Pedido {pedido.pedido_id}: {pedido.estado}")
        pc+=1
    print("          Pedidos no procesados: ")
    for pedido in pedidos_no_procesados:
        print(f"Pedido {pedido.pedido_id}: {pedido.estado}")
        pnc+=1
    print("Estado final del inventario:", inventario.consultar_inventario())
    print("Pedidos completados:", pc)
    print("Pedidos no procesados:", pnc)