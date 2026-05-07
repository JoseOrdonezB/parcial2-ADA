def hacerCambio(m):
    monedas = [25, 10, 5, 1]
    cantidad = 0
    usadas = []

    for moneda in monedas:
        while m >= moneda:
            m -= moneda
            cantidad += 1
            usadas.append(moneda)

    return cantidad, usadas

# Ejemplos
print("=== Ejemplo ===")
opcion = int(input("ingresa una opción: "))
if opcion == 1:
    monto = 37
elif opcion == 2:
    monto = 89
elif opcion == 3:
    monto = 130

cantidad, monedas_usadas = hacerCambio(monto)

print("Monto: ",monto)
print("Monedas: ",monedas_usadas)
print("Cantidad minima: ",cantidad)