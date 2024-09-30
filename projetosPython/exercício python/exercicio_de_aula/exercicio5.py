n = int(input('Digite um número natural: '))

def fizzbuzz(n):
    if n % 5 == 0 and n % 7 == 0:
        return 'fizzbuzz'  # Retorna 'fizzbuzz' se o número for divisível por 5 e por 7
    elif n % 5 == 0:
        return 'fizz'  # Retorna 'fizz' se o número for divisível apenas por 5
    elif n % 7 == 0:
        return 'buzz'  # Retorna 'buzz' se o número for divisível apenas por 7
    else:
        return 'miss'  # Retorna 'miss' se o número não for divisível por 5 nem por 7

# Importa o módulo unittest para realizar os testes
import unittest
from multiplos import fizzbuzz

# Define a classe de teste
class TestFizzBuzz(unittest.TestCase):
    def test_multiplo_5_e_7(self):
        resultado = fizzbuzz(35)
        self.assertEqual(resultado, "fizzbuzz")  # Verifica se o resultado é 'fizzbuzz'

    def test_multiplo_5(self):
        resultado = fizzbuzz(10)
        self.assertEqual(resultado, "fizz")  # Verifica se o resultado é 'fizz'

    def test_multiplo_7(self):
        resultado = fizzbuzz(14)
        self.assertEqual(resultado, "buzz")  # Verifica se o resultado é 'buzz'

    def test_nao_multiplo_5_e_7(self):
        resultado = fizzbuzz(8)
        self.assertEqual(resultado, "miss")  # Verifica se o resultado é 'miss'

if __name__ == '__main__':
    unittest.main()  # Executa os testes