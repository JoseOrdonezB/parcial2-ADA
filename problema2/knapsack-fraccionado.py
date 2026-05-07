def knapsackFraccionado(W, articulos):
    articulos.sort(
        key=lambda x: x[1] / x[2],
        reverse=True
    )

    valorTotal = 0
    usados = []

    for articulo in articulos:
        nombre = articulo[0]
        valor = articulo[1]
        peso = articulo[2]

        if peso <= W:
            W -= peso
            valorTotal += valor
            usados.append((nombre, 1))

        else:
            fraccion = W / peso
            valorTotal += valor * fraccion
            usados.append((nombre, fraccion))
            W = 0

        if W == 0:
            break

    return valorTotal, usados

# Ejemplos
print("=== Ejemplo ===")
opcion = int(input("Ingresa una opción: "))

if opcion == 1:
    articulos = [
        ("Laptop", 500, 10),
        ("Tablet", 300, 6),
        ("Camara", 200, 4)
    ]
    capacidad = 12

elif opcion == 2:
    articulos = [
        ("Oro", 1000, 20),
        ("Plata", 500, 10),
        ("Bronce", 300, 15)
    ]
    capacidad = 25

elif opcion == 3:
    articulos = [
        ("Reloj", 400, 5),
        ("Telefono", 600, 8),
        ("Audifonos", 150, 3)
    ]
    capacidad = 14

valor, usados = knapsackFraccionado(capacidad, articulos)

print("Capacidad:", capacidad)
print("Articulos tomados:", usados)
print("Valor máximo:", valor)