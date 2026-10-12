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

    try:
        option = int(input("Option: "))
    except ValueError:
        print("Debes ingresar un número.")
        return

    coffees = {
        1: {
            "name": "Expresso",
            "price": 5.50
        },
        2: {
            "name": "Cappuccino",
            "price": 7.00
        },
        3: {
            "name": "Latte",
            "price": 6.50
        },
        4: {
            "name": "Americano",
            "price": 5.00
        }
    }

    selected_coffee = coffees.get(option)

    if selected_coffee is None:
        print("La opción no es válida; intenta de nuevo.")
        return

    print(
        f"Has elegido {selected_coffee['name']} "
        f"con valor S/ {selected_coffee['price']:.2f}. "
        f"Preparando tu café."
    )

    with open(ORDER_FILES, "a", encoding="utf-8") as file:
        file.write(selected_coffee["name"].upper() + "\n")