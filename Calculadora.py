def calculadora():
    print("Selecciona la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Introduce el número de la operación (1/2/3/4): ")

    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if opcion == '1':
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif opcion == '2':
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif opcion == '3':
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")
    elif opcion == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Error: No se puede dividir por cero.")
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

calculadora()
