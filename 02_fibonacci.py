


def fib(n):
    ant = 1
    inic = 2

    prox = inic + ant
    if 0 <= n <= 2 or prox == n:
        print('Ok, é uma sequência de Fibonacci.')

    else:
        while prox < n:
            ant = inic
            inic = prox
            prox = inic + ant

        if prox == n:
            print('Ok, é uma sequência de Fibonacci.')
        else:
            print('Não existe na sequência de Fibonacci.')




fib(89)

