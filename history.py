from config import ORDER_FILES

def history_view():
    try:
        print("\n Historial de pedidos")
        with open(ORDER_FILES, "r", encoding="utf-8") as file:
            orders = file.readlines()
            if orders:
                # enumerate: nos dá el índice de línea y contenido
                ## start: indica en donde arranca la lectura (línea)
                for i, order in enumerate(orders, start=1):
                    print(str(i) + f". {order.strip()}")
            else:
                print("Aún no hay ningún pedido.")
    except FileNotFoundError:
        print("\n Todavía no existe un historial de pedidos.")