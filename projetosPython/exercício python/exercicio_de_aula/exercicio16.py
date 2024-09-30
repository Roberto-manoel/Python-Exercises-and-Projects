import time

class Chiclete():
    def __init__(self):
        pass

    def pegar(self):
        print("Pegando o chiclete")
        time.sleep(1)

    def tirar_plastico(self):
        print("Tirando o plástico do chiclete")
        time.sleep(1)

    def mastigar(self):
        print("Mastigando o chiclete")
        time.sleep(2)

    def jogar_fora(self):
        print("Jogando o chiclete fora")

# Cria uma instância da classe Chiclete
chiclete = Chiclete()

# Executa as ações do chiclete em sequência
chiclete.pegar()
chiclete.tirar_plastico()
chiclete.mastigar()
chiclete.jogar_fora()