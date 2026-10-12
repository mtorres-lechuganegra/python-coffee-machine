from menu import menu_view
from orders import order_coffee
from history import history_view

def  main():
    while True:
        # Mostrar el menú
        menu_view()
        option = input("Selecciona una opción: ") # Siempre devuelve string

        if option == "1":
            # pedir un café
            order_coffee()
        elif option == "2":
            # ver el historial
            history_view()
        elif option == "3":
            print("\n Muchas gracias por haber tomado nuestro café.")
            break
        else:
            print("Opción inválida; por favor, indique una de las opciones sugeridas")

# Punto d einicio
if __name__ == "__main__":
    main()