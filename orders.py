from config import ORDER_FILES

'''
Solicitar café:
- Brinda la selección de café
- Escribe en el archivo de pedidos, el café elegido
'''
def order_coffee():
    print("\n Elige el café que prefieras: ")
    print("1: Expresso")
    print("2: Cappuccino")
    print("3: Latte")
    print("4: Americano")

    option = input("Option: ")

    coffees = {
        "1": "Expresso",
        "2": "Cappuccino",
        "3": "Latte",
        "4": "Americano"
    }

    if option in coffees:
        selected_coffee = coffees[option]
        print(f"Has elegido {selected_coffee}. Preparando tu café.")
        with open(ORDER_FILES, "a", encoding="utf-8") as file:
            file.write(selected_coffee.upper() + "\n")
    else:
        print("La opción no es válida; por favor, intenta de nuevo")