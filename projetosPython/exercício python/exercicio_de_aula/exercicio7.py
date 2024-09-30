import pygame

pygame.init()

# definir as cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Definir o tamanho da tela
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Meu Jogo")

# Carregar imagem do carro
carImg = pygame.image.load('fotos/images.jpeg')

# Definir posição inicial do carro
carX = 300
carY = 400

# Definir velocidade do carro
carSpeed = 235

# Definir distância percorrida pelo carro
distance = 0

# Loop até o usuário clicar no botão de fechar.
done = False

# Usado para gerenciar a taxa de atualização da tela
clock = pygame.time.Clock()

# -------- Loop principal do Programa --------
while not done:
    # -- Eventos do mouse e teclado --
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Lógica do jogo aqui ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        carX -= 5
    if keys[pygame.K_RIGHT]:
        carX += 5

    # Atualizar a distância percorrida pelo carro
    distance += carSpeed / 50 / 60

    # Verificar se o carro atingiu a distância máxima
    if distance >= 1200:
        print("Você atingiu a distância máxima! Diminua a velocidade.")

    # --- Desenho do jogo aqui ---
    # Primeiro, limpe a tela para branco. Não coloque outros desenhos acima desta linha.
    screen.fill(WHITE)

    # Desenhar o carro na tela
    screen.blit(carImg, (carX, carY))

    # --- Atualização da tela com o que foi desenhado ---
    pygame.display.flip()

    # --- Limita a taxa de atualização da tela ---
    clock.tick(60)

# Fechar a janela e sair.
pygame.quit()