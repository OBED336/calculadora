from calculator import sumar, restar, multiplicar, dividir


def main():
    operaciones = {
        "1": sumar,
        "2": restar,
        "3": multiplicar,
        "4": dividir
    }

    while True:
        print("\n=== CALCULADORA ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "5":
            print("¡Hasta luego!")
            break

        if opcion not in operaciones:
            print("Opción inválida.")
            continue

        try:
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
        except ValueError:
            print("Debes ingresar números válidos.")
            continue

        try:
            resultado = operaciones[opcion](a, b)
            print(f"Resultado: {resultado}")
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()
