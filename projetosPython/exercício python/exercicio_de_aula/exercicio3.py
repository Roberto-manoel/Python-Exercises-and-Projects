class Fibonacci:
    def __init__(self, iteracao):
        self.iteracao = iteracao
        self.anterior = 0
        self.proximo = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteracao == 0:
            raise StopIteration

        resultado = self.anterior + self.proximo
        self.anterior = self.proximo
        self.proximo = resultado
        self.iteracao -= 1
        return self.proximo

# Cria uma instância da classe Fibonacci com 10 iterações
fibonacci = Fibonacci(10)

# Cria um dicionário onde as chaves são as posições e os valores são os números da sequência de Fibonacci
resultado = {posicao: valor for posicao, valor in enumerate(fibonacci)}
print(resultado)

import unittest

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        # Cria uma instância da classe Fibonacci com 10 iterações
        fib = Fibonacci(10)

        # Sequência de Fibonacci esperada
        fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

        # Compara cada número gerado pela instância de Fibonacci com a sequência esperada
        for i in range(10):
            self.assertEqual(next(fib), fibonacci_sequence[i])

if __name__ == '__main__':
    # Executa os testes definidos na classe TestFibonacci
    unittest.main()