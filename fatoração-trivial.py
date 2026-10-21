def algoritmo():

    n = int(input()) # recebe o número que quer fatorar.

    f = 2 # f representa os fatores primos que vão tentar dividir o número.
    fatores = {} # representação dos fatores na forma {primo,potência}

    while n > 1:
        if n % f == 0:
            fatores[f] = fatores.get(f, 0) + 1
            n = n // f
        else:
            f += 1

    """
    Enquanto n > 1, se o fator primo que estamos analisando dividir n,
    adiciona um na sua potência e n = n/f.
    Se o fator primo não dividir mais n, então f++.
    """

    for primo, potencia in fatores.items():
        print(f"{primo}^{potencia} x ", end="")

    print(1)


algoritmo()
