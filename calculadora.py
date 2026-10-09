def calculadora():
    while True:
        print("\n=== CALCULADORA BÁSICA ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "5":
            print("¡Hasta luego!")
            break

        if opcion not in ("1", "2", "3", "4"):
            print("Opción inválida. Selecciona del 1 al 5.")
            continue

        try:
            numero1 = float(input("Primer número: "))
            numero2 = float(input("Segundo número: "))
        except ValueError:
            print("Debes ingresar números válidos.")
            continue

        if opcion == "1":
            resultado = numero1 + numero2
        elif opcion == "2":
            resultado = numero1 - numero2
        elif opcion == "3":
            resultado = numero1 * numero2
        else:
            if numero2 == 0:
                print("No se puede dividir entre cero.")
                continue
            resultado = numero1 / numero2

        print(f"Resultado: {resultado}")


if __name__ == "__main__":
    calculadora()
