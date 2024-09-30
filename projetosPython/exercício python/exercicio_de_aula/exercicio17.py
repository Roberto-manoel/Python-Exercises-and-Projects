class Tempo():
    def __init__(self, clima, temperatura):
        # inicializa os parâmetros clima e temperatura
        self.clima = clima
        self.temperatura = temperatura

    def previsao(self):
        # Verifica se o clima é "sol"
        if self.clima == "sol":
            # Verifica se a temperatura é maior que 30 graus Celsius
            if self.temperatura > 30:
                # Retorna "Vou à praia" se a temperatura for maior que 30 graus Celsius
                return "Vou à praia"
            else:
                # Retorna "Vou ao parque" se a temperatura for menor ou igual a 30 graus Celsius 
                return "Vou ao parque"
        # Verifica se o clima é "chuva"
        elif self.clima == "chuva":
            # Retorna as atividades para um dia de chuva
            return "Vou estudar\nalmoçar\nver televisão\ndormir"
        # Verifica se o clima é "neve"
        elif self.clima == "neve":
            # Retorna as atividades para um dia de neve
            return "Vou esquiar\ntomar chocolate quente"
        else:
            # Retorna uma mensagem padrão se o clima não for nenhum desses três
            return "Não sei o que fazer"

# Cria um objeto da classe Tempo com o clima "sol" e a temperatura 25 graus Celsius
tempo = Tempo("sol", 25)

# Chama o método previsao() do objeto tempo e imprime o resultado
print(tempo.previsao())