class TrocarLampada():
    def __init__(self):
        self.escada = False
        self.lampada = False

    def subir_escada(self):
        # Método para subir na escada
        print("Subindo na escada")

    def retirar_lampada(self):
        # Método para retirar a lâmpada
        print("Retirando a lâmpada")

    def instalar_nova_lampada(self):
        # Método para instalar a nova lâmpada
        print("Instalando a nova lâmpada")

    def descer_escada(self):
        # Método para descer da escada
        print("Descendo da escada")

    def localizar_escada(self):
        # Método para localizar a escada
        self.escada = True

    def verificar_posicao_escada(self):
        # Método para verificar a posição da escada em relação à lâmpada
        if self.escada:
            print("Calculando subida")
        else:
            print("Avisando o operador")

    def chegou_ao_topo_da_escada(self):
        # Método para verificar se chegou ao topo da escada
        return True  # ou False, dependendo da lógica específica

    def chegou_ao_inicio_da_escada(self):
        # Método para verificar se chegou ao início da escada
        return True  # ou False, dependendo da lógica específica

    def subir_escada_4_vezes(self):
        # Método para subir na escada 4 vezes
        for _ in range(4):
            self.subir_escada()
            if self.chegou_ao_topo_da_escada():
                break

    def localizar_lampada(self):
        # Método para localizar a lâmpada
        self.lampada = True

    def lampada_queimada(self):
        # Método para verificar se a lâmpada está queimada
        return True  # ou False, dependendo da lógica específica

    def lampada_no_terminal(self):
        # Método para verificar se a lâmpada está no terminal
        return True  # ou False, dependendo da lógica específica

    def girar_sentido_anti_horario(self):
        # Método para girar no sentido anti-horário
        print("Girando no sentido anti-horário")

    def guardar_no_recipiente(self):
        # Método para guardar no recipiente
        print("Guardando no recipiente")

    def testar_lampada(self):
        # Método para testar a lâmpada
        if self.lampada_queimada():
            while self.lampada_no_terminal():
                self.girar_sentido_anti_horario()
                self.guardar_no_recipiente()
            else:
                self.avisar_operador()

    def pegar_nova_lampada(self):
        # Método para pegar uma nova lâmpada
        while not self.lampada_esta_fixa_no_terminal():
            self.girar_sentido_horario()

    def lampada_esta_fixa_no_terminal(self):
        # Método para verificar se a lâmpada está fixa no terminal
        return True  # ou False, dependendo da lógica específica

    def girar_sentido_horario(self):
        # Método para girar no sentido horário
        print("Girando no sentido horário")

    def descer_escada_ate_o_inicio(self):
        # Método para descer da escada até o início
        while True:
            self.descer_escada()
            if self.chegou_ao_inicio_da_escada():
                break

    def avisar_operador(self):
        # Método para avisar o operador
        print("Avisando o operador")

# Exemplo de uso da classe TrocarLampada
if __name__ == "__main__":
    troca_lamp = TrocarLampada()
    troca_lamp.localizar_escada()
    troca_lamp.verificar_posicao_escada()
    troca_lamp.subir_escada()
    troca_lamp.localizar_lampada()
    troca_lamp.testar_lampada()
    troca_lamp.retirar_lampada()
    troca_lamp.pegar_nova_lampada()
    troca_lamp.instalar_nova_lampada()
    troca_lamp.descer_escada_ate_o_inicio()