import pygame
import random


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
        self.rect.y += 1
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

# TRANSFORMA AMBAS LISTAS EM SPRITES
# SPRITES(LIVROS)
block_list = pygame.sprite.Group()
# LISTA COM TODAS AS SPRITES
all_sprites_list = pygame.sprite.Group()

# NOME DA TELA
pygame.display.set_caption('Tentativa do jogo!')

clock = pygame.time.Clock()

# IMAGENS
background_position = [0, 0]
background_image = pygame.image.load("fundo.jpg").convert()
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
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            # VERIFICA SE É UMA SETA
            # AJUSTA A VELOCIDADE
            if event.key == pygame.K_LEFT and x_coord > -1:
                x_speed = -40
            elif event.key == pygame.K_RIGHT and x_coord < 555:
                x_speed = 40
            elif event.key == pygame.K_ESCAPE:  # Verificação da tecla ESC pressionada
                tela_pergunta = False
            elif event.key == pygame.K_1:  # Verificação da tecla 1 pressionada
                tela_pergunta = False
                resposta = 1
            elif event.key == pygame.K_2:  # Verificação da tecla 2 pressionada
                tela_pergunta = False
                resposta = 2
            elif event.key == pygame.K_3:  # Verificação da tecla 3 pressionada
                tela_pergunta = False
                resposta = 3
            elif event.key == pygame.K_4:  # Verificação da tecla 4 pressionada
                tela_pergunta = False
                resposta = 4

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
    all_sprites_list.update()

    # VERIFICA SE O JOGADOR COLIDIU COM ALGO-------------------------------------------------------
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
    # PERGUNTAS ----------------------------------------------------------------------------------
    txt = ["Capital da argentina?", "Qual é o maior planeta do sistema solar?", "Quem foi o primeiro presidente dos Estados Unidos?", ""]
    alt1 = ["1 - Rio de Janeiro ", "1 - Vênus", "1 - Abraham Lincoln", ""]
    alt2 = ["2 - Buenos Aires", "2 - Saturno", "2 - Thomas Jefferson", ""]
    alt3 = ["3 - Santiago", "3 - Júpiter", "3 - Washington", ""]
    alt4 = ["4 -  Lima", "4 - Urano", "4 - John F. Kennedy", ""]
    resp = (2, 3, 3, 4)
    pygame.font.init()
    fonte = pygame.font.get_default_font()                      ##### carrega com a fonte padrão
    fontesys = pygame.font.SysFont(fonte, 35)                   ##### usa a fonte padrão
    txttela = fontesys.render(txt[cont], 1, BLACK)
    alt1tela = fontesys.render(alt1[cont], 1, BLACK)
    alt2tela = fontesys.render(alt2[cont], 1, BLACK)
    alt3tela = fontesys.render(alt3[cont], 1, BLACK)
    alt4tela = fontesys.render(alt4[cont], 1, BLACK)

    if resposta is not None and resposta == resp[cont] and resposta != 0:
        acertos += 1
        resposta = 0
        cont += 1
        print(acertos)

    if 2 > acertos >= 1:
        player.mudar_imagem('SpritePescador.png')
    elif 3 > acertos >= 2:
        player.mudar_imagem('SpriteFerreiro.png')
    elif acertos >= 3:
        player.mudar_imagem('SpriteCavaleiro.png')

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

    # ATUALIZA A TELA
    pygame.display.flip()

    # FPS
    clock.tick(60)

# FECHA
pygame.quit()
