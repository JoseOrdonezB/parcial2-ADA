def combinacionNokia(n):

    vecinos = {
        0: [0, 8],
        1: [1, 2, 4],
        2: [2, 1, 3, 5],
        3: [3, 2, 6],
        4: [4, 1, 5, 7],
        5: [5, 2, 4, 6, 8],
        6: [6, 3, 5, 9],
        7: [7, 4, 8],
        8: [8, 5, 7, 9, 0],
        9: [9, 6, 8]
    }

    dp = [1] * 10

    for longitud in range(2, n + 1):
        nuevo = [0] * 10

        for digito in range(10):
            for vecino in vecinos[digito]:
                nuevo[digito] += dp[vecino]

        dp = nuevo

    total = sum(dp)

    return total


# Ejemplos
print("n = 2:", combinacionNokia(2))
print("n = 4:", combinacionNokia(4))
print("n = 6:", combinacionNokia(6))