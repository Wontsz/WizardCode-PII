import pygame
import random
import time
import mysql.connector

# conecta ao banco de dados ""aqui tem q os dados do banco de dados da maquina de vcs ou a q vai ser host do jogo""
dbperguntas = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mateusw23011890",
    database="jogo")

# define o cursor
cursor = dbperguntas.cursor()

# função que pega um valor aleatorio de cada linha e coloca em uma variavel
def perguntaAleatoria():
    cursor.execute("SELECT * FROM perguntas ORDER BY RAND() LIMIT 1")
    linha = cursor.fetchone()
    txt = linha[0]
    alt1 = linha[1]
    alt2 = linha[2]
    alt3 = linha[3]
    alt4 = linha[4]
    resp = linha[5]
    materia = linha[6]
    return txt, alt1, alt2, alt3, alt4, resp, materia

# CORES
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# RECT = RETANGULO = HITBOX RETANGULAR
class Livros(pygame.sprite.Sprite):
    def __init__(self): # ATRIBUTOS
        super().__init__()
        self.image = book_image
        self.rect = self.image.get_rect()

    def reset_pos(self): # MÉTODO
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, LARGURA)

    def update(self): # MÉTODO
        self.rect.y += 3
        if self.rect.y > 650:
            self.reset_pos()


class Player(pygame.sprite.Sprite):
    def __init__(self): # ATRIBUTOS
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()

    def update(self): # MÉTODO
        pos = [x_coord, y_coord]
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def mudar_imagem(self, nova_imagem):
        self.image.fill((0, 0, 0))  # REMOVE A PRIMEIRA SKIN
        player_image.set_colorkey(BLACK)
        self.image = pygame.image.load(nova_imagem).convert_alpha()

    def atualizar_informacoes(self):
        # Renderize o texto para cada informação
        texto_vidas = fontesys.render("Vidas: " + str(vidas), True, (255, 255, 255))  # Preto
        texto_acertos = fontesys.render("Acertos: " + str(acertos), True, (255, 255, 255))
        # Posicione os textos na tela
        TELA.blit(texto_vidas, (10, 50))
        TELA.blit(texto_acertos, (10, 10))

#CRONOMETRO PARA REGISTRAR O TEMPO EM QUE A PESSOA COMPLETA O JOGO
class Timer:
    def __init__(self):
        self.start = time.time()
    
    def get(self) -> float:
        return time.time() - self.start
    
    def start(self, args):
        self.timer = Timer()

    def update(self):
        print(self.timer.get())

# INICIO DO JOGO--------------------------------------------------------------------------------------------
pygame.init()
LARGURA = 700
ALTURA = 900
TAMANHO = [LARGURA, ALTURA]
TELA = pygame.display.set_mode(TAMANHO)
question_surface = pygame.Surface((540, 300))  # cria uma nova surface para a tela de pergunta
question_surface.fill((255, 255, 255))
cont = 0
acertos = 0
resposta = 0
erros = acertos -1
vidas = 3
# TRANSFORMA AMBAS LISTAS EM SPRITES
# SPRITES(LIVROS)
block_list = pygame.sprite.Group()
# LISTA COM TODAS AS SPRITES
all_sprites_list = pygame.sprite.Group()

# NOME DA TELA
pygame.display.set_caption('CODE WIZARD')

clock = pygame.time.Clock()

# IMAGENS
background_position = [0, 0]
background_image = pygame.image.load("fundo.png").convert()
player_image = pygame.image.load("SpriteFazendeiro.png").convert_alpha()
book_image = pygame.image.load("livro.png").convert()
book_image.set_colorkey(BLACK)
# icon_image = pygame.image.load('images/icon.png')
# pygame.display.set_icon(icon_image)


# VELOCIDADE POR FRAME (ANDAR)
x_speed = 0
y_speed = 0

# POSIÇÃO ATUAL (JUNÇÃO COM ANDAR)
x_coord = 275
y_coord = 600

player = Player()
all_sprites_list.add(player)

# OBJETO LIVRO------------------------------------------------------------------------------------------------
for i in range(3):
    livro = Livros()

    # LOCALIZAÇÃO RANDOMICA P OBJETO
    livro.rect.x = random.randrange(LARGURA)
    livro.rect.y = random.randrange(ALTURA)

    # ADICIONA O OBJETO NA LISTA DE SPRITES
    block_list.add(livro)
    all_sprites_list.add(livro)

tela_pergunta = False
# LOOP PRINCIPAL DO JOGO---------------------------------------------------------------------------------------
pause = False
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            # VERIFICA SE É UMA SETA
            # AJUSTA A VELOCIDADE
            if event.key == pygame.K_LEFT and x_coord > -1 and not pause:
                x_speed = -40
            elif event.key == pygame.K_RIGHT and x_coord < 555 and not pause:
                x_speed = 40
            elif event.key == pygame.K_ESCAPE:  # Verificação da tecla ESC pressionada
                tela_pergunta = False
                pause = False
            elif event.key == pygame.K_1 and tela_pergunta:  # Verificação da tecla 1 pressionada
                tela_pergunta = False
                resposta = 1
                pause = False
            elif event.key == pygame.K_2 and tela_pergunta:  # Verificação da tecla 2 pressionada
                tela_pergunta = False
                resposta = 2
                pause = False
            elif event.key == pygame.K_3 and tela_pergunta:  # Verificação da tecla 3 pressionada
                tela_pergunta = False
                resposta = 3
                pause = False
            elif event.key == pygame.K_4 and tela_pergunta:  # Verificação da tecla 4 pressionada
                tela_pergunta = False
                resposta = 4
                pause = False

        elif event.type == pygame.KEYUP:
            # PARA DE ANDAR AO SOLTAR
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

        # ANDAR
        x_coord = x_coord + x_speed
        y_coord = y_coord + y_speed

    # COPIA A IMAGEM NA TELA--------------------------------------------------------------------------------
    TELA.fill(WHITE)
    TELA.blit(background_image, background_position)
    TELA.blit(player_image, [x_coord, y_coord])

    # CHAMA O MÉTODO QUE MOVIMENTA OS LIVROS-----------------------------------------------------------------
    if not pause:
        all_sprites_list.update()

    # VERIFICA SE O JOGADOR COLIDIU COM ALGO-------------------------------------------------------
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
     # PERGUNTAS ----------------------------------------------------------------------------------
    pygame.font.init()
    txt, alt1, alt2, alt3, alt4, resp, materia = perguntaAleatoria()
    fonte = pygame.font.get_default_font()                     # carrega com a fonte padrão
    fontesys = pygame.font.SysFont(fonte, 29)                  # usa a fonte padrão
    player.atualizar_informacoes()
    colicao = False


    # se o jogador colidir com um livro, gerar uma pergunta
    if len(blocks_hit_list) > 0 and not tela_pergunta:
        txt, alt1, alt2, alt3, alt4, resp, materia = perguntaAleatoria()
        txttela = fontesys.render(txt, 1, BLACK)
        alt1tela = fontesys.render(alt1, 1, BLACK)
        alt2tela = fontesys.render(alt2, 1, BLACK)
        alt3tela = fontesys.render(alt3, 1, BLACK)
        alt4tela = fontesys.render(alt4, 1, BLACK)
        colisao = True
        print(txt, alt1, alt2, alt3, alt4, resp, materia)

    if resposta == resp and resposta != 0 and colisao == True:
        acertos += 1
        resposta = 0
        cont += 1
        print(acertos)
        
    if resposta is not None and resposta != resp != resposta != 0:
        resposta = 0
        cont += 1
        vidas -= 1
        print(acertos)

    if 2 > acertos >= 1:
        player.mudar_imagem('SpritePescador.png')
    elif 3 > acertos >= 2:
        player.mudar_imagem('SpriteFerreiro.png')
    elif acertos >= 3:
        player.mudar_imagem('SpriteCavaleiro.png')
    elif vidas == -1:
        pygame.quit()

    # CHECA COLISÕES----------------------------------------------------------------------
    for block in blocks_hit_list:
        # ABRE PERGUNTA NA TELA
        tela_pergunta = True
        # RESETA PARA O INICIO DA TELA
        block.reset_pos()
    all_sprites_list.draw(TELA)

    if tela_pergunta:
        TELA.blit(question_surface, (80, 250))
        TELA.blit(txttela, (100, 270))
        TELA.blit(alt1tela, (100, 310))
        TELA.blit(alt2tela, (100, 350))
        TELA.blit(alt3tela, (100, 390))
        TELA.blit(alt4tela, (100, 430))
        pause = True

    # ATUALIZA A TELA
    pygame.display.flip()

    # FPS
    clock.tick(60)

# FECHA
pygame.quit()
