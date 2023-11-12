import pygame, sys

pygame.init()
# Configuração da janela
ALTURA = 500
LARGURA = 900
tamanhoDaJanela = (LARGURA, ALTURA)
clock = pygame.time.Clock()
# Configuração de cores
branco = (255, 255, 255)
cinza = (150, 150, 150)
cinza_claro = (200, 200, 200)
preto = (0, 0, 0)
azul = (0, 0, 255)
azul_escuro = (0, 0, 125)
vermelho = (255, 0, 0)
vermelho_escuro = (125, 0, 0)
verde = (0, 255, 0)
verde_escuro = (0, 125, 0)
# Criando a janela
janela = pygame.display.set_mode(tamanhoDaJanela)
pygame.display.set_caption('Estaquinha')
# Fonte
fonte = pygame.font.Font(None, 16)
fonte14 = pygame.font.Font(None, 14)
# Menu
recMenu_width = 160
recMenu_height = ALTURA
recMenu_x = 0
recMenu_y = 0
Menu_cor = cinza
# Retângulo do menu
Menu_rect = pygame.Rect(recMenu_x, recMenu_y, recMenu_width, recMenu_height)
# Botões
button_spacing = 20
button_width = recMenu_width - (button_spacing * 2)
button_height = (ALTURA // 10) - (ALTURA // 25)
button_x = button_spacing
button_y = button_spacing
# Retângulo dos botões
button1_rect = pygame.Rect(button_x, button_y, button_width, button_height)
button1_cor = azul
button2_rect = pygame.Rect(button_x, button1_rect.y + button1_rect.width // 2, button_width, button_height)
button2_cor = azul
button3_rect = pygame.Rect(button_x, button2_rect.y + button2_rect.width // 2, button_width, button_height)
button3_cor = azul
button4_rect = pygame.Rect(button_x, button3_rect.y + button3_rect.width // 2, button_width, button_height)
button4_cor = vermelho
# Acessar diferentes telas
estaca = True
perfil_sondagem = False
resultado = False
calcular = False
# Tabela NSPT
NSPT = "0"
NSPT2 = "0"
NSPT3 = "0"
NSPT4 = "0"
NSPT5 = "0"
NSPT6 = "0"
NSPT7 = "0"
NSPT8 = "0"
NSPT9 = "0"
NSPT10 = "0"
NSPT11 = "0"
NSPT12 = "0"
NSPT13 = "0"
NSPT14 = "0"
NSPT15 = "0"
NSPT16 = "0"
NSPT17 = "0"
NSPT18 = "0"
NSPT19 = "0"
NSPT20 = "0"
NSPT21 = "0"
NSPT22 = "0"
NSPT23 = "0"
NSPT24 = "0"
NSPT25 = "0"
NSPT_select = False
NSPT2_select = False
NSPT3_select = False
NSPT4_select = False
NSPT5_select = False
NSPT6_select = False
NSPT7_select = False
NSPT8_select = False
NSPT9_select = False
NSPT10_select = False
NSPT11_select = False
NSPT12_select = False
NSPT13_select = False
NSPT14_select = False
NSPT15_select = False
NSPT16_select = False
NSPT17_select = False
NSPT18_select = False
NSPT19_select = False
NSPT20_select = False
NSPT21_select = False
NSPT22_select = False
NSPT23_select = False
NSPT24_select = False
NSPT25_select = False
solos = ['Areia', 'Areia Siltosa', 'Areia Siltoargilosa', 'Areia Argilosa', 'Areia Argilossiltosa', 'Silte', 'Silte Arenoso', 'Silte Arenoargiloso', 'Silte Argiloso', 'Silte Argiloarenoso', 'Argila', 'Argila Arenosa', 'Argila Arenossiltosa', 'Argila Siltosa', 'Argila Siltoarenosa']
solos_select = False
solos_select2 = False
solos_select3 = False
solos_select4 = False
solos_select5 = False
solos_select6 = False
solos_select7 = False
solos_select8 = False
solos_select9 = False
solos_select10 = False
solos_select11 = False
solos_select12 = False
solos_select13 = False
solos_select14 = False
solos_select15 = False
solos_select16 = False
solos_select17 = False
solos_select18 = False
solos_select19 = False
solos_select20 = False
solos_select21 = False
solos_select22 = False
solos_select23 = False
solos_select24 = False
solos_select25 = False
solo = None
solo2 = None
solo3 = None
solo4 = None
solo5 = None
solo6 = None
solo7 = None
solo8 = None
solo9 = None
solo10 = None
solo11 = None
solo12 = None
solo13 = None
solo14 = None
solo15 = None
solo16 = None
solo17 = None
solo18 = None
solo19 = None
solo20 = None
solo21 = None
solo22 = None
solo23 = None
solo24 = None
solo25 = None
profundidade = '1'
profundidade2 = '2'
profundidade3 = '3'
profundidade4 = '4'
profundidade5 = '5'
profundidade6 = '6'
profundidade7 = '7'
profundidade8 = '8'
profundidade9 = '9'
profundidade10 = '10'
profundidade11 = '11'
profundidade12 = '12'
profundidade13 = '13'
profundidade14 = '14'
profundidade15 = '15'
profundidade16 = '16'
profundidade17 = '17'
profundidade18 = '18'
profundidade19 = '19'
profundidade20 = '20'
profundidade21 = '21'
profundidade22 = '22'
profundidade23 = '23'
profundidade24 = '24'
profundidade25 = '25'
coluna1 = 'Profundidade'
coluna2 = 'NSPT'
coluna3 = 'Tipo de Solo'
# Dimensões da tabela
cell_width = 150
cell_height = 40
#tab posição
tab_position = 0
# Retângulo tabela e texto
rec_coluna1 = pygame.Rect(recMenu_width + button_spacing, 0, cell_width, cell_height)
rec_coluna2 = pygame.Rect(rec_coluna1.x + rec_coluna1.width, 0, cell_width, cell_height)
rec_coluna3 = pygame.Rect(rec_coluna2.x + rec_coluna2.width, 0, cell_width, cell_height)
rec_profundidade = pygame.Rect(rec_coluna1.x, rec_coluna1.y + rec_coluna1.height, cell_width, cell_height)
rec_profundidade2 = pygame.Rect(rec_profundidade.x, rec_profundidade.y + cell_height, cell_width, cell_height)
rec_profundidade3 = pygame.Rect(rec_profundidade2.x, rec_profundidade2.y + cell_height, cell_width, cell_height)
rec_profundidade4 = pygame.Rect(rec_profundidade3.x, rec_profundidade3.y + cell_height, cell_width, cell_height)
rec_profundidade5 = pygame.Rect(rec_profundidade4.x, rec_profundidade4.y + cell_height, cell_width, cell_height)
rec_profundidade6 = pygame.Rect(rec_profundidade5.x, rec_profundidade5.y + cell_height, cell_width, cell_height)
rec_profundidade7 = pygame.Rect(rec_profundidade6.x, rec_profundidade6.y + cell_height, cell_width, cell_height)
rec_profundidade8 = pygame.Rect(rec_profundidade7.x, rec_profundidade7.y + cell_height, cell_width, cell_height)
rec_profundidade9 = pygame.Rect(rec_profundidade8.x, rec_profundidade8.y + cell_height, cell_width, cell_height)
rec_profundidade10 = pygame.Rect(rec_profundidade9.x, rec_profundidade9.y + cell_height, cell_width, cell_height)
rec_profundidade11 = pygame.Rect(rec_profundidade10.x, rec_profundidade10.y + cell_height, cell_width, cell_height)
rec_profundidade12 = pygame.Rect(rec_profundidade11.x, rec_profundidade11.y + cell_height, cell_width, cell_height)
rec_profundidade13 = pygame.Rect(rec_profundidade12.x, rec_profundidade12.y + cell_height, cell_width, cell_height)
rec_profundidade14 = pygame.Rect(rec_profundidade13.x, rec_profundidade13.y + cell_height, cell_width, cell_height)
rec_profundidade15 = pygame.Rect(rec_profundidade14.x, rec_profundidade14.y + cell_height, cell_width, cell_height)
rec_profundidade16 = pygame.Rect(rec_profundidade15.x, rec_profundidade15.y + cell_height, cell_width, cell_height)
rec_profundidade17 = pygame.Rect(rec_profundidade16.x, rec_profundidade16.y + cell_height, cell_width, cell_height)
rec_profundidade18 = pygame.Rect(rec_profundidade17.x, rec_profundidade17.y + cell_height, cell_width, cell_height)
rec_profundidade19 = pygame.Rect(rec_profundidade18.x, rec_profundidade18.y + cell_height, cell_width, cell_height)
rec_profundidade20 = pygame.Rect(rec_profundidade19.x, rec_profundidade19.y + cell_height, cell_width, cell_height)
rec_profundidade21 = pygame.Rect(rec_profundidade20.x, rec_profundidade20.y + cell_height, cell_width, cell_height)
rec_profundidade22 = pygame.Rect(rec_profundidade21.x, rec_profundidade21.y + cell_height, cell_width, cell_height)
rec_profundidade23 = pygame.Rect(rec_profundidade22.x, rec_profundidade22.y + cell_height, cell_width, cell_height)
rec_profundidade24 = pygame.Rect(rec_profundidade23.x, rec_profundidade23.y + cell_height, cell_width, cell_height)
rec_profundidade25 = pygame.Rect(rec_profundidade24.x, rec_profundidade24.y + cell_height, cell_width, cell_height)
rec_NSPT = pygame.Rect(rec_coluna2.x, rec_coluna2.y + rec_coluna2.height, cell_width, cell_height)
rec_NSPT2 = pygame.Rect(rec_NSPT.x, rec_NSPT.y + cell_height, cell_width, cell_height)
rec_NSPT3 = pygame.Rect(rec_NSPT2.x, rec_NSPT2.y + cell_height, cell_width, cell_height)
rec_NSPT4 = pygame.Rect(rec_NSPT3.x, rec_NSPT3.y + cell_height, cell_width, cell_height)
rec_NSPT5 = pygame.Rect(rec_NSPT4.x, rec_NSPT4.y + cell_height, cell_width, cell_height)
rec_NSPT6 = pygame.Rect(rec_NSPT5.x, rec_NSPT5.y + cell_height, cell_width, cell_height)
rec_NSPT7 = pygame.Rect(rec_NSPT6.x, rec_NSPT6.y + cell_height, cell_width, cell_height)
rec_NSPT8 = pygame.Rect(rec_NSPT7.x, rec_NSPT7.y + cell_height, cell_width, cell_height)
rec_NSPT9 = pygame.Rect(rec_NSPT8.x, rec_NSPT8.y + cell_height, cell_width, cell_height)
rec_NSPT10 = pygame.Rect(rec_NSPT9.x, rec_NSPT9.y + cell_height, cell_width, cell_height)
rec_NSPT11 = pygame.Rect(rec_NSPT10.x, rec_NSPT10.y + cell_height, cell_width, cell_height)
rec_NSPT12 = pygame.Rect(rec_NSPT11.x, rec_NSPT11.y + cell_height, cell_width, cell_height)
rec_NSPT13 = pygame.Rect(rec_NSPT12.x, rec_NSPT12.y + cell_height, cell_width, cell_height)
rec_NSPT14 = pygame.Rect(rec_NSPT13.x, rec_NSPT13.y + cell_height, cell_width, cell_height)
rec_NSPT15 = pygame.Rect(rec_NSPT14.x, rec_NSPT14.y + cell_height, cell_width, cell_height)
rec_NSPT16 = pygame.Rect(rec_NSPT15.x, rec_NSPT15.y + cell_height, cell_width, cell_height)
rec_NSPT17 = pygame.Rect(rec_NSPT16.x, rec_NSPT16.y + cell_height, cell_width, cell_height)
rec_NSPT18 = pygame.Rect(rec_NSPT17.x, rec_NSPT17.y + cell_height, cell_width, cell_height)
rec_NSPT19 = pygame.Rect(rec_NSPT18.x, rec_NSPT18.y + cell_height, cell_width, cell_height)
rec_NSPT20 = pygame.Rect(rec_NSPT19.x, rec_NSPT19.y + cell_height, cell_width, cell_height)
rec_NSPT21 = pygame.Rect(rec_NSPT20.x, rec_NSPT20.y + cell_height, cell_width, cell_height)
rec_NSPT22 = pygame.Rect(rec_NSPT21.x, rec_NSPT21.y + cell_height, cell_width, cell_height)
rec_NSPT23 = pygame.Rect(rec_NSPT22.x, rec_NSPT22.y + cell_height, cell_width, cell_height)
rec_NSPT24 = pygame.Rect(rec_NSPT23.x, rec_NSPT23.y + cell_height, cell_width, cell_height)
rec_NSPT25 = pygame.Rect(rec_NSPT24.x, rec_NSPT24.y + cell_height, cell_width, cell_height)
rec_solos = pygame.Rect(rec_coluna3.x, rec_coluna3.y + rec_coluna3.height, cell_width, cell_height)
rec_solos2 = pygame.Rect(rec_solos.x, rec_solos.y + cell_height, cell_width, cell_height)
rec_solos3 = pygame.Rect(rec_solos2.x, rec_solos2.y + cell_height, cell_width, cell_height)
rec_solos4 = pygame.Rect(rec_solos3.x, rec_solos3.y + cell_height, cell_width, cell_height)
rec_solos5 = pygame.Rect(rec_solos4.x, rec_solos4.y + cell_height, cell_width, cell_height)
rec_solos6 = pygame.Rect(rec_solos5.x, rec_solos5.y + cell_height, cell_width, cell_height)
rec_solos7 = pygame.Rect(rec_solos6.x, rec_solos6.y + cell_height, cell_width, cell_height)
rec_solos8 = pygame.Rect(rec_solos7.x, rec_solos7.y + cell_height, cell_width, cell_height)
rec_solos9 = pygame.Rect(rec_solos8.x, rec_solos8.y + cell_height, cell_width, cell_height)
rec_solos10 = pygame.Rect(rec_solos9.x, rec_solos9.y + cell_height, cell_width, cell_height)
rec_solos11 = pygame.Rect(rec_solos10.x, rec_solos10.y + cell_height, cell_width, cell_height)
rec_solos12 = pygame.Rect(rec_solos11.x, rec_solos11.y + cell_height, cell_width, cell_height)
rec_solos13 = pygame.Rect(rec_solos12.x, rec_solos12.y + cell_height, cell_width, cell_height)
rec_solos14 = pygame.Rect(rec_solos13.x, rec_solos13.y + cell_height, cell_width, cell_height)
rec_solos15 = pygame.Rect(rec_solos14.x, rec_solos14.y + cell_height, cell_width, cell_height)
rec_solos16 = pygame.Rect(rec_solos15.x, rec_solos15.y + cell_height, cell_width, cell_height)
rec_solos17 = pygame.Rect(rec_solos16.x, rec_solos16.y + cell_height, cell_width, cell_height)
rec_solos18 = pygame.Rect(rec_solos17.x, rec_solos17.y + cell_height, cell_width, cell_height)
rec_solos19 = pygame.Rect(rec_solos18.x, rec_solos18.y + cell_height, cell_width, cell_height)
rec_solos20 = pygame.Rect(rec_solos19.x, rec_solos19.y + cell_height, cell_width, cell_height)
rec_solos21 = pygame.Rect(rec_solos20.x, rec_solos20.y + cell_height, cell_width, cell_height)
rec_solos22 = pygame.Rect(rec_solos21.x, rec_solos21.y + cell_height, cell_width, cell_height)
rec_solos23 = pygame.Rect(rec_solos22.x, rec_solos22.y + cell_height, cell_width, cell_height)
rec_solos24 = pygame.Rect(rec_solos23.x, rec_solos23.y + cell_height, cell_width, cell_height)
rec_solos25 = pygame.Rect(rec_solos24.x, rec_solos24.y + cell_height, cell_width, cell_height)
rec_add = pygame.Rect(rec_coluna3.x + (button_spacing * 2) + cell_width, 0, button_width, button_height)
rec_add_color = verde
rec_remove = pygame.Rect(rec_add.x, rec_add.y + (button_spacing * 5), rec_add.width, rec_add.height)
rec_remove_color = verde
rec_metodo = pygame.Rect(recMenu_width + button_spacing, cell_height, cell_width, cell_height)
rec_diametro = pygame.Rect(rec_metodo.x + cell_width + button_spacing, rec_metodo.y, cell_width, cell_height)
rec_estaca = pygame.Rect(rec_diametro.x + cell_width + button_spacing, rec_diametro.y, cell_width, cell_height)
rec_calcular = pygame.Rect(rec_estaca.x + cell_width + button_spacing, rec_estaca.y, cell_width, cell_height)
rec_calcular_color = verde
rec_anterior = pygame.Rect(recMenu_width + button_spacing, ALTURA - 15, cell_width, 15)
rec_anterior_color = cinza_claro
rec_proximo = pygame.Rect(rec_anterior.x + rec_anterior.width + button_spacing, rec_anterior.y, rec_anterior.width, rec_anterior.height )
rec_proximo_color = cinza_claro
# Rolagem
tab_visivel = (ALTURA - rec_profundidade.y) // (rec_profundidade.height) - 1
scroll_position = 0
scroll_speed = 1
itens_visiveis = (ALTURA - rec_solos.y) // (rec_solos.height)
# Variáveis
pi = 3.14159265359
k2 = 0
k3 = 0
k4 = 0
k5 = 0
k6 = 0
k7 = 0
k8 = 0
k9 = 0
k10 = 0
k11 = 0
k12 = 0
k13 = 0
k14 = 0
k15 = 0
k16 = 0
k17 = 0
k18 = 0
k19 = 0
k20 = 0
k21 = 0
k22 = 0
k23 = 0
k24 = 0
k25 = 0
f1 = 0
f2 = 0
alfa2 = 0
alfa3 = 0
alfa4 = 0
alfa5 = 0
alfa6 = 0
alfa7 = 0
alfa8 = 0
alfa9 = 0
alfa10 = 0
alfa11 = 0
alfa12 = 0
alfa13 = 0
alfa14 = 0
alfa15 = 0
alfa16 = 0
alfa17 = 0
alfa18 = 0
alfa19 = 0
alfa20 = 0
alfa21 = 0
alfa22 = 0
alfa23 = 0
alfa24 = 0
alfa25 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0
c10 = 0
c11 = 0
c12 = 0
c13 = 0
c14 = 0
c15 = 0
c16 = 0
c17 = 0
c18 = 0
c19 = 0
c20 = 0
c21 = 0
c22 = 0
c23 = 0
c24 = 0
c25 = 0
beta2 = 0
beta3 = 0
beta4 = 0
beta5 = 0
beta6 = 0
beta7 = 0
beta8 = 0
beta9 = 0
beta10 = 0
beta11 = 0
beta12 = 0
beta13 = 0
beta14 = 0
beta15 = 0
beta16 = 0
beta17 = 0
beta18 = 0
beta19 = 0
beta20 = 0
beta21 = 0
beta22 = 0
beta23 = 0
beta24 = 0
beta25 = 0
diametro = '0'
area = 0
circunferencia = 0
Rp3 = 0
Rp4 = 0
Rp5 = 0
Rp6 = 0
Rp7 = 0
Rp8 = 0
Rp9 = 0
Rp10 = 0
Rp11 = 0
Rp12 = 0
Rp13 = 0
Rp14 = 0
Rp15 = 0
Rp16 = 0
Rp17 = 0
Rp18 = 0
Rp19 = 0
Rp20 = 0
Rp21 = 0
Rp22 = 0
Rp23 = 0
Rp24 = 0
Rp25 = 0
Rl2 = 0
Rl3 = 0
Rl4 = 0
Rl5 = 0
Rl6 = 0
Rl7 = 0
Rl8 = 0
Rl9 = 0
Rl10 = 0
Rl11 = 0
Rl12 = 0
Rl13 = 0
Rl14 = 0
Rl15 = 0
Rl16 = 0
Rl17 = 0
Rl18 = 0
Rl19 = 0
Rl20 = 0
Rl21 = 0
Rl22 = 0
Rl23 = 0
Rl24 = 0
Rltotal2 = 0
Rltotal3 = 0
Rltotal4 = 0
Rltotal5 = 0
Rltotal6 = 0
Rltotal7 = 0
Rltotal8 = 0
Rltotal9 = 0
Rltotal10 = 0
Rltotal11 = 0
Rltotal12 = 0
Rltotal13 = 0
Rltotal14 = 0
Rltotal15 = 0
Rltotal16 = 0
Rltotal17 = 0
Rltotal18 = 0
Rltotal19 = 0
Rltotal20 = 0
Rltotal21 = 0
Rltotal22 = 0
Rltotal23 = 0
Rltotal24 = 0
Rt2 = 0
Rt3 = 0
Rt4 = 0
Rt5 = 0
Rt6 = 0
Rt7 = 0
Rt8 = 0
Rt9 = 0
Rt10 = 0
Rt11 = 0
Rt12 = 0
Rt13 = 0
Rt14 = 0
Rt15 = 0
Rt16 = 0
Rt17 = 0
Rt18 = 0
Rt19 = 0
Rt20 = 0
Rt21 = 0
Rt22 = 0
Rt23 = 0
Rt24 = 0
diametro_select = False
# Estacas
estaca_aoki = ['Franki', 'Metálica', 'Pré-moldada', 'Escavada', 'Raiz', 'Hélice contínua', 'Ômega']
estaca_quaresma = ['Escavada em geral', 'Escavada (bentonita)', 'Hélice contínua', 'Raiz', 'Injet. sob altas pressões']
estaca_selecionado = None
estaca_aberto = False
# Selecionado metodo por dropdown
metodos = ['DECOURT & QUARESMA', 'AOKI & VELLOSO']
metodo_selecionado = None
metodo_aberto = False
#Funções
# Função para ver se é numero
def e_numero (caractere):
    return caractere.isdigit()
# Contagens
pcount = 0
count = 0

# Loop Principal
while True:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if button1_rect.collidepoint(mouse_pos):
                    button1_cor = azul_escuro
                    estaca = True
                    perfil_sondagem = False
                    resultado = False
                    solos_select = False
                if button2_rect.collidepoint(mouse_pos):
                    button2_cor = azul_escuro
                    estaca = False
                    perfil_sondagem = True
                    resultado = False
                    solos_select = False
                if button3_rect.collidepoint(mouse_pos):
                    button3_cor = azul_escuro
                    estaca = False
                    perfil_sondagem = False
                    resultado = True
                    solos_select = False
                if button4_rect.collidepoint(mouse_pos):
                    button4_cor = vermelho_escuro
                    estaca = True
                    perfil_sondagem = False
                    resultado = False
                    solos_select = False
                    NSPT = "0"
                    NSPT2 = "0"
                    NSPT3 = "0"
                    NSPT4 = "0"
                    NSPT5 = "0"
                    NSPT6 = "0"
                    NSPT7 = "0"
                    NSPT8 = "0"
                    NSPT9 = "0"
                    NSPT10 = "0"
                    NSPT11 = "0"
                    NSPT12 = "0"
                    NSPT13 = "0"
                    NSPT14 = "0"
                    NSPT15 = "0"
                    NSPT16 = "0"
                    NSPT17 = "0"
                    NSPT18 = "0"
                    NSPT19 = "0"
                    NSPT20 = "0"
                    NSPT21 = "0"
                    NSPT22 = "0"
                    NSPT23 = "0"
                    NSPT24 = "0"
                    NSPT25 = "0"
                    NSPT_select = False
                    NSPT2_select = False
                    NSPT3_select = False
                    NSPT4_select = False
                    NSPT5_select = False
                    NSPT6_select = False
                    NSPT7_select = False
                    NSPT8_select = False
                    NSPT9_select = False
                    NSPT10_select = False
                    NSPT11_select = False
                    NSPT12_select = False
                    NSPT13_select = False
                    NSPT14_select = False
                    NSPT15_select = False
                    NSPT16_select = False
                    NSPT17_select = False
                    NSPT18_select = False
                    NSPT19_select = False
                    NSPT20_select = False
                    NSPT21_select = False
                    NSPT22_select = False
                    NSPT23_select = False
                    NSPT24_select = False
                    NSPT25_select = False
                    solos_select = False
                    solos_select2 = False
                    solos_select3 = False
                    solos_select4 = False
                    solos_select5 = False
                    solos_select6 = False
                    solos_select7 = False
                    solos_select8 = False
                    solos_select9 = False
                    solos_select10 = False
                    solos_select11 = False
                    solos_select12 = False
                    solos_select13 = False
                    solos_select14 = False
                    solos_select15 = False
                    solos_select16 = False
                    solos_select17 = False
                    solos_select18 = False
                    solos_select19 = False
                    solos_select20 = False
                    solos_select21 = False
                    solos_select22 = False
                    solos_select23 = False
                    solos_select24 = False
                    solos_select25 = False
                    solo = None
                    solo2 = None
                    solo3 = None
                    solo4 = None
                    solo5 = None
                    solo6 = None
                    solo7 = None
                    solo8 = None
                    solo9 = None
                    solo10 = None
                    solo11 = None
                    solo12 = None
                    solo13 = None
                    solo14 = None
                    solo15 = None
                    solo16 = None
                    solo17 = None
                    solo18 = None
                    solo19 = None
                    solo20 = None
                    solo21 = None
                    solo22 = None
                    solo23 = None
                    solo24 = None
                    solo25 = None
                    count = 0
                    tab_position = 0
                    diametro = '0'
                    metodo_selecionado = None
                    estaca_selecionado = None
                
                if resultado:

                    if rec_diametro.collidepoint(mouse_pos) and not metodo_aberto:
                        diametro_select = True
                        estaca_aberto = False
                        NSPT_select = False
                        NSPT2_select = False
                        NSPT3_select = False
                        NSPT4_select = False
                        NSPT5_select = False
                        NSPT6_select = False
                        NSPT7_select = False
                        NSPT8_select = False
                        NSPT9_select = False
                        NSPT10_select = False
                        NSPT11_select = False
                        NSPT12_select = False
                        NSPT13_select = False
                        NSPT14_select = False
                        NSPT15_select = False
                        NSPT16_select = False
                        NSPT17_select = False
                        NSPT18_select = False
                        NSPT19_select = False
                        NSPT20_select = False
                        NSPT21_select = False
                        NSPT22_select = False
                        NSPT23_select = False
                        NSPT24_select = False
                        NSPT25_select = False
                    else:
                        diametro_select = False

                    if rec_calcular.collidepoint(mouse_pos):
                        rec_calcular_color = verde_escuro
                        calcular = True
                    
                    if rec_proximo.collidepoint(mouse_pos) and pcount < 6:
                        pcount += 1
                        rec_proximo_color = cinza
                    
                    if rec_anterior.collidepoint(mouse_pos) and pcount > 0:
                        pcount -= 1
                        rec_anterior_color = cinza
                    
                    if rec_metodo.collidepoint(mouse_pos):
                        metodo_aberto = not metodo_aberto
                        diametro_select = False
                    else:
                        if metodo_aberto:
                            for i, opcao in enumerate(metodos):
                                rec_opcaometodo = pygame.Rect(rec_metodo.x, rec_metodo.y + (i+1) * rec_metodo.height, rec_metodo.width, rec_metodo.height)
                                if rec_opcaometodo.collidepoint(mouse_pos):
                                    metodo_selecionado = opcao
                                    metodo_aberto = False
                                    estaca_selecionado = None
                                else:
                                    metodo_aberto = False
                    
                    if rec_estaca.collidepoint(mouse_pos) and metodo_selecionado is not None:
                        estaca_aberto = not estaca_aberto
                        diametro_select = False
                    else:
                        if estaca_aberto:
                            if metodo_selecionado == 'DECOURT & QUARESMA':
                                for i, opcao in enumerate(estaca_quaresma):
                                    rec_opcaoestaca = pygame.Rect(rec_estaca.x, rec_estaca.y + (i+1) * rec_estaca.height, rec_estaca.width, rec_estaca.height)
                                    if rec_opcaoestaca.collidepoint(mouse_pos):
                                        estaca_selecionado = opcao
                                        estaca_aberto = False
                                    else:
                                        estaca_aberto = False
                            
                            if metodo_selecionado == 'AOKI & VELLOSO':
                                for i, opcao in enumerate(estaca_aoki):
                                    rec_opcaoestaca = pygame.Rect(rec_estaca.x, rec_estaca.y + (i+1) * rec_estaca.height, rec_estaca.width, rec_estaca.height)
                                    if rec_opcaoestaca.collidepoint(mouse_pos):
                                        estaca_selecionado = opcao
                                        estaca_aberto = False
                                    else:
                                        estaca_aberto = False
                
                if perfil_sondagem:

                    if rec_add.collidepoint(mouse_pos) and count < 25:
                        rec_add_color = verde_escuro
                        count += 1
                    if rec_remove.collidepoint(mouse_pos) and count > 0 and solos_select == False and solos_select2 == False:
                        rec_remove_color = verde_escuro
                        count -= 1
                    if rec_NSPT.collidepoint(mouse_pos):
                        NSPT_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT_select = False
                    if rec_NSPT2.collidepoint(mouse_pos):
                        NSPT2_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT2_select = False
                    if rec_NSPT3.collidepoint(mouse_pos):
                        NSPT3_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT3_select = False
                    if rec_NSPT4.collidepoint(mouse_pos):
                        NSPT4_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT4_select = False
                    if rec_NSPT5.collidepoint(mouse_pos):
                        NSPT5_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT5_select = False
                    if rec_NSPT6.collidepoint(mouse_pos):
                        NSPT6_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT6_select = False
                    if rec_NSPT7.collidepoint(mouse_pos):
                        NSPT7_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT7_select = False
                    if rec_NSPT8.collidepoint(mouse_pos):
                        NSPT8_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT8_select = False
                    if rec_NSPT9.collidepoint(mouse_pos):
                        NSPT9_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT9_select = False
                    if rec_NSPT10.collidepoint(mouse_pos):
                        NSPT10_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT10_select = False
                    if rec_NSPT11.collidepoint(mouse_pos):
                        NSPT11_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT11_select = False
                    if rec_NSPT12.collidepoint(mouse_pos):
                        NSPT12_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT12_select = False
                    if rec_NSPT13.collidepoint(mouse_pos):
                        NSPT13_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT13_select = False
                    if rec_NSPT14.collidepoint(mouse_pos):
                        NSPT14_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT14_select = False
                    if rec_NSPT15.collidepoint(mouse_pos):
                        NSPT15_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT15_select = False
                    if rec_NSPT16.collidepoint(mouse_pos):
                        NSPT16_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT16_select = False
                    if rec_NSPT17.collidepoint(mouse_pos):
                        NSPT17_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT17_select = False
                    if rec_NSPT18.collidepoint(mouse_pos):
                        NSPT18_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT18_select = False
                    if rec_NSPT19.collidepoint(mouse_pos):
                        NSPT19_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT19_select = False
                    if rec_NSPT20.collidepoint(mouse_pos):
                        NSPT20_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT20_select = False
                    if rec_NSPT21.collidepoint(mouse_pos):
                        NSPT21_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT21_select = False
                    if rec_NSPT22.collidepoint(mouse_pos):
                        NSPT22_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT22_select = False
                    if rec_NSPT23.collidepoint(mouse_pos):
                        NSPT23_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT23_select = False
                    if rec_NSPT24.collidepoint(mouse_pos):
                        NSPT24_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT24_select = False
                    if rec_NSPT25.collidepoint(mouse_pos):
                        NSPT25_select = True
                        solos_select = False
                        solos_select2 = False
                        solos_select3 = False
                        solos_select4 = False
                        solos_select5 = False
                        solos_select6 = False
                        solos_select7 = False
                        solos_select8 = False
                        solos_select9 = False
                        solos_select10 = False
                        solos_select11 = False
                        solos_select12 = False
                        solos_select13 = False
                        solos_select14 = False
                        solos_select15 = False
                        solos_select16 = False
                        solos_select17 = False
                        solos_select18 = False
                        solos_select19 = False
                        solos_select20 = False
                        solos_select21 = False
                        solos_select22 = False
                        solos_select23 = False
                        solos_select24 = False
                        solos_select25 = False
                        diametro_select = False
                    else:
                        NSPT25_select = False
                    if rec_solos.collidepoint(mouse_pos):
                        solos_select = not solos_select
                    else:
                        if solos_select:
                            for i, opcao in enumerate(solos):
                                rec_opcao = pygame.Rect(rec_solos.x, rec_solos.y + (i-scroll_position+1) * rec_solos.height, rec_solos.width, rec_solos.height)
                                if rec_opcao.collidepoint(mouse_pos):
                                    solo = opcao
                                    solos_select = False
                                else:
                                    solos_select= False
                    if rec_solos2.collidepoint(mouse_pos):
                        solos_select2 = not solos_select2
                    else:
                        if solos_select2:
                            for i, opcao in enumerate(solos):
                                rec_opcao2 = pygame.Rect(rec_solos2.x, rec_solos2.y + (i-scroll_position+1) * rec_solos2.height, rec_solos2.width, rec_solos2.height)
                                if rec_opcao2.collidepoint(mouse_pos):
                                    solo2 = opcao
                                    solos_select2 = False
                                else:
                                    solos_select2 = False
                    if rec_solos3.collidepoint(mouse_pos):
                        solos_select3 = not solos_select3
                    else:
                        if solos_select3:
                            for i, opcao in enumerate(solos):
                                rec_opcao3 = pygame.Rect(rec_solos3.x, rec_solos3.y + (i-scroll_position+1) * rec_solos3.height, rec_solos3.width, rec_solos3.height)
                                if rec_opcao3.collidepoint(mouse_pos):
                                    solo3 = opcao
                                    solos_select3 = False
                                else:
                                    solos_select3 = False
                    if rec_solos4.collidepoint(mouse_pos):
                        solos_select4 = not solos_select4
                    else:
                        if solos_select4:
                            for i, opcao in enumerate(solos):
                                rec_opcao4 = pygame.Rect(rec_solos4.x, rec_solos4.y + (i-scroll_position+1) * rec_solos4.height, rec_solos4.width, rec_solos4.height)
                                if rec_opcao4.collidepoint(mouse_pos):
                                    solo4 = opcao
                                    solos_select4 = False
                                else:
                                    solos_select4 = False
                    if rec_solos5.collidepoint(mouse_pos):
                        solos_select5 = not solos_select5
                    else:
                        if solos_select5:
                            for i, opcao in enumerate(solos):
                                rec_opcao5 = pygame.Rect(rec_solos5.x, rec_solos5.y + (i-scroll_position+1) * rec_solos5.height, rec_solos5.width, rec_solos5.height)
                                if rec_opcao5.collidepoint(mouse_pos):
                                    solo5 = opcao
                                    solos_select5 = False
                                else:
                                    solos_select5 = False
                    if rec_solos6.collidepoint(mouse_pos):
                        solos_select6 = not solos_select6
                    else:
                        if solos_select6:
                            for i, opcao in enumerate(solos):
                                rec_opcao6 = pygame.Rect(rec_solos6.x, rec_solos6.y + (i-scroll_position+1) * rec_solos6.height, rec_solos6.width, rec_solos6.height)
                                if rec_opcao6.collidepoint(mouse_pos):
                                    solo6 = opcao
                                    solos_select6 = False
                                else:
                                    solos_select6 = False
                    if rec_solos7.collidepoint(mouse_pos):
                        solos_select7 = not solos_select7
                    else:
                        if solos_select7:
                            for i, opcao in enumerate(solos):
                                rec_opcao7 = pygame.Rect(rec_solos7.x, rec_solos7.y + (i-scroll_position+1) * rec_solos7.height, rec_solos7.width, rec_solos7.height)
                                if rec_opcao7.collidepoint(mouse_pos):
                                    solo7 = opcao
                                    solos_select7 = False
                                else:
                                    solos_select7 = False
                    if rec_solos8.collidepoint(mouse_pos):
                        solos_select8 = not solos_select8
                    else:
                        if solos_select8:
                            for i, opcao in enumerate(solos):
                                rec_opcao8 = pygame.Rect(rec_solos8.x, rec_solos8.y + (i-scroll_position+1) * rec_solos8.height, rec_solos8.width, rec_solos8.height)
                                if rec_opcao8.collidepoint(mouse_pos):
                                    solo8 = opcao
                                    solos_select8 = False
                                else:
                                    solos_select8 = False
                    if rec_solos9.collidepoint(mouse_pos):
                        solos_select9 = not solos_select9
                    else:
                        if solos_select9:
                            for i, opcao in enumerate(solos):
                                rec_opcao9 = pygame.Rect(rec_solos9.x, rec_solos9.y + (i-scroll_position+1) * rec_solos9.height, rec_solos9.width, rec_solos9.height)
                                if rec_opcao9.collidepoint(mouse_pos):
                                    solo9 = opcao
                                    solos_select9 = False
                                else:
                                    solos_select9 = False
                    if rec_solos10.collidepoint(mouse_pos):
                        solos_select10 = not solos_select10
                    else:
                        if solos_select10:
                            for i, opcao in enumerate(solos):
                                rec_opcao10 = pygame.Rect(rec_solos10.x, rec_solos10.y + (i-scroll_position+1) * rec_solos10.height, rec_solos10.width, rec_solos10.height)
                                if rec_opcao10.collidepoint(mouse_pos):
                                    solo10 = opcao
                                    solos_select10 = False
                                else:
                                    solos_select10 = False
                    if rec_solos11.collidepoint(mouse_pos):
                        solos_select11 = not solos_select11
                    else:
                        if solos_select11:
                            for i, opcao in enumerate(solos):
                                rec_opcao11 = pygame.Rect(rec_solos11.x, rec_solos11.y + (i-scroll_position+1) * rec_solos11.height, rec_solos11.width, rec_solos11.height)
                                if rec_opcao11.collidepoint(mouse_pos):
                                    solo11 = opcao
                                    solos_select11 = False
                                else:
                                    solos_select11 = False
                    if rec_solos12.collidepoint(mouse_pos):
                        solos_select12 = not solos_select12
                    else:
                        if solos_select12:
                            for i, opcao in enumerate(solos):
                                rec_opcao12 = pygame.Rect(rec_solos12.x, rec_solos12.y + (i-scroll_position+1) * rec_solos12.height, rec_solos12.width, rec_solos12.height)
                                if rec_opcao12.collidepoint(mouse_pos):
                                    solo12 = opcao
                                    solos_select12 = False
                                else:
                                    solos_select12 = False
                    if rec_solos13.collidepoint(mouse_pos):
                        solos_select13 = not solos_select13
                    else:
                        if solos_select13:
                            for i, opcao in enumerate(solos):
                                rec_opcao13 = pygame.Rect(rec_solos13.x, rec_solos13.y + (i-scroll_position+1) * rec_solos13.height, rec_solos13.width, rec_solos13.height)
                                if rec_opcao13.collidepoint(mouse_pos):
                                    solo13 = opcao
                                    solos_select13 = False
                                else:
                                    solos_select13 = False
                    if rec_solos14.collidepoint(mouse_pos):
                        solos_select14 = not solos_select14
                    else:
                        if solos_select14:
                            for i, opcao in enumerate(solos):
                                rec_opcao14 = pygame.Rect(rec_solos14.x, rec_solos14.y + (i-scroll_position+1) * rec_solos14.height, rec_solos14.width, rec_solos14.height)
                                if rec_opcao14.collidepoint(mouse_pos):
                                    solo14 = opcao
                                    solos_select14 = False
                                else:
                                    solos_select14 = False
                    if rec_solos15.collidepoint(mouse_pos):
                        solos_select15 = not solos_select15
                    else:
                        if solos_select15:
                            for i, opcao in enumerate(solos):
                                rec_opcao15 = pygame.Rect(rec_solos15.x, rec_solos15.y + (i-scroll_position+1) * rec_solos15.height, rec_solos15.width, rec_solos15.height)
                                if rec_opcao15.collidepoint(mouse_pos):
                                    solo15 = opcao
                                    solos_select15 = False
                                else:
                                    solos_select15 = False
                    if rec_solos16.collidepoint(mouse_pos):
                        solos_select16 = not solos_select16
                    else:
                        if solos_select16:
                            for i, opcao in enumerate(solos):
                                rec_opcao16 = pygame.Rect(rec_solos16.x, rec_solos16.y + (i-scroll_position+1) * rec_solos16.height, rec_solos16.width, rec_solos16.height)
                                if rec_opcao16.collidepoint(mouse_pos):
                                    solo16 = opcao
                                    solos_select16 = False
                                else:
                                    solos_select16 = False
                    if rec_solos17.collidepoint(mouse_pos):
                        solos_select17 = not solos_select17
                    else:
                        if solos_select17:
                            for i, opcao in enumerate(solos):
                                rec_opcao17 = pygame.Rect(rec_solos17.x, rec_solos17.y + (i-scroll_position+1) * rec_solos17.height, rec_solos17.width, rec_solos17.height)
                                if rec_opcao17.collidepoint(mouse_pos):
                                    solo17 = opcao
                                    solos_select17 = False
                                else:
                                    solos_select17 = False
                    if rec_solos18.collidepoint(mouse_pos):
                        solos_select18 = not solos_select18
                    else:
                        if solos_select18:
                            for i, opcao in enumerate(solos):
                                rec_opcao18 = pygame.Rect(rec_solos18.x, rec_solos18.y + (i-scroll_position+1) * rec_solos18.height, rec_solos18.width, rec_solos18.height)
                                if rec_opcao18.collidepoint(mouse_pos):
                                    solo18 = opcao
                                    solos_select18 = False
                                else:
                                    solos_select18 = False
                    if rec_solos19.collidepoint(mouse_pos):
                        solos_select19 = not solos_select19
                    else:
                        if solos_select19:
                            for i, opcao in enumerate(solos):
                                rec_opcao19 = pygame.Rect(rec_solos19.x, rec_solos19.y + (i-scroll_position+1) * rec_solos19.height, rec_solos19.width, rec_solos19.height)
                                if rec_opcao19.collidepoint(mouse_pos):
                                    solo19 = opcao
                                    solos_select19 = False
                                else:
                                    solos_select19 = False
                    if rec_solos20.collidepoint(mouse_pos):
                        solos_select20 = not solos_select20
                    else:
                        if solos_select20:
                            for i, opcao in enumerate(solos):
                                rec_opcao20 = pygame.Rect(rec_solos20.x, rec_solos20.y + (i-scroll_position+1) * rec_solos20.height, rec_solos20.width, rec_solos20.height)
                                if rec_opcao20.collidepoint(mouse_pos):
                                    solo20 = opcao
                                    solos_select20 = False
                                else:
                                    solos_select20 = False
                    if rec_solos21.collidepoint(mouse_pos):
                        solos_select21 = not solos_select21
                    else:
                        if solos_select21:
                            for i, opcao in enumerate(solos):
                                rec_opcao21 = pygame.Rect(rec_solos21.x, rec_solos21.y + (i-scroll_position+1) * rec_solos21.height, rec_solos21.width, rec_solos21.height)
                                if rec_opcao21.collidepoint(mouse_pos):
                                    solo21 = opcao
                                    solos_select21 = False
                                else:
                                    solos_select21 = False
                    if rec_solos22.collidepoint(mouse_pos):
                        solos_select22 = not solos_select22
                    else:
                        if solos_select22:
                            for i, opcao in enumerate(solos):
                                rec_opcao22 = pygame.Rect(rec_solos22.x, rec_solos22.y + (i-scroll_position+1) * rec_solos22.height, rec_solos22.width, rec_solos22.height)
                                if rec_opcao22.collidepoint(mouse_pos):
                                    solo22 = opcao
                                    solos_select22 = False
                                else:
                                    solos_select22 = False
                    if rec_solos23.collidepoint(mouse_pos):
                        solos_select23 = not solos_select23
                    else:
                        if solos_select23:
                            for i, opcao in enumerate(solos):
                                rec_opcao23 = pygame.Rect(rec_solos23.x, rec_solos23.y + (i-scroll_position+1) * rec_solos23.height, rec_solos23.width, rec_solos23.height)
                                if rec_opcao23.collidepoint(mouse_pos):
                                    solo23 = opcao
                                    solos_select23 = False
                                else:
                                    solos_select23 = False
                    if rec_solos24.collidepoint(mouse_pos):
                        solos_select24 = not solos_select24
                    else:
                        if solos_select24:
                            for i, opcao in enumerate(solos):
                                rec_opcao24 = pygame.Rect(rec_solos24.x, rec_solos24.y + (i-scroll_position+1) * rec_solos24.height, rec_solos24.width, rec_solos24.height)
                                if rec_opcao24.collidepoint(mouse_pos):
                                    solo24 = opcao
                                    solos_select24 = False
                                else:
                                    solos_select24 = False
                    if rec_solos25.collidepoint(mouse_pos):
                        solos_select25 = not solos_select25
                    else:
                        if solos_select25:
                            for i, opcao in enumerate(solos):
                                rec_opcao25 = pygame.Rect(rec_solos25.x, rec_solos25.y + (i-scroll_position+1) * rec_solos25.height, rec_solos25.width, rec_solos25.height)
                                if rec_opcao25.collidepoint(mouse_pos):
                                    solo25 = opcao
                                    solos_select25 = False
                                else:
                                    solos_select25 = False
            if event.button == 4:

                if perfil_sondagem:

                    if solos_select or solos_select2 or solos_select3 or solos_select4 or solos_select5 or solos_select6 or solos_select7 or solos_select8 or solos_select9 or solos_select10 or solos_select11 or solos_select12 or solos_select13 or solos_select14 or solos_select15 or solos_select16 or solos_select17 or solos_select18 or solos_select19 or solos_select20 or solos_select21 or solos_select22 or solos_select23 or solos_select24 or solos_select25:
                        if scroll_position > 0:
                            scroll_position -= scroll_speed
                    else:
                        if tab_position < 0:
                            tab_position += scroll_speed
                            rec_coluna1.y += (scroll_speed * cell_height)
                            rec_coluna2.y += (scroll_speed * cell_height)
                            rec_coluna3.y += (scroll_speed * cell_height)
                            rec_profundidade.y = rec_coluna1.y + rec_coluna1.height
                            rec_profundidade2.y = rec_profundidade.y + cell_height
                            rec_profundidade3.y = rec_profundidade2.y + cell_height
                            rec_profundidade4.y = rec_profundidade3.y + cell_height
                            rec_profundidade5.y = rec_profundidade4.y + cell_height
                            rec_profundidade6.y = rec_profundidade5.y + cell_height
                            rec_profundidade7.y = rec_profundidade6.y + cell_height
                            rec_profundidade8.y = rec_profundidade7.y + cell_height
                            rec_profundidade9.y = rec_profundidade8.y + cell_height
                            rec_profundidade10.y = rec_profundidade9.y + cell_height
                            rec_profundidade11.y = rec_profundidade10.y + cell_height
                            rec_profundidade12.y = rec_profundidade11.y + cell_height
                            rec_profundidade13.y = rec_profundidade12.y + cell_height
                            rec_profundidade14.y = rec_profundidade13.y + cell_height
                            rec_profundidade15.y = rec_profundidade14.y + cell_height
                            rec_profundidade16.y = rec_profundidade15.y + cell_height
                            rec_profundidade17.y = rec_profundidade16.y + cell_height
                            rec_profundidade18.y = rec_profundidade17.y + cell_height
                            rec_profundidade19.y = rec_profundidade18.y + cell_height
                            rec_profundidade20.y = rec_profundidade19.y + cell_height
                            rec_profundidade21.y = rec_profundidade20.y + cell_height
                            rec_profundidade22.y = rec_profundidade21.y + cell_height
                            rec_profundidade23.y = rec_profundidade22.y + cell_height
                            rec_profundidade24.y = rec_profundidade23.y + cell_height
                            rec_profundidade25.y = rec_profundidade24.y + cell_height
                            rec_NSPT.y = rec_coluna2.y + rec_coluna2.height
                            rec_NSPT2.y = rec_NSPT.y + cell_height
                            rec_NSPT3.y = rec_NSPT2.y + cell_height
                            rec_NSPT4.y = rec_NSPT3.y + cell_height
                            rec_NSPT5.y = rec_NSPT4.y + cell_height
                            rec_NSPT6.y = rec_NSPT5.y + cell_height
                            rec_NSPT7.y = rec_NSPT6.y + cell_height
                            rec_NSPT8.y = rec_NSPT7.y + cell_height
                            rec_NSPT9.y = rec_NSPT8.y + cell_height
                            rec_NSPT10.y = rec_NSPT9.y + cell_height
                            rec_NSPT11.y = rec_NSPT10.y + cell_height
                            rec_NSPT12.y = rec_NSPT11.y + cell_height
                            rec_NSPT13.y = rec_NSPT12.y + cell_height
                            rec_NSPT14.y = rec_NSPT13.y + cell_height
                            rec_NSPT15.y = rec_NSPT14.y + cell_height
                            rec_NSPT16.y = rec_NSPT15.y + cell_height
                            rec_NSPT17.y = rec_NSPT16.y + cell_height
                            rec_NSPT18.y = rec_NSPT17.y + cell_height
                            rec_NSPT19.y = rec_NSPT18.y + cell_height
                            rec_NSPT20.y = rec_NSPT19.y + cell_height
                            rec_NSPT21.y = rec_NSPT20.y + cell_height
                            rec_NSPT22.y = rec_NSPT21.y + cell_height
                            rec_NSPT23.y = rec_NSPT22.y + cell_height
                            rec_NSPT24.y = rec_NSPT23.y + cell_height
                            rec_NSPT25.y = rec_NSPT24.y + cell_height
                            rec_solos.y = rec_coluna3.y + rec_coluna3.height
                            rec_solos2.y = rec_solos.y + cell_height
                            rec_solos3.y = rec_solos2.y + cell_height
                            rec_solos4.y = rec_solos3.y + cell_height
                            rec_solos5.y = rec_solos4.y + cell_height
                            rec_solos6.y = rec_solos5.y + cell_height
                            rec_solos7.y = rec_solos6.y + cell_height
                            rec_solos8.y = rec_solos7.y + cell_height
                            rec_solos9.y = rec_solos8.y + cell_height
                            rec_solos10.y = rec_solos9.y + cell_height
                            rec_solos11.y = rec_solos10.y + cell_height
                            rec_solos12.y = rec_solos11.y + cell_height
                            rec_solos13.y = rec_solos12.y + cell_height
                            rec_solos14.y = rec_solos13.y + cell_height
                            rec_solos15.y = rec_solos14.y + cell_height
                            rec_solos16.y = rec_solos15.y + cell_height
                            rec_solos17.y = rec_solos16.y + cell_height
                            rec_solos18.y = rec_solos17.y + cell_height
                            rec_solos19.y = rec_solos18.y + cell_height
                            rec_solos20.y = rec_solos19.y + cell_height
                            rec_solos21.y = rec_solos20.y + cell_height
                            rec_solos22.y = rec_solos21.y + cell_height
                            rec_solos23.y = rec_solos22.y + cell_height
                            rec_solos24.y = rec_solos23.y + cell_height
                            rec_solos25.y = rec_solos24.y + cell_height

            if event.button == 5:

                if perfil_sondagem:

                    if solos_select or solos_select2 or solos_select3 or solos_select4 or solos_select5 or solos_select6 or solos_select7 or solos_select8 or solos_select9 or solos_select10 or solos_select11 or solos_select12 or solos_select13 or solos_select14 or solos_select15 or solos_select16 or solos_select17 or solos_select18 or solos_select19 or solos_select20 or solos_select21 or solos_select22 or solos_select23 or solos_select24 or solos_select25:
                        if scroll_position + itens_visiveis < len(solos) + 10:
                            scroll_position += scroll_speed
                    else:
                        if count > 10 and (-1 * tab_position) < (count - 8):
                            tab_position -= scroll_speed
                            rec_coluna1.y -= (scroll_speed * cell_height)
                            rec_coluna2.y -= (scroll_speed * cell_height)
                            rec_coluna3.y -= (scroll_speed * cell_height)
                            rec_profundidade.y = rec_coluna1.y + rec_coluna1.height
                            rec_profundidade2.y = rec_profundidade.y + cell_height
                            rec_profundidade3.y = rec_profundidade2.y + cell_height
                            rec_profundidade4.y = rec_profundidade3.y + cell_height
                            rec_profundidade5.y = rec_profundidade4.y + cell_height
                            rec_profundidade6.y = rec_profundidade5.y + cell_height
                            rec_profundidade7.y = rec_profundidade6.y + cell_height
                            rec_profundidade8.y = rec_profundidade7.y + cell_height
                            rec_profundidade9.y = rec_profundidade8.y + cell_height
                            rec_profundidade10.y = rec_profundidade9.y + cell_height
                            rec_profundidade11.y = rec_profundidade10.y + cell_height
                            rec_profundidade12.y = rec_profundidade11.y + cell_height
                            rec_profundidade13.y = rec_profundidade12.y + cell_height
                            rec_profundidade14.y = rec_profundidade13.y + cell_height
                            rec_profundidade15.y = rec_profundidade14.y + cell_height
                            rec_profundidade16.y = rec_profundidade15.y + cell_height
                            rec_profundidade17.y = rec_profundidade16.y + cell_height
                            rec_profundidade18.y = rec_profundidade17.y + cell_height
                            rec_profundidade19.y = rec_profundidade18.y + cell_height
                            rec_profundidade20.y = rec_profundidade19.y + cell_height
                            rec_profundidade21.y = rec_profundidade20.y + cell_height
                            rec_profundidade22.y = rec_profundidade21.y + cell_height
                            rec_profundidade23.y = rec_profundidade22.y + cell_height
                            rec_profundidade24.y = rec_profundidade23.y + cell_height
                            rec_profundidade25.y = rec_profundidade24.y + cell_height
                            rec_NSPT.y = rec_coluna2.y + rec_coluna2.height
                            rec_NSPT2.y = rec_NSPT.y + cell_height
                            rec_NSPT3.y = rec_NSPT2.y + cell_height
                            rec_NSPT4.y = rec_NSPT3.y + cell_height
                            rec_NSPT5.y = rec_NSPT4.y + cell_height
                            rec_NSPT6.y = rec_NSPT5.y + cell_height
                            rec_NSPT7.y = rec_NSPT6.y + cell_height
                            rec_NSPT8.y = rec_NSPT7.y + cell_height
                            rec_NSPT9.y = rec_NSPT8.y + cell_height
                            rec_NSPT10.y = rec_NSPT9.y + cell_height
                            rec_NSPT11.y = rec_NSPT10.y + cell_height
                            rec_NSPT12.y = rec_NSPT11.y + cell_height
                            rec_NSPT13.y = rec_NSPT12.y + cell_height
                            rec_NSPT14.y = rec_NSPT13.y + cell_height
                            rec_NSPT15.y = rec_NSPT14.y + cell_height
                            rec_NSPT16.y = rec_NSPT15.y + cell_height
                            rec_NSPT17.y = rec_NSPT16.y + cell_height
                            rec_NSPT18.y = rec_NSPT17.y + cell_height
                            rec_NSPT19.y = rec_NSPT18.y + cell_height
                            rec_NSPT20.y = rec_NSPT19.y + cell_height
                            rec_NSPT21.y = rec_NSPT20.y + cell_height
                            rec_NSPT22.y = rec_NSPT21.y + cell_height
                            rec_NSPT23.y = rec_NSPT22.y + cell_height
                            rec_NSPT24.y = rec_NSPT23.y + cell_height
                            rec_NSPT25.y = rec_NSPT24.y + cell_height
                            rec_solos.y = rec_coluna3.y + rec_coluna3.height
                            rec_solos2.y = rec_solos.y + cell_height
                            rec_solos3.y = rec_solos2.y + cell_height
                            rec_solos4.y = rec_solos3.y + cell_height
                            rec_solos5.y = rec_solos4.y + cell_height
                            rec_solos6.y = rec_solos5.y + cell_height
                            rec_solos7.y = rec_solos6.y + cell_height
                            rec_solos8.y = rec_solos7.y + cell_height
                            rec_solos9.y = rec_solos8.y + cell_height
                            rec_solos10.y = rec_solos9.y + cell_height
                            rec_solos11.y = rec_solos10.y + cell_height
                            rec_solos12.y = rec_solos11.y + cell_height
                            rec_solos13.y = rec_solos12.y + cell_height
                            rec_solos14.y = rec_solos13.y + cell_height
                            rec_solos15.y = rec_solos14.y + cell_height
                            rec_solos16.y = rec_solos15.y + cell_height
                            rec_solos17.y = rec_solos16.y + cell_height
                            rec_solos18.y = rec_solos17.y + cell_height
                            rec_solos19.y = rec_solos18.y + cell_height
                            rec_solos20.y = rec_solos19.y + cell_height
                            rec_solos21.y = rec_solos20.y + cell_height
                            rec_solos22.y = rec_solos21.y + cell_height
                            rec_solos23.y = rec_solos22.y + cell_height
                            rec_solos24.y = rec_solos23.y + cell_height
                            rec_solos25.y = rec_solos24.y + cell_height

        elif event.type == pygame.MOUSEBUTTONUP:
            if button1_rect.collidepoint(mouse_pos):
                button1_cor = azul
            if button2_rect.collidepoint(mouse_pos):
                button2_cor = azul
            if button3_rect.collidepoint(mouse_pos):
                button3_cor = azul
            if button4_rect.collidepoint(mouse_pos):
                button4_cor = vermelho
            if rec_add.collidepoint(mouse_pos):
                rec_add_color = verde
            if rec_remove.collidepoint(mouse_pos):
                rec_remove_color = verde
            if rec_calcular.collidepoint(mouse_pos):
                rec_calcular_color = verde
            if rec_proximo.collidepoint(mouse_pos):
                rec_proximo_color = cinza_claro
            if rec_anterior.collidepoint(mouse_pos):
                rec_anterior_color = cinza_claro
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                if NSPT_select:
                    NSPT_select = False
                if NSPT2_select:
                    NSPT2_select = False
                if NSPT3_select:
                    NSPT3_select = False
                if NSPT4_select:
                    NSPT4_select = False
                if NSPT5_select:
                    NSPT5_select = False
                if NSPT6_select:
                    NSPT6_select = False
                if NSPT7_select:
                    NSPT7_select = False
                if NSPT8_select:
                    NSPT8_select = False
                if NSPT9_select:
                    NSPT9_select = False
                if NSPT10_select:
                    NSPT10_select = False
                if NSPT11_select:
                    NSPT11_select = False
                if NSPT12_select:
                    NSPT12_select = False
                if NSPT13_select:
                    NSPT13_select = False
                if NSPT14_select:
                    NSPT14_select = False
                if NSPT15_select:
                    NSPT15_select = False
                if NSPT16_select:
                    NSPT16_select = False
                if NSPT17_select:
                    NSPT17_select = False
                if NSPT18_select:
                    NSPT18_select = False
                if NSPT19_select:
                    NSPT19_select = False
                if NSPT20_select:
                    NSPT20_select = False
                if NSPT21_select:
                    NSPT21_select = False
                if NSPT22_select:
                    NSPT22_select = False
                if NSPT23_select:
                    NSPT23_select = False
                if NSPT24_select:
                    NSPT24_select = False
                if NSPT25_select:
                    NSPT25_select = False
                if diametro_select:
                    diametro_select = False
            elif event.key == pygame.K_BACKSPACE:
                if NSPT_select:
                    NSPT = NSPT[:-1]
                if NSPT2_select:
                    NSPT2 = NSPT2[:-1]
                if NSPT3_select:
                    NSPT3 = NSPT3[:-1]
                if NSPT4_select:
                    NSPT4 = NSPT4[:-1]
                if NSPT5_select:
                    NSPT5 = NSPT5[:-1]
                if NSPT6_select:
                    NSPT6 = NSPT6[:-1]
                if NSPT7_select:
                    NSPT7 = NSPT7[:-1]
                if NSPT8_select:
                    NSPT8 = NSPT8[:-1]
                if NSPT9_select:
                    NSPT9 = NSPT9[:-1]
                if NSPT10_select:
                    NSPT10 = NSPT10[:-1]
                if NSPT11_select:
                    NSPT11 = NSPT11[:-1]
                if NSPT12_select:
                    NSPT12 = NSPT12[:-1]
                if NSPT13_select:
                    NSPT13 = NSPT13[:-1]
                if NSPT14_select:
                    NSPT14 = NSPT14[:-1]
                if NSPT15_select:
                    NSPT15 = NSPT15[:-1]
                if NSPT16_select:
                    NSPT16 = NSPT16[:-1]
                if NSPT17_select:
                    NSPT17 = NSPT17[:-1]
                if NSPT18_select:
                    NSPT18 = NSPT18[:-1]
                if NSPT19_select:
                    NSPT19 = NSPT19[:-1]
                if NSPT20_select:
                    NSPT20 = NSPT20[:-1]
                if NSPT21_select:
                    NSPT21 = NSPT21[:-1]
                if NSPT22_select:
                    NSPT22 = NSPT22[:-1]
                if NSPT23_select:
                    NSPT23 = NSPT23[:-1]
                if NSPT24_select:
                    NSPT24 = NSPT24[:-1]
                if NSPT25_select:
                    NSPT25 = NSPT25[:-1]
                if diametro_select:
                    diametro = diametro[:-1]
            elif e_numero(event.unicode):
                if NSPT_select:
                    NSPT += event.unicode
                if NSPT2_select:
                    NSPT2 += event.unicode
                if NSPT3_select:
                    NSPT3 += event.unicode
                if NSPT4_select:
                    NSPT4 += event.unicode
                if NSPT5_select:
                    NSPT5 += event.unicode
                if NSPT6_select:
                    NSPT6 += event.unicode
                if NSPT7_select:
                    NSPT7 += event.unicode
                if NSPT8_select:
                    NSPT8 += event.unicode
                if NSPT9_select:
                    NSPT9 += event.unicode
                if NSPT10_select:
                    NSPT10 += event.unicode
                if NSPT11_select:
                    NSPT11 += event.unicode
                if NSPT12_select:
                    NSPT12 += event.unicode
                if NSPT13_select:
                    NSPT13 += event.unicode
                if NSPT14_select:
                    NSPT14 += event.unicode
                if NSPT15_select:
                    NSPT15 += event.unicode
                if NSPT16_select:
                    NSPT16 += event.unicode
                if NSPT17_select:
                    NSPT17 += event.unicode
                if NSPT18_select:
                    NSPT18 += event.unicode
                if NSPT19_select:
                    NSPT19 += event.unicode
                if NSPT20_select:
                    NSPT20 += event.unicode
                if NSPT21_select:
                    NSPT21 += event.unicode
                if NSPT22_select:
                    NSPT22 += event.unicode
                if NSPT23_select:
                    NSPT23 += event.unicode
                if NSPT24_select:
                    NSPT24 += event.unicode
                if NSPT25_select:
                    NSPT25 += event.unicode
                if diametro_select:
                    diametro += event.unicode

    
    janela.fill(branco) # Cor de fundo
    # Retângulos
    pygame.draw.rect(janela, Menu_cor, Menu_rect)
    pygame.draw.rect(janela, button1_cor, button1_rect)
    pygame.draw.rect(janela, button2_cor, button2_rect)
    pygame.draw.rect(janela, button3_cor, button3_rect)
    pygame.draw.rect(janela, button4_cor, button4_rect)
    # Textos
    # Texto retângulo 1:
    text_button1_surface = fonte.render("Inicio", True, branco)
    text_button1_rect = text_button1_surface.get_rect(center = button1_rect.center)
    janela.blit(text_button1_surface, text_button1_rect)
    # Texto retângulo 2:
    text_button2_surface = fonte.render("Perfil de sondagem", True, branco)
    text_button2_rect = text_button2_surface.get_rect(center = button2_rect.center)
    janela.blit(text_button2_surface, text_button2_rect)
    # Texto retângulo 3:
    text_button3_surface = fonte.render("Calculo", True, branco)
    text_button3_rect = text_button3_surface.get_rect(center = button3_rect.center)
    janela.blit(text_button3_surface, text_button3_rect)
    # Texto retângulo 4:
    text_button4_surface = fonte.render("Novo", True, branco)
    text_button4_rect = text_button4_surface.get_rect(center = button4_rect.center)
    janela.blit(text_button4_surface, text_button4_rect)
    if estaca:
        texto_inicial = fonte.render('Bem vindo ao Estaquinha!', True, preto)
        rec_texto_inicial = pygame.Rect((Menu_rect.width // 2) + ((LARGURA - Menu_rect.width) // 2), 0, LARGURA, 10)
        janela.blit(texto_inicial, rec_texto_inicial)

        texto_tutorial = fonte.render('Ao clicar em Inicio ou Novo, você verá esse tutorial. O botão Novo deletará seu projeto, enquanto o botão Inicio não.', True, preto)
        rec_texto_tutorial = pygame.Rect(Menu_rect.width + button_spacing, rec_texto_inicial.y + rec_texto_inicial.height + button_spacing, LARGURA - Menu_rect.width, 10)
        janela.blit(texto_tutorial, rec_texto_tutorial)

        texto_tutorial2 = fonte.render('Ao clicar em Perfil de Sondagem você será redirecionado a página de preenchimento dos dados de sondagem', True, preto)
        rec_texto_tutorial2 = pygame.Rect(Menu_rect.width + button_spacing, rec_texto_tutorial.y + rec_texto_tutorial.height + button_spacing, LARGURA - Menu_rect.width, 10)
        janela.blit(texto_tutorial2, rec_texto_tutorial2)

        texto_tutorial3 = fonte.render('aonde você definirá o NSPT, a profundidade e o tipo de solo de cada camada.', True, preto)
        rec_texto_tutorial3 = pygame.Rect(Menu_rect.width + button_spacing, rec_texto_tutorial2.y + rec_texto_tutorial2.height + button_spacing, LARGURA - Menu_rect.width, 10)
        janela.blit(texto_tutorial3, rec_texto_tutorial3)

        texto_tutorial4 = fonte.render('E ao clicar em calculo você será redirecinado a página de cálculo, onde poderá definir o método utilizado e os dados de sua estaca.', True, preto)
        rec_texto_tutorial4 = pygame.Rect(Menu_rect.width + button_spacing, rec_texto_tutorial3.y + rec_texto_tutorial3.height + button_spacing, LARGURA - Menu_rect.width, 10)
        janela.blit(texto_tutorial4, rec_texto_tutorial4)

        texto_tutorial5 = fonte.render('Hello from the pygame community. https://www.pygame.org/contribute.html', True, preto)
        rec_texto_tutorial5 = pygame.Rect(Menu_rect.width + button_spacing, ALTURA - 10 - button_spacing, LARGURA - Menu_rect.width, 10)
        janela.blit(texto_tutorial5, rec_texto_tutorial5)

        texto_tutorial6 = fonte.render('Obrigado por usar o Estaquinha', True, preto)
        rec_texto_tutorial6 = pygame.Rect(Menu_rect.width + button_spacing, rec_texto_tutorial5.y - button_spacing - rec_texto_tutorial5.height, LARGURA - Menu_rect.width, 10)
        janela.blit(texto_tutorial6, rec_texto_tutorial6)

    if resultado:
        if count < 1:
            texto_addsondagem = fonte.render('Adicione um perfil de sondagem!', True, vermelho)
            rec_texto_addsondagem = pygame.Rect((LARGURA // 2)-(cell_width // 2), (ALTURA // 3), LARGURA, ALTURA)
            janela.blit(texto_addsondagem, rec_texto_addsondagem)

        if count > 0:

            if metodo_selecionado == 'AOKI & VELLOSO':

                if estaca_selecionado == 'Franki':
                    f1 = 2.5
                
                elif estaca_selecionado == 'Metálica':
                    f1 = 1.75
                
                elif estaca_selecionado == 'Pré-moldada':
                    if diametro == '':
                        f1 = 1
                    else:
                        f1 = 1 + ((int(diametro)/1000)/0.8)
                
                elif estaca_selecionado == 'Escavada':
                    f1 = 3
                
                elif estaca_selecionado is None:
                    f1 = 1
                
                else:
                    f1 = 2
                
                f2 = 2 * f1

                if solo2 == 'Areia':
                    k2 = 1
                    alfa2 = 0.014                
                elif solo2 == 'Areia Siltosa':
                    k2 = 0.8
                    alfa2 = 0.02
                elif solo2 == 'Areia Siltoargilosa':
                    k2 = 0.7
                    alfa2 = 0.024
                elif solo2 == 'Areia Argilosa':
                    k2 = 0.6
                    alfa2 = 0.03
                elif solo2 == 'Areia Argilossiltosa':
                    k2 = 0.5
                    alfa2 = 0.028
                elif solo2 == 'Silte':
                    k2 = 0.4
                    alfa2 = 0.03
                elif solo2 == 'Silte Arenoso':
                    k2 = 0.55
                    alfa2 = 0.022
                elif solo2 == 'Silte Arenoargiloso':
                    k2 = 0.45
                    alfa2 = 0.028
                elif solo2 == 'Silte Argiloso':
                    k2 = 0.23
                    alfa2 = 0.034
                elif solo2 == 'Silte Argiloarenoso':
                    k2 = 0.25
                    alfa2 = 0.03
                elif solo2 == 'Argila':
                    k2 = 0.2
                    alfa2 = 0.06
                elif solo2 == 'Argila Arenosa':
                    k2 = 0.35
                    alfa2 = 0.024
                elif solo2 == 'Argila Arenossiltosa':
                    k2 = 0.3
                    alfa2 = 0.028
                elif solo2 == 'Argila Siltosa':
                    k2 = 0.22
                    alfa2 = 0.04
                elif solo2 == 'Argila Siltoarenosa':
                    k2 = 0.33
                    alfa2 = 0.03
                else:
                    k2 = 0
                    alfa2 = 0
                
                if solo3 == 'Areia':
                    k3 = 1
                    alfa3 = 0.014                
                elif solo3 == 'Areia Siltosa':
                    k3 = 0.8
                    alfa3 = 0.02
                elif solo3 == 'Areia Siltoargilosa':
                    k3 = 0.7
                    alfa3 = 0.024
                elif solo3 == 'Areia Argilosa':
                    k3 = 0.6
                    alfa3 = 0.03
                elif solo3 == 'Areia Argilossiltosa':
                    k3 = 0.5
                    alfa3 = 0.028
                elif solo3 == 'Silte':
                    k3 = 0.4
                    alfa3 = 0.03
                elif solo3 == 'Silte Arenoso':
                    k3 = 0.55
                    alfa3 = 0.022
                elif solo3 == 'Silte Arenoargiloso':
                    k3 = 0.45
                    alfa3 = 0.028
                elif solo3 == 'Silte Argiloso':
                    k3 = 0.23
                    alfa3 = 0.034
                elif solo3 == 'Silte Argiloarenoso':
                    k3 = 0.25
                    alfa3 = 0.03
                elif solo3 == 'Argila':
                    k3 = 0.2
                    alfa3 = 0.06
                elif solo3 == 'Argila Arenosa':
                    k3 = 0.35
                    alfa3 = 0.024
                elif solo3 == 'Argila Arenossiltosa':
                    k3 = 0.3
                    alfa3 = 0.028
                elif solo3 == 'Argila Siltosa':
                    k3 = 0.22
                    alfa3 = 0.04
                elif solo3 == 'Argila Siltoarenosa':
                    k3 = 0.33
                    alfa3 = 0.03
                else:
                    k3 = 0
                    alfa3 = 0
                
                if solo4 == 'Areia':
                    k4 = 1
                    alfa4 = 0.014                
                elif solo4 == 'Areia Siltosa':
                    k4 = 0.8
                    alfa4 = 0.02
                elif solo4 == 'Areia Siltoargilosa':
                    k4 = 0.7
                    alfa4 = 0.024
                elif solo4 == 'Areia Argilosa':
                    k4 = 0.6
                    alfa4 = 0.03
                elif solo4 == 'Areia Argilossiltosa':
                    k4 = 0.5
                    alfa4 = 0.028
                elif solo4 == 'Silte':
                    k4 = 0.4
                    alfa4 = 0.03
                elif solo4 == 'Silte Arenoso':
                    k4 = 0.55
                    alfa4 = 0.022
                elif solo4 == 'Silte Arenoargiloso':
                    k4 = 0.45
                    alfa4 = 0.028
                elif solo4 == 'Silte Argiloso':
                    k4 = 0.23
                    alfa4 = 0.034
                elif solo4 == 'Silte Argiloarenoso':
                    k4 = 0.25
                    alfa4 = 0.03
                elif solo4 == 'Argila':
                    k4 = 0.2
                    alfa4 = 0.06
                elif solo4 == 'Argila Arenosa':
                    k4 = 0.35
                    alfa4 = 0.024
                elif solo4 == 'Argila Arenossiltosa':
                    k4 = 0.3
                    alfa4 = 0.028
                elif solo4 == 'Argila Siltosa':
                    k4 = 0.22
                    alfa4 = 0.04
                elif solo4 == 'Argila Siltoarenosa':
                    k4 = 0.33
                    alfa4 = 0.03
                else:
                    k4 = 0
                    alfa4 = 0
                
                if solo5 == 'Areia':
                    k5 = 1
                    alfa5 = 0.014                
                elif solo5 == 'Areia Siltosa':
                    k5 = 0.8
                    alfa5 = 0.02
                elif solo5 == 'Areia Siltoargilosa':
                    k5 = 0.7
                    alfa5 = 0.024
                elif solo5 == 'Areia Argilosa':
                    k5 = 0.6
                    alfa5 = 0.03
                elif solo5 == 'Areia Argilossiltosa':
                    k5 = 0.5
                    alfa5 = 0.028
                elif solo5 == 'Silte':
                    k5 = 0.4
                    alfa5 = 0.03
                elif solo5 == 'Silte Arenoso':
                    k5 = 0.55
                    alfa5 = 0.022
                elif solo5 == 'Silte Arenoargiloso':
                    k5 = 0.45
                    alfa5 = 0.028
                elif solo5 == 'Silte Argiloso':
                    k5 = 0.23
                    alfa5 = 0.034
                elif solo5 == 'Silte Argiloarenoso':
                    k5 = 0.25
                    alfa5 = 0.03
                elif solo5 == 'Argila':
                    k5 = 0.2
                    alfa5 = 0.06
                elif solo5 == 'Argila Arenosa':
                    k5 = 0.35
                    alfa5 = 0.024
                elif solo5 == 'Argila Arenossiltosa':
                    k5 = 0.3
                    alfa5 = 0.028
                elif solo5 == 'Argila Siltosa':
                    k5 = 0.22
                    alfa5 = 0.04
                elif solo5 == 'Argila Siltoarenosa':
                    k5 = 0.33
                    alfa5 = 0.03
                else:
                    k5 = 0
                    alfa5 = 0

                if solo6 == 'Areia':
                    k6 = 1
                    alfa6 = 0.014                
                elif solo6 == 'Areia Siltosa':
                    k6 = 0.8
                    alfa6 = 0.02
                elif solo6 == 'Areia Siltoargilosa':
                    k6 = 0.7
                    alfa6 = 0.024
                elif solo6 == 'Areia Argilosa':
                    k6 = 0.6
                    alfa6 = 0.03
                elif solo6 == 'Areia Argilossiltosa':
                    k6 = 0.5
                    alfa6 = 0.028
                elif solo6 == 'Silte':
                    k6 = 0.4
                    alfa6 = 0.03
                elif solo6 == 'Silte Arenoso':
                    k6 = 0.55
                    alfa6 = 0.022
                elif solo6 == 'Silte Arenoargiloso':
                    k6 = 0.45
                    alfa6 = 0.028
                elif solo6 == 'Silte Argiloso':
                    k6 = 0.23
                    alfa6 = 0.034
                elif solo6 == 'Silte Argiloarenoso':
                    k6 = 0.25
                    alfa6 = 0.03
                elif solo6 == 'Argila':
                    k6 = 0.2
                    alfa6 = 0.06
                elif solo6 == 'Argila Arenosa':
                    k6 = 0.35
                    alfa6 = 0.024
                elif solo6 == 'Argila Arenossiltosa':
                    k6 = 0.3
                    alfa6 = 0.028
                elif solo6 == 'Argila Siltosa':
                    k6 = 0.22
                    alfa6 = 0.04
                elif solo6 == 'Argila Siltoarenosa':
                    k6 = 0.33
                    alfa6 = 0.03
                else:
                    k6 = 0
                    alfa6 = 0
                
                if solo7 == 'Areia':
                    k7 = 1
                    alfa7 = 0.014                
                elif solo7 == 'Areia Siltosa':
                    k7 = 0.8
                    alfa7 = 0.02
                elif solo7 == 'Areia Siltoargilosa':
                    k7 = 0.7
                    alfa7 = 0.024
                elif solo7 == 'Areia Argilosa':
                    k7 = 0.6
                    alfa7 = 0.03
                elif solo7 == 'Areia Argilossiltosa':
                    k7 = 0.5
                    alfa7 = 0.028
                elif solo7 == 'Silte':
                    k7 = 0.4
                    alfa7 = 0.03
                elif solo7 == 'Silte Arenoso':
                    k7 = 0.55
                    alfa7 = 0.022
                elif solo7 == 'Silte Arenoargiloso':
                    k7 = 0.45
                    alfa7 = 0.028
                elif solo7 == 'Silte Argiloso':
                    k7 = 0.23
                    alfa7 = 0.034
                elif solo7 == 'Silte Argiloarenoso':
                    k7 = 0.25
                    alfa7 = 0.03
                elif solo7 == 'Argila':
                    k7 = 0.2
                    alfa7 = 0.06
                elif solo7 == 'Argila Arenosa':
                    k7 = 0.35
                    alfa7 = 0.024
                elif solo7 == 'Argila Arenossiltosa':
                    k7 = 0.3
                    alfa7 = 0.028
                elif solo7 == 'Argila Siltosa':
                    k7 = 0.22
                    alfa7 = 0.04
                elif solo7 == 'Argila Siltoarenosa':
                    k7 = 0.33
                    alfa7 = 0.03
                else:
                    k7 = 0
                    alfa7 = 0
                
                if solo8 == 'Areia':
                    k8 = 1
                    alfa8 = 0.014                
                elif solo8 == 'Areia Siltosa':
                    k8 = 0.8
                    alfa8 = 0.02
                elif solo8 == 'Areia Siltoargilosa':
                    k8 = 0.7
                    alfa8 = 0.024
                elif solo8 == 'Areia Argilosa':
                    k8 = 0.6
                    alfa8 = 0.03
                elif solo8 == 'Areia Argilossiltosa':
                    k8 = 0.5
                    alfa8 = 0.028
                elif solo8 == 'Silte':
                    k8 = 0.4
                    alfa8 = 0.03
                elif solo8 == 'Silte Arenoso':
                    k8 = 0.55
                    alfa8 = 0.022
                elif solo8 == 'Silte Arenoargiloso':
                    k8 = 0.45
                    alfa8 = 0.028
                elif solo8 == 'Silte Argiloso':
                    k8 = 0.23
                    alfa8 = 0.034
                elif solo8 == 'Silte Argiloarenoso':
                    k8 = 0.25
                    alfa8 = 0.03
                elif solo8 == 'Argila':
                    k8 = 0.2
                    alfa8 = 0.06
                elif solo8 == 'Argila Arenosa':
                    k8 = 0.35
                    alfa8 = 0.024
                elif solo8 == 'Argila Arenossiltosa':
                    k8 = 0.3
                    alfa8 = 0.028
                elif solo8 == 'Argila Siltosa':
                    k8 = 0.22
                    alfa8 = 0.04
                elif solo8 == 'Argila Siltoarenosa':
                    k8 = 0.33
                    alfa8 = 0.03
                else:
                    k8 = 0
                    alfa8 = 0
                
                if solo9 == 'Areia':
                    k9 = 1
                    alfa9 = 0.014                
                elif solo9 == 'Areia Siltosa':
                    k9 = 0.8
                    alfa9 = 0.02
                elif solo9 == 'Areia Siltoargilosa':
                    k9 = 0.7
                    alfa9 = 0.024
                elif solo9 == 'Areia Argilosa':
                    k9 = 0.6
                    alfa9 = 0.03
                elif solo9 == 'Areia Argilossiltosa':
                    k9 = 0.5
                    alfa9 = 0.028
                elif solo9 == 'Silte':
                    k9 = 0.4
                    alfa9 = 0.03
                elif solo9 == 'Silte Arenoso':
                    k9 = 0.55
                    alfa9 = 0.022
                elif solo9 == 'Silte Arenoargiloso':
                    k9 = 0.45
                    alfa9 = 0.028
                elif solo9 == 'Silte Argiloso':
                    k9 = 0.23
                    alfa9 = 0.034
                elif solo9 == 'Silte Argiloarenoso':
                    k9 = 0.25
                    alfa9 = 0.03
                elif solo9 == 'Argila':
                    k9 = 0.2
                    alfa9 = 0.06
                elif solo9 == 'Argila Arenosa':
                    k9 = 0.35
                    alfa9 = 0.024
                elif solo9 == 'Argila Arenossiltosa':
                    k9 = 0.3
                    alfa9 = 0.028
                elif solo9 == 'Argila Siltosa':
                    k9 = 0.22
                    alfa9 = 0.04
                elif solo9 == 'Argila Siltoarenosa':
                    k9 = 0.33
                    alfa9 = 0.03
                else:
                    k9 = 0
                    alfa9 = 0
                
                if solo10 == 'Areia':
                    k10 = 1
                    alfa10 = 0.014                
                elif solo10 == 'Areia Siltosa':
                    k10 = 0.8
                    alfa10 = 0.02
                elif solo10 == 'Areia Siltoargilosa':
                    k10 = 0.7
                    alfa10 = 0.024
                elif solo10 == 'Areia Argilosa':
                    k10 = 0.6
                    alfa10 = 0.03
                elif solo10 == 'Areia Argilossiltosa':
                    k10 = 0.5
                    alfa10 = 0.028
                elif solo10 == 'Silte':
                    k10 = 0.4
                    alfa10 = 0.03
                elif solo10 == 'Silte Arenoso':
                    k10 = 0.55
                    alfa10 = 0.022
                elif solo10 == 'Silte Arenoargiloso':
                    k10 = 0.45
                    alfa10 = 0.028
                elif solo10 == 'Silte Argiloso':
                    k10 = 0.23
                    alfa10 = 0.034
                elif solo10 == 'Silte Argiloarenoso':
                    k10 = 0.25
                    alfa10 = 0.03
                elif solo10 == 'Argila':
                    k10 = 0.2
                    alfa10 = 0.06
                elif solo10 == 'Argila Arenosa':
                    k10 = 0.35
                    alfa10 = 0.024
                elif solo10 == 'Argila Arenossiltosa':
                    k10 = 0.3
                    alfa10 = 0.028
                elif solo10 == 'Argila Siltosa':
                    k10 = 0.22
                    alfa10 = 0.04
                elif solo10 == 'Argila Siltoarenosa':
                    k10 = 0.33
                    alfa10 = 0.03
                else:
                    k10 = 0
                    alfa10 = 0
                
                if solo11 == 'Areia':
                    k11 = 1
                    alfa11 = 0.014                
                elif solo11 == 'Areia Siltosa':
                    k11 = 0.8
                    alfa11 = 0.02
                elif solo11 == 'Areia Siltoargilosa':
                    k11 = 0.7
                    alfa11 = 0.024
                elif solo11 == 'Areia Argilosa':
                    k11 = 0.6
                    alfa11 = 0.03
                elif solo11 == 'Areia Argilossiltosa':
                    k11 = 0.5
                    alfa11 = 0.028
                elif solo11 == 'Silte':
                    k11 = 0.4
                    alfa11 = 0.03
                elif solo11 == 'Silte Arenoso':
                    k11 = 0.55
                    alfa11 = 0.022
                elif solo11 == 'Silte Arenoargiloso':
                    k11 = 0.45
                    alfa11 = 0.028
                elif solo11 == 'Silte Argiloso':
                    k11 = 0.23
                    alfa11 = 0.034
                elif solo11 == 'Silte Argiloarenoso':
                    k11 = 0.25
                    alfa11 = 0.03
                elif solo11 == 'Argila':
                    k11 = 0.2
                    alfa11 = 0.06
                elif solo11 == 'Argila Arenosa':
                    k11 = 0.35
                    alfa11 = 0.024
                elif solo11 == 'Argila Arenossiltosa':
                    k11 = 0.3
                    alfa11 = 0.028
                elif solo11 == 'Argila Siltosa':
                    k11 = 0.22
                    alfa11 = 0.04
                elif solo11 == 'Argila Siltoarenosa':
                    k11 = 0.33
                    alfa11 = 0.03
                else:
                    k11 = 0
                    alfa11 = 0
                
                if solo12 == 'Areia':
                    k12 = 1
                    alfa12 = 0.014                
                elif solo12 == 'Areia Siltosa':
                    k12 = 0.8
                    alfa12 = 0.02
                elif solo12 == 'Areia Siltoargilosa':
                    k12 = 0.7
                    alfa12 = 0.024
                elif solo12 == 'Areia Argilosa':
                    k12 = 0.6
                    alfa12 = 0.03
                elif solo12 == 'Areia Argilossiltosa':
                    k12 = 0.5
                    alfa12 = 0.028
                elif solo12 == 'Silte':
                    k12 = 0.4
                    alfa12 = 0.03
                elif solo12 == 'Silte Arenoso':
                    k12 = 0.55
                    alfa12 = 0.022
                elif solo12 == 'Silte Arenoargiloso':
                    k12 = 0.45
                    alfa12 = 0.028
                elif solo12 == 'Silte Argiloso':
                    k12 = 0.23
                    alfa12 = 0.034
                elif solo12 == 'Silte Argiloarenoso':
                    k12 = 0.25
                    alfa12 = 0.03
                elif solo12 == 'Argila':
                    k12 = 0.2
                    alfa12 = 0.06
                elif solo12 == 'Argila Arenosa':
                    k12 = 0.35
                    alfa12 = 0.024
                elif solo12 == 'Argila Arenossiltosa':
                    k12 = 0.3
                    alfa12 = 0.028
                elif solo12 == 'Argila Siltosa':
                    k12 = 0.22
                    alfa12 = 0.04
                elif solo12 == 'Argila Siltoarenosa':
                    k12 = 0.33
                    alfa12 = 0.03
                else:
                    k12 = 0
                    alfa12 = 0
                
                if solo13 == 'Areia':
                    k13 = 1
                    alfa13 = 0.014                
                elif solo13 == 'Areia Siltosa':
                    k13 = 0.8
                    alfa13 = 0.02
                elif solo13 == 'Areia Siltoargilosa':
                    k13 = 0.7
                    alfa13 = 0.024
                elif solo13 == 'Areia Argilosa':
                    k13 = 0.6
                    alfa13 = 0.03
                elif solo13 == 'Areia Argilossiltosa':
                    k13 = 0.5
                    alfa13 = 0.028
                elif solo13 == 'Silte':
                    k13 = 0.4
                    alfa13 = 0.03
                elif solo13 == 'Silte Arenoso':
                    k13 = 0.55
                    alfa13 = 0.022
                elif solo13 == 'Silte Arenoargiloso':
                    k13 = 0.45
                    alfa13 = 0.028
                elif solo13 == 'Silte Argiloso':
                    k13 = 0.23
                    alfa13 = 0.034
                elif solo13 == 'Silte Argiloarenoso':
                    k13 = 0.25
                    alfa13 = 0.03
                elif solo13 == 'Argila':
                    k13 = 0.2
                    alfa13 = 0.06
                elif solo13 == 'Argila Arenosa':
                    k13 = 0.35
                    alfa13 = 0.024
                elif solo13 == 'Argila Arenossiltosa':
                    k13 = 0.3
                    alfa13 = 0.028
                elif solo13 == 'Argila Siltosa':
                    k13 = 0.22
                    alfa13 = 0.04
                elif solo13 == 'Argila Siltoarenosa':
                    k13 = 0.33
                    alfa13 = 0.03
                else:
                    k13 = 0
                    alfa13 = 0
                
                if solo14 == 'Areia':
                    k14 = 1
                    alfa14 = 0.014                
                elif solo14 == 'Areia Siltosa':
                    k14 = 0.8
                    alfa14 = 0.02
                elif solo14 == 'Areia Siltoargilosa':
                    k14 = 0.7
                    alfa14 = 0.024
                elif solo14 == 'Areia Argilosa':
                    k14 = 0.6
                    alfa14 = 0.03
                elif solo14 == 'Areia Argilossiltosa':
                    k14 = 0.5
                    alfa14 = 0.028
                elif solo14 == 'Silte':
                    k14 = 0.4
                    alfa14 = 0.03
                elif solo14 == 'Silte Arenoso':
                    k14 = 0.55
                    alfa14 = 0.022
                elif solo14 == 'Silte Arenoargiloso':
                    k14 = 0.45
                    alfa14 = 0.028
                elif solo14 == 'Silte Argiloso':
                    k14 = 0.23
                    alfa14 = 0.034
                elif solo14 == 'Silte Argiloarenoso':
                    k14 = 0.25
                    alfa14 = 0.03
                elif solo14 == 'Argila':
                    k14 = 0.2
                    alfa14 = 0.06
                elif solo14 == 'Argila Arenosa':
                    k14 = 0.35
                    alfa14 = 0.024
                elif solo14 == 'Argila Arenossiltosa':
                    k14 = 0.3
                    alfa14 = 0.028
                elif solo14 == 'Argila Siltosa':
                    k14 = 0.22
                    alfa14 = 0.04
                elif solo14 == 'Argila Siltoarenosa':
                    k14 = 0.33
                    alfa14 = 0.03
                else:
                    k14 = 0
                    alfa14 = 0
                
                if solo15 == 'Areia':
                    k15 = 1
                    alfa15 = 0.014                
                elif solo15 == 'Areia Siltosa':
                    k15 = 0.8
                    alfa15 = 0.02
                elif solo15 == 'Areia Siltoargilosa':
                    k15 = 0.7
                    alfa15 = 0.024
                elif solo15 == 'Areia Argilosa':
                    k15 = 0.6
                    alfa15 = 0.03
                elif solo15 == 'Areia Argilossiltosa':
                    k15 = 0.5
                    alfa15 = 0.028
                elif solo15 == 'Silte':
                    k15 = 0.4
                    alfa15 = 0.03
                elif solo15 == 'Silte Arenoso':
                    k15 = 0.55
                    alfa15 = 0.022
                elif solo15 == 'Silte Arenoargiloso':
                    k15 = 0.45
                    alfa15 = 0.028
                elif solo15 == 'Silte Argiloso':
                    k15 = 0.23
                    alfa15 = 0.034
                elif solo15 == 'Silte Argiloarenoso':
                    k15 = 0.25
                    alfa15 = 0.03
                elif solo15 == 'Argila':
                    k15 = 0.2
                    alfa15 = 0.06
                elif solo15 == 'Argila Arenosa':
                    k15 = 0.35
                    alfa15 = 0.024
                elif solo15 == 'Argila Arenossiltosa':
                    k15 = 0.3
                    alfa15 = 0.028
                elif solo15 == 'Argila Siltosa':
                    k15 = 0.22
                    alfa15 = 0.04
                elif solo15 == 'Argila Siltoarenosa':
                    k15 = 0.33
                    alfa15 = 0.03
                else:
                    k15 = 0
                    alfa15 = 0
                
                if solo16 == 'Areia':
                    k16 = 1
                    alfa16 = 0.014                
                elif solo16 == 'Areia Siltosa':
                    k16 = 0.8
                    alfa16 = 0.02
                elif solo16 == 'Areia Siltoargilosa':
                    k16 = 0.7
                    alfa16 = 0.024
                elif solo16 == 'Areia Argilosa':
                    k16 = 0.6
                    alfa16 = 0.03
                elif solo16 == 'Areia Argilossiltosa':
                    k16 = 0.5
                    alfa16 = 0.028
                elif solo16 == 'Silte':
                    k16 = 0.4
                    alfa16 = 0.03
                elif solo16 == 'Silte Arenoso':
                    k16 = 0.55
                    alfa16 = 0.022
                elif solo16 == 'Silte Arenoargiloso':
                    k16 = 0.45
                    alfa16 = 0.028
                elif solo16 == 'Silte Argiloso':
                    k16 = 0.23
                    alfa16 = 0.034
                elif solo16 == 'Silte Argiloarenoso':
                    k16 = 0.25
                    alfa16 = 0.03
                elif solo16 == 'Argila':
                    k16 = 0.2
                    alfa16 = 0.06
                elif solo16 == 'Argila Arenosa':
                    k16 = 0.35
                    alfa16 = 0.024
                elif solo16 == 'Argila Arenossiltosa':
                    k16 = 0.3
                    alfa16 = 0.028
                elif solo16 == 'Argila Siltosa':
                    k16 = 0.22
                    alfa16 = 0.04
                elif solo16 == 'Argila Siltoarenosa':
                    k16 = 0.33
                    alfa16 = 0.03
                else:
                    k16 = 0
                    alfa16 = 0
                
                if solo17 == 'Areia':
                    k17 = 1
                    alfa17 = 0.014                
                elif solo17 == 'Areia Siltosa':
                    k17 = 0.8
                    alfa17 = 0.02
                elif solo17 == 'Areia Siltoargilosa':
                    k17 = 0.7
                    alfa17 = 0.024
                elif solo17 == 'Areia Argilosa':
                    k17 = 0.6
                    alfa17 = 0.03
                elif solo17 == 'Areia Argilossiltosa':
                    k17 = 0.5
                    alfa17 = 0.028
                elif solo17 == 'Silte':
                    k17 = 0.4
                    alfa17 = 0.03
                elif solo17 == 'Silte Arenoso':
                    k17 = 0.55
                    alfa17 = 0.022
                elif solo17 == 'Silte Arenoargiloso':
                    k17 = 0.45
                    alfa17 = 0.028
                elif solo17 == 'Silte Argiloso':
                    k17 = 0.23
                    alfa17 = 0.034
                elif solo17 == 'Silte Argiloarenoso':
                    k17 = 0.25
                    alfa17 = 0.03
                elif solo17 == 'Argila':
                    k17 = 0.2
                    alfa17 = 0.06
                elif solo17 == 'Argila Arenosa':
                    k17 = 0.35
                    alfa17 = 0.024
                elif solo17 == 'Argila Arenossiltosa':
                    k17 = 0.3
                    alfa17 = 0.028
                elif solo17 == 'Argila Siltosa':
                    k17 = 0.22
                    alfa17 = 0.04
                elif solo17 == 'Argila Siltoarenosa':
                    k17 = 0.33
                    alfa17 = 0.03
                else:
                    k17 = 0
                    alfa17 = 0
                
                if solo18 == 'Areia':
                    k18 = 1
                    alfa18 = 0.014                
                elif solo18 == 'Areia Siltosa':
                    k18 = 0.8
                    alfa18 = 0.02
                elif solo18 == 'Areia Siltoargilosa':
                    k18 = 0.7
                    alfa18 = 0.024
                elif solo18 == 'Areia Argilosa':
                    k18 = 0.6
                    alfa18 = 0.03
                elif solo18 == 'Areia Argilossiltosa':
                    k18 = 0.5
                    alfa18 = 0.028
                elif solo18 == 'Silte':
                    k18 = 0.4
                    alfa18 = 0.03
                elif solo18 == 'Silte Arenoso':
                    k18 = 0.55
                    alfa18 = 0.022
                elif solo18 == 'Silte Arenoargiloso':
                    k18 = 0.45
                    alfa18 = 0.028
                elif solo18 == 'Silte Argiloso':
                    k18 = 0.23
                    alfa18 = 0.034
                elif solo18 == 'Silte Argiloarenoso':
                    k18 = 0.25
                    alfa18 = 0.03
                elif solo18 == 'Argila':
                    k18 = 0.2
                    alfa18 = 0.06
                elif solo18 == 'Argila Arenosa':
                    k18 = 0.35
                    alfa18 = 0.024
                elif solo18 == 'Argila Arenossiltosa':
                    k18 = 0.3
                    alfa18 = 0.028
                elif solo18 == 'Argila Siltosa':
                    k18 = 0.22
                    alfa18 = 0.04
                elif solo18 == 'Argila Siltoarenosa':
                    k18 = 0.33
                    alfa18 = 0.03
                else:
                    k18 = 0
                    alfa18 = 0
                
                if solo19 == 'Areia':
                    k19 = 1
                    alfa19 = 0.014                
                elif solo19 == 'Areia Siltosa':
                    k19 = 0.8
                    alfa19 = 0.02
                elif solo19 == 'Areia Siltoargilosa':
                    k19 = 0.7
                    alfa19 = 0.024
                elif solo19 == 'Areia Argilosa':
                    k19 = 0.6
                    alfa19 = 0.03
                elif solo19 == 'Areia Argilossiltosa':
                    k19 = 0.5
                    alfa19 = 0.028
                elif solo19 == 'Silte':
                    k19 = 0.4
                    alfa19 = 0.03
                elif solo19 == 'Silte Arenoso':
                    k19 = 0.55
                    alfa19 = 0.022
                elif solo19 == 'Silte Arenoargiloso':
                    k19 = 0.45
                    alfa19 = 0.028
                elif solo19 == 'Silte Argiloso':
                    k19 = 0.23
                    alfa19 = 0.034
                elif solo19 == 'Silte Argiloarenoso':
                    k19 = 0.25
                    alfa19 = 0.03
                elif solo19 == 'Argila':
                    k19 = 0.2
                    alfa19 = 0.06
                elif solo19 == 'Argila Arenosa':
                    k19 = 0.35
                    alfa19 = 0.024
                elif solo19 == 'Argila Arenossiltosa':
                    k19 = 0.3
                    alfa19 = 0.028
                elif solo19 == 'Argila Siltosa':
                    k19 = 0.22
                    alfa19 = 0.04
                elif solo19 == 'Argila Siltoarenosa':
                    k19 = 0.33
                    alfa19 = 0.03
                else:
                    k19 = 0
                    alfa19 = 0
                
                if solo20 == 'Areia':
                    k20 = 1
                    alfa20 = 0.014                
                elif solo20 == 'Areia Siltosa':
                    k20 = 0.8
                    alfa20 = 0.02
                elif solo20 == 'Areia Siltoargilosa':
                    k20 = 0.7
                    alfa20 = 0.024
                elif solo20 == 'Areia Argilosa':
                    k20 = 0.6
                    alfa20 = 0.03
                elif solo20 == 'Areia Argilossiltosa':
                    k20 = 0.5
                    alfa20 = 0.028
                elif solo20 == 'Silte':
                    k20 = 0.4
                    alfa20 = 0.03
                elif solo20 == 'Silte Arenoso':
                    k20 = 0.55
                    alfa20 = 0.022
                elif solo20 == 'Silte Arenoargiloso':
                    k20 = 0.45
                    alfa20 = 0.028
                elif solo20 == 'Silte Argiloso':
                    k20 = 0.23
                    alfa20 = 0.034
                elif solo20 == 'Silte Argiloarenoso':
                    k20 = 0.25
                    alfa20 = 0.03
                elif solo20 == 'Argila':
                    k20 = 0.2
                    alfa20 = 0.06
                elif solo20 == 'Argila Arenosa':
                    k20 = 0.35
                    alfa20 = 0.024
                elif solo20 == 'Argila Arenossiltosa':
                    k20 = 0.3
                    alfa20 = 0.028
                elif solo20 == 'Argila Siltosa':
                    k20 = 0.22
                    alfa20 = 0.04
                elif solo20 == 'Argila Siltoarenosa':
                    k20 = 0.33
                    alfa20 = 0.03
                else:
                    k20 = 0
                    alfa20 = 0
                
                if solo21 == 'Areia':
                    k21 = 1
                    alfa21 = 0.014                
                elif solo21 == 'Areia Siltosa':
                    k21 = 0.8
                    alfa21 = 0.02
                elif solo21 == 'Areia Siltoargilosa':
                    k21 = 0.7
                    alfa21 = 0.024
                elif solo21 == 'Areia Argilosa':
                    k21 = 0.6
                    alfa21 = 0.03
                elif solo21 == 'Areia Argilossiltosa':
                    k21 = 0.5
                    alfa21 = 0.028
                elif solo21 == 'Silte':
                    k21 = 0.4
                    alfa21 = 0.03
                elif solo21 == 'Silte Arenoso':
                    k21 = 0.55
                    alfa21 = 0.022
                elif solo21 == 'Silte Arenoargiloso':
                    k21 = 0.45
                    alfa21 = 0.028
                elif solo21 == 'Silte Argiloso':
                    k21 = 0.23
                    alfa21 = 0.034
                elif solo21 == 'Silte Argiloarenoso':
                    k21 = 0.25
                    alfa21 = 0.03
                elif solo21 == 'Argila':
                    k21 = 0.2
                    alfa21 = 0.06
                elif solo21 == 'Argila Arenosa':
                    k21 = 0.35
                    alfa21 = 0.024
                elif solo21 == 'Argila Arenossiltosa':
                    k21 = 0.3
                    alfa21 = 0.028
                elif solo21 == 'Argila Siltosa':
                    k21 = 0.22
                    alfa21 = 0.04
                elif solo21 == 'Argila Siltoarenosa':
                    k21 = 0.33
                    alfa21 = 0.03
                else:
                    k21 = 0
                    alfa21 = 0
                
                if solo22 == 'Areia':
                    k22 = 1
                    alfa22 = 0.014                
                elif solo22 == 'Areia Siltosa':
                    k22 = 0.8
                    alfa22 = 0.02
                elif solo22 == 'Areia Siltoargilosa':
                    k22 = 0.7
                    alfa22 = 0.024
                elif solo22 == 'Areia Argilosa':
                    k22 = 0.6
                    alfa22 = 0.03
                elif solo22 == 'Areia Argilossiltosa':
                    k22 = 0.5
                    alfa22 = 0.028
                elif solo22 == 'Silte':
                    k22 = 0.4
                    alfa22 = 0.03
                elif solo22 == 'Silte Arenoso':
                    k22 = 0.55
                    alfa22 = 0.022
                elif solo22 == 'Silte Arenoargiloso':
                    k22 = 0.45
                    alfa22 = 0.028
                elif solo22 == 'Silte Argiloso':
                    k22 = 0.23
                    alfa22 = 0.034
                elif solo22 == 'Silte Argiloarenoso':
                    k22 = 0.25
                    alfa22 = 0.03
                elif solo22 == 'Argila':
                    k22 = 0.2
                    alfa22 = 0.06
                elif solo22 == 'Argila Arenosa':
                    k22 = 0.35
                    alfa22 = 0.024
                elif solo22 == 'Argila Arenossiltosa':
                    k22 = 0.3
                    alfa22 = 0.028
                elif solo22 == 'Argila Siltosa':
                    k22 = 0.22
                    alfa22 = 0.04
                elif solo22 == 'Argila Siltoarenosa':
                    k22 = 0.33
                    alfa22 = 0.03
                else:
                    k22 = 0
                    alfa22 = 0
                
                if solo23 == 'Areia':
                    k23 = 1
                    alfa23 = 0.014                
                elif solo23 == 'Areia Siltosa':
                    k23 = 0.8
                    alfa23 = 0.02
                elif solo23 == 'Areia Siltoargilosa':
                    k23 = 0.7
                    alfa23 = 0.024
                elif solo23 == 'Areia Argilosa':
                    k23 = 0.6
                    alfa23 = 0.03
                elif solo23 == 'Areia Argilossiltosa':
                    k23 = 0.5
                    alfa23 = 0.028
                elif solo23 == 'Silte':
                    k23 = 0.4
                    alfa23 = 0.03
                elif solo23 == 'Silte Arenoso':
                    k23 = 0.55
                    alfa23 = 0.022
                elif solo23 == 'Silte Arenoargiloso':
                    k23 = 0.45
                    alfa23 = 0.028
                elif solo23 == 'Silte Argiloso':
                    k23 = 0.23
                    alfa23 = 0.034
                elif solo23 == 'Silte Argiloarenoso':
                    k23 = 0.25
                    alfa23 = 0.03
                elif solo23 == 'Argila':
                    k23 = 0.2
                    alfa23 = 0.06
                elif solo23 == 'Argila Arenosa':
                    k23 = 0.35
                    alfa23 = 0.024
                elif solo23 == 'Argila Arenossiltosa':
                    k23 = 0.3
                    alfa23 = 0.028
                elif solo23 == 'Argila Siltosa':
                    k23 = 0.22
                    alfa23 = 0.04
                elif solo23 == 'Argila Siltoarenosa':
                    k23 = 0.33
                    alfa23 = 0.03
                else:
                    k23 = 0
                    alfa23 = 0
                
                if solo24 == 'Areia':
                    k24 = 1
                    alfa24 = 0.014                
                elif solo24 == 'Areia Siltosa':
                    k24 = 0.8
                    alfa24 = 0.02
                elif solo24 == 'Areia Siltoargilosa':
                    k24 = 0.7
                    alfa24 = 0.024
                elif solo24 == 'Areia Argilosa':
                    k24 = 0.6
                    alfa24 = 0.03
                elif solo24 == 'Areia Argilossiltosa':
                    k24 = 0.5
                    alfa24 = 0.028
                elif solo24 == 'Silte':
                    k24 = 0.4
                    alfa24 = 0.03
                elif solo24 == 'Silte Arenoso':
                    k24 = 0.55
                    alfa24 = 0.022
                elif solo24 == 'Silte Arenoargiloso':
                    k24 = 0.45
                    alfa24 = 0.028
                elif solo24 == 'Silte Argiloso':
                    k24 = 0.23
                    alfa24 = 0.034
                elif solo24 == 'Silte Argiloarenoso':
                    k24 = 0.25
                    alfa24 = 0.03
                elif solo24 == 'Argila':
                    k24 = 0.2
                    alfa24 = 0.06
                elif solo24 == 'Argila Arenosa':
                    k24 = 0.35
                    alfa24 = 0.024
                elif solo24 == 'Argila Arenossiltosa':
                    k24 = 0.3
                    alfa24 = 0.028
                elif solo24 == 'Argila Siltosa':
                    k24 = 0.22
                    alfa24 = 0.04
                elif solo24 == 'Argila Siltoarenosa':
                    k24 = 0.33
                    alfa24 = 0.03
                else:
                    k24 = 0
                    alfa24 = 0
                
                if solo25 == 'Areia':
                    k25 = 1
                    alfa25 = 0.014                
                elif solo25 == 'Areia Siltosa':
                    k25 = 0.8
                    alfa25 = 0.02
                elif solo25 == 'Areia Siltoargilosa':
                    k25 = 0.7
                    alfa25 = 0.024
                elif solo25 == 'Areia Argilosa':
                    k25 = 0.6
                    alfa25 = 0.03
                elif solo25 == 'Areia Argilossiltosa':
                    k25 = 0.5
                    alfa25 = 0.028
                elif solo25 == 'Silte':
                    k25 = 0.4
                    alfa25 = 0.03
                elif solo25 == 'Silte Arenoso':
                    k25 = 0.55
                    alfa25 = 0.022
                elif solo25 == 'Silte Arenoargiloso':
                    k25 = 0.45
                    alfa25 = 0.028
                elif solo25 == 'Silte Argiloso':
                    k25 = 0.23
                    alfa25 = 0.034
                elif solo25 == 'Silte Argiloarenoso':
                    k25 = 0.25
                    alfa25 = 0.03
                elif solo25 == 'Argila':
                    k25 = 0.2
                    alfa25 = 0.06
                elif solo25 == 'Argila Arenosa':
                    k25 = 0.35
                    alfa25 = 0.024
                elif solo25 == 'Argila Arenossiltosa':
                    k25 = 0.3
                    alfa25 = 0.028
                elif solo25 == 'Argila Siltosa':
                    k25 = 0.22
                    alfa25 = 0.04
                elif solo25 == 'Argila Siltoarenosa':
                    k25 = 0.33
                    alfa25 = 0.03
                else:
                    k25 = 0
                    alfa25 = 0

            if metodo_selecionado == 'DECOURT & QUARESMA':
                if estaca_selecionado == 'Escavada em geral':
                    if solo2 == 'Argila':
                        alfa2 = 0.85
                        beta2 = 0.8
                        c2 = 120
                    elif solo2 == 'Areia':
                        alfa2 = 0.5
                        beta2 = 0.5
                        c2 = 400
                    elif solo2 == 'Silte Argiloso' or solo2 == 'Silte Argiloarenoso' or solo2 == 'Silte' or solo2 == 'Argila Arenossiltosa' or solo2 == 'Argila Siltosa' or solo2 == 'Argila Siltoarenosa':
                        alfa2 = 0.6
                        beta2 = 0.65
                        c2 = 200
                    elif solo2 is None:
                        alfa2 = 0
                        beta2 = 0
                        c2 = 0
                    else:
                        alfa2 = 0.6
                        beta2 = 0.65
                        c2 = 250

                    if solo3 == 'Argila':
                        alfa3 = 0.85
                        beta3 = 0.8
                        c3 = 120
                    elif solo3 == 'Areia':
                        alfa3 = 0.5
                        beta3 = 0.5
                        c3 = 400
                    elif solo3 == 'Silte Argiloso' or solo3 == 'Silte Argiloarenoso' or solo3 == 'Silte' or solo3 == 'Argila Arenossiltosa' or solo3 == 'Argila Siltosa' or solo3 == 'Argila Siltoarenosa':
                        alfa3 = 0.6
                        beta3 = 0.65
                        c3 = 200
                    elif solo3 is None:
                        alfa3 = 0
                        beta3 = 0
                        c3 = 0
                    else:
                        alfa3 = 0.6
                        beta3 = 0.65
                        c3 = 250

                    if solo4 == 'Argila':
                        alfa4 = 0.85
                        beta4 = 0.8
                        c4 = 120
                    elif solo4 == 'Areia':
                        alfa4 = 0.5
                        beta4 = 0.5
                        c4 = 400
                    elif solo4 == 'Silte Argiloso' or solo4 == 'Silte Argiloarenoso' or solo4 == 'Silte' or solo4 == 'Argila Arenossiltosa' or solo4 == 'Argila Siltosa' or solo4 == 'Argila Siltoarenosa':
                        alfa4 = 0.6
                        beta4 = 0.65
                        c4 = 200
                    elif solo4 is None:
                        alfa4 = 0
                        beta4 = 0
                        c4 = 0
                    else:
                        alfa4 = 0.6
                        beta4 = 0.65
                        c4 = 250
                    
                    if solo5 == 'Argila':
                        alfa5 = 0.85
                        beta5 = 0.8
                        c5 = 120
                    elif solo5 == 'Areia':
                        alfa5 = 0.5
                        beta5 = 0.5
                        c5 = 400
                    elif solo5 == 'Silte Argiloso' or solo5 == 'Silte Argiloarenoso' or solo5 == 'Silte' or solo5 == 'Argila Arenossiltosa' or solo5 == 'Argila Siltosa' or solo5 == 'Argila Siltoarenosa':
                        alfa5 = 0.6
                        beta5 = 0.65
                        c5 = 200
                    elif solo5 is None:
                        alfa5 = 0
                        beta5 = 0
                        c5 = 0
                    else:
                        alfa5 = 0.6
                        beta5 = 0.65
                        c5 = 250
                    
                    if solo6 == 'Argila':
                        alfa6 = 0.85
                        beta6 = 0.8
                        c6 = 120
                    elif solo6 == 'Areia':
                        alfa6 = 0.5
                        beta6 = 0.5
                        c6 = 400
                    elif solo6 == 'Silte Argiloso' or solo6 == 'Silte Argiloarenoso' or solo6 == 'Silte' or solo6 == 'Argila Arenossiltosa' or solo6 == 'Argila Siltosa' or solo6 == 'Argila Siltoarenosa':
                        alfa6 = 0.6
                        beta6 = 0.65
                        c6 = 200
                    elif solo6 is None:
                        alfa6 = 0
                        beta6 = 0
                        c6 = 0
                    else:
                        alfa6 = 0.6
                        beta6 = 0.65
                        c6 = 250

                    if solo7 == 'Argila':
                        alfa7 = 0.85
                        beta7 = 0.8
                        c7 = 120
                    elif solo7 == 'Areia':
                        alfa7 = 0.5
                        beta7 = 0.5
                        c7 = 400
                    elif solo7 == 'Silte Argiloso' or solo7 == 'Silte Argiloarenoso' or solo7 == 'Silte' or solo7 == 'Argila Arenossiltosa' or solo7 == 'Argila Siltosa' or solo7 == 'Argila Siltoarenosa':
                        alfa7 = 0.6
                        beta7 = 0.65
                        c7 = 200
                    elif solo7 is None:
                        alfa7 = 0
                        beta7 = 0
                        c7 = 0
                    else:
                        alfa7 = 0.6
                        beta7 = 0.65
                        c7 = 250
                    
                    if solo8 == 'Argila':
                        alfa8 = 0.85
                        beta8 = 0.8
                        c8 = 120
                    elif solo8 == 'Areia':
                        alfa8 = 0.5
                        beta8 = 0.5
                        c8 = 400
                    elif solo8 == 'Silte Argiloso' or solo8 == 'Silte Argiloarenoso' or solo8 == 'Silte' or solo8 == 'Argila Arenossiltosa' or solo8 == 'Argila Siltosa' or solo8 == 'Argila Siltoarenosa':
                        alfa8 = 0.6
                        beta8 = 0.65
                        c8 = 200
                    elif solo8 is None:
                        alfa8 = 0
                        beta8 = 0
                        c8 = 0
                    else:
                        alfa8 = 0.6
                        beta8 = 0.65
                        c8 = 250
                    
                    if solo9 == 'Argila':
                        alfa9 = 0.85
                        beta9 = 0.8
                        c9 = 120
                    elif solo9 == 'Areia':
                        alfa9 = 0.5
                        beta9 = 0.5
                        c9 = 400
                    elif solo9 == 'Silte Argiloso' or solo9 == 'Silte Argiloarenoso' or solo9 == 'Silte' or solo9 == 'Argila Arenossiltosa' or solo9 == 'Argila Siltosa' or solo9 == 'Argila Siltoarenosa':
                        alfa9 = 0.6
                        beta9 = 0.65
                        c9 = 200
                    elif solo9 is None:
                        alfa9 = 0
                        beta9 = 0
                        c9 = 0
                    else:
                        alfa9 = 0.6
                        beta9 = 0.65
                        c9 = 250
                    
                    if solo10 == 'Argila':
                        alfa10 = 0.85
                        beta10 = 0.8
                        c10 = 120
                    elif solo10 == 'Areia':
                        alfa10 = 0.5
                        beta10 = 0.5
                        c10 = 400
                    elif solo10 == 'Silte Argiloso' or solo10 == 'Silte Argiloarenoso' or solo10 == 'Silte' or solo10 == 'Argila Arenossiltosa' or solo10 == 'Argila Siltosa' or solo10 == 'Argila Siltoarenosa':
                        alfa10 = 0.6
                        beta10 = 0.65
                        c10 = 200
                    elif solo10 is None:
                        alfa10 = 0
                        beta10 = 0
                        c10 = 0
                    else:
                        alfa10 = 0.6
                        beta10 = 0.65
                        c10 = 250
                    
                    if solo11 == 'Argila':
                        alfa11 = 0.85
                        beta11 = 0.8
                        c11 = 120
                    elif solo11 == 'Areia':
                        alfa11 = 0.5
                        beta11 = 0.5
                        c11 = 400
                    elif solo11 == 'Silte Argiloso' or solo11 == 'Silte Argiloarenoso' or solo11 == 'Silte' or solo11 == 'Argila Arenossiltosa' or solo11 == 'Argila Siltosa' or solo11 == 'Argila Siltoarenosa':
                        alfa11 = 0.6
                        beta11 = 0.65
                        c11 = 200
                    elif solo11 is None:
                        alfa11 = 0
                        beta11 = 0
                        c11 = 0
                    else:
                        alfa11 = 0.6
                        beta11 = 0.65
                        c11 = 250
                    
                    if solo12 == 'Argila':
                        alfa12 = 0.85
                        beta12 = 0.8
                        c12 = 120
                    elif solo12 == 'Areia':
                        alfa12 = 0.5
                        beta12 = 0.5
                        c12 = 400
                    elif solo12 == 'Silte Argiloso' or solo12 == 'Silte Argiloarenoso' or solo12 == 'Silte' or solo12 == 'Argila Arenossiltosa' or solo12 == 'Argila Siltosa' or solo12 == 'Argila Siltoarenosa':
                        alfa12 = 0.6
                        beta12 = 0.65
                        c12 = 200
                    elif solo12 is None:
                        alfa12 = 0
                        beta12 = 0
                        c12 = 0
                    else:
                        alfa12 = 0.6
                        beta12 = 0.65
                        c12 = 250
                    
                    if solo13 == 'Argila':
                        alfa13 = 0.85
                        beta13 = 0.8
                        c13 = 120
                    elif solo13 == 'Areia':
                        alfa13 = 0.5
                        beta13 = 0.5
                        c13 = 400
                    elif solo13 == 'Silte Argiloso' or solo13 == 'Silte Argiloarenoso' or solo13 == 'Silte' or solo13 == 'Argila Arenossiltosa' or solo13 == 'Argila Siltosa' or solo13 == 'Argila Siltoarenosa':
                        alfa13 = 0.6
                        beta13 = 0.65
                        c13 = 200
                    elif solo13 is None:
                        alfa13 = 0
                        beta13 = 0
                        c13 = 0
                    else:
                        alfa13 = 0.6
                        beta13 = 0.65
                        c13 = 250
                    
                    if solo14 == 'Argila':
                        alfa14 = 0.85
                        beta14 = 0.8
                        c14 = 120
                    elif solo14 == 'Areia':
                        alfa14 = 0.5
                        beta14 = 0.5
                        c14 = 400
                    elif solo14 == 'Silte Argiloso' or solo14 == 'Silte Argiloarenoso' or solo14 == 'Silte' or solo14 == 'Argila Arenossiltosa' or solo14 == 'Argila Siltosa' or solo14 == 'Argila Siltoarenosa':
                        alfa14 = 0.6
                        beta14 = 0.65
                        c14 = 200
                    elif solo14 is None:
                        alfa14 = 0
                        beta14 = 0
                        c14 = 0
                    else:
                        alfa14 = 0.6
                        beta14 = 0.65
                        c14 = 250
                    
                    if solo15 == 'Argila':
                        alfa15 = 0.85
                        beta15 = 0.8
                        c15 = 120
                    elif solo15 == 'Areia':
                        alfa15 = 0.5
                        beta15 = 0.5
                        c15 = 400
                    elif solo15 == 'Silte Argiloso' or solo15 == 'Silte Argiloarenoso' or solo15 == 'Silte' or solo15 == 'Argila Arenossiltosa' or solo15 == 'Argila Siltosa' or solo15 == 'Argila Siltoarenosa':
                        alfa15 = 0.6
                        beta15 = 0.65
                        c15 = 200
                    elif solo15 is None:
                        alfa15 = 0
                        beta15 = 0
                        c15 = 0
                    else:
                        alfa15 = 0.6
                        beta15 = 0.65
                        c15 = 250
                    
                    if solo16 == 'Argila':
                        alfa16 = 0.85
                        beta16 = 0.8
                        c16 = 120
                    elif solo16 == 'Areia':
                        alfa16 = 0.5
                        beta16 = 0.5
                        c16 = 400
                    elif solo16 == 'Silte Argiloso' or solo16 == 'Silte Argiloarenoso' or solo16 == 'Silte' or solo16 == 'Argila Arenossiltosa' or solo16 == 'Argila Siltosa' or solo16 == 'Argila Siltoarenosa':
                        alfa16 = 0.6
                        beta16 = 0.65
                        c16 = 200
                    elif solo16 is None:
                        alfa16 = 0
                        beta16 = 0
                        c16 = 0
                    else:
                        alfa16 = 0.6
                        beta16 = 0.65
                        c16 = 250
                    
                    if solo17 == 'Argila':
                        alfa17 = 0.85
                        beta17 = 0.8
                        c17 = 120
                    elif solo17 == 'Areia':
                        alfa17 = 0.5
                        beta17 = 0.5
                        c17 = 400
                    elif solo17 == 'Silte Argiloso' or solo17 == 'Silte Argiloarenoso' or solo17 == 'Silte' or solo17 == 'Argila Arenossiltosa' or solo17 == 'Argila Siltosa' or solo17 == 'Argila Siltoarenosa':
                        alfa17 = 0.6
                        beta17 = 0.65
                        c17 = 200
                    elif solo17 is None:
                        alfa17 = 0
                        beta17 = 0
                        c17 = 0
                    else:
                        alfa17 = 0.6
                        beta17 = 0.65
                        c17 = 250
                    
                    if solo18 == 'Argila':
                        alfa18 = 0.85
                        beta18 = 0.8
                        c18 = 120
                    elif solo18 == 'Areia':
                        alfa18 = 0.5
                        beta18 = 0.5
                        c18 = 400
                    elif solo18 == 'Silte Argiloso' or solo18 == 'Silte Argiloarenoso' or solo18 == 'Silte' or solo18 == 'Argila Arenossiltosa' or solo18 == 'Argila Siltosa' or solo18 == 'Argila Siltoarenosa':
                        alfa18 = 0.6
                        beta18 = 0.65
                        c18 = 200
                    elif solo18 is None:
                        alfa18 = 0
                        beta18 = 0
                        c18 = 0
                    else:
                        alfa18 = 0.6
                        beta18 = 0.65
                        c18 = 250
                    
                    if solo19 == 'Argila':
                        alfa19 = 0.85
                        beta19 = 0.8
                        c19 = 120
                    elif solo19 == 'Areia':
                        alfa19 = 0.5
                        beta19 = 0.5
                        c19 = 400
                    elif solo19 == 'Silte Argiloso' or solo19 == 'Silte Argiloarenoso' or solo19 == 'Silte' or solo19 == 'Argila Arenossiltosa' or solo19 == 'Argila Siltosa' or solo19 == 'Argila Siltoarenosa':
                        alfa19 = 0.6
                        beta19 = 0.65
                        c19 = 200
                    elif solo19 is None:
                        alfa19 = 0
                        beta19 = 0
                        c19 = 0
                    else:
                        alfa19 = 0.6
                        beta19 = 0.65
                        c19 = 250
                    
                    if solo20 == 'Argila':
                        alfa20 = 0.85
                        beta20 = 0.8
                        c20 = 120
                    elif solo20 == 'Areia':
                        alfa20 = 0.5
                        beta20 = 0.5
                        c20 = 400
                    elif solo20 == 'Silte Argiloso' or solo20 == 'Silte Argiloarenoso' or solo20 == 'Silte' or solo20 == 'Argila Arenossiltosa' or solo20 == 'Argila Siltosa' or solo20 == 'Argila Siltoarenosa':
                        alfa20 = 0.6
                        beta20 = 0.65
                        c20 = 200
                    elif solo20 is None:
                        alfa20 = 0
                        beta20 = 0
                        c20 = 0
                    else:
                        alfa20 = 0.6
                        beta20 = 0.65
                        c20 = 250
                    
                    if solo21 == 'Argila':
                        alfa21 = 0.85
                        beta21 = 0.8
                        c21 = 120
                    elif solo21 == 'Areia':
                        alfa21 = 0.5
                        beta21 = 0.5
                        c21 = 400
                    elif solo21 == 'Silte Argiloso' or solo21 == 'Silte Argiloarenoso' or solo21 == 'Silte' or solo21 == 'Argila Arenossiltosa' or solo21 == 'Argila Siltosa' or solo21 == 'Argila Siltoarenosa':
                        alfa21 = 0.6
                        beta21 = 0.65
                        c21 = 200
                    elif solo21 is None:
                        alfa21 = 0
                        beta21 = 0
                        c21 = 0
                    else:
                        alfa21 = 0.6
                        beta21 = 0.65
                        c21 = 250
                    
                    if solo22 == 'Argila':
                        alfa22 = 0.85
                        beta22 = 0.8
                        c22 = 120
                    elif solo22 == 'Areia':
                        alfa22 = 0.5
                        beta22 = 0.5
                        c22 = 400
                    elif solo22 == 'Silte Argiloso' or solo22 == 'Silte Argiloarenoso' or solo22 == 'Silte' or solo22 == 'Argila Arenossiltosa' or solo22 == 'Argila Siltosa' or solo22 == 'Argila Siltoarenosa':
                        alfa22 = 0.6
                        beta22 = 0.65
                        c22 = 200
                    elif solo22 is None:
                        alfa22 = 0
                        beta22 = 0
                        c22 = 0
                    else:
                        alfa22 = 0.6
                        beta22 = 0.65
                        c22 = 250
                    
                    if solo23 == 'Argila':
                        alfa23 = 0.85
                        beta23 = 0.8
                        c23 = 120
                    elif solo23 == 'Areia':
                        alfa23 = 0.5
                        beta23 = 0.5
                        c23 = 400
                    elif solo23 == 'Silte Argiloso' or solo23 == 'Silte Argiloarenoso' or solo23 == 'Silte' or solo23 == 'Argila Arenossiltosa' or solo23 == 'Argila Siltosa' or solo23 == 'Argila Siltoarenosa':
                        alfa23 = 0.6
                        beta23 = 0.65
                        c23 = 200
                    elif solo23 is None:
                        alfa23 = 0
                        beta23 = 0
                        c23 = 0
                    else:
                        alfa23 = 0.6
                        beta23 = 0.65
                        c23 = 250
                    
                    if solo24 == 'Argila':
                        alfa24 = 0.85
                        beta24 = 0.8
                        c24 = 120
                    elif solo24 == 'Areia':
                        alfa24 = 0.5
                        beta24 = 0.5
                        c24 = 400
                    elif solo24 == 'Silte Argiloso' or solo24 == 'Silte Argiloarenoso' or solo24 == 'Silte' or solo24 == 'Argila Arenossiltosa' or solo24 == 'Argila Siltosa' or solo24 == 'Argila Siltoarenosa':
                        alfa24 = 0.6
                        beta24 = 0.65
                        c24 = 200
                    elif solo24 is None:
                        alfa24 = 0
                        beta24 = 0
                        c24 = 0
                    else:
                        alfa24 = 0.6
                        beta24 = 0.65
                        c24 = 250
                    
                    if solo25 == 'Argila':
                        alfa25 = 0.85
                        beta25 = 0.8
                        c25 = 120
                    elif solo25 == 'Areia':
                        alfa25 = 0.5
                        beta25 = 0.5
                        c25 = 400
                    elif solo25 == 'Silte Argiloso' or solo25 == 'Silte Argiloarenoso' or solo25 == 'Silte' or solo25 == 'Argila Arenossiltosa' or solo25 == 'Argila Siltosa' or solo25 == 'Argila Siltoarenosa':
                        alfa25 = 0.6
                        beta25 = 0.65
                        c25 = 200
                    elif solo25 is None:
                        alfa25 = 0
                        beta25 = 0
                        c25 = 0
                    else:
                        alfa25 = 0.6
                        beta25 = 0.65
                        c25 = 250

                elif estaca_selecionado == 'Escavada (bentonita)':
                    if solo2 == 'Argila':
                        alfa2 = 0.85
                        beta2 = 0.9
                        c2 = 120
                    elif solo2 == 'Areia':
                        alfa2 = 0.5
                        beta2 = 0.6
                        c2 = 400
                    elif solo2 == 'Silte Argiloso' or solo2 == 'Silte Argiloarenoso' or solo2 == 'Silte' or solo2 == 'Argila Arenossiltosa' or solo2 == 'Argila Siltosa' or solo2 == 'Argila Siltoarenosa':
                        alfa2 = 0.6
                        beta2 = 0.75
                        c2 = 200
                    elif solo2 is None:
                        alfa2 = 0
                        beta2 = 0
                        c2 = 0
                    else:
                        alfa2 = 0.6
                        beta2 = 0.75
                        c2 = 250

                    if solo3 == 'Argila':
                        alfa3 = 0.85
                        beta3 = 0.9
                        c3 = 120
                    elif solo3 == 'Areia':
                        alfa3 = 0.5
                        beta3 = 0.6
                        c3 = 400
                    elif solo3 == 'Silte Argiloso' or solo3 == 'Silte Argiloarenoso' or solo3 == 'Silte' or solo3 == 'Argila Arenossiltosa' or solo3 == 'Argila Siltosa' or solo3 == 'Argila Siltoarenosa':
                        alfa3 = 0.6
                        beta3 = 0.75
                        c3 = 200
                    elif solo3 is None:
                        alfa3 = 0
                        beta3 = 0
                        c3 = 0
                    else:
                        alfa3 = 0.6
                        beta3 = 0.75
                        c3 = 250
                    
                    if solo4 == 'Argila':
                        alfa4 = 0.85
                        beta4 = 0.9
                        c4 = 120
                    elif solo4 == 'Areia':
                        alfa4 = 0.5
                        beta4 = 0.6
                        c4 = 400
                    elif solo4 == 'Silte Argiloso' or solo4 == 'Silte Argiloarenoso' or solo4 == 'Silte' or solo4 == 'Argila Arenossiltosa' or solo4 == 'Argila Siltosa' or solo4 == 'Argila Siltoarenosa':
                        alfa4 = 0.6
                        beta4 = 0.75
                        c4 = 200
                    elif solo4 is None:
                        alfa4 = 0
                        beta4 = 0
                        c4 = 0
                    else:
                        alfa4 = 0.6
                        beta4 = 0.75
                        c4 = 250
                    
                    if solo5 == 'Argila':
                        alfa5 = 0.85
                        beta5 = 0.9
                        c5 = 120
                    elif solo5 == 'Areia':
                        alfa5 = 0.5
                        beta5 = 0.6
                        c5 = 400
                    elif solo5 == 'Silte Argiloso' or solo5 == 'Silte Argiloarenoso' or solo5 == 'Silte' or solo5 == 'Argila Arenossiltosa' or solo5 == 'Argila Siltosa' or solo5 == 'Argila Siltoarenosa':
                        alfa5 = 0.6
                        beta5 = 0.75
                        c5 = 200
                    elif solo5 is None:
                        alfa5 = 0
                        beta5 = 0
                        c5 = 0
                    else:
                        alfa5 = 0.6
                        beta5 = 0.75
                        c5 = 250
                    
                    if solo6 == 'Argila':
                        alfa6 = 0.85
                        beta6 = 0.9
                        c6 = 120
                    elif solo6 == 'Areia':
                        alfa6 = 0.5
                        beta6 = 0.6
                        c6 = 400
                    elif solo6 == 'Silte Argiloso' or solo6 == 'Silte Argiloarenoso' or solo6 == 'Silte' or solo6 == 'Argila Arenossiltosa' or solo6 == 'Argila Siltosa' or solo6 == 'Argila Siltoarenosa':
                        alfa6 = 0.6
                        beta6 = 0.75
                        c6 = 200
                    elif solo6 is None:
                        alfa6 = 0
                        beta6 = 0
                        c6 = 0
                    else:
                        alfa6 = 0.6
                        beta6 = 0.75
                        c6 = 250

                    if solo7 == 'Argila':
                        alfa7 = 0.85
                        beta7 = 0.9
                        c7 = 120
                    elif solo7 == 'Areia':
                        alfa7 = 0.5
                        beta7 = 0.6
                        c7 = 400
                    elif solo7 == 'Silte Argiloso' or solo7 == 'Silte Argiloarenoso' or solo7 == 'Silte' or solo7 == 'Argila Arenossiltosa' or solo7 == 'Argila Siltosa' or solo7 == 'Argila Siltoarenosa':
                        alfa7 = 0.6
                        beta7 = 0.75
                        c7 = 200
                    elif solo7 is None:
                        alfa7 = 0
                        beta7 = 0
                        c7 = 0
                    else:
                        alfa7 = 0.6
                        beta7 = 0.75
                        c7 = 250
                    
                    if solo8 == 'Argila':
                        alfa8 = 0.85
                        beta8 = 0.9
                        c8 = 120
                    elif solo8 == 'Areia':
                        alfa8 = 0.5
                        beta8 = 0.6
                        c8 = 400
                    elif solo8 == 'Silte Argiloso' or solo8 == 'Silte Argiloarenoso' or solo8 == 'Silte' or solo8 == 'Argila Arenossiltosa' or solo8 == 'Argila Siltosa' or solo8 == 'Argila Siltoarenosa':
                        alfa8 = 0.6
                        beta8 = 0.75
                        c8 = 200
                    elif solo8 is None:
                        alfa8 = 0
                        beta8 = 0
                        c8 = 0
                    else:
                        alfa8 = 0.6
                        beta8 = 0.75
                        c8 = 250
                    
                    if solo9 == 'Argila':
                        alfa9 = 0.85
                        beta9 = 0.9
                        c9 = 120
                    elif solo9 == 'Areia':
                        alfa9 = 0.5
                        beta9 = 0.6
                        c9 = 400
                    elif solo9 == 'Silte Argiloso' or solo9 == 'Silte Argiloarenoso' or solo9 == 'Silte' or solo9 == 'Argila Arenossiltosa' or solo9 == 'Argila Siltosa' or solo9 == 'Argila Siltoarenosa':
                        alfa9 = 0.6
                        beta9 = 0.75
                        c9 = 200
                    elif solo9 is None:
                        alfa9 = 0
                        beta9 = 0
                        c9 = 0
                    else:
                        alfa9 = 0.6
                        beta9 = 0.75
                        c9 = 250

                    if solo10 == 'Argila':
                        alfa10 = 0.85
                        beta10 = 0.9
                        c10 = 120
                    elif solo10 == 'Areia':
                        alfa10 = 0.5
                        beta10 = 0.6
                        c10 = 400
                    elif solo10 == 'Silte Argiloso' or solo10 == 'Silte Argiloarenoso' or solo10 == 'Silte' or solo10 == 'Argila Arenossiltosa' or solo10 == 'Argila Siltosa' or solo10 == 'Argila Siltoarenosa':
                        alfa10 = 0.6
                        beta10 = 0.75
                        c10 = 200
                    elif solo10 is None:
                        alfa10 = 0
                        beta10 = 0
                        c10 = 0
                    else:
                        alfa10 = 0.6
                        beta10 = 0.75
                        c10 = 250
                    
                    if solo11 == 'Argila':
                        alfa11 = 0.85
                        beta11 = 0.9
                        c11 = 120
                    elif solo11 == 'Areia':
                        alfa11 = 0.5
                        beta11 = 0.6
                        c11 = 400
                    elif solo11 == 'Silte Argiloso' or solo11 == 'Silte Argiloarenoso' or solo11 == 'Silte' or solo11 == 'Argila Arenossiltosa' or solo11 == 'Argila Siltosa' or solo11 == 'Argila Siltoarenosa':
                        alfa11 = 0.6
                        beta11 = 0.75
                        c11 = 200
                    elif solo11 is None:
                        alfa11 = 0
                        beta11 = 0
                        c11 = 0
                    else:
                        alfa11 = 0.6
                        beta11 = 0.75
                        c11 = 250
                    
                    if solo12 == 'Argila':
                        alfa12 = 0.85
                        beta12 = 0.9
                        c12 = 120
                    elif solo12 == 'Areia':
                        alfa12 = 0.5
                        beta12 = 0.6
                        c12 = 400
                    elif solo12 == 'Silte Argiloso' or solo12 == 'Silte Argiloarenoso' or solo12 == 'Silte' or solo12 == 'Argila Arenossiltosa' or solo12 == 'Argila Siltosa' or solo12 == 'Argila Siltoarenosa':
                        alfa12 = 0.6
                        beta12 = 0.75
                        c12 = 200
                    elif solo12 is None:
                        alfa12 = 0
                        beta12 = 0
                        c12 = 0
                    else:
                        alfa12 = 0.6
                        beta12 = 0.75
                        c12 = 250
                    
                    if solo13 == 'Argila':
                        alfa13 = 0.85
                        beta13 = 0.9
                        c13 = 120
                    elif solo13 == 'Areia':
                        alfa13 = 0.5
                        beta13 = 0.6
                        c13 = 400
                    elif solo13 == 'Silte Argiloso' or solo13 == 'Silte Argiloarenoso' or solo13 == 'Silte' or solo13 == 'Argila Arenossiltosa' or solo13 == 'Argila Siltosa' or solo13 == 'Argila Siltoarenosa':
                        alfa13 = 0.6
                        beta13 = 0.75
                        c13 = 200
                    elif solo13 is None:
                        alfa13 = 0
                        beta13 = 0
                        c13 = 0
                    else:
                        alfa13 = 0.6
                        beta13 = 0.75
                        c13 = 250
                    
                    if solo14 == 'Argila':
                        alfa14 = 0.85
                        beta14 = 0.9
                        c14 = 120
                    elif solo14 == 'Areia':
                        alfa14 = 0.5
                        beta14 = 0.6
                        c14 = 400
                    elif solo14 == 'Silte Argiloso' or solo14 == 'Silte Argiloarenoso' or solo14 == 'Silte' or solo14 == 'Argila Arenossiltosa' or solo14 == 'Argila Siltosa' or solo14 == 'Argila Siltoarenosa':
                        alfa14 = 0.6
                        beta14 = 0.75
                        c14 = 200
                    elif solo14 is None:
                        alfa14 = 0
                        beta14 = 0
                        c14 = 0
                    else:
                        alfa14 = 0.6
                        beta14 = 0.75
                        c14 = 250
                    
                    if solo15 == 'Argila':
                        alfa15 = 0.85
                        beta15 = 0.9
                        c15 = 120
                    elif solo15 == 'Areia':
                        alfa15 = 0.5
                        beta15 = 0.6
                        c15 = 400
                    elif solo15 == 'Silte Argiloso' or solo15 == 'Silte Argiloarenoso' or solo15 == 'Silte' or solo15 == 'Argila Arenossiltosa' or solo15 == 'Argila Siltosa' or solo15 == 'Argila Siltoarenosa':
                        alfa15 = 0.6
                        beta15 = 0.75
                        c15 = 200
                    elif solo15 is None:
                        alfa15 = 0
                        beta15 = 0
                        c15 = 0
                    else:
                        alfa15 = 0.6
                        beta15 = 0.75
                        c15 = 250
                    
                    if solo16 == 'Argila':
                        alfa16 = 0.85
                        beta16 = 0.9
                        c16 = 120
                    elif solo16 == 'Areia':
                        alfa16 = 0.5
                        beta16 = 0.6
                        c16 = 400
                    elif solo16 == 'Silte Argiloso' or solo16 == 'Silte Argiloarenoso' or solo16 == 'Silte' or solo16 == 'Argila Arenossiltosa' or solo16 == 'Argila Siltosa' or solo16 == 'Argila Siltoarenosa':
                        alfa16 = 0.6
                        beta16 = 0.75
                        c16 = 200
                    elif solo16 is None:
                        alfa16 = 0
                        beta16 = 0
                        c16 = 0
                    else:
                        alfa16 = 0.6
                        beta16 = 0.75
                        c16 = 250
                    
                    if solo17 == 'Argila':
                        alfa17 = 0.85
                        beta17 = 0.9
                        c17 = 120
                    elif solo17 == 'Areia':
                        alfa17 = 0.5
                        beta17 = 0.6
                        c17 = 400
                    elif solo17 == 'Silte Argiloso' or solo17 == 'Silte Argiloarenoso' or solo17 == 'Silte' or solo17 == 'Argila Arenossiltosa' or solo17 == 'Argila Siltosa' or solo17 == 'Argila Siltoarenosa':
                        alfa17 = 0.6
                        beta17 = 0.75
                        c17 = 200
                    elif solo17 is None:
                        alfa17 = 0
                        beta17 = 0
                        c17 = 0
                    else:
                        alfa17 = 0.6
                        beta17 = 0.75
                        c17 = 250
                    
                    if solo18 == 'Argila':
                        alfa18 = 0.85
                        beta18 = 0.9
                        c18 = 120
                    elif solo18 == 'Areia':
                        alfa18 = 0.5
                        beta18 = 0.6
                        c18 = 400
                    elif solo18 == 'Silte Argiloso' or solo18 == 'Silte Argiloarenoso' or solo18 == 'Silte' or solo18 == 'Argila Arenossiltosa' or solo18 == 'Argila Siltosa' or solo18 == 'Argila Siltoarenosa':
                        alfa18 = 0.6
                        beta18 = 0.75
                        c18 = 200
                    elif solo18 is None:
                        alfa18 = 0
                        beta18 = 0
                        c18 = 0
                    else:
                        alfa18 = 0.6
                        beta18 = 0.75
                        c18 = 250
                    
                    if solo19 == 'Argila':
                        alfa19 = 0.85
                        beta19 = 0.9
                        c19 = 120
                    elif solo19 == 'Areia':
                        alfa19 = 0.5
                        beta19 = 0.6
                        c19 = 400
                    elif solo19 == 'Silte Argiloso' or solo19 == 'Silte Argiloarenoso' or solo19 == 'Silte' or solo19 == 'Argila Arenossiltosa' or solo19 == 'Argila Siltosa' or solo19 == 'Argila Siltoarenosa':
                        alfa19 = 0.6
                        beta19 = 0.75
                        c19 = 200
                    elif solo19 is None:
                        alfa19 = 0
                        beta19 = 0
                        c19 = 0
                    else:
                        alfa19 = 0.6
                        beta19 = 0.75
                        c19 = 250
                    
                    if solo20 == 'Argila':
                        alfa20 = 0.85
                        beta20 = 0.9
                        c20 = 120
                    elif solo20 == 'Areia':
                        alfa20 = 0.5
                        beta20 = 0.6
                        c20 = 400
                    elif solo20 == 'Silte Argiloso' or solo20 == 'Silte Argiloarenoso' or solo20 == 'Silte' or solo20 == 'Argila Arenossiltosa' or solo20 == 'Argila Siltosa' or solo20 == 'Argila Siltoarenosa':
                        alfa20 = 0.6
                        beta20 = 0.75
                        c20 = 200
                    elif solo20 is None:
                        alfa20 = 0
                        beta20 = 0
                        c20 = 0
                    else:
                        alfa20 = 0.6
                        beta20 = 0.75
                        c20 = 250
                    
                    if solo21 == 'Argila':
                        alfa21 = 0.85
                        beta21 = 0.9
                        c21 = 120
                    elif solo21 == 'Areia':
                        alfa21 = 0.5
                        beta21 = 0.6
                        c21 = 400
                    elif solo21 == 'Silte Argiloso' or solo21 == 'Silte Argiloarenoso' or solo21 == 'Silte' or solo21 == 'Argila Arenossiltosa' or solo21 == 'Argila Siltosa' or solo21 == 'Argila Siltoarenosa':
                        alfa21 = 0.6
                        beta21 = 0.75
                        c21 = 200
                    elif solo21 is None:
                        alfa21 = 0
                        beta21 = 0
                        c21 = 0
                    else:
                        alfa21 = 0.6
                        beta21 = 0.75
                        c21 = 250
                    
                    if solo22 == 'Argila':
                        alfa22 = 0.85
                        beta22 = 0.9
                        c22 = 120
                    elif solo22 == 'Areia':
                        alfa22 = 0.5
                        beta22 = 0.6
                        c22 = 400
                    elif solo22 == 'Silte Argiloso' or solo22 == 'Silte Argiloarenoso' or solo22 == 'Silte' or solo22 == 'Argila Arenossiltosa' or solo22 == 'Argila Siltosa' or solo22 == 'Argila Siltoarenosa':
                        alfa22 = 0.6
                        beta22 = 0.75
                        c22 = 200
                    elif solo22 is None:
                        alfa22 = 0
                        beta22 = 0
                        c22 = 0
                    else:
                        alfa22 = 0.6
                        beta22 = 0.75
                        c22 = 250
                    
                    if solo23 == 'Argila':
                        alfa23 = 0.85
                        beta23 = 0.9
                        c23 = 120
                    elif solo23 == 'Areia':
                        alfa23 = 0.5
                        beta23 = 0.6
                        c23 = 400
                    elif solo23 == 'Silte Argiloso' or solo23 == 'Silte Argiloarenoso' or solo23 == 'Silte' or solo23 == 'Argila Arenossiltosa' or solo23 == 'Argila Siltosa' or solo23 == 'Argila Siltoarenosa':
                        alfa23 = 0.6
                        beta23 = 0.75
                        c23 = 200
                    elif solo23 is None:
                        alfa23 = 0
                        beta23 = 0
                        c23 = 0
                    else:
                        alfa23 = 0.6
                        beta23 = 0.75
                        c23 = 250
                    
                    if solo24 == 'Argila':
                        alfa24 = 0.85
                        beta24 = 0.9
                        c24 = 120
                    elif solo24 == 'Areia':
                        alfa24 = 0.5
                        beta24 = 0.6
                        c24 = 400
                    elif solo24 == 'Silte Argiloso' or solo24 == 'Silte Argiloarenoso' or solo24 == 'Silte' or solo24 == 'Argila Arenossiltosa' or solo24 == 'Argila Siltosa' or solo24 == 'Argila Siltoarenosa':
                        alfa24 = 0.6
                        beta24 = 0.75
                        c24 = 200
                    elif solo24 is None:
                        alfa24 = 0
                        beta24 = 0
                        c24 = 0
                    else:
                        alfa24 = 0.6
                        beta24 = 0.75
                        c24 = 250
                    
                    if solo25 == 'Argila':
                        alfa25 = 0.85
                        beta25 = 0.9
                        c25 = 120
                    elif solo25 == 'Areia':
                        alfa25 = 0.5
                        beta25 = 0.6
                        c25 = 400
                    elif solo25 == 'Silte Argiloso' or solo25 == 'Silte Argiloarenoso' or solo25 == 'Silte' or solo25 == 'Argila Arenossiltosa' or solo25 == 'Argila Siltosa' or solo25 == 'Argila Siltoarenosa':
                        alfa25 = 0.6
                        beta25 = 0.75
                        c25 = 200
                    elif solo25 is None:
                        alfa25 = 0
                        beta25 = 0
                        c25 = 0
                    else:
                        alfa25 = 0.6
                        beta25 = 0.75
                        c25 = 250
                
                elif estaca_selecionado == 'Hélice contínua':

                    if solo2 == 'Argila':
                        alfa2 = 0.3
                        beta2 = 1
                        c2 = 120
                    elif solo2 == 'Areia':
                        alfa2 = 0.3
                        beta2 = 1
                        c2 = 400
                    elif solo2 == 'Silte Argiloso' or solo2 == 'Silte Argiloarenoso' or solo2 == 'Silte' or solo2 == 'Argila Arenossiltosa' or solo2 == 'Argila Siltosa' or solo2 == 'Argila Siltoarenosa':
                        alfa2 = 0.3
                        beta2 = 1
                        c2 = 200
                    elif solo2 is None:
                        alfa2 = 0
                        beta2 = 0
                        c2 = 0
                    else:
                        alfa2 = 0.3
                        beta2 = 1
                        c2 = 250
                    
                    if solo3 == 'Argila':
                        alfa3 = 0.3
                        beta3 = 1
                        c3 = 120
                    elif solo3 == 'Areia':
                        alfa3 = 0.3
                        beta3 = 1
                        c3 = 400
                    elif solo3 == 'Silte Argiloso' or solo3 == 'Silte Argiloarenoso' or solo3 == 'Silte' or solo3 == 'Argila Arenossiltosa' or solo3 == 'Argila Siltosa' or solo3 == 'Argila Siltoarenosa':
                        alfa3 = 0.3
                        beta3 = 1
                        c3 = 200
                    elif solo3 is None:
                        alfa3 = 0
                        beta3 = 0
                        c3 = 0
                    else:
                        alfa3 = 0.3
                        beta3 = 1
                        c3 = 250
                    
                    if solo4 == 'Argila':
                        alfa4 = 0.3
                        beta4 = 1
                        c4 = 120
                    elif solo4 == 'Areia':
                        alfa4 = 0.3
                        beta4 = 1
                        c4 = 400
                    elif solo4 == 'Silte Argiloso' or solo4 == 'Silte Argiloarenoso' or solo4 == 'Silte' or solo4 == 'Argila Arenossiltosa' or solo4 == 'Argila Siltosa' or solo4 == 'Argila Siltoarenosa':
                        alfa4 = 0.3
                        beta4 = 1
                        c4 = 200
                    elif solo4 is None:
                        alfa4 = 0
                        beta4 = 0
                        c4 = 0
                    else:
                        alfa4 = 0.3
                        beta4 = 1
                        c4 = 250
                    
                    if solo5 == 'Argila':
                        alfa5 = 0.3
                        beta5 = 1
                        c5 = 120
                    elif solo5 == 'Areia':
                        alfa5 = 0.3
                        beta5 = 1
                        c5 = 400
                    elif solo5 == 'Silte Argiloso' or solo5 == 'Silte Argiloarenoso' or solo5 == 'Silte' or solo5 == 'Argila Arenossiltosa' or solo5 == 'Argila Siltosa' or solo5 == 'Argila Siltoarenosa':
                        alfa5 = 0.3
                        beta5 = 1
                        c5 = 200
                    elif solo5 is None:
                        alfa5 = 0
                        beta5 = 0
                        c5 = 0
                    else:
                        alfa5 = 0.3
                        beta5 = 1
                        c5 = 250
                    
                    if solo6 == 'Argila':
                        alfa6 = 0.3
                        beta6 = 1
                        c6 = 120
                    elif solo6 == 'Areia':
                        alfa6 = 0.3
                        beta6 = 1
                        c6 = 400
                    elif solo6 == 'Silte Argiloso' or solo6 == 'Silte Argiloarenoso' or solo6 == 'Silte' or solo6 == 'Argila Arenossiltosa' or solo6 == 'Argila Siltosa' or solo6 == 'Argila Siltoarenosa':
                        alfa6 = 0.3
                        beta6 = 1
                        c6 = 200
                    elif solo6 is None:
                        alfa6 = 0
                        beta6 = 0
                        c6 = 0
                    else:
                        alfa6 = 0.3
                        beta6 = 1
                        c6 = 250
                    
                    if solo7 == 'Argila':
                        alfa7 = 0.3
                        beta7 = 1
                        c7 = 120
                    elif solo7 == 'Areia':
                        alfa7 = 0.3
                        beta7 = 1
                        c7 = 400
                    elif solo7 == 'Silte Argiloso' or solo7 == 'Silte Argiloarenoso' or solo7 == 'Silte' or solo7 == 'Argila Arenossiltosa' or solo7 == 'Argila Siltosa' or solo7 == 'Argila Siltoarenosa':
                        alfa7 = 0.3
                        beta7 = 1
                        c7 = 200
                    elif solo7 is None:
                        alfa7 = 0
                        beta7 = 0
                        c7 = 0
                    else:
                        alfa7 = 0.3
                        beta7 = 1
                        c7 = 250
                    
                    if solo8 == 'Argila':
                        alfa8 = 0.3
                        beta8 = 1
                        c8 = 120
                    elif solo8 == 'Areia':
                        alfa8 = 0.3
                        beta8 = 1
                        c8 = 400
                    elif solo8 == 'Silte Argiloso' or solo8 == 'Silte Argiloarenoso' or solo8 == 'Silte' or solo8 == 'Argila Arenossiltosa' or solo8 == 'Argila Siltosa' or solo8 == 'Argila Siltoarenosa':
                        alfa8 = 0.3
                        beta8 = 1
                        c8 = 200
                    elif solo8 is None:
                        alfa8 = 0
                        beta8 = 0
                        c8 = 0
                    else:
                        alfa8 = 0.3
                        beta8 = 1
                        c8 = 250
                    
                    if solo9 == 'Argila':
                        alfa9 = 0.3
                        beta9 = 1
                        c9 = 120
                    elif solo9 == 'Areia':
                        alfa9 = 0.3
                        beta9 = 1
                        c9 = 400
                    elif solo9 == 'Silte Argiloso' or solo9 == 'Silte Argiloarenoso' or solo9 == 'Silte' or solo9 == 'Argila Arenossiltosa' or solo9 == 'Argila Siltosa' or solo9 == 'Argila Siltoarenosa':
                        alfa9 = 0.3
                        beta9 = 1
                        c9 = 200
                    elif solo9 is None:
                        alfa9 = 0
                        beta9 = 0
                        c9 = 0
                    else:
                        alfa9 = 0.3
                        beta9 = 1
                        c9 = 250
                    
                    if solo10 == 'Argila':
                        alfa10 = 0.3
                        beta10 = 1
                        c10 = 120
                    elif solo10 == 'Areia':
                        alfa10 = 0.3
                        beta10 = 1
                        c10 = 400
                    elif solo10 == 'Silte Argiloso' or solo10 == 'Silte Argiloarenoso' or solo10 == 'Silte' or solo10 == 'Argila Arenossiltosa' or solo10 == 'Argila Siltosa' or solo10 == 'Argila Siltoarenosa':
                        alfa10 = 0.3
                        beta10 = 1
                        c10 = 200
                    elif solo10 is None:
                        alfa10 = 0
                        beta10 = 0
                        c10 = 0
                    else:
                        alfa10 = 0.3
                        beta10 = 1
                        c10 = 250
                    
                    if solo11 == 'Argila':
                        alfa11 = 0.3
                        beta11 = 1
                        c11 = 120
                    elif solo11 == 'Areia':
                        alfa11 = 0.3
                        beta11 = 1
                        c11 = 400
                    elif solo11 == 'Silte Argiloso' or solo11 == 'Silte Argiloarenoso' or solo11 == 'Silte' or solo11 == 'Argila Arenossiltosa' or solo11 == 'Argila Siltosa' or solo11 == 'Argila Siltoarenosa':
                        alfa11 = 0.3
                        beta11 = 1
                        c11 = 200
                    elif solo11 is None:
                        alfa11 = 0
                        beta11 = 0
                        c11 = 0
                    else:
                        alfa11 = 0.3
                        beta11 = 1
                        c11 = 250
                    
                    if solo12 == 'Argila':
                        alfa12 = 0.3
                        beta12 = 1
                        c12 = 120
                    elif solo12 == 'Areia':
                        alfa12 = 0.3
                        beta12 = 1
                        c12 = 400
                    elif solo12 == 'Silte Argiloso' or solo12 == 'Silte Argiloarenoso' or solo12 == 'Silte' or solo12 == 'Argila Arenossiltosa' or solo12 == 'Argila Siltosa' or solo12 == 'Argila Siltoarenosa':
                        alfa12 = 0.3
                        beta12 = 1
                        c12 = 200
                    elif solo12 is None:
                        alfa12 = 0
                        beta12 = 0
                        c12 = 0
                    else:
                        alfa12 = 0.3
                        beta12 = 1
                        c12 = 250
                    
                    if solo13 == 'Argila':
                        alfa13 = 0.3
                        beta13 = 1
                        c13 = 120
                    elif solo13 == 'Areia':
                        alfa13 = 0.3
                        beta13 = 1
                        c13 = 400
                    elif solo13 == 'Silte Argiloso' or solo13 == 'Silte Argiloarenoso' or solo13 == 'Silte' or solo13 == 'Argila Arenossiltosa' or solo13 == 'Argila Siltosa' or solo13 == 'Argila Siltoarenosa':
                        alfa13 = 0.3
                        beta13 = 1
                        c13 = 200
                    elif solo13 is None:
                        alfa13 = 0
                        beta13 = 0
                        c13 = 0
                    else:
                        alfa13 = 0.3
                        beta13 = 1
                        c13 = 250
                    
                    if solo14 == 'Argila':
                        alfa14 = 0.3
                        beta14 = 1
                        c14 = 120
                    elif solo14 == 'Areia':
                        alfa14 = 0.3
                        beta14 = 1
                        c14 = 400
                    elif solo14 == 'Silte Argiloso' or solo14 == 'Silte Argiloarenoso' or solo14 == 'Silte' or solo14 == 'Argila Arenossiltosa' or solo14 == 'Argila Siltosa' or solo14 == 'Argila Siltoarenosa':
                        alfa14 = 0.3
                        beta14 = 1
                        c14 = 200
                    elif solo14 is None:
                        alfa14 = 0
                        beta14 = 0
                        c14 = 0
                    else:
                        alfa14 = 0.3
                        beta14 = 1
                        c14 = 250
                    
                    if solo15 == 'Argila':
                        alfa15 = 0.3
                        beta15 = 1
                        c15 = 120
                    elif solo15 == 'Areia':
                        alfa15 = 0.3
                        beta15 = 1
                        c15 = 400
                    elif solo15 == 'Silte Argiloso' or solo15 == 'Silte Argiloarenoso' or solo15 == 'Silte' or solo15 == 'Argila Arenossiltosa' or solo15 == 'Argila Siltosa' or solo15 == 'Argila Siltoarenosa':
                        alfa15 = 0.3
                        beta15 = 1
                        c15 = 200
                    elif solo15 is None:
                        alfa15 = 0
                        beta15 = 0
                        c15 = 0
                    else:
                        alfa15 = 0.3
                        beta15 = 1
                        c15 = 250
                    
                    if solo16 == 'Argila':
                        alfa16 = 0.3
                        beta16 = 1
                        c16 = 120
                    elif solo16 == 'Areia':
                        alfa16 = 0.3
                        beta16 = 1
                        c16 = 400
                    elif solo16 == 'Silte Argiloso' or solo16 == 'Silte Argiloarenoso' or solo16 == 'Silte' or solo16 == 'Argila Arenossiltosa' or solo16 == 'Argila Siltosa' or solo16 == 'Argila Siltoarenosa':
                        alfa16 = 0.3
                        beta16 = 1
                        c16 = 200
                    elif solo16 is None:
                        alfa16 = 0
                        beta16 = 0
                        c16 = 0
                    else:
                        alfa16 = 0.3
                        beta16 = 1
                        c16 = 250
                    
                    if solo17 == 'Argila':
                        alfa17 = 0.3
                        beta17 = 1
                        c17 = 120
                    elif solo17 == 'Areia':
                        alfa17 = 0.3
                        beta17 = 1
                        c17 = 400
                    elif solo17 == 'Silte Argiloso' or solo17 == 'Silte Argiloarenoso' or solo17 == 'Silte' or solo17 == 'Argila Arenossiltosa' or solo17 == 'Argila Siltosa' or solo17 == 'Argila Siltoarenosa':
                        alfa17 = 0.3
                        beta17 = 1
                        c17 = 200
                    elif solo17 is None:
                        alfa17 = 0
                        beta17 = 0
                        c17 = 0
                    else:
                        alfa17 = 0.3
                        beta17 = 1
                        c17 = 250
                    
                    if solo18 == 'Argila':
                        alfa18 = 0.3
                        beta18 = 1
                        c18 = 120
                    elif solo18 == 'Areia':
                        alfa18 = 0.3
                        beta18 = 1
                        c18 = 400
                    elif solo18 == 'Silte Argiloso' or solo18 == 'Silte Argiloarenoso' or solo18 == 'Silte' or solo18 == 'Argila Arenossiltosa' or solo18 == 'Argila Siltosa' or solo18 == 'Argila Siltoarenosa':
                        alfa18 = 0.3
                        beta18 = 1
                        c18 = 200
                    elif solo18 is None:
                        alfa18 = 0
                        beta18 = 0
                        c18 = 0
                    else:
                        alfa18 = 0.3
                        beta18 = 1
                        c18 = 250
                    
                    if solo19 == 'Argila':
                        alfa19 = 0.3
                        beta19 = 1
                        c19 = 120
                    elif solo19 == 'Areia':
                        alfa19 = 0.3
                        beta19 = 1
                        c19 = 400
                    elif solo19 == 'Silte Argiloso' or solo19 == 'Silte Argiloarenoso' or solo19 == 'Silte' or solo19 == 'Argila Arenossiltosa' or solo19 == 'Argila Siltosa' or solo19 == 'Argila Siltoarenosa':
                        alfa19 = 0.3
                        beta19 = 1
                        c19 = 200
                    elif solo19 is None:
                        alfa19 = 0
                        beta19 = 0
                        c19 = 0
                    else:
                        alfa19 = 0.3
                        beta19 = 1
                        c19 = 250
                    
                    if solo20 == 'Argila':
                        alfa20 = 0.3
                        beta20 = 1
                        c20 = 120
                    elif solo20 == 'Areia':
                        alfa20 = 0.3
                        beta20 = 1
                        c20 = 400
                    elif solo20 == 'Silte Argiloso' or solo20 == 'Silte Argiloarenoso' or solo20 == 'Silte' or solo20 == 'Argila Arenossiltosa' or solo20 == 'Argila Siltosa' or solo20 == 'Argila Siltoarenosa':
                        alfa20 = 0.3
                        beta20 = 1
                        c20 = 200
                    elif solo20 is None:
                        alfa20 = 0
                        beta20 = 0
                        c20 = 0
                    else:
                        alfa20 = 0.3
                        beta20 = 1
                        c20 = 250
                    
                    if solo21 == 'Argila':
                        alfa21 = 0.3
                        beta21 = 1
                        c21 = 120
                    elif solo21 == 'Areia':
                        alfa21 = 0.3
                        beta21 = 1
                        c21 = 400
                    elif solo21 == 'Silte Argiloso' or solo21 == 'Silte Argiloarenoso' or solo21 == 'Silte' or solo21 == 'Argila Arenossiltosa' or solo21 == 'Argila Siltosa' or solo21 == 'Argila Siltoarenosa':
                        alfa21 = 0.3
                        beta21 = 1
                        c21 = 200
                    elif solo21 is None:
                        alfa21 = 0
                        beta21 = 0
                        c21 = 0
                    else:
                        alfa21 = 0.3
                        beta21 = 1
                        c21 = 250
                    
                    if solo22 == 'Argila':
                        alfa22 = 0.3
                        beta22 = 1
                        c22 = 120
                    elif solo22 == 'Areia':
                        alfa22 = 0.3
                        beta22 = 1
                        c22 = 400
                    elif solo22 == 'Silte Argiloso' or solo22 == 'Silte Argiloarenoso' or solo22 == 'Silte' or solo22 == 'Argila Arenossiltosa' or solo22 == 'Argila Siltosa' or solo22 == 'Argila Siltoarenosa':
                        alfa22 = 0.3
                        beta22 = 1
                        c22 = 200
                    elif solo22 is None:
                        alfa22 = 0
                        beta22 = 0
                        c22 = 0
                    else:
                        alfa22 = 0.3
                        beta22 = 1
                        c22 = 250
                    
                    if solo23 == 'Argila':
                        alfa23 = 0.3
                        beta23 = 1
                        c23 = 120
                    elif solo23 == 'Areia':
                        alfa23 = 0.3
                        beta23 = 1
                        c23 = 400
                    elif solo23 == 'Silte Argiloso' or solo23 == 'Silte Argiloarenoso' or solo23 == 'Silte' or solo23 == 'Argila Arenossiltosa' or solo23 == 'Argila Siltosa' or solo23 == 'Argila Siltoarenosa':
                        alfa23 = 0.3
                        beta23 = 1
                        c23 = 200
                    elif solo23 is None:
                        alfa23 = 0
                        beta23 = 0
                        c23 = 0
                    else:
                        alfa23 = 0.3
                        beta23 = 1
                        c23 = 250
                    
                    if solo24 == 'Argila':
                        alfa24 = 0.3
                        beta24 = 1
                        c24 = 120
                    elif solo24 == 'Areia':
                        alfa24 = 0.3
                        beta24 = 1
                        c24 = 400
                    elif solo24 == 'Silte Argiloso' or solo24 == 'Silte Argiloarenoso' or solo24 == 'Silte' or solo24 == 'Argila Arenossiltosa' or solo24 == 'Argila Siltosa' or solo24 == 'Argila Siltoarenosa':
                        alfa24 = 0.3
                        beta24 = 1
                        c24 = 200
                    elif solo24 is None:
                        alfa24 = 0
                        beta24 = 0
                        c24 = 0
                    else:
                        alfa24 = 0.3
                        beta24 = 1
                        c24 = 250
                    
                    if solo25 == 'Argila':
                        alfa25 = 0.3
                        beta25 = 1
                        c25 = 120
                    elif solo25 == 'Areia':
                        alfa25 = 0.3
                        beta25 = 1
                        c25 = 400
                    elif solo25 == 'Silte Argiloso' or solo25 == 'Silte Argiloarenoso' or solo25 == 'Silte' or solo25 == 'Argila Arenossiltosa' or solo25 == 'Argila Siltosa' or solo25 == 'Argila Siltoarenosa':
                        alfa25 = 0.3
                        beta25 = 1
                        c25 = 200
                    elif solo25 is None:
                        alfa25 = 0
                        beta25 = 0
                        c25 = 0
                    else:
                        alfa25 = 0.3
                        beta25 = 1
                        c25 = 250

                elif estaca_selecionado == 'Raiz':

                    if solo2 == 'Argila':
                        alfa2 = 0.85
                        beta2 = 1.5
                        c2 = 120
                    elif solo2 == 'Areia':
                        alfa2 = 0.5
                        beta2 = 1.5
                        c2 = 400
                    elif solo2 == 'Silte Argiloso' or solo2 == 'Silte Argiloarenoso' or solo2 == 'Silte' or solo2 == 'Argila Arenossiltosa' or solo2 == 'Argila Siltosa' or solo2 == 'Argila Siltoarenosa':
                        alfa2 = 0.6
                        beta2 = 1.5
                        c2 = 200
                    elif solo2 is None:
                        alfa2 = 0
                        beta2 = 0
                        c2 = 0
                    else:
                        alfa2 = 0.6
                        beta2 = 1.5
                        c2 = 250
                    
                    if solo3 == 'Argila':
                        alfa3 = 0.85
                        beta3 = 1.5
                        c3 = 120
                    elif solo3 == 'Areia':
                        alfa3 = 0.5
                        beta3 = 1.5
                        c3 = 400
                    elif solo3 == 'Silte Argiloso' or solo3 == 'Silte Argiloarenoso' or solo3 == 'Silte' or solo3 == 'Argila Arenossiltosa' or solo3 == 'Argila Siltosa' or solo3 == 'Argila Siltoarenosa':
                        alfa3 = 0.6
                        beta3 = 1.5
                        c3 = 200
                    elif solo3 is None:
                        alfa3 = 0
                        beta3 = 0
                        c3 = 0
                    else:
                        alfa3 = 0.6
                        beta3 = 1.5
                        c3 = 250
                    
                    if solo4 == 'Argila':
                        alfa4 = 0.85
                        beta4 = 1.5
                        c4 = 120
                    elif solo4 == 'Areia':
                        alfa4 = 0.5
                        beta4 = 1.5
                        c4 = 400
                    elif solo4 == 'Silte Argiloso' or solo4 == 'Silte Argiloarenoso' or solo4 == 'Silte' or solo4 == 'Argila Arenossiltosa' or solo4 == 'Argila Siltosa' or solo4 == 'Argila Siltoarenosa':
                        alfa4 = 0.6
                        beta4 = 1.5
                        c4 = 200
                    elif solo4 is None:
                        alfa4 = 0
                        beta4 = 0
                        c4 = 0
                    else:
                        alfa4 = 0.6
                        beta4 = 1.5
                        c4 = 250
                    
                    if solo5 == 'Argila':
                        alfa5 = 0.85
                        beta5 = 1.5
                        c5 = 120
                    elif solo5 == 'Areia':
                        alfa5 = 0.5
                        beta5 = 1.5
                        c5 = 400
                    elif solo5 == 'Silte Argiloso' or solo5 == 'Silte Argiloarenoso' or solo5 == 'Silte' or solo5 == 'Argila Arenossiltosa' or solo5 == 'Argila Siltosa' or solo5 == 'Argila Siltoarenosa':
                        alfa5 = 0.6
                        beta5 = 1.5
                        c5 = 200
                    elif solo5 is None:
                        alfa5 = 0
                        beta5 = 0
                        c5 = 0
                    else:
                        alfa5 = 0.6
                        beta5 = 1.5
                        c5 = 250
                    
                    if solo6 == 'Argila':
                        alfa6 = 0.85
                        beta6 = 1.5
                        c6 = 120
                    elif solo6 == 'Areia':
                        alfa6 = 0.5
                        beta6 = 1.5
                        c6 = 400
                    elif solo6 == 'Silte Argiloso' or solo6 == 'Silte Argiloarenoso' or solo6 == 'Silte' or solo6 == 'Argila Arenossiltosa' or solo6 == 'Argila Siltosa' or solo6 == 'Argila Siltoarenosa':
                        alfa6 = 0.6
                        beta6 = 1.5
                        c6 = 200
                    elif solo6 is None:
                        alfa6 = 0
                        beta6 = 0
                        c6 = 0
                    else:
                        alfa6 = 0.6
                        beta6 = 1.5
                        c6 = 250
                    
                    if solo7 == 'Argila':
                        alfa7 = 0.85
                        beta7 = 1.5
                        c7 = 120
                    elif solo7 == 'Areia':
                        alfa7 = 0.5
                        beta7 = 1.5
                        c7 = 400
                    elif solo7 == 'Silte Argiloso' or solo7 == 'Silte Argiloarenoso' or solo7 == 'Silte' or solo7 == 'Argila Arenossiltosa' or solo7 == 'Argila Siltosa' or solo7 == 'Argila Siltoarenosa':
                        alfa7 = 0.6
                        beta7 = 1.5
                        c7 = 200
                    elif solo7 is None:
                        alfa7 = 0
                        beta7 = 0
                        c7 = 0
                    else:
                        alfa7 = 0.6
                        beta7 = 1.5
                        c7 = 250
                    
                    if solo8 == 'Argila':
                        alfa8 = 0.85
                        beta8 = 1.5
                        c8 = 120
                    elif solo8 == 'Areia':
                        alfa8 = 0.5
                        beta8 = 1.5
                        c8 = 400
                    elif solo8 == 'Silte Argiloso' or solo8 == 'Silte Argiloarenoso' or solo8 == 'Silte' or solo8 == 'Argila Arenossiltosa' or solo8 == 'Argila Siltosa' or solo8 == 'Argila Siltoarenosa':
                        alfa8 = 0.6
                        beta8 = 1.5
                        c8 = 200
                    elif solo8 is None:
                        alfa8 = 0
                        beta8 = 0
                        c8 = 0
                    else:
                        alfa8 = 0.6
                        beta8 = 1.5
                        c8 = 250
                    
                    if solo9 == 'Argila':
                        alfa9 = 0.85
                        beta9 = 1.5
                        c9 = 120
                    elif solo9 == 'Areia':
                        alfa9 = 0.5
                        beta9 = 1.5
                        c9 = 400
                    elif solo9 == 'Silte Argiloso' or solo9 == 'Silte Argiloarenoso' or solo9 == 'Silte' or solo9 == 'Argila Arenossiltosa' or solo9 == 'Argila Siltosa' or solo9 == 'Argila Siltoarenosa':
                        alfa9 = 0.6
                        beta9 = 1.5
                        c9 = 200
                    elif solo9 is None:
                        alfa9 = 0
                        beta9 = 0
                        c9 = 0
                    else:
                        alfa9 = 0.6
                        beta9 = 1.5
                        c9 = 250
                    
                    if solo10 == 'Argila':
                        alfa10 = 0.85
                        beta10 = 1.5
                        c10 = 120
                    elif solo10 == 'Areia':
                        alfa10 = 0.5
                        beta10 = 1.5
                        c10 = 400
                    elif solo10 == 'Silte Argiloso' or solo10 == 'Silte Argiloarenoso' or solo10 == 'Silte' or solo10 == 'Argila Arenossiltosa' or solo10 == 'Argila Siltosa' or solo10 == 'Argila Siltoarenosa':
                        alfa10 = 0.6
                        beta10 = 1.5
                        c10 = 200
                    elif solo10 is None:
                        alfa10 = 0
                        beta10 = 0
                        c10 = 0
                    else:
                        alfa10 = 0.6
                        beta10 = 1.5
                        c10 = 250
                    
                    if solo11 == 'Argila':
                        alfa11 = 0.85
                        beta11 = 1.5
                        c11 = 120
                    elif solo11 == 'Areia':
                        alfa11 = 0.5
                        beta11 = 1.5
                        c11 = 400
                    elif solo11 == 'Silte Argiloso' or solo11 == 'Silte Argiloarenoso' or solo11 == 'Silte' or solo11 == 'Argila Arenossiltosa' or solo11 == 'Argila Siltosa' or solo11 == 'Argila Siltoarenosa':
                        alfa11 = 0.6
                        beta11 = 1.5
                        c11 = 200
                    elif solo11 is None:
                        alfa11 = 0
                        beta11 = 0
                        c11 = 0
                    else:
                        alfa11 = 0.6
                        beta11 = 1.5
                        c11 = 250
                    
                    if solo12 == 'Argila':
                        alfa12 = 0.85
                        beta12 = 1.5
                        c12 = 120
                    elif solo12 == 'Areia':
                        alfa12 = 0.5
                        beta12 = 1.5
                        c12 = 400
                    elif solo12 == 'Silte Argiloso' or solo12 == 'Silte Argiloarenoso' or solo12 == 'Silte' or solo12 == 'Argila Arenossiltosa' or solo12 == 'Argila Siltosa' or solo12 == 'Argila Siltoarenosa':
                        alfa12 = 0.6
                        beta12 = 1.5
                        c12 = 200
                    elif solo12 is None:
                        alfa12 = 0
                        beta12 = 0
                        c12 = 0
                    else:
                        alfa12 = 0.6
                        beta12 = 1.5
                        c12 = 250
                    
                    if solo13 == 'Argila':
                        alfa13 = 0.85
                        beta13 = 1.5
                        c13 = 120
                    elif solo13 == 'Areia':
                        alfa13 = 0.5
                        beta13 = 1.5
                        c13 = 400
                    elif solo13 == 'Silte Argiloso' or solo13 == 'Silte Argiloarenoso' or solo13 == 'Silte' or solo13 == 'Argila Arenossiltosa' or solo13 == 'Argila Siltosa' or solo13 == 'Argila Siltoarenosa':
                        alfa13 = 0.6
                        beta13 = 1.5
                        c13 = 200
                    elif solo13 is None:
                        alfa13 = 0
                        beta13 = 0
                        c13 = 0
                    else:
                        alfa13 = 0.6
                        beta13 = 1.5
                        c13 = 250
                    
                    if solo14 == 'Argila':
                        alfa14 = 0.85
                        beta14 = 1.5
                        c14 = 120
                    elif solo14 == 'Areia':
                        alfa14 = 0.5
                        beta14 = 1.5
                        c14 = 400
                    elif solo14 == 'Silte Argiloso' or solo14 == 'Silte Argiloarenoso' or solo14 == 'Silte' or solo14 == 'Argila Arenossiltosa' or solo14 == 'Argila Siltosa' or solo14 == 'Argila Siltoarenosa':
                        alfa14 = 0.6
                        beta14 = 1.5
                        c14 = 200
                    elif solo14 is None:
                        alfa14 = 0
                        beta14 = 0
                        c14 = 0
                    else:
                        alfa14 = 0.6
                        beta14 = 1.5
                        c14 = 250
                    
                    if solo15 == 'Argila':
                        alfa15 = 0.85
                        beta15 = 1.5
                        c15 = 120
                    elif solo15 == 'Areia':
                        alfa15 = 0.5
                        beta15 = 1.5
                        c15 = 400
                    elif solo15 == 'Silte Argiloso' or solo15 == 'Silte Argiloarenoso' or solo15 == 'Silte' or solo15 == 'Argila Arenossiltosa' or solo15 == 'Argila Siltosa' or solo15 == 'Argila Siltoarenosa':
                        alfa15 = 0.6
                        beta15 = 1.5
                        c15 = 200
                    elif solo15 is None:
                        alfa15 = 0
                        beta15 = 0
                        c15 = 0
                    else:
                        alfa15 = 0.6
                        beta15 = 1.5
                        c15 = 250
                    
                    if solo16 == 'Argila':
                        alfa16 = 0.85
                        beta16 = 1.5
                        c16 = 120
                    elif solo16 == 'Areia':
                        alfa16 = 0.5
                        beta16 = 1.5
                        c16 = 400
                    elif solo16 == 'Silte Argiloso' or solo16 == 'Silte Argiloarenoso' or solo16 == 'Silte' or solo16 == 'Argila Arenossiltosa' or solo16 == 'Argila Siltosa' or solo16 == 'Argila Siltoarenosa':
                        alfa16 = 0.6
                        beta16 = 1.5
                        c16 = 200
                    elif solo16 is None:
                        alfa16 = 0
                        beta16 = 0
                        c16 = 0
                    else:
                        alfa16 = 0.6
                        beta16 = 1.5
                        c16 = 250

                    if solo17 == 'Argila':
                        alfa17 = 0.85
                        beta17 = 1.5
                        c17 = 120
                    elif solo17 == 'Areia':
                        alfa17 = 0.5
                        beta17 = 1.5
                        c17 = 400
                    elif solo17 == 'Silte Argiloso' or solo17 == 'Silte Argiloarenoso' or solo17 == 'Silte' or solo17 == 'Argila Arenossiltosa' or solo17 == 'Argila Siltosa' or solo17 == 'Argila Siltoarenosa':
                        alfa17 = 0.6
                        beta17 = 1.5
                        c17 = 200
                    elif solo17 is None:
                        alfa17 = 0
                        beta17 = 0
                        c17 = 0
                    else:
                        alfa17 = 0.6
                        beta17 = 1.5
                        c17 = 250
                    
                    if solo18 == 'Argila':
                        alfa18 = 0.85
                        beta18 = 1.5
                        c18 = 120
                    elif solo18 == 'Areia':
                        alfa18 = 0.5
                        beta18 = 1.5
                        c18 = 400
                    elif solo18 == 'Silte Argiloso' or solo18 == 'Silte Argiloarenoso' or solo18 == 'Silte' or solo18 == 'Argila Arenossiltosa' or solo18 == 'Argila Siltosa' or solo18 == 'Argila Siltoarenosa':
                        alfa18 = 0.6
                        beta18 = 1.5
                        c18 = 200
                    elif solo18 is None:
                        alfa18 = 0
                        beta18 = 0
                        c18 = 0
                    else:
                        alfa18 = 0.6
                        beta18 = 1.5
                        c18 = 250
                    
                    if solo19 == 'Argila':
                        alfa19 = 0.85
                        beta19 = 1.5
                        c19 = 120
                    elif solo19 == 'Areia':
                        alfa19 = 0.5
                        beta19 = 1.5
                        c19 = 400
                    elif solo19 == 'Silte Argiloso' or solo19 == 'Silte Argiloarenoso' or solo19 == 'Silte' or solo19 == 'Argila Arenossiltosa' or solo19 == 'Argila Siltosa' or solo19 == 'Argila Siltoarenosa':
                        alfa19 = 0.6
                        beta19 = 1.5
                        c19 = 200
                    elif solo19 is None:
                        alfa19 = 0
                        beta19 = 0
                        c19 = 0
                    else:
                        alfa19 = 0.6
                        beta19 = 1.5
                        c19 = 250
                    
                    if solo20 == 'Argila':
                        alfa20 = 0.85
                        beta20 = 1.5
                        c20 = 120
                    elif solo20 == 'Areia':
                        alfa20 = 0.5
                        beta20 = 1.5
                        c20 = 400
                    elif solo20 == 'Silte Argiloso' or solo20 == 'Silte Argiloarenoso' or solo20 == 'Silte' or solo20 == 'Argila Arenossiltosa' or solo20 == 'Argila Siltosa' or solo20 == 'Argila Siltoarenosa':
                        alfa20 = 0.6
                        beta20 = 1.5
                        c20 = 200
                    elif solo20 is None:
                        alfa20 = 0
                        beta20 = 0
                        c20 = 0
                    else:
                        alfa20 = 0.6
                        beta20 = 1.5
                        c20 = 250
                    
                    if solo21 == 'Argila':
                        alfa21 = 0.85
                        beta21 = 1.5
                        c21 = 120
                    elif solo21 == 'Areia':
                        alfa21 = 0.5
                        beta21 = 1.5
                        c21 = 400
                    elif solo21 == 'Silte Argiloso' or solo21 == 'Silte Argiloarenoso' or solo21 == 'Silte' or solo21 == 'Argila Arenossiltosa' or solo21 == 'Argila Siltosa' or solo21 == 'Argila Siltoarenosa':
                        alfa21 = 0.6
                        beta21 = 1.5
                        c21 = 200
                    elif solo21 is None:
                        alfa21 = 0
                        beta21 = 0
                        c21 = 0
                    else:
                        alfa21 = 0.6
                        beta21 = 1.5
                        c21 = 250
                    
                    if solo22 == 'Argila':
                        alfa22 = 0.85
                        beta22 = 1.5
                        c22 = 120
                    elif solo22 == 'Areia':
                        alfa22 = 0.5
                        beta22 = 1.5
                        c22 = 400
                    elif solo22 == 'Silte Argiloso' or solo22 == 'Silte Argiloarenoso' or solo22 == 'Silte' or solo22 == 'Argila Arenossiltosa' or solo22 == 'Argila Siltosa' or solo22 == 'Argila Siltoarenosa':
                        alfa22 = 0.6
                        beta22 = 1.5
                        c22 = 200
                    elif solo22 is None:
                        alfa22 = 0
                        beta22 = 0
                        c22 = 0
                    else:
                        alfa22 = 0.6
                        beta22 = 1.5
                        c22 = 250
                    
                    if solo23 == 'Argila':
                        alfa23 = 0.85
                        beta23 = 1.5
                        c23 = 120
                    elif solo23 == 'Areia':
                        alfa23 = 0.5
                        beta23 = 1.5
                        c23 = 400
                    elif solo23 == 'Silte Argiloso' or solo23 == 'Silte Argiloarenoso' or solo23 == 'Silte' or solo23 == 'Argila Arenossiltosa' or solo23 == 'Argila Siltosa' or solo23 == 'Argila Siltoarenosa':
                        alfa23 = 0.6
                        beta23 = 1.5
                        c23 = 200
                    elif solo23 is None:
                        alfa23 = 0
                        beta23 = 0
                        c23 = 0
                    else:
                        alfa23 = 0.6
                        beta23 = 1.5
                        c23 = 250
                    
                    if solo24 == 'Argila':
                        alfa24 = 0.85
                        beta24 = 1.5
                        c24 = 120
                    elif solo24 == 'Areia':
                        alfa24 = 0.5
                        beta24 = 1.5
                        c24 = 400
                    elif solo24 == 'Silte Argiloso' or solo24 == 'Silte Argiloarenoso' or solo24 == 'Silte' or solo24 == 'Argila Arenossiltosa' or solo24 == 'Argila Siltosa' or solo24 == 'Argila Siltoarenosa':
                        alfa24 = 0.6
                        beta24 = 1.5
                        c24 = 200
                    elif solo24 is None:
                        alfa24 = 0
                        beta24 = 0
                        c24 = 0
                    else:
                        alfa24 = 0.6
                        beta24 = 1.5
                        c24 = 250
                    
                    if solo25 == 'Argila':
                        alfa25 = 0.85
                        beta25 = 1.5
                        c25 = 120
                    elif solo25 == 'Areia':
                        alfa25 = 0.5
                        beta25 = 1.5
                        c25 = 400
                    elif solo25 == 'Silte Argiloso' or solo25 == 'Silte Argiloarenoso' or solo25 == 'Silte' or solo25 == 'Argila Arenossiltosa' or solo25 == 'Argila Siltosa' or solo25 == 'Argila Siltoarenosa':
                        alfa25 = 0.6
                        beta25 = 1.5
                        c25 = 200
                    elif solo25 is None:
                        alfa25 = 0
                        beta25 = 0
                        c25 = 0
                    else:
                        alfa25 = 0.6
                        beta25 = 1.5
                        c25 = 250
                        
                elif estaca_selecionado == 'Injet. sob altas pressões':

                    if solo2 == 'Argila':
                        alfa2 = 1
                        beta2 = 3
                        c2 = 120
                    elif solo2 == 'Areia':
                        alfa2 = 1
                        beta2 = 3
                        c2 = 400
                    elif solo2 == 'Silte Argiloso' or solo2 == 'Silte Argiloarenoso' or solo2 == 'Silte' or solo2 == 'Argila Arenossiltosa' or solo2 == 'Argila Siltosa' or solo2 == 'Argila Siltoarenosa':
                        alfa2 = 1
                        beta2 = 3
                        c2 = 200
                    elif solo2 is None:
                        alfa2 = 0
                        beta2 = 0
                        c2 = 0
                    else:
                        alfa2 = 1
                        beta2 = 3
                        c2 = 250
                    
                    if solo3 == 'Argila':
                        alfa3 = 1
                        beta3 = 3
                        c3 = 120
                    elif solo3 == 'Areia':
                        alfa3 = 1
                        beta3 = 3
                        c3 = 400
                    elif solo3 == 'Silte Argiloso' or solo3 == 'Silte Argiloarenoso' or solo3 == 'Silte' or solo3 == 'Argila Arenossiltosa' or solo3 == 'Argila Siltosa' or solo3 == 'Argila Siltoarenosa':
                        alfa3 = 1
                        beta3 = 3
                        c3 = 200
                    elif solo3 is None:
                        alfa3 = 0
                        beta3 = 0
                        c3 = 0
                    else:
                        alfa3 = 1
                        beta3 = 3
                        c3 = 250
                    
                    if solo4 == 'Argila':
                        alfa4 = 1
                        beta4 = 3
                        c4 = 120
                    elif solo4 == 'Areia':
                        alfa4 = 1
                        beta4 = 3
                        c4 = 400
                    elif solo4 == 'Silte Argiloso' or solo4 == 'Silte Argiloarenoso' or solo4 == 'Silte' or solo4 == 'Argila Arenossiltosa' or solo4 == 'Argila Siltosa' or solo4 == 'Argila Siltoarenosa':
                        alfa4 = 1
                        beta4 = 3
                        c4 = 200
                    elif solo4 is None:
                        alfa4 = 0
                        beta4 = 0
                        c4 = 0
                    else:
                        alfa4 = 1
                        beta4 = 3
                        c4 = 250
                    
                    if solo5 == 'Argila':
                        alfa5 = 1
                        beta5 = 3
                        c5 = 120
                    elif solo5 == 'Areia':
                        alfa5 = 1
                        beta5 = 3
                        c5 = 400
                    elif solo5 == 'Silte Argiloso' or solo5 == 'Silte Argiloarenoso' or solo5 == 'Silte' or solo5 == 'Argila Arenossiltosa' or solo5 == 'Argila Siltosa' or solo5 == 'Argila Siltoarenosa':
                        alfa5 = 1
                        beta5 = 3
                        c5 = 200
                    elif solo5 is None:
                        alfa5 = 0
                        beta5 = 0
                        c5 = 0
                    else:
                        alfa5 = 1
                        beta5 = 3
                        c5 = 250
                    
                    if solo6 == 'Argila':
                        alfa6 = 1
                        beta6 = 3
                        c6 = 120
                    elif solo6 == 'Areia':
                        alfa6 = 1
                        beta6 = 3
                        c6 = 400
                    elif solo6 == 'Silte Argiloso' or solo6 == 'Silte Argiloarenoso' or solo6 == 'Silte' or solo6 == 'Argila Arenossiltosa' or solo6 == 'Argila Siltosa' or solo6 == 'Argila Siltoarenosa':
                        alfa6 = 1
                        beta6 = 3
                        c6 = 200
                    elif solo6 is None:
                        alfa6 = 0
                        beta6 = 0
                        c6 = 0
                    else:
                        alfa6 = 1
                        beta6 = 3
                        c6 = 250
                    
                    if solo7 == 'Argila':
                        alfa7 = 1
                        beta7 = 3
                        c7 = 120
                    elif solo7 == 'Areia':
                        alfa7 = 1
                        beta7 = 3
                        c7 = 400
                    elif solo7 == 'Silte Argiloso' or solo7 == 'Silte Argiloarenoso' or solo7 == 'Silte' or solo7 == 'Argila Arenossiltosa' or solo7 == 'Argila Siltosa' or solo7 == 'Argila Siltoarenosa':
                        alfa7 = 1
                        beta7 = 3
                        c7 = 200
                    elif solo7 is None:
                        alfa7 = 0
                        beta7 = 0
                        c7 = 0
                    else:
                        alfa7 = 1
                        beta7 = 3
                        c7 = 250
                    
                    if solo8 == 'Argila':
                        alfa8 = 1
                        beta8 = 3
                        c8 = 120
                    elif solo8 == 'Areia':
                        alfa8 = 1
                        beta8 = 3
                        c8 = 400
                    elif solo8 == 'Silte Argiloso' or solo8 == 'Silte Argiloarenoso' or solo8 == 'Silte' or solo8 == 'Argila Arenossiltosa' or solo8 == 'Argila Siltosa' or solo8 == 'Argila Siltoarenosa':
                        alfa8 = 1
                        beta8 = 3
                        c8 = 200
                    elif solo8 is None:
                        alfa8 = 0
                        beta8 = 0
                        c8 = 0
                    else:
                        alfa8 = 1
                        beta8 = 3
                        c8 = 250
                    
                    if solo9 == 'Argila':
                        alfa9 = 1
                        beta9 = 3
                        c9 = 120
                    elif solo9 == 'Areia':
                        alfa9 = 1
                        beta9 = 3
                        c9 = 400
                    elif solo9 == 'Silte Argiloso' or solo9 == 'Silte Argiloarenoso' or solo9 == 'Silte' or solo9 == 'Argila Arenossiltosa' or solo9 == 'Argila Siltosa' or solo9 == 'Argila Siltoarenosa':
                        alfa9 = 1
                        beta9 = 3
                        c9 = 200
                    elif solo9 is None:
                        alfa9 = 0
                        beta9 = 0
                        c9 = 0
                    else:
                        alfa9 = 1
                        beta9 = 3
                        c9 = 250
                    
                    if solo10 == 'Argila':
                        alfa10 = 1
                        beta10 = 3
                        c10 = 120
                    elif solo10 == 'Areia':
                        alfa10 = 1
                        beta10 = 3
                        c10 = 400
                    elif solo10 == 'Silte Argiloso' or solo10 == 'Silte Argiloarenoso' or solo10 == 'Silte' or solo10 == 'Argila Arenossiltosa' or solo10 == 'Argila Siltosa' or solo10 == 'Argila Siltoarenosa':
                        alfa10 = 1
                        beta10 = 3
                        c10 = 200
                    elif solo10 is None:
                        alfa10 = 0
                        beta10 = 0
                        c10 = 0
                    else:
                        alfa10 = 1
                        beta10 = 3
                        c10 = 250
                    
                    if solo11 == 'Argila':
                        alfa11 = 1
                        beta11 = 3
                        c11 = 120
                    elif solo11 == 'Areia':
                        alfa11 = 1
                        beta11 = 3
                        c11 = 400
                    elif solo11 == 'Silte Argiloso' or solo11 == 'Silte Argiloarenoso' or solo11 == 'Silte' or solo11 == 'Argila Arenossiltosa' or solo11 == 'Argila Siltosa' or solo11 == 'Argila Siltoarenosa':
                        alfa11 = 1
                        beta11 = 3
                        c11 = 200
                    elif solo11 is None:
                        alfa11 = 0
                        beta11 = 0
                        c11 = 0
                    else:
                        alfa11 = 1
                        beta11 = 3
                        c11 = 250
                    
                    if solo12 == 'Argila':
                        alfa12 = 1
                        beta12 = 3
                        c12 = 120
                    elif solo12 == 'Areia':
                        alfa12 = 1
                        beta12 = 3
                        c12 = 400
                    elif solo12 == 'Silte Argiloso' or solo12 == 'Silte Argiloarenoso' or solo12 == 'Silte' or solo12 == 'Argila Arenossiltosa' or solo12 == 'Argila Siltosa' or solo12 == 'Argila Siltoarenosa':
                        alfa12 = 1
                        beta12 = 3
                        c12 = 200
                    elif solo12 is None:
                        alfa12 = 0
                        beta12 = 0
                        c12 = 0
                    else:
                        alfa12 = 1
                        beta12 = 3
                        c12 = 250
                    
                    if solo13 == 'Argila':
                        alfa13 = 1
                        beta13 = 3
                        c13 = 120
                    elif solo13 == 'Areia':
                        alfa13 = 1
                        beta13 = 3
                        c13 = 400
                    elif solo13 == 'Silte Argiloso' or solo13 == 'Silte Argiloarenoso' or solo13 == 'Silte' or solo13 == 'Argila Arenossiltosa' or solo13 == 'Argila Siltosa' or solo13 == 'Argila Siltoarenosa':
                        alfa13 = 1
                        beta13 = 3
                        c13 = 200
                    elif solo13 is None:
                        alfa13 = 0
                        beta13 = 0
                        c13 = 0
                    else:
                        alfa13 = 1
                        beta13 = 3
                        c13 = 250
                    
                    if solo14 == 'Argila':
                        alfa14 = 1
                        beta14 = 3
                        c14 = 120
                    elif solo14 == 'Areia':
                        alfa14 = 1
                        beta14 = 3
                        c14 = 400
                    elif solo14 == 'Silte Argiloso' or solo14 == 'Silte Argiloarenoso' or solo14 == 'Silte' or solo14 == 'Argila Arenossiltosa' or solo14 == 'Argila Siltosa' or solo14 == 'Argila Siltoarenosa':
                        alfa14 = 1
                        beta14 = 3
                        c14 = 200
                    elif solo14 is None:
                        alfa14 = 0
                        beta14 = 0
                        c14 = 0
                    else:
                        alfa14 = 1
                        beta14 = 3
                        c14 = 250
                    
                    if solo15 == 'Argila':
                        alfa15 = 1
                        beta15 = 3
                        c15 = 120
                    elif solo15 == 'Areia':
                        alfa15 = 1
                        beta15 = 3
                        c15 = 400
                    elif solo15 == 'Silte Argiloso' or solo15 == 'Silte Argiloarenoso' or solo15 == 'Silte' or solo15 == 'Argila Arenossiltosa' or solo15 == 'Argila Siltosa' or solo15 == 'Argila Siltoarenosa':
                        alfa15 = 1
                        beta15 = 3
                        c15 = 200
                    elif solo15 is None:
                        alfa15 = 0
                        beta15 = 0
                        c15 = 0
                    else:
                        alfa15 = 1
                        beta15 = 3
                        c15 = 250
                    
                    if solo16 == 'Argila':
                        alfa16 = 1
                        beta16 = 3
                        c16 = 120
                    elif solo16 == 'Areia':
                        alfa16 = 1
                        beta16 = 3
                        c16 = 400
                    elif solo16 == 'Silte Argiloso' or solo16 == 'Silte Argiloarenoso' or solo16 == 'Silte' or solo16 == 'Argila Arenossiltosa' or solo16 == 'Argila Siltosa' or solo16 == 'Argila Siltoarenosa':
                        alfa16 = 1
                        beta16 = 3
                        c16 = 200
                    elif solo16 is None:
                        alfa16 = 0
                        beta16 = 0
                        c16 = 0
                    else:
                        alfa16 = 1
                        beta16 = 3
                        c16 = 250
                    
                    if solo17 == 'Argila':
                        alfa17 = 1
                        beta17 = 3
                        c17 = 120
                    elif solo17 == 'Areia':
                        alfa17 = 1
                        beta17 = 3
                        c17 = 400
                    elif solo17 == 'Silte Argiloso' or solo17 == 'Silte Argiloarenoso' or solo17 == 'Silte' or solo17 == 'Argila Arenossiltosa' or solo17 == 'Argila Siltosa' or solo17 == 'Argila Siltoarenosa':
                        alfa17 = 1
                        beta17 = 3
                        c17 = 200
                    elif solo17 is None:
                        alfa17 = 0
                        beta17 = 0
                        c17 = 0
                    else:
                        alfa17 = 1
                        beta17 = 3
                        c17 = 250
                    
                    if solo18 == 'Argila':
                        alfa18 = 1
                        beta18 = 3
                        c18 = 120
                    elif solo18 == 'Areia':
                        alfa18 = 1
                        beta18 = 3
                        c18 = 400
                    elif solo18 == 'Silte Argiloso' or solo18 == 'Silte Argiloarenoso' or solo18 == 'Silte' or solo18 == 'Argila Arenossiltosa' or solo18 == 'Argila Siltosa' or solo18 == 'Argila Siltoarenosa':
                        alfa18 = 1
                        beta18 = 3
                        c18 = 200
                    elif solo18 is None:
                        alfa18 = 0
                        beta18 = 0
                        c18 = 0
                    else:
                        alfa18 = 1
                        beta18 = 3
                        c18 = 250
                    
                    if solo19 == 'Argila':
                        alfa19 = 1
                        beta19 = 3
                        c19 = 120
                    elif solo19 == 'Areia':
                        alfa19 = 1
                        beta19 = 3
                        c19 = 400
                    elif solo19 == 'Silte Argiloso' or solo19 == 'Silte Argiloarenoso' or solo19 == 'Silte' or solo19 == 'Argila Arenossiltosa' or solo19 == 'Argila Siltosa' or solo19 == 'Argila Siltoarenosa':
                        alfa19 = 1
                        beta19 = 3
                        c19 = 200
                    elif solo19 is None:
                        alfa19 = 0
                        beta19 = 0
                        c19 = 0
                    else:
                        alfa19 = 1
                        beta19 = 3
                        c19 = 250
                    
                    if solo20 == 'Argila':
                        alfa20 = 1
                        beta20 = 3
                        c20 = 120
                    elif solo20 == 'Areia':
                        alfa20 = 1
                        beta20 = 3
                        c20 = 400
                    elif solo20 == 'Silte Argiloso' or solo20 == 'Silte Argiloarenoso' or solo20 == 'Silte' or solo20 == 'Argila Arenossiltosa' or solo20 == 'Argila Siltosa' or solo20 == 'Argila Siltoarenosa':
                        alfa20 = 1
                        beta20 = 3
                        c20 = 200
                    elif solo20 is None:
                        alfa20 = 0
                        beta20 = 0
                        c20 = 0
                    else:
                        alfa20 = 1
                        beta20 = 3
                        c20 = 250
                    
                    if solo21 == 'Argila':
                        alfa21 = 1
                        beta21 = 3
                        c21 = 120
                    elif solo21 == 'Areia':
                        alfa21 = 1
                        beta21 = 3
                        c21 = 400
                    elif solo21 == 'Silte Argiloso' or solo21 == 'Silte Argiloarenoso' or solo21 == 'Silte' or solo21 == 'Argila Arenossiltosa' or solo21 == 'Argila Siltosa' or solo21 == 'Argila Siltoarenosa':
                        alfa21 = 1
                        beta21 = 3
                        c21 = 200
                    elif solo21 is None:
                        alfa21 = 0
                        beta21 = 0
                        c21 = 0
                    else:
                        alfa21 = 1
                        beta21 = 3
                        c21 = 250
                    
                    if solo22 == 'Argila':
                        alfa22 = 1
                        beta22 = 3
                        c22 = 120
                    elif solo22 == 'Areia':
                        alfa22 = 1
                        beta22 = 3
                        c22 = 400
                    elif solo22 == 'Silte Argiloso' or solo22 == 'Silte Argiloarenoso' or solo22 == 'Silte' or solo22 == 'Argila Arenossiltosa' or solo22 == 'Argila Siltosa' or solo22 == 'Argila Siltoarenosa':
                        alfa22 = 1
                        beta22 = 3
                        c22 = 200
                    elif solo22 is None:
                        alfa22 = 0
                        beta22 = 0
                        c22 = 0
                    else:
                        alfa22 = 1
                        beta22 = 3
                        c22 = 250
                    
                    if solo23 == 'Argila':
                        alfa23 = 1
                        beta23 = 3
                        c23 = 120
                    elif solo23 == 'Areia':
                        alfa23 = 1
                        beta23 = 3
                        c23 = 400
                    elif solo23 == 'Silte Argiloso' or solo23 == 'Silte Argiloarenoso' or solo23 == 'Silte' or solo23 == 'Argila Arenossiltosa' or solo23 == 'Argila Siltosa' or solo23 == 'Argila Siltoarenosa':
                        alfa23 = 1
                        beta23 = 3
                        c23 = 200
                    elif solo23 is None:
                        alfa23 = 0
                        beta23 = 0
                        c23 = 0
                    else:
                        alfa23 = 1
                        beta23 = 3
                        c23 = 250
                    
                    if solo24 == 'Argila':
                        alfa24 = 1
                        beta24 = 3
                        c24 = 120
                    elif solo24 == 'Areia':
                        alfa24 = 1
                        beta24 = 3
                        c24 = 400
                    elif solo24 == 'Silte Argiloso' or solo24 == 'Silte Argiloarenoso' or solo24 == 'Silte' or solo24 == 'Argila Arenossiltosa' or solo24 == 'Argila Siltosa' or solo24 == 'Argila Siltoarenosa':
                        alfa24 = 1
                        beta24 = 3
                        c24 = 200
                    elif solo24 is None:
                        alfa24 = 0
                        beta24 = 0
                        c24 = 0
                    else:
                        alfa24 = 1
                        beta24 = 3
                        c24 = 250
                    
                    if solo25 == 'Argila':
                        alfa25 = 1
                        beta25 = 3
                        c25 = 120
                    elif solo25 == 'Areia':
                        alfa25 = 1
                        beta25 = 3
                        c25 = 400
                    elif solo25 == 'Silte Argiloso' or solo25 == 'Silte Argiloarenoso' or solo25 == 'Silte' or solo25 == 'Argila Arenossiltosa' or solo25 == 'Argila Siltosa' or solo25 == 'Argila Siltoarenosa':
                        alfa25 = 1
                        beta25 = 3
                        c25 = 200
                    elif solo25 is None:
                        alfa25 = 0
                        beta25 = 0
                        c25 = 0
                    else:
                        alfa25 = 1
                        beta25 = 3
                        c25 = 250
            
            if calcular:

                texto_calculo1 = fonte.render('O primeiro metro é ignorado, para todos os casos, pois é a parte da estaca que estará no bloco. Esta parte do solo é escavada.', True, vermelho_escuro)
                rec_texto_calculo1 = pygame.Rect(rec_metodo.x, rec_metodo.y + cell_height + button_spacing, 700, 15)
                janela.blit(texto_calculo1, rec_texto_calculo1)

                texto_calculo1a = fonte.render('RL - resistência lateral; RP - resistência de ponta; RT - resistência total; Rl2 - resitência lateral da profundidade de 2m', True, vermelho_escuro)
                rec_texto_calculo1a = pygame.Rect(rec_texto_calculo1.x, rec_texto_calculo1.y + rec_texto_calculo1.height, 700, 15)
                janela.blit(texto_calculo1a, rec_texto_calculo1a)

                texto_calculo1b = fonte.render('Rl3 - resitência lateral da profundidade de 3m e assim sucessivamente.', True, vermelho_escuro)
                rec_texto_calculo1b = pygame.Rect(rec_texto_calculo1a.x, rec_texto_calculo1a.y + rec_texto_calculo1a.height, 700, 15)
                janela.blit(texto_calculo1b, rec_texto_calculo1b)

                if metodo_selecionado == 'DECOURT & QUARESMA':

                    Rp3 = round(alfa3*c3*int(NSPT3)*area, 2)
                    Rl2 = beta2*circunferencia*10*((int(NSPT2)/3)+1)
                    Rltotal2 = round(Rl2, 2)
                    Rt2 = round(Rp3 + Rltotal2, 2)

                    Rp4 = round(alfa4*c4*int(NSPT4)*area, 2)
                    Rl3 = beta3*circunferencia*10*((int(NSPT3)/3)+1)
                    Rltotal3 = round(Rltotal2 + Rl3, 2)
                    Rt3 = round(Rp4 + Rltotal3, 2)

                    Rp5 = round(alfa5*c5*int(NSPT5)*area, 2)
                    Rl4 = beta4*circunferencia*10*((int(NSPT4)/3)+1)
                    Rltotal4 = round(Rltotal3 + Rl4, 2)
                    Rt4 = round(Rp5 + Rltotal4, 2)

                    Rp6 = round(alfa6*c6*int(NSPT6)*area, 2)
                    Rl5 = beta5*circunferencia*10*((int(NSPT5)/3)+1)
                    Rltotal5 = round(Rltotal4 + Rl5, 2)
                    Rt5 = round(Rp6 + Rltotal5, 2)

                    Rp7 = round(alfa7*c7*int(NSPT7)*area, 2)
                    Rl6 = beta6*circunferencia*10*((int(NSPT6)/3)+1)
                    Rltotal6 = round(Rltotal5 + Rl6, 2)
                    Rt6 = round(Rp7 + Rltotal6, 2)

                    Rp8 = round(alfa8*c8*int(NSPT8)*area, 2)
                    Rl7 = beta7*circunferencia*10*((int(NSPT7)/3)+1)
                    Rltotal7 = round(Rltotal6 + Rl7, 2)
                    Rt7 = round(Rp8 + Rltotal7, 2)

                    Rp9 = round(alfa9*c9*int(NSPT9)*area, 2)
                    Rl8 = beta8*circunferencia*10*((int(NSPT8)/3)+1)
                    Rltotal8 = round(Rltotal7 + Rl8, 2)
                    Rt8 = round(Rp9 + Rltotal8, 2)

                    Rp10 = round(alfa10*c10*int(NSPT10)*area, 2)
                    Rl9 = beta9*circunferencia*10*((int(NSPT9)/3)+1)
                    Rltotal9 = round(Rltotal8 + Rl9, 2)
                    Rt9 = round(Rp10 + Rltotal9, 2)

                    Rp11 = round(alfa11*c11*int(NSPT11)*area, 2)
                    Rl10 = beta10*circunferencia*10*((int(NSPT10)/3)+1)
                    Rltotal10 = round(Rltotal9 + Rl10, 2)
                    Rt10 = round(Rp11 + Rltotal10, 2)

                    Rp12 = round(alfa12*c12*int(NSPT12)*area, 2)
                    Rl11 = beta11*circunferencia*10*((int(NSPT11)/3)+1)
                    Rltotal11 = round(Rltotal10 + Rl11, 2)
                    Rt11 = round(Rp12 + Rltotal11, 2)

                    Rp13 = round(alfa13*c13*int(NSPT13)*area, 2)
                    Rl12 = beta12*circunferencia*10*((int(NSPT12)/3)+1)
                    Rltotal12 = round(Rltotal11 + Rl12, 2)
                    Rt12 = round(Rp13 + Rltotal12, 2)

                    Rp14 = round(alfa14*c14*int(NSPT14)*area, 2)
                    Rl13 = beta13*circunferencia*10*((int(NSPT13)/3)+1)
                    Rltotal13 = round(Rltotal12 + Rl13, 2)
                    Rt13 = round(Rp14 + Rltotal13, 2)

                    Rp15 = round(alfa15*c15*int(NSPT15)*area, 2)
                    Rl14 = beta14*circunferencia*10*((int(NSPT14)/3)+1)
                    Rltotal14 = round(Rltotal13 + Rl14, 2)
                    Rt14 = round(Rp15 + Rltotal14, 2)

                    Rp16 = round(alfa16*c16*int(NSPT16)*area, 2)
                    Rl15 = beta15*circunferencia*10*((int(NSPT15)/3)+1)
                    Rltotal15 = round(Rltotal14 + Rl15, 2)
                    Rt15 = round(Rp16 + Rltotal15, 2)

                    Rp17 = round(alfa17*c17*int(NSPT17)*area, 2)
                    Rl16 = beta16*circunferencia*10*((int(NSPT16)/3)+1)
                    Rltotal16 = round(Rltotal15 + Rl16, 2)
                    Rt16 = round(Rp17 + Rltotal16, 2)

                    Rp18 = round(alfa18*c18*int(NSPT18)*area, 2)
                    Rl17 = beta17*circunferencia*10*((int(NSPT17)/3)+1)
                    Rltotal17 = round(Rltotal16 + Rl17, 2)
                    Rt17 = round(Rp18 + Rltotal17, 2)

                    Rp19 = round(alfa19*c19*int(NSPT19)*area, 2)
                    Rl18 = beta18*circunferencia*10*((int(NSPT18)/3)+1)
                    Rltotal18 = round(Rltotal17 + Rl18, 2)
                    Rt18 = round(Rp19 + Rltotal18, 2)

                    Rp20 = round(alfa20*c20*int(NSPT20)*area, 2)
                    Rl19 = beta19*circunferencia*10*((int(NSPT19)/3)+1)
                    Rltotal19 = round(Rltotal18 + Rl19, 2)
                    Rt19 = round(Rp20 + Rltotal19, 2)

                    Rp21 = round(alfa21*c21*int(NSPT21)*area, 2)
                    Rl20 = beta20*circunferencia*10*((int(NSPT20)/3)+1)
                    Rltotal20 = round(Rltotal19 + Rl20, 2)
                    Rt20 = round(Rp21 + Rltotal20, 2)

                    Rp22 = round(alfa22*c22*int(NSPT22)*area, 2)
                    Rl21 = beta21*circunferencia*10*((int(NSPT21)/3)+1)
                    Rltotal21 = round(Rltotal20 + Rl21, 2)
                    Rt21 = round(Rp22 + Rltotal21, 2)

                    Rp23 = round(alfa23*c23*int(NSPT23)*area, 2)
                    Rl22 = beta22*circunferencia*10*((int(NSPT22)/3)+1)
                    Rltotal22 = round(Rltotal21 + Rl22, 2)
                    Rt22 = round(Rp23 + Rltotal22, 2)

                    Rp24 = round(alfa24*c24*int(NSPT24)*area, 2)
                    Rl23 = beta23*circunferencia*10*((int(NSPT23)/3)+1)
                    Rltotal23 = round(Rltotal22 + Rl23, 2)
                    Rt23 = round(Rp24 + Rltotal23, 2)

                    Rp25 = round(alfa25*c25*int(NSPT25)*area, 2)
                    Rl24 = beta24*circunferencia*10*((int(NSPT24)/3)+1)
                    Rltotal24 = round(Rltotal23 + Rl24, 2)
                    Rt24 = round(Rp25 + Rltotal24, 2)

                    if pcount == 0:

                        if count > 1:

                            texto_calculo2 = fonte.render('Para a estaca apoiada na profundidade de 2m:', True, preto)
                            rec_texto_calculo2 = pygame.Rect(rec_texto_calculo1b.x, rec_texto_calculo1b.y + rec_texto_calculo1b.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo2, rec_texto_calculo2)

                            texto_calculo2a = fonte.render('RL = Rl2 = '+str(beta2)+'*10*'+str(circunferencia)+'*(('+NSPT2+'/3)+1)'+' = '+str(Rltotal2)+' kN', True, preto)
                            rec_texto_calculo2a = pygame.Rect(rec_texto_calculo2.x, rec_texto_calculo2.y + rec_texto_calculo2.height, 700, 15)
                            janela.blit(texto_calculo2a, rec_texto_calculo2a)

                            texto_calculo2b = fonte.render('RP = '+str(alfa3)+'*'+str(c3)+'*'+NSPT3+'*'+str(area)+' = '+str(Rp3)+' kN', True, preto)
                            rec_texto_calculo2b = pygame.Rect(rec_texto_calculo2a.x, rec_texto_calculo2a.y + rec_texto_calculo2a.height, 700, 15)
                            janela.blit(texto_calculo2b, rec_texto_calculo2b)

                            texto_calculo2c = fonte.render('RT = RL + RP = '+str(Rltotal2)+' + '+str(Rp3)+' = '+str(Rt2)+' kN', True, preto)
                            rec_texto_calculo2c = pygame.Rect(rec_texto_calculo2b.x, rec_texto_calculo2b.y + rec_texto_calculo2b.height, 700, 15)
                            janela.blit(texto_calculo2c, rec_texto_calculo2c)

                        if count > 2:                            

                            texto_calculo3 = fonte.render('Para a estaca apoiada na profundidade de 3m:', True, preto)
                            rec_texto_calculo3 = pygame.Rect(rec_texto_calculo2c.x, rec_texto_calculo2c.y + rec_texto_calculo2c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo3, rec_texto_calculo3)

                            texto_calculo3a = fonte.render('RL = Rl2+Rl3 = '+str(Rltotal2)+' + '+str(beta3)+'*10*'+str(circunferencia)+'*(('+NSPT3+'/3)+1))'+' = '+str(Rltotal3)+' kN', True, preto)
                            rec_texto_calculo3a = pygame.Rect(rec_texto_calculo3.x, rec_texto_calculo3.y + rec_texto_calculo3.height, 700, 15)
                            janela.blit(texto_calculo3a, rec_texto_calculo3a)

                            texto_calculo3b = fonte.render('RP = '+str(alfa4)+'*'+str(c4)+'*'+NSPT4+'*'+str(area)+' = '+str(Rp4)+' kN', True, preto)
                            rec_texto_calculo3b = pygame.Rect(rec_texto_calculo3a.x, rec_texto_calculo3a.y + rec_texto_calculo3a.height, 700, 15)
                            janela.blit(texto_calculo3b, rec_texto_calculo3b)

                            texto_calculo3c = fonte.render('RT = RL + RP = '+str(Rltotal3)+' + '+str(Rp4)+' = '+str(Rt3)+' kN', True, preto)
                            rec_texto_calculo3c = pygame.Rect(rec_texto_calculo3b.x, rec_texto_calculo3b.y + rec_texto_calculo3b.height, 700, 15)
                            janela.blit(texto_calculo3c, rec_texto_calculo3c)
                        
                        if count > 3:                            

                            texto_calculo4 = fonte.render('Para a estaca apoiada na profundidade de 4m:', True, preto)
                            rec_texto_calculo4 = pygame.Rect(rec_texto_calculo3c.x, rec_texto_calculo3c.y + rec_texto_calculo3c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo4, rec_texto_calculo4)

                            texto_calculo4a = fonte.render('RL = Rl2+Rl3+Rl4 = '+str(Rltotal3)+' + '+str(beta4)+'*10*'+str(circunferencia)+'*(('+NSPT4+'/3)+1))'+' = '+str(Rltotal4)+' kN', True, preto)
                            rec_texto_calculo4a = pygame.Rect(rec_texto_calculo4.x, rec_texto_calculo4.y + rec_texto_calculo4.height, 700, 15)
                            janela.blit(texto_calculo4a, rec_texto_calculo4a)

                            texto_calculo4b = fonte.render('RP = '+str(alfa5)+'*'+str(c5)+'*'+NSPT5+'*'+str(area)+' = '+str(Rp5)+' kN', True, preto)
                            rec_texto_calculo4b = pygame.Rect(rec_texto_calculo4a.x, rec_texto_calculo4a.y + rec_texto_calculo4a.height, 700, 15)
                            janela.blit(texto_calculo4b, rec_texto_calculo4b)

                            texto_calculo4c = fonte.render('RT = RL + RP = '+str(Rltotal4)+' + '+str(Rp5)+' = '+str(Rt4)+' kN', True, preto)
                            rec_texto_calculo4c = pygame.Rect(rec_texto_calculo4b.x, rec_texto_calculo4b.y + rec_texto_calculo4b.height, 700, 15)
                            janela.blit(texto_calculo4c, rec_texto_calculo4c)
                        
                        if count > 4:                            

                            texto_calculo5 = fonte.render('Para a estaca apoiada na profundidade de 5m:', True, preto)
                            rec_texto_calculo5 = pygame.Rect(rec_texto_calculo4c.x, rec_texto_calculo4c.y + rec_texto_calculo4c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo5, rec_texto_calculo5)

                            texto_calculo5a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5 = '+str(Rltotal4)+' + '+str(beta5)+'*10*'+str(circunferencia)+'*(('+NSPT5+'/3)+1))'+' = '+str(Rltotal5)+' kN', True, preto)
                            rec_texto_calculo5a = pygame.Rect(rec_texto_calculo5.x, rec_texto_calculo5.y + rec_texto_calculo5.height, 700, 15)
                            janela.blit(texto_calculo5a, rec_texto_calculo5a)

                            texto_calculo5b = fonte.render('RP = '+str(alfa6)+'*'+str(c6)+'*'+NSPT6+'*'+str(area)+' = '+str(Rp6)+' kN', True, preto)
                            rec_texto_calculo5b = pygame.Rect(rec_texto_calculo5a.x, rec_texto_calculo5a.y + rec_texto_calculo5a.height, 700, 15)
                            janela.blit(texto_calculo5b, rec_texto_calculo5b)

                            texto_calculo5c = fonte.render('RT = RL + RP = '+str(Rltotal5)+' + '+str(Rp6)+' = '+str(Rt5)+' kN', True, preto)
                            rec_texto_calculo5c = pygame.Rect(rec_texto_calculo5b.x, rec_texto_calculo5b.y + rec_texto_calculo5b.height, 700, 15)
                            janela.blit(texto_calculo5c, rec_texto_calculo5c)
                        
                    if pcount == 1:

                        if count > 5:                            

                            texto_calculo6 = fonte.render('Para a estaca apoiada na profundidade de 6m:', True, preto)
                            rec_texto_calculo6 = pygame.Rect(rec_texto_calculo2.x, rec_texto_calculo2.y, 700, 15)
                            janela.blit(texto_calculo6, rec_texto_calculo6)

                            texto_calculo6a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6 = '+str(Rltotal5)+' + '+str(beta6)+'*10*'+str(circunferencia)+'*(('+NSPT6+'/3)+1))'+' = '+str(Rltotal6)+' kN', True, preto)
                            rec_texto_calculo6a = pygame.Rect(rec_texto_calculo6.x, rec_texto_calculo6.y + rec_texto_calculo6.height, 700, 15)
                            janela.blit(texto_calculo6a, rec_texto_calculo6a)

                            texto_calculo6b = fonte.render('RP = '+str(alfa7)+'*'+str(c7)+'*'+NSPT7+'*'+str(area)+' = '+str(Rp7)+' kN', True, preto)
                            rec_texto_calculo6b = pygame.Rect(rec_texto_calculo6a.x, rec_texto_calculo6a.y + rec_texto_calculo6a.height, 700, 15)
                            janela.blit(texto_calculo6b, rec_texto_calculo6b)

                            texto_calculo6c = fonte.render('RT = RL + RP = '+str(Rltotal6)+' + '+str(Rp7)+' = '+str(Rt6)+' kN', True, preto)
                            rec_texto_calculo6c = pygame.Rect(rec_texto_calculo6b.x, rec_texto_calculo6b.y + rec_texto_calculo6b.height, 700, 15)
                            janela.blit(texto_calculo6c, rec_texto_calculo6c)
                        
                        if count > 6:                            

                            texto_calculo7 = fonte.render('Para a estaca apoiada na profundidade de 7m:', True, preto)
                            rec_texto_calculo7 = pygame.Rect(rec_texto_calculo6c.x, rec_texto_calculo6c.y + rec_texto_calculo6c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo7, rec_texto_calculo7)

                            texto_calculo7a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7 = '+str(Rltotal6)+' + '+str(beta7)+'*10*'+str(circunferencia)+'*(('+NSPT7+'/3)+1))'+' = '+str(Rltotal7)+' kN', True, preto)
                            rec_texto_calculo7a = pygame.Rect(rec_texto_calculo7.x, rec_texto_calculo7.y + rec_texto_calculo7.height, 700, 15)
                            janela.blit(texto_calculo7a, rec_texto_calculo7a)

                            texto_calculo7b = fonte.render('RP = '+str(alfa8)+'*'+str(c8)+'*'+NSPT8+'*'+str(area)+' = '+str(Rp8)+' kN', True, preto)
                            rec_texto_calculo7b = pygame.Rect(rec_texto_calculo7a.x, rec_texto_calculo7a.y + rec_texto_calculo7a.height, 700, 15)
                            janela.blit(texto_calculo7b, rec_texto_calculo7b)

                            texto_calculo7c = fonte.render('RT = RL + RP = '+str(Rltotal7)+' + '+str(Rp8)+' = '+str(Rt7)+' kN', True, preto)
                            rec_texto_calculo7c = pygame.Rect(rec_texto_calculo7b.x, rec_texto_calculo7b.y + rec_texto_calculo7b.height, 700, 15)
                            janela.blit(texto_calculo7c, rec_texto_calculo7c)
                        
                        if count > 7:                            

                            texto_calculo8 = fonte.render('Para a estaca apoiada na profundidade de 8m:', True, preto)
                            rec_texto_calculo8 = pygame.Rect(rec_texto_calculo7c.x, rec_texto_calculo7c.y + rec_texto_calculo7c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo8, rec_texto_calculo8)

                            texto_calculo8a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8 = '+str(Rltotal7)+' + '+str(beta8)+'*10*'+str(circunferencia)+'*(('+NSPT8+'/3)+1))'+' = '+str(Rltotal8)+' kN', True, preto)
                            rec_texto_calculo8a = pygame.Rect(rec_texto_calculo8.x, rec_texto_calculo8.y + rec_texto_calculo8.height, 700, 15)
                            janela.blit(texto_calculo8a, rec_texto_calculo8a)

                            texto_calculo8b = fonte.render('RP = '+str(alfa9)+'*'+str(c9)+'*'+NSPT9+'*'+str(area)+' = '+str(Rp9)+' kN', True, preto)
                            rec_texto_calculo8b = pygame.Rect(rec_texto_calculo8a.x, rec_texto_calculo8a.y + rec_texto_calculo8a.height, 700, 15)
                            janela.blit(texto_calculo8b, rec_texto_calculo8b)

                            texto_calculo8c = fonte.render('RT = RL + RP = '+str(Rltotal8)+' + '+str(Rp9)+' = '+str(Rt8)+' kN', True, preto)
                            rec_texto_calculo8c = pygame.Rect(rec_texto_calculo8b.x, rec_texto_calculo8b.y + rec_texto_calculo8b.height, 700, 15)
                            janela.blit(texto_calculo8c, rec_texto_calculo8c)
                        
                        if count > 8:

                            texto_calculo9 = fonte.render('Para a estaca apoiada na profundidade de 9m:', True, preto)
                            rec_texto_calculo9 = pygame.Rect(rec_texto_calculo8c.x, rec_texto_calculo8c.y + rec_texto_calculo8c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo9, rec_texto_calculo9)

                            texto_calculo9a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9 = '+str(Rltotal8)+' + '+str(beta9)+'*10*'+str(circunferencia)+'*(('+NSPT9+'/3)+1))'+' = '+str(Rltotal9)+' kN', True, preto)
                            rec_texto_calculo9a = pygame.Rect(rec_texto_calculo9.x, rec_texto_calculo9.y + rec_texto_calculo9.height, 700, 15)
                            janela.blit(texto_calculo9a, rec_texto_calculo9a)

                            texto_calculo9b = fonte.render('RP = '+str(alfa10)+'*'+str(c10)+'*'+NSPT10+'*'+str(area)+' = '+str(Rp10)+' kN', True, preto)
                            rec_texto_calculo9b = pygame.Rect(rec_texto_calculo9a.x, rec_texto_calculo9a.y + rec_texto_calculo9a.height, 700, 15)
                            janela.blit(texto_calculo9b, rec_texto_calculo9b)

                            texto_calculo9c = fonte.render('RT = RL + RP = '+str(Rltotal9)+' + '+str(Rp10)+' = '+str(Rt9)+' kN', True, preto)
                            rec_texto_calculo9c = pygame.Rect(rec_texto_calculo9b.x, rec_texto_calculo9b.y + rec_texto_calculo9b.height, 700, 15)
                            janela.blit(texto_calculo9c, rec_texto_calculo9c)
                        
                    if pcount == 2:

                        if count > 9:
                            
                            texto_calculo10 = fonte.render('Para a estaca apoiada na profundidade de 10m:', True, preto)
                            rec_texto_calculo10 = pygame.Rect(rec_texto_calculo2.x, rec_texto_calculo2.y, 700, 15)
                            janela.blit(texto_calculo10, rec_texto_calculo10)

                            texto_calculo10a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10 = '+str(Rltotal9)+' + '+str(beta10)+'*10*'+str(circunferencia)+'*(('+NSPT10+'/3)+1))'+' = '+str(Rltotal10)+' kN', True, preto)
                            rec_texto_calculo10a = pygame.Rect(rec_texto_calculo10.x, rec_texto_calculo10.y + rec_texto_calculo10.height, 700, 15)
                            janela.blit(texto_calculo10a, rec_texto_calculo10a)

                            texto_calculo10b = fonte.render('RP = '+str(alfa11)+'*'+str(c11)+'*'+NSPT11+'*'+str(area)+' = '+str(Rp11)+' kN', True, preto)
                            rec_texto_calculo10b = pygame.Rect(rec_texto_calculo10a.x, rec_texto_calculo10a.y + rec_texto_calculo10a.height, 700, 15)
                            janela.blit(texto_calculo10b, rec_texto_calculo10b)

                            texto_calculo10c = fonte.render('RT = RL + RP = '+str(Rltotal10)+' + '+str(Rp11)+' = '+str(Rt10)+' kN', True, preto)
                            rec_texto_calculo10c = pygame.Rect(rec_texto_calculo10b.x, rec_texto_calculo10b.y + rec_texto_calculo10b.height, 700, 15)
                            janela.blit(texto_calculo10c, rec_texto_calculo10c)
                        
                        if count > 10:                            

                            texto_calculo11 = fonte.render('Para a estaca apoiada na profundidade de 11m:', True, preto)
                            rec_texto_calculo11 = pygame.Rect(rec_texto_calculo10c.x, rec_texto_calculo10c.y + rec_texto_calculo10c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo11, rec_texto_calculo11)

                            texto_calculo11a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11 = '+str(Rltotal10)+' + '+str(beta11)+'*10*'+str(circunferencia)+'*(('+NSPT11+'/3)+1))'+' = '+str(Rltotal11)+' kN', True, preto)
                            rec_texto_calculo11a = pygame.Rect(rec_texto_calculo11.x, rec_texto_calculo11.y + rec_texto_calculo11.height, 700, 15)
                            janela.blit(texto_calculo11a, rec_texto_calculo11a)

                            texto_calculo11b = fonte.render('RP = '+str(alfa12)+'*'+str(c12)+'*'+NSPT12+'*'+str(area)+' = '+str(Rp12)+' kN', True, preto)
                            rec_texto_calculo11b = pygame.Rect(rec_texto_calculo11a.x, rec_texto_calculo11a.y + rec_texto_calculo11a.height, 700, 15)
                            janela.blit(texto_calculo11b, rec_texto_calculo11b)

                            texto_calculo11c = fonte.render('RT = RL + RP = '+str(Rltotal11)+' + '+str(Rp12)+' = '+str(Rt11)+' kN', True, preto)
                            rec_texto_calculo11c = pygame.Rect(rec_texto_calculo11b.x, rec_texto_calculo11b.y + rec_texto_calculo11b.height, 700, 15)
                            janela.blit(texto_calculo11c, rec_texto_calculo11c)
                        
                        if count > 11:                            

                            texto_calculo12 = fonte.render('Para a estaca apoiada na profundidade de 12m:', True, preto)
                            rec_texto_calculo12 = pygame.Rect(rec_texto_calculo11c.x, rec_texto_calculo11c.y + rec_texto_calculo11c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo12, rec_texto_calculo12)

                            texto_calculo12a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12 = '+str(Rltotal11)+' + '+str(beta12)+'*10*'+str(circunferencia)+'*(('+NSPT12+'/3)+1))'+' = '+str(Rltotal12)+' kN', True, preto)
                            rec_texto_calculo12a = pygame.Rect(rec_texto_calculo12.x, rec_texto_calculo12.y + rec_texto_calculo12.height, 700, 15)
                            janela.blit(texto_calculo12a, rec_texto_calculo12a)

                            texto_calculo12b = fonte.render('RP = '+str(alfa13)+'*'+str(c13)+'*'+NSPT13+'*'+str(area)+' = '+str(Rp13)+' kN', True, preto)
                            rec_texto_calculo12b = pygame.Rect(rec_texto_calculo12a.x, rec_texto_calculo12a.y + rec_texto_calculo12a.height, 700, 15)
                            janela.blit(texto_calculo12b, rec_texto_calculo12b)

                            texto_calculo12c = fonte.render('RT = RL + RP = '+str(Rltotal12)+' + '+str(Rp13)+' = '+str(Rt12)+' kN', True, preto)
                            rec_texto_calculo12c = pygame.Rect(rec_texto_calculo12b.x, rec_texto_calculo12b.y + rec_texto_calculo12b.height, 700, 15)
                            janela.blit(texto_calculo12c, rec_texto_calculo12c)
                        
                        if count > 12:                            

                            texto_calculo13 = fonte.render('Para a estaca apoiada na profundidade de 13m:', True, preto)
                            rec_texto_calculo13 = pygame.Rect(rec_texto_calculo12c.x, rec_texto_calculo12c.y + rec_texto_calculo12c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo13, rec_texto_calculo13)

                            texto_calculo13a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13 = '+str(Rltotal12)+' + '+str(beta13)+'*10*'+str(circunferencia)+'*(('+NSPT13+'/3)+1))'+' = '+str(Rltotal13)+' kN', True, preto)
                            rec_texto_calculo13a = pygame.Rect(rec_texto_calculo13.x, rec_texto_calculo13.y + rec_texto_calculo13.height, 700, 15)
                            janela.blit(texto_calculo13a, rec_texto_calculo13a)

                            texto_calculo13b = fonte.render('RP = '+str(alfa14)+'*'+str(c14)+'*'+NSPT14+'*'+str(area)+' = '+str(Rp14)+' kN', True, preto)
                            rec_texto_calculo13b = pygame.Rect(rec_texto_calculo13a.x, rec_texto_calculo13a.y + rec_texto_calculo13a.height, 700, 15)
                            janela.blit(texto_calculo13b, rec_texto_calculo13b)

                            texto_calculo13c = fonte.render('RT = RL + RP = '+str(Rltotal13)+' + '+str(Rp14)+' = '+str(Rt13)+' kN', True, preto)
                            rec_texto_calculo13c = pygame.Rect(rec_texto_calculo13b.x, rec_texto_calculo13b.y + rec_texto_calculo13b.height, 700, 15)
                            janela.blit(texto_calculo13c, rec_texto_calculo13c)
                        
                    if pcount == 3:

                        if count > 13:

                            texto_calculo14 = fonte.render('Para a estaca apoiada na profundidade de 14m:', True, preto)
                            rec_texto_calculo14 = pygame.Rect(rec_texto_calculo2.x, rec_texto_calculo2.y, 700, 15)
                            janela.blit(texto_calculo14, rec_texto_calculo14)

                            texto_calculo14a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13+Rl14 = '+str(Rltotal13)+' + '+str(beta14)+'*10*'+str(circunferencia)+'*(('+NSPT14+'/3)+1))'+' = '+str(Rltotal14)+' kN', True, preto)
                            rec_texto_calculo14a = pygame.Rect(rec_texto_calculo14.x, rec_texto_calculo14.y + rec_texto_calculo14.height, 700, 15)
                            janela.blit(texto_calculo14a, rec_texto_calculo14a)

                            texto_calculo14b = fonte.render('RP = '+str(alfa15)+'*'+str(c15)+'*'+NSPT15+'*'+str(area)+' = '+str(Rp15)+' kN', True, preto)
                            rec_texto_calculo14b = pygame.Rect(rec_texto_calculo14a.x, rec_texto_calculo14a.y + rec_texto_calculo14a.height, 700, 15)
                            janela.blit(texto_calculo14b, rec_texto_calculo14b)

                            texto_calculo14c = fonte.render('RT = RL + RP = '+str(Rltotal14)+' + '+str(Rp15)+' = '+str(Rt14)+' kN', True, preto)
                            rec_texto_calculo14c = pygame.Rect(rec_texto_calculo14b.x, rec_texto_calculo14b.y + rec_texto_calculo14b.height, 700, 15)
                            janela.blit(texto_calculo14c, rec_texto_calculo14c)

                        if count > 14:

                            texto_calculo15 = fonte.render('Para a estaca apoiada na profundidade de 15m:', True, preto)
                            rec_texto_calculo15 = pygame.Rect(rec_texto_calculo14c.x, rec_texto_calculo14c.y + rec_texto_calculo14c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo15, rec_texto_calculo15)

                            texto_calculo15a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13+Rl14+Rl15 = '+str(Rltotal14)+' + '+str(beta15)+'*10*'+str(circunferencia)+'*(('+NSPT15+'/3)+1))'+' = '+str(Rltotal15)+' kN', True, preto)
                            rec_texto_calculo15a = pygame.Rect(rec_texto_calculo15.x, rec_texto_calculo15.y + rec_texto_calculo15.height, 700, 15)
                            janela.blit(texto_calculo15a, rec_texto_calculo15a)

                            texto_calculo15b = fonte.render('RP = '+str(alfa16)+'*'+str(c16)+'*'+NSPT16+'*'+str(area)+' = '+str(Rp16)+' kN', True, preto)
                            rec_texto_calculo15b = pygame.Rect(rec_texto_calculo15a.x, rec_texto_calculo15a.y + rec_texto_calculo15a.height, 700, 15)
                            janela.blit(texto_calculo15b, rec_texto_calculo15b)

                            texto_calculo15c = fonte.render('RT = RL + RP = '+str(Rltotal15)+' + '+str(Rp16)+' = '+str(Rt15)+' kN', True, preto)
                            rec_texto_calculo15c = pygame.Rect(rec_texto_calculo15b.x, rec_texto_calculo15b.y + rec_texto_calculo15b.height, 700, 15)
                            janela.blit(texto_calculo15c, rec_texto_calculo15c)
                        
                        if count > 15:

                            texto_calculo16 = fonte.render('Para a estaca apoiada na profundidade de 16m:', True, preto)
                            rec_texto_calculo16 = pygame.Rect(rec_texto_calculo15c.x, rec_texto_calculo15c.y + rec_texto_calculo15c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo16, rec_texto_calculo16)

                            texto_calculo16a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13+Rl14+Rl15+Rl16 = '+str(Rltotal15)+' + '+str(beta16)+'*10*'+str(circunferencia)+'*(('+NSPT16+'/3)+1))'+' = '+str(Rltotal16)+' kN', True, preto)
                            rec_texto_calculo16a = pygame.Rect(rec_texto_calculo16.x, rec_texto_calculo16.y + rec_texto_calculo16.height, 700, 15)
                            janela.blit(texto_calculo16a, rec_texto_calculo16a)

                            texto_calculo16b = fonte.render('RP = '+str(alfa17)+'*'+str(c17)+'*'+NSPT17+'*'+str(area)+' = '+str(Rp17)+' kN', True, preto)
                            rec_texto_calculo16b = pygame.Rect(rec_texto_calculo16a.x, rec_texto_calculo16a.y + rec_texto_calculo16a.height, 700, 15)
                            janela.blit(texto_calculo16b, rec_texto_calculo16b)

                            texto_calculo16c = fonte.render('RT = RL + RP = '+str(Rltotal16)+' + '+str(Rp17)+' = '+str(Rt16)+' kN', True, preto)
                            rec_texto_calculo16c = pygame.Rect(rec_texto_calculo16b.x, rec_texto_calculo16b.y + rec_texto_calculo16b.height, 700, 15)
                            janela.blit(texto_calculo16c, rec_texto_calculo16c)
                        
                        if count > 16:

                            texto_calculo17 = fonte.render('Para a estaca apoiada na profundidade de 17m:', True, preto)
                            rec_texto_calculo17 = pygame.Rect(rec_texto_calculo16c.x, rec_texto_calculo16c.y + rec_texto_calculo16c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo17, rec_texto_calculo17)

                            texto_calculo17a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13+Rl14+Rl15+Rl16+Rl17 = '+str(Rltotal16)+' + '+str(beta17)+'*10*'+str(circunferencia)+'*(('+NSPT17+'/3)+1))'+' = '+str(Rltotal17)+' kN', True, preto)
                            rec_texto_calculo17a = pygame.Rect(rec_texto_calculo17.x, rec_texto_calculo17.y + rec_texto_calculo17.height, 700, 15)
                            janela.blit(texto_calculo17a, rec_texto_calculo17a)

                            texto_calculo17b = fonte.render('RP = '+str(alfa18)+'*'+str(c18)+'*'+NSPT18+'*'+str(area)+' = '+str(Rp18)+' kN', True, preto)
                            rec_texto_calculo17b = pygame.Rect(rec_texto_calculo17a.x, rec_texto_calculo17a.y + rec_texto_calculo17a.height, 700, 15)
                            janela.blit(texto_calculo17b, rec_texto_calculo17b)

                            texto_calculo17c = fonte.render('RT = RL + RP = '+str(Rltotal17)+' + '+str(Rp18)+' = '+str(Rt17)+' kN', True, preto)
                            rec_texto_calculo17c = pygame.Rect(rec_texto_calculo17b.x, rec_texto_calculo17b.y + rec_texto_calculo17b.height, 700, 15)
                            janela.blit(texto_calculo17c, rec_texto_calculo17c)
                    
                    if pcount == 4:

                        if count > 17:

                            texto_calculo18 = fonte.render('Para a estaca apoiada na profundidade de 18m:', True, preto)
                            rec_texto_calculo18 = pygame.Rect(rec_texto_calculo2.x, rec_texto_calculo2.y, 700, 15)
                            janela.blit(texto_calculo18, rec_texto_calculo18)

                            texto_calculo18a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13+Rl14+Rl15+Rl16+Rl17+Rl18', True, preto)
                            rec_texto_calculo18a = pygame.Rect(rec_texto_calculo18.x, rec_texto_calculo18.y + rec_texto_calculo18.height, 700, 15)
                            janela.blit(texto_calculo18a, rec_texto_calculo18a)

                            texto_calculo18b = fonte.render('RL = '+str(Rltotal17)+' + '+str(beta18)+'*10*'+str(circunferencia)+'*(('+NSPT18+'/3)+1))'+' = '+str(Rltotal18)+' kN', True, preto)
                            rec_texto_calculo18b = pygame.Rect(rec_texto_calculo18a.x, rec_texto_calculo18a.y + rec_texto_calculo18a.height, 700, 15)
                            janela.blit(texto_calculo18b, rec_texto_calculo18b)

                            texto_calculo18c = fonte.render('RP = '+str(alfa19)+'*'+str(c19)+'*'+NSPT19+'*'+str(area)+' = '+str(Rp19)+' kN', True, preto)
                            rec_texto_calculo18c = pygame.Rect(rec_texto_calculo18b.x, rec_texto_calculo18b.y + rec_texto_calculo18b.height, 700, 15)
                            janela.blit(texto_calculo18c, rec_texto_calculo18c)

                            texto_calculo18d = fonte.render('RT = RL + RP = '+str(Rltotal18)+' + '+str(Rp19)+' = '+str(Rt18)+' kN', True, preto)
                            rec_texto_calculo18d = pygame.Rect(rec_texto_calculo18c.x, rec_texto_calculo18c.y + rec_texto_calculo18c.height, 700, 15)
                            janela.blit(texto_calculo18d, rec_texto_calculo18d)
                        
                        if count > 18:

                            texto_calculo19 = fonte.render('Para a estaca apoiada na profundidade de 19m:', True, preto)
                            rec_texto_calculo19 = pygame.Rect(rec_texto_calculo18d.x, rec_texto_calculo18d.y + rec_texto_calculo18d.height + 5, 700, 15)
                            janela.blit(texto_calculo19, rec_texto_calculo19)

                            texto_calculo19a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13+Rl14+Rl15+Rl16+Rl17+Rl18+Rl19', True, preto)
                            rec_texto_calculo19a = pygame.Rect(rec_texto_calculo19.x, rec_texto_calculo19.y + rec_texto_calculo19.height, 700, 15)
                            janela.blit(texto_calculo19a, rec_texto_calculo19a)

                            texto_calculo19b = fonte.render('RL = '+str(Rltotal18)+' + '+str(beta19)+'*10*'+str(circunferencia)+'*(('+NSPT19+'/3)+1))'+' = '+str(Rltotal19)+' kN', True, preto)
                            rec_texto_calculo19b = pygame.Rect(rec_texto_calculo19a.x, rec_texto_calculo19a.y + rec_texto_calculo19a.height, 700, 15)
                            janela.blit(texto_calculo19b, rec_texto_calculo19b)

                            texto_calculo19c = fonte.render('RP = '+str(alfa20)+'*'+str(c20)+'*'+NSPT20+'*'+str(area)+' = '+str(Rp20)+' kN', True, preto)
                            rec_texto_calculo19c = pygame.Rect(rec_texto_calculo19b.x, rec_texto_calculo19b.y + rec_texto_calculo19b.height, 700, 15)
                            janela.blit(texto_calculo19c, rec_texto_calculo19c)

                            texto_calculo19d = fonte.render('RT = RL + RP = '+str(Rltotal19)+' + '+str(Rp20)+' = '+str(Rt19)+' kN', True, preto)
                            rec_texto_calculo19d = pygame.Rect(rec_texto_calculo19c.x, rec_texto_calculo19c.y + rec_texto_calculo19c.height, 700, 15)
                            janela.blit(texto_calculo19d, rec_texto_calculo19d)
                        
                        if count > 19:

                            texto_calculo20 = fonte.render('Para a estaca apoiada na profundidade de 20m:', True, preto)
                            rec_texto_calculo20 = pygame.Rect(rec_texto_calculo19d.x, rec_texto_calculo19d.y + rec_texto_calculo19d.height + 5, 700, 15)
                            janela.blit(texto_calculo20, rec_texto_calculo20)

                            texto_calculo20a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13+Rl14+Rl15+Rl16+Rl17+Rl18+Rl19+Rl20', True, preto)
                            rec_texto_calculo20a = pygame.Rect(rec_texto_calculo20.x, rec_texto_calculo20.y + rec_texto_calculo20.height, 700, 15)
                            janela.blit(texto_calculo20a, rec_texto_calculo20a)

                            texto_calculo20b = fonte.render('RL = '+str(Rltotal19)+' + '+str(beta20)+'*10*'+str(circunferencia)+'*(('+NSPT20+'/3)+1))'+' = '+str(Rltotal20)+' kN', True, preto)
                            rec_texto_calculo20b = pygame.Rect(rec_texto_calculo20a.x, rec_texto_calculo20a.y + rec_texto_calculo20a.height, 700, 15)
                            janela.blit(texto_calculo20b, rec_texto_calculo20b)

                            texto_calculo20c = fonte.render('RP = '+str(alfa21)+'*'+str(c21)+'*'+NSPT21+'*'+str(area)+' = '+str(Rp21)+' kN', True, preto)
                            rec_texto_calculo20c = pygame.Rect(rec_texto_calculo20b.x, rec_texto_calculo20b.y + rec_texto_calculo20b.height, 700, 15)
                            janela.blit(texto_calculo20c, rec_texto_calculo20c)

                            texto_calculo20d = fonte.render('RT = RL + RP = '+str(Rltotal20)+' + '+str(Rp21)+' = '+str(Rt20)+' kN', True, preto)
                            rec_texto_calculo20d = pygame.Rect(rec_texto_calculo20c.x, rec_texto_calculo20c.y + rec_texto_calculo20c.height, 700, 15)
                            janela.blit(texto_calculo20d, rec_texto_calculo20d)
                        
                        if count > 20:

                            texto_calculo21 = fonte.render('Para a estaca apoiada na profundidade de 21m:', True, preto)
                            rec_texto_calculo21 = pygame.Rect(rec_texto_calculo20d.x, rec_texto_calculo20d.y + rec_texto_calculo20d.height + 5, 700, 15)
                            janela.blit(texto_calculo21, rec_texto_calculo21)

                            texto_calculo21a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13+Rl14+Rl15+Rl16+Rl17+Rl18+Rl19+Rl20+Rl21', True, preto)
                            rec_texto_calculo21a = pygame.Rect(rec_texto_calculo21.x, rec_texto_calculo21.y + rec_texto_calculo21.height, 700, 15)
                            janela.blit(texto_calculo21a, rec_texto_calculo21a)

                            texto_calculo21b = fonte.render('RL = '+str(Rltotal20)+' + '+str(beta21)+'*10*'+str(circunferencia)+'*(('+NSPT21+'/3)+1))'+' = '+str(Rltotal21)+' kN', True, preto)
                            rec_texto_calculo21b = pygame.Rect(rec_texto_calculo21a.x, rec_texto_calculo21a.y + rec_texto_calculo21a.height, 700, 15)
                            janela.blit(texto_calculo21b, rec_texto_calculo21b)

                            texto_calculo21c = fonte.render('RP = '+str(alfa22)+'*'+str(c22)+'*'+NSPT22+'*'+str(area)+' = '+str(Rp22)+' kN', True, preto)
                            rec_texto_calculo21c = pygame.Rect(rec_texto_calculo21b.x, rec_texto_calculo21b.y + rec_texto_calculo21b.height, 700, 15)
                            janela.blit(texto_calculo21c, rec_texto_calculo21c)

                            texto_calculo21d = fonte.render('RT = RL + RP = '+str(Rltotal21)+' + '+str(Rp22)+' = '+str(Rt21)+' kN', True, preto)
                            rec_texto_calculo21d = pygame.Rect(rec_texto_calculo21c.x, rec_texto_calculo21c.y + rec_texto_calculo21c.height, 700, 15)
                            janela.blit(texto_calculo21d, rec_texto_calculo21d)
                    
                    if pcount == 5:

                        if count > 21:

                            texto_calculo22 = fonte.render('Para a estaca apoiada na profundidade de 22m:', True, preto)
                            rec_texto_calculo22 = pygame.Rect(rec_texto_calculo2.x, rec_texto_calculo2.y, 700, 15)
                            janela.blit(texto_calculo22, rec_texto_calculo22)

                            texto_calculo22a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13+Rl14+Rl15+Rl16+Rl17+Rl18+Rl19+Rl20+Rl21+Rl22', True, preto)
                            rec_texto_calculo22a = pygame.Rect(rec_texto_calculo22.x, rec_texto_calculo22.y + rec_texto_calculo22.height, 700, 15)
                            janela.blit(texto_calculo22a, rec_texto_calculo22a)

                            texto_calculo22b = fonte.render('RL = '+str(Rltotal21)+' + '+str(beta22)+'*10*'+str(circunferencia)+'*(('+NSPT22+'/3)+1))'+' = '+str(Rltotal22)+' kN', True, preto)
                            rec_texto_calculo22b = pygame.Rect(rec_texto_calculo22a.x, rec_texto_calculo22a.y + rec_texto_calculo22a.height, 700, 15)
                            janela.blit(texto_calculo22b, rec_texto_calculo22b)

                            texto_calculo22c = fonte.render('RP = '+str(alfa23)+'*'+str(c23)+'*'+NSPT23+'*'+str(area)+' = '+str(Rp23)+' kN', True, preto)
                            rec_texto_calculo22c = pygame.Rect(rec_texto_calculo22b.x, rec_texto_calculo22b.y + rec_texto_calculo22b.height, 700, 15)
                            janela.blit(texto_calculo22c, rec_texto_calculo22c)

                            texto_calculo22d = fonte.render('RT = RL + RP = '+str(Rltotal22)+' + '+str(Rp23)+' = '+str(Rt23)+' kN', True, preto)
                            rec_texto_calculo22d = pygame.Rect(rec_texto_calculo22c.x, rec_texto_calculo22c.y + rec_texto_calculo22c.height, 700, 15)
                            janela.blit(texto_calculo22d, rec_texto_calculo22d)
                        
                        if count > 22:

                            texto_calculo23 = fonte.render('Para a estaca apoiada na profundidade de 23m:', True, preto)
                            rec_texto_calculo23 = pygame.Rect(rec_texto_calculo22d.x, rec_texto_calculo22d.y + rec_texto_calculo22d.height + 5, 700, 15)
                            janela.blit(texto_calculo23, rec_texto_calculo23)

                            texto_calculo23a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13+Rl14+Rl15+Rl16+Rl17+Rl18+Rl19+Rl20+Rl21+Rl22+Rl23', True, preto)
                            rec_texto_calculo23a = pygame.Rect(rec_texto_calculo23.x, rec_texto_calculo23.y + rec_texto_calculo23.height, 700, 15)
                            janela.blit(texto_calculo23a, rec_texto_calculo23a)

                            texto_calculo23b = fonte.render('RL = '+str(Rltotal22)+' + '+str(beta23)+'*10*'+str(circunferencia)+'*(('+NSPT23+'/3)+1))'+' = '+str(Rltotal23)+' kN', True, preto)
                            rec_texto_calculo23b = pygame.Rect(rec_texto_calculo23a.x, rec_texto_calculo23a.y + rec_texto_calculo23a.height, 700, 15)
                            janela.blit(texto_calculo23b, rec_texto_calculo23b)

                            texto_calculo23c = fonte.render('RP = '+str(alfa24)+'*'+str(c24)+'*'+NSPT24+'*'+str(area)+' = '+str(Rp24)+' kN', True, preto)
                            rec_texto_calculo23c = pygame.Rect(rec_texto_calculo23b.x, rec_texto_calculo23b.y + rec_texto_calculo23b.height, 700, 15)
                            janela.blit(texto_calculo23c, rec_texto_calculo23c)

                            texto_calculo23d = fonte.render('RT = RL + RP = '+str(Rltotal23)+' + '+str(Rp24)+' = '+str(Rt23)+' kN', True, preto)
                            rec_texto_calculo23d = pygame.Rect(rec_texto_calculo23c.x, rec_texto_calculo23c.y + rec_texto_calculo23c.height, 700, 15)
                            janela.blit(texto_calculo23d, rec_texto_calculo23d)
                        
                        if count > 23:

                            texto_calculo24 = fonte.render('Para a estaca apoiada na profundidade de 24m:', True, preto)
                            rec_texto_calculo24 = pygame.Rect(rec_texto_calculo23d.x, rec_texto_calculo23d.y + rec_texto_calculo23d.height + 5, 700, 15)
                            janela.blit(texto_calculo24, rec_texto_calculo24)

                            texto_calculo24a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13+Rl14+Rl15+Rl16+Rl17+Rl18+Rl19+Rl20+Rl21+Rl22+Rl23+Rl24', True, preto)
                            rec_texto_calculo24a = pygame.Rect(rec_texto_calculo24.x, rec_texto_calculo24.y + rec_texto_calculo24.height, 700, 15)
                            janela.blit(texto_calculo24a, rec_texto_calculo24a)

                            texto_calculo24b = fonte.render('RL = '+str(Rltotal23)+' + '+str(beta24)+'*10*'+str(circunferencia)+'*(('+NSPT24+'/3)+1))'+' = '+str(Rltotal24)+' kN', True, preto)
                            rec_texto_calculo24b = pygame.Rect(rec_texto_calculo24a.x, rec_texto_calculo24a.y + rec_texto_calculo24a.height, 700, 15)
                            janela.blit(texto_calculo24b, rec_texto_calculo24b)

                            texto_calculo24c = fonte.render('RP = '+str(alfa25)+'*'+str(c25)+'*'+NSPT25+'*'+str(area)+' = '+str(Rp25)+' kN', True, preto)
                            rec_texto_calculo24c = pygame.Rect(rec_texto_calculo24b.x, rec_texto_calculo24b.y + rec_texto_calculo24b.height, 700, 15)
                            janela.blit(texto_calculo24c, rec_texto_calculo24c)

                            texto_calculo24d = fonte.render('RT = RL + RP = '+str(Rltotal24)+' + '+str(Rp25)+' = '+str(Rt24)+' kN', True, preto)
                            rec_texto_calculo24d = pygame.Rect(rec_texto_calculo24c.x, rec_texto_calculo24c.y + rec_texto_calculo24c.height, 700, 15)
                            janela.blit(texto_calculo24d, rec_texto_calculo24d)

                if metodo_selecionado == 'AOKI & VELLOSO':

                    Rp3 = round((k3*1000*int(NSPT3)*area)/f1, 2)
                    Rl2 = (alfa2*k2*1000*int(NSPT2)*circunferencia)/f2
                    Rltotal2 = round(Rl2, 2)
                    Rt2 = round(Rp3 + Rltotal2, 2)

                    Rp4 = round((k4*1000*int(NSPT4)*area)/f1, 2)
                    Rl3 = (alfa3*k3*1000*int(NSPT3)*circunferencia)/f2
                    Rltotal3 = round(Rltotal2 + Rl3, 2)
                    Rt3 = round(Rp4 + Rltotal3, 2)

                    Rp5 = round((k5*1000*int(NSPT5)*area)/f1, 2)
                    Rl4 = (alfa4*k4*1000*int(NSPT4)*circunferencia)/f2
                    Rltotal4 = round(Rltotal3 + Rl4, 2)
                    Rt4 = round(Rp5 + Rltotal4, 2)

                    Rp6 = round((k6*1000*int(NSPT6)*area)/f1, 2)
                    Rl5 = (alfa5*k5*1000*int(NSPT5)*circunferencia)/f2
                    Rltotal5 = round(Rltotal4 + Rl5, 2)
                    Rt5 = round(Rp6 + Rltotal5, 2)

                    Rp7 = round((k7*1000*int(NSPT7)*area)/f1, 2)
                    Rl6 = (alfa6*k6*1000*int(NSPT6)*circunferencia)/f2
                    Rltotal6 = round(Rltotal5 + Rl6, 2)
                    Rt6 = round(Rp7 + Rltotal6, 2)

                    Rp8 = round((k8*1000*int(NSPT8)*area)/f1, 2)
                    Rl7 = (alfa7*k7*1000*int(NSPT7)*circunferencia)/f2
                    Rltotal7 = round(Rltotal6 + Rl7, 2)
                    Rt7 = round(Rp8 + Rltotal7, 2)

                    Rp9 = round((k9*1000*int(NSPT9)*area)/f1, 2)
                    Rl8 = (alfa8*k8*1000*int(NSPT8)*circunferencia)/f2
                    Rltotal8 = round(Rltotal7 + Rl8, 2)
                    Rt8 = round(Rp9 + Rltotal8, 2)

                    Rp10 = round((k10*1000*int(NSPT10)*area)/f1, 2)
                    Rl9 = (alfa9*k9*1000*int(NSPT9)*circunferencia)/f2
                    Rltotal9 = round(Rltotal8 + Rl9, 2)
                    Rt9 = round(Rp10 + Rltotal9, 2)

                    Rp11 = round((k11*1000*int(NSPT11)*area)/f1, 2)
                    Rl10 = (alfa10*k10*1000*int(NSPT10)*circunferencia)/f2
                    Rltotal10 = round(Rltotal9 + Rl10, 2)
                    Rt10 = round(Rp11 + Rltotal10, 2)

                    Rp12 = round((k12*1000*int(NSPT12)*area)/f1, 2)
                    Rl11 = (alfa11*k11*1000*int(NSPT11)*circunferencia)/f2
                    Rltotal11 = round(Rltotal10 + Rl11, 2)
                    Rt11 = round(Rp12 + Rltotal11, 2)

                    Rp13 = round((k13*1000*int(NSPT13)*area)/f1, 2)
                    Rl12 = (alfa12*k12*1000*int(NSPT12)*circunferencia)/f2
                    Rltotal12 = round(Rltotal11 + Rl12, 2)
                    Rt12 = round(Rp13 + Rltotal12, 2)

                    Rp14 = round((k14*1000*int(NSPT14)*area)/f1, 2)
                    Rl13 = (alfa13*k13*1000*int(NSPT13)*circunferencia)/f2
                    Rltotal13 = round(Rltotal12 + Rl13, 2)
                    Rt13 = round(Rp14 + Rltotal13, 2)

                    Rp15 = round((k15*1000*int(NSPT15)*area)/f1, 2)
                    Rl14 = (alfa14*k14*1000*int(NSPT14)*circunferencia)/f2
                    Rltotal14 = round(Rltotal13 + Rl14, 2)
                    Rt14 = round(Rp15 + Rltotal14, 2)

                    Rp16 = round((k16*1000*int(NSPT16)*area)/f1, 2)
                    Rl15 = (alfa15*k15*1000*int(NSPT15)*circunferencia)/f2
                    Rltotal15 = round(Rltotal14 + Rl15, 2)
                    Rt15 = round(Rp16 + Rltotal15, 2)

                    Rp17 = round((k17*1000*int(NSPT17)*area)/f1, 2)
                    Rl16 = (alfa16*k16*1000*int(NSPT16)*circunferencia)/f2
                    Rltotal16 = round(Rltotal15 + Rl16, 2)
                    Rt16 = round(Rp17 + Rltotal16, 2)

                    Rp18 = round((k18*1000*int(NSPT18)*area)/f1, 2)
                    Rl17 = (alfa17*k17*1000*int(NSPT17)*circunferencia)/f2
                    Rltotal17 = round(Rltotal16 + Rl17, 2)
                    Rt17 = round(Rp18 + Rltotal17, 2)

                    Rp19 = round((k19*1000*int(NSPT19)*area)/f1, 2)
                    Rl18 = (alfa18*k18*1000*int(NSPT18)*circunferencia)/f2
                    Rltotal18 = round(Rltotal17 + Rl18, 2)
                    Rt18 = round(Rp19 + Rltotal18, 2)

                    Rp20 = round((k20*1000*int(NSPT20)*area)/f1, 2)
                    Rl19 = (alfa19*k19*1000*int(NSPT19)*circunferencia)/f2
                    Rltotal19 = round(Rltotal18 + Rl19, 2)
                    Rt19 = round(Rp20 + Rltotal19, 2)

                    Rp21 = round((k21*1000*int(NSPT21)*area)/f1, 2)
                    Rl20 = (alfa20*k20*1000*int(NSPT20)*circunferencia)/f2
                    Rltotal20 = round(Rltotal19 + Rl20, 2)
                    Rt20 = round(Rp21 + Rltotal20, 2)

                    Rp22 = round((k22*1000*int(NSPT22)*area)/f1, 2)
                    Rl21 = (alfa21*k21*1000*int(NSPT21)*circunferencia)/f2
                    Rltotal21 = round(Rltotal20 + Rl21, 2)
                    Rt21 = round(Rp22 + Rltotal21, 2)

                    Rp23 = round((k23*1000*int(NSPT23)*area)/f1, 2)
                    Rl22 = (alfa22*k22*1000*int(NSPT22)*circunferencia)/f2
                    Rltotal22 = round(Rltotal21 + Rl22, 2)
                    Rt22 = round(Rp23 + Rltotal22, 2)

                    Rp24 = round((k24*1000*int(NSPT24)*area)/f1, 2)
                    Rl23 = (alfa23*k23*1000*int(NSPT23)*circunferencia)/f2
                    Rltotal23 = round(Rltotal22 + Rl23, 2)
                    Rt23 = round(Rp24 + Rltotal23, 2)

                    Rp25 = round((k25*1000*int(NSPT25)*area)/f1, 2)
                    Rl24 = (alfa24*k24*1000*int(NSPT24)*circunferencia)/f2
                    Rltotal24 = round(Rltotal23 + Rl24, 2)
                    Rt24 = round(Rp25 + Rltotal24, 2)

                    if pcount == 0:

                        if count > 1:

                            texto_calculo2 = fonte.render('Para a estaca apoiada na profundidade de 2m:', True, preto)
                            rec_texto_calculo2 = pygame.Rect(rec_texto_calculo1b.x, rec_texto_calculo1b.y + rec_texto_calculo1b.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo2, rec_texto_calculo2)

                            texto_calculo2a = fonte.render('RL = Rl2 = ('+str(alfa2)+'*'+str(k2*1000)+'*'+NSPT2+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal2)+' kN', True, preto)
                            rec_texto_calculo2a = pygame.Rect(rec_texto_calculo2.x, rec_texto_calculo2.y + rec_texto_calculo2.height, 700, 15)
                            janela.blit(texto_calculo2a, rec_texto_calculo2a)

                            texto_calculo2b = fonte.render('RP = ('+str(k3*1000)+'*'+NSPT3+'*'+str(area)+')/'+str(f1)+' = '+str(Rp3)+' kN', True, preto)
                            rec_texto_calculo2b = pygame.Rect(rec_texto_calculo2a.x, rec_texto_calculo2a.y + rec_texto_calculo2a.height, 700, 15)
                            janela.blit(texto_calculo2b, rec_texto_calculo2b)

                            texto_calculo2c = fonte.render('RT = RL + RP = '+str(Rltotal2)+' + '+str(Rp3)+' = '+str(Rt2)+' kN', True, preto)
                            rec_texto_calculo2c = pygame.Rect(rec_texto_calculo2b.x, rec_texto_calculo2b.y + rec_texto_calculo2b.height, 700, 15)
                            janela.blit(texto_calculo2c, rec_texto_calculo2c)

                        if count > 2:                            

                            texto_calculo3 = fonte.render('Para a estaca apoiada na profundidade de 3m:', True, preto)
                            rec_texto_calculo3 = pygame.Rect(rec_texto_calculo2c.x, rec_texto_calculo2c.y + rec_texto_calculo2c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo3, rec_texto_calculo3)

                            texto_calculo3a = fonte.render('RL = Rl2+Rl3 = '+str(Rltotal2)+' + '+'('+str(alfa3)+'*'+str(k3*1000)+'*'+NSPT3+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal3)+' kN', True, preto)
                            rec_texto_calculo3a = pygame.Rect(rec_texto_calculo3.x, rec_texto_calculo3.y + rec_texto_calculo3.height, 700, 15)
                            janela.blit(texto_calculo3a, rec_texto_calculo3a)

                            texto_calculo3b = fonte.render('RP = ('+str(k4*1000)+'*'+NSPT4+'*'+str(area)+')/'+str(f1)+' = '+str(Rp4)+' kN', True, preto)
                            rec_texto_calculo3b = pygame.Rect(rec_texto_calculo3a.x, rec_texto_calculo3a.y + rec_texto_calculo3a.height, 700, 15)
                            janela.blit(texto_calculo3b, rec_texto_calculo3b)

                            texto_calculo3c = fonte.render('RT = RL + RP = '+str(Rltotal3)+' + '+str(Rp4)+' = '+str(Rt3)+' kN', True, preto)
                            rec_texto_calculo3c = pygame.Rect(rec_texto_calculo3b.x, rec_texto_calculo3b.y + rec_texto_calculo3b.height, 700, 15)
                            janela.blit(texto_calculo3c, rec_texto_calculo3c)
                        
                        if count > 3:                            

                            texto_calculo4 = fonte.render('Para a estaca apoiada na profundidade de 4m:', True, preto)
                            rec_texto_calculo4 = pygame.Rect(rec_texto_calculo3c.x, rec_texto_calculo3c.y + rec_texto_calculo3c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo4, rec_texto_calculo4)

                            texto_calculo4a = fonte.render('RL = Rl2+Rl3+Rl4 = '+str(Rltotal3)+' + '+'('+str(alfa4)+'*'+str(k4*1000)+'*'+NSPT4+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal4)+' kN', True, preto)
                            rec_texto_calculo4a = pygame.Rect(rec_texto_calculo4.x, rec_texto_calculo4.y + rec_texto_calculo4.height, 700, 15)
                            janela.blit(texto_calculo4a, rec_texto_calculo4a)

                            texto_calculo4b = fonte.render('RP = ('+str(k5*1000)+'*'+NSPT5+'*'+str(area)+')/'+str(f1)+' = '+str(Rp5)+' kN', True, preto)
                            rec_texto_calculo4b = pygame.Rect(rec_texto_calculo4a.x, rec_texto_calculo4a.y + rec_texto_calculo4a.height, 700, 15)
                            janela.blit(texto_calculo4b, rec_texto_calculo4b)

                            texto_calculo4c = fonte.render('RT = RL + RP = '+str(Rltotal4)+' + '+str(Rp5)+' = '+str(Rt4)+' kN', True, preto)
                            rec_texto_calculo4c = pygame.Rect(rec_texto_calculo4b.x, rec_texto_calculo4b.y + rec_texto_calculo4b.height, 700, 15)
                            janela.blit(texto_calculo4c, rec_texto_calculo4c)
                        
                        if count > 4:                            

                            texto_calculo5 = fonte.render('Para a estaca apoiada na profundidade de 5m:', True, preto)
                            rec_texto_calculo5 = pygame.Rect(rec_texto_calculo4c.x, rec_texto_calculo4c.y + rec_texto_calculo4c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo5, rec_texto_calculo5)

                            texto_calculo5a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5 = '+str(Rltotal4)+' + '+'('+str(alfa5)+'*'+str(k5*1000)+'*'+NSPT5+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal5)+' kN', True, preto)
                            rec_texto_calculo5a = pygame.Rect(rec_texto_calculo5.x, rec_texto_calculo5.y + rec_texto_calculo5.height, 700, 15)
                            janela.blit(texto_calculo5a, rec_texto_calculo5a)

                            texto_calculo5b = fonte.render('RP = ('+str(k6*1000)+'*'+NSPT6+'*'+str(area)+')/'+str(f1)+' = '+str(Rp6)+' kN', True, preto)
                            rec_texto_calculo5b = pygame.Rect(rec_texto_calculo5a.x, rec_texto_calculo5a.y + rec_texto_calculo5a.height, 700, 15)
                            janela.blit(texto_calculo5b, rec_texto_calculo5b)

                            texto_calculo5c = fonte.render('RT = RL + RP = '+str(Rltotal5)+' + '+str(Rp6)+' = '+str(Rt5)+' kN', True, preto)
                            rec_texto_calculo5c = pygame.Rect(rec_texto_calculo5b.x, rec_texto_calculo5b.y + rec_texto_calculo5b.height, 700, 15)
                            janela.blit(texto_calculo5c, rec_texto_calculo5c)
                        
                    if pcount == 1:

                        if count > 5:                            

                            texto_calculo6 = fonte.render('Para a estaca apoiada na profundidade de 6m:', True, preto)
                            rec_texto_calculo6 = pygame.Rect(rec_texto_calculo2.x, rec_texto_calculo2.y, 700, 15)
                            janela.blit(texto_calculo6, rec_texto_calculo6)

                            texto_calculo6a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6 = '+str(Rltotal5)+' + '+'('+str(alfa6)+'*'+str(k6*1000)+'*'+NSPT6+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal6)+' kN', True, preto)
                            rec_texto_calculo6a = pygame.Rect(rec_texto_calculo6.x, rec_texto_calculo6.y + rec_texto_calculo6.height, 700, 15)
                            janela.blit(texto_calculo6a, rec_texto_calculo6a)

                            texto_calculo6b = fonte.render('RP = ('+str(k7*1000)+'*'+NSPT7+'*'+str(area)+')/'+str(f1)+' = '+str(Rp7)+' kN', True, preto)
                            rec_texto_calculo6b = pygame.Rect(rec_texto_calculo6a.x, rec_texto_calculo6a.y + rec_texto_calculo6a.height, 700, 15)
                            janela.blit(texto_calculo6b, rec_texto_calculo6b)

                            texto_calculo6c = fonte.render('RT = RL + RP = '+str(Rltotal6)+' + '+str(Rp7)+' = '+str(Rt6)+' kN', True, preto)
                            rec_texto_calculo6c = pygame.Rect(rec_texto_calculo6b.x, rec_texto_calculo6b.y + rec_texto_calculo6b.height, 700, 15)
                            janela.blit(texto_calculo6c, rec_texto_calculo6c)
                        
                        if count > 6:                            

                            texto_calculo7 = fonte.render('Para a estaca apoiada na profundidade de 7m:', True, preto)
                            rec_texto_calculo7 = pygame.Rect(rec_texto_calculo6c.x, rec_texto_calculo6c.y + rec_texto_calculo6c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo7, rec_texto_calculo7)

                            texto_calculo7a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7 = '+str(Rltotal6)+' + '+'('+str(alfa7)+'*'+str(k7*1000)+'*'+NSPT7+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal7)+' kN', True, preto)
                            rec_texto_calculo7a = pygame.Rect(rec_texto_calculo7.x, rec_texto_calculo7.y + rec_texto_calculo7.height, 700, 15)
                            janela.blit(texto_calculo7a, rec_texto_calculo7a)

                            texto_calculo7b = fonte.render('RP = ('+str(k8*1000)+'*'+NSPT8+'*'+str(area)+')/'+str(f1)+' = '+str(Rp8)+' kN', True, preto)
                            rec_texto_calculo7b = pygame.Rect(rec_texto_calculo7a.x, rec_texto_calculo7a.y + rec_texto_calculo7a.height, 700, 15)
                            janela.blit(texto_calculo7b, rec_texto_calculo7b)

                            texto_calculo7c = fonte.render('RT = RL + RP = '+str(Rltotal7)+' + '+str(Rp8)+' = '+str(Rt7)+' kN', True, preto)
                            rec_texto_calculo7c = pygame.Rect(rec_texto_calculo7b.x, rec_texto_calculo7b.y + rec_texto_calculo7b.height, 700, 15)
                            janela.blit(texto_calculo7c, rec_texto_calculo7c)
                        
                        if count > 7:                            

                            texto_calculo8 = fonte.render('Para a estaca apoiada na profundidade de 8m:', True, preto)
                            rec_texto_calculo8 = pygame.Rect(rec_texto_calculo7c.x, rec_texto_calculo7c.y + rec_texto_calculo7c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo8, rec_texto_calculo8)

                            texto_calculo8a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8 = '+str(Rltotal7)+' + '+'('+str(alfa8)+'*'+str(k8*1000)+'*'+NSPT8+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal8)+' kN', True, preto)
                            rec_texto_calculo8a = pygame.Rect(rec_texto_calculo8.x, rec_texto_calculo8.y + rec_texto_calculo8.height, 700, 15)
                            janela.blit(texto_calculo8a, rec_texto_calculo8a)

                            texto_calculo8b = fonte.render('RP = ('+str(k9*1000)+'*'+NSPT9+'*'+str(area)+')/'+str(f1)+' = '+str(Rp9)+' kN', True, preto)
                            rec_texto_calculo8b = pygame.Rect(rec_texto_calculo8a.x, rec_texto_calculo8a.y + rec_texto_calculo8a.height, 700, 15)
                            janela.blit(texto_calculo8b, rec_texto_calculo8b)

                            texto_calculo8c = fonte.render('RT = RL + RP = '+str(Rltotal8)+' + '+str(Rp9)+' = '+str(Rt8)+' kN', True, preto)
                            rec_texto_calculo8c = pygame.Rect(rec_texto_calculo8b.x, rec_texto_calculo8b.y + rec_texto_calculo8b.height, 700, 15)
                            janela.blit(texto_calculo8c, rec_texto_calculo8c)
                        
                        if count > 8:

                            texto_calculo9 = fonte.render('Para a estaca apoiada na profundidade de 9m:', True, preto)
                            rec_texto_calculo9 = pygame.Rect(rec_texto_calculo8c.x, rec_texto_calculo8c.y + rec_texto_calculo8c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo9, rec_texto_calculo9)

                            texto_calculo9a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9 = '+str(Rltotal8)+' + '+'('+str(alfa9)+'*'+str(k9*1000)+'*'+NSPT9+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal9)+' kN', True, preto)
                            rec_texto_calculo9a = pygame.Rect(rec_texto_calculo9.x, rec_texto_calculo9.y + rec_texto_calculo9.height, 700, 15)
                            janela.blit(texto_calculo9a, rec_texto_calculo9a)

                            texto_calculo9b = fonte.render('RP = ('+str(k10*1000)+'*'+NSPT10+'*'+str(area)+')/'+str(f1)+' = '+str(Rp10)+' kN', True, preto)
                            rec_texto_calculo9b = pygame.Rect(rec_texto_calculo9a.x, rec_texto_calculo9a.y + rec_texto_calculo9a.height, 700, 15)
                            janela.blit(texto_calculo9b, rec_texto_calculo9b)

                            texto_calculo9c = fonte.render('RT = RL + RP = '+str(Rltotal9)+' + '+str(Rp10)+' = '+str(Rt9)+' kN', True, preto)
                            rec_texto_calculo9c = pygame.Rect(rec_texto_calculo9b.x, rec_texto_calculo9b.y + rec_texto_calculo9b.height, 700, 15)
                            janela.blit(texto_calculo9c, rec_texto_calculo9c)
                        
                    if pcount == 2:

                        if count > 9:
                            
                            texto_calculo10 = fonte.render('Para a estaca apoiada na profundidade de 10m:', True, preto)
                            rec_texto_calculo10 = pygame.Rect(rec_texto_calculo2.x, rec_texto_calculo2.y, 700, 15)
                            janela.blit(texto_calculo10, rec_texto_calculo10)

                            texto_calculo10a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10 = '+str(Rltotal9)+' + '+'('+str(alfa10)+'*'+str(k10*1000)+'*'+NSPT10+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal10)+' kN', True, preto)
                            rec_texto_calculo10a = pygame.Rect(rec_texto_calculo10.x, rec_texto_calculo10.y + rec_texto_calculo10.height, 700, 15)
                            janela.blit(texto_calculo10a, rec_texto_calculo10a)

                            texto_calculo10b = fonte.render('RP = ('+str(k11*1000)+'*'+NSPT11+'*'+str(area)+')/'+str(f1)+' = '+str(Rp11)+' kN', True, preto)
                            rec_texto_calculo10b = pygame.Rect(rec_texto_calculo10a.x, rec_texto_calculo10a.y + rec_texto_calculo10a.height, 700, 15)
                            janela.blit(texto_calculo10b, rec_texto_calculo10b)

                            texto_calculo10c = fonte.render('RT = RL + RP = '+str(Rltotal10)+' + '+str(Rp11)+' = '+str(Rt10)+' kN', True, preto)
                            rec_texto_calculo10c = pygame.Rect(rec_texto_calculo10b.x, rec_texto_calculo10b.y + rec_texto_calculo10b.height, 700, 15)
                            janela.blit(texto_calculo10c, rec_texto_calculo10c)
                        
                        if count > 10:                            

                            texto_calculo11 = fonte.render('Para a estaca apoiada na profundidade de 11m:', True, preto)
                            rec_texto_calculo11 = pygame.Rect(rec_texto_calculo10c.x, rec_texto_calculo10c.y + rec_texto_calculo10c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo11, rec_texto_calculo11)

                            texto_calculo11a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11 = '+str(Rltotal10)+' + '+'('+str(alfa11)+'*'+str(k11*1000)+'*'+NSPT11+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal11)+' kN', True, preto)
                            rec_texto_calculo11a = pygame.Rect(rec_texto_calculo11.x, rec_texto_calculo11.y + rec_texto_calculo11.height, 700, 15)
                            janela.blit(texto_calculo11a, rec_texto_calculo11a)

                            texto_calculo11b = fonte.render('RP = ('+str(k12*1000)+'*'+NSPT12+'*'+str(area)+')/'+str(f1)+' = '+str(Rp12)+' kN', True, preto)
                            rec_texto_calculo11b = pygame.Rect(rec_texto_calculo11a.x, rec_texto_calculo11a.y + rec_texto_calculo11a.height, 700, 15)
                            janela.blit(texto_calculo11b, rec_texto_calculo11b)

                            texto_calculo11c = fonte.render('RT = RL + RP = '+str(Rltotal11)+' + '+str(Rp12)+' = '+str(Rt11)+' kN', True, preto)
                            rec_texto_calculo11c = pygame.Rect(rec_texto_calculo11b.x, rec_texto_calculo11b.y + rec_texto_calculo11b.height, 700, 15)
                            janela.blit(texto_calculo11c, rec_texto_calculo11c)
                        
                        if count > 11:                            

                            texto_calculo12 = fonte.render('Para a estaca apoiada na profundidade de 12m:', True, preto)
                            rec_texto_calculo12 = pygame.Rect(rec_texto_calculo11c.x, rec_texto_calculo11c.y + rec_texto_calculo11c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo12, rec_texto_calculo12)

                            texto_calculo12a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12 = '+str(Rltotal11)+' + '+'('+str(alfa12)+'*'+str(k12*1000)+'*'+NSPT12+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal12)+' kN', True, preto)
                            rec_texto_calculo12a = pygame.Rect(rec_texto_calculo12.x, rec_texto_calculo12.y + rec_texto_calculo12.height, 700, 15)
                            janela.blit(texto_calculo12a, rec_texto_calculo12a)

                            texto_calculo12b = fonte.render('RP = ('+str(k13*1000)+'*'+NSPT13+'*'+str(area)+')/'+str(f1)+' = '+str(Rp13)+' kN', True, preto)
                            rec_texto_calculo12b = pygame.Rect(rec_texto_calculo12a.x, rec_texto_calculo12a.y + rec_texto_calculo12a.height, 700, 15)
                            janela.blit(texto_calculo12b, rec_texto_calculo12b)

                            texto_calculo12c = fonte.render('RT = RL + RP = '+str(Rltotal12)+' + '+str(Rp13)+' = '+str(Rt12)+' kN', True, preto)
                            rec_texto_calculo12c = pygame.Rect(rec_texto_calculo12b.x, rec_texto_calculo12b.y + rec_texto_calculo12b.height, 700, 15)
                            janela.blit(texto_calculo12c, rec_texto_calculo12c)
                        
                        if count > 12:                            

                            texto_calculo13 = fonte.render('Para a estaca apoiada na profundidade de 13m:', True, preto)
                            rec_texto_calculo13 = pygame.Rect(rec_texto_calculo12c.x, rec_texto_calculo12c.y + rec_texto_calculo12c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo13, rec_texto_calculo13)

                            texto_calculo13a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13 = '+str(Rltotal12)+' + '+'('+str(alfa13)+'*'+str(k13*1000)+'*'+NSPT13+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal13)+' kN', True, preto)
                            rec_texto_calculo13a = pygame.Rect(rec_texto_calculo13.x, rec_texto_calculo13.y + rec_texto_calculo13.height, 700, 15)
                            janela.blit(texto_calculo13a, rec_texto_calculo13a)

                            texto_calculo13b = fonte.render('RP = ('+str(k14*1000)+'*'+NSPT14+'*'+str(area)+')/'+str(f1)+' = '+str(Rp14)+' kN', True, preto)
                            rec_texto_calculo13b = pygame.Rect(rec_texto_calculo13a.x, rec_texto_calculo13a.y + rec_texto_calculo13a.height, 700, 15)
                            janela.blit(texto_calculo13b, rec_texto_calculo13b)

                            texto_calculo13c = fonte.render('RT = RL + RP = '+str(Rltotal13)+' + '+str(Rp14)+' = '+str(Rt13)+' kN', True, preto)
                            rec_texto_calculo13c = pygame.Rect(rec_texto_calculo13b.x, rec_texto_calculo13b.y + rec_texto_calculo13b.height, 700, 15)
                            janela.blit(texto_calculo13c, rec_texto_calculo13c)
                        
                    if pcount == 3:

                        if count > 13:

                            texto_calculo14 = fonte.render('Para a estaca apoiada na profundidade de 14m:', True, preto)
                            rec_texto_calculo14 = pygame.Rect(rec_texto_calculo2.x, rec_texto_calculo2.y, 700, 15)
                            janela.blit(texto_calculo14, rec_texto_calculo14)

                            texto_calculo14a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13+Rl14 = '+str(Rltotal13)+' + '+'('+str(alfa14)+'*'+str(k14*1000)+'*'+NSPT14+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal14)+' kN', True, preto)
                            rec_texto_calculo14a = pygame.Rect(rec_texto_calculo14.x, rec_texto_calculo14.y + rec_texto_calculo14.height, 700, 15)
                            janela.blit(texto_calculo14a, rec_texto_calculo14a)

                            texto_calculo14b = fonte.render('RP = ('+str(k15*1000)+'*'+NSPT15+'*'+str(area)+')/'+str(f1)+' = '+str(Rp15)+' kN', True, preto)
                            rec_texto_calculo14b = pygame.Rect(rec_texto_calculo14a.x, rec_texto_calculo14a.y + rec_texto_calculo14a.height, 700, 15)
                            janela.blit(texto_calculo14b, rec_texto_calculo14b)

                            texto_calculo14c = fonte.render('RT = RL + RP = '+str(Rltotal14)+' + '+str(Rp15)+' = '+str(Rt14)+' kN', True, preto)
                            rec_texto_calculo14c = pygame.Rect(rec_texto_calculo14b.x, rec_texto_calculo14b.y + rec_texto_calculo14b.height, 700, 15)
                            janela.blit(texto_calculo14c, rec_texto_calculo14c)

                        if count > 14:

                            texto_calculo15 = fonte.render('Para a estaca apoiada na profundidade de 15m:', True, preto)
                            rec_texto_calculo15 = pygame.Rect(rec_texto_calculo14c.x, rec_texto_calculo14c.y + rec_texto_calculo14c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo15, rec_texto_calculo15)

                            texto_calculo15a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13+Rl14+Rl15 = '+str(Rltotal14)+' + '+'('+str(alfa15)+'*'+str(k15*1000)+'*'+NSPT15+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal15)+' kN', True, preto)
                            rec_texto_calculo15a = pygame.Rect(rec_texto_calculo15.x, rec_texto_calculo15.y + rec_texto_calculo15.height, 700, 15)
                            janela.blit(texto_calculo15a, rec_texto_calculo15a)

                            texto_calculo15b = fonte.render('RP = ('+str(k16*1000)+'*'+NSPT16+'*'+str(area)+')/'+str(f1)+' = '+str(Rp16)+' kN', True, preto)
                            rec_texto_calculo15b = pygame.Rect(rec_texto_calculo15a.x, rec_texto_calculo15a.y + rec_texto_calculo15a.height, 700, 15)
                            janela.blit(texto_calculo15b, rec_texto_calculo15b)

                            texto_calculo15c = fonte.render('RT = RL + RP = '+str(Rltotal15)+' + '+str(Rp16)+' = '+str(Rt15)+' kN', True, preto)
                            rec_texto_calculo15c = pygame.Rect(rec_texto_calculo15b.x, rec_texto_calculo15b.y + rec_texto_calculo15b.height, 700, 15)
                            janela.blit(texto_calculo15c, rec_texto_calculo15c)
                        
                        if count > 15:

                            texto_calculo16 = fonte.render('Para a estaca apoiada na profundidade de 16m:', True, preto)
                            rec_texto_calculo16 = pygame.Rect(rec_texto_calculo15c.x, rec_texto_calculo15c.y + rec_texto_calculo15c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo16, rec_texto_calculo16)

                            texto_calculo16a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13+Rl14+Rl15+Rl16 = '+str(Rltotal15)+' + '+'('+str(alfa16)+'*'+str(k16*1000)+'*'+NSPT16+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal16)+' kN', True, preto)
                            rec_texto_calculo16a = pygame.Rect(rec_texto_calculo16.x, rec_texto_calculo16.y + rec_texto_calculo16.height, 700, 15)
                            janela.blit(texto_calculo16a, rec_texto_calculo16a)

                            texto_calculo16b = fonte.render('RP = ('+str(k17*1000)+'*'+NSPT17+'*'+str(area)+')/'+str(f1)+' = '+str(Rp17)+' kN', True, preto)
                            rec_texto_calculo16b = pygame.Rect(rec_texto_calculo16a.x, rec_texto_calculo16a.y + rec_texto_calculo16a.height, 700, 15)
                            janela.blit(texto_calculo16b, rec_texto_calculo16b)

                            texto_calculo16c = fonte.render('RT = RL + RP = '+str(Rltotal16)+' + '+str(Rp17)+' = '+str(Rt16)+' kN', True, preto)
                            rec_texto_calculo16c = pygame.Rect(rec_texto_calculo16b.x, rec_texto_calculo16b.y + rec_texto_calculo16b.height, 700, 15)
                            janela.blit(texto_calculo16c, rec_texto_calculo16c)
                        
                        if count > 16:

                            texto_calculo17 = fonte.render('Para a estaca apoiada na profundidade de 17m:', True, preto)
                            rec_texto_calculo17 = pygame.Rect(rec_texto_calculo16c.x, rec_texto_calculo16c.y + rec_texto_calculo16c.height + button_spacing, 700, 15)
                            janela.blit(texto_calculo17, rec_texto_calculo17)

                            texto_calculo17a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13+Rl14+Rl15+Rl16+Rl17 = '+str(Rltotal16)+' + '+'('+str(alfa17)+'*'+str(k17*1000)+'*'+NSPT17+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal17)+' kN', True, preto)
                            rec_texto_calculo17a = pygame.Rect(rec_texto_calculo17.x, rec_texto_calculo17.y + rec_texto_calculo17.height, 700, 15)
                            janela.blit(texto_calculo17a, rec_texto_calculo17a)

                            texto_calculo17b = fonte.render('RP = ('+str(k18*1000)+'*'+NSPT18+'*'+str(area)+')/'+str(f1)+' = '+str(Rp18)+' kN', True, preto)
                            rec_texto_calculo17b = pygame.Rect(rec_texto_calculo17a.x, rec_texto_calculo17a.y + rec_texto_calculo17a.height, 700, 15)
                            janela.blit(texto_calculo17b, rec_texto_calculo17b)

                            texto_calculo17c = fonte.render('RT = RL + RP = '+str(Rltotal17)+' + '+str(Rp18)+' = '+str(Rt17)+' kN', True, preto)
                            rec_texto_calculo17c = pygame.Rect(rec_texto_calculo17b.x, rec_texto_calculo17b.y + rec_texto_calculo17b.height, 700, 15)
                            janela.blit(texto_calculo17c, rec_texto_calculo17c)
                    
                    if pcount == 4:

                        if count > 17:

                            texto_calculo18 = fonte.render('Para a estaca apoiada na profundidade de 18m:', True, preto)
                            rec_texto_calculo18 = pygame.Rect(rec_texto_calculo2.x, rec_texto_calculo2.y, 700, 15)
                            janela.blit(texto_calculo18, rec_texto_calculo18)

                            texto_calculo18a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13+Rl14+Rl15+Rl16+Rl17+Rl18', True, preto)
                            rec_texto_calculo18a = pygame.Rect(rec_texto_calculo18.x, rec_texto_calculo18.y + rec_texto_calculo18.height, 700, 15)
                            janela.blit(texto_calculo18a, rec_texto_calculo18a)

                            texto_calculo18b = fonte.render('RL = '+str(Rltotal17)+' + '+'('+str(alfa18)+'*'+str(k18*1000)+'*'+NSPT18+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal18)+' kN', True, preto)
                            rec_texto_calculo18b = pygame.Rect(rec_texto_calculo18a.x, rec_texto_calculo18a.y + rec_texto_calculo18a.height, 700, 15)
                            janela.blit(texto_calculo18b, rec_texto_calculo18b)

                            texto_calculo18c = fonte.render('RP = ('+str(k19*1000)+'*'+NSPT19+'*'+str(area)+')/'+str(f1)+' = '+str(Rp19)+' kN', True, preto)
                            rec_texto_calculo18c = pygame.Rect(rec_texto_calculo18b.x, rec_texto_calculo18b.y + rec_texto_calculo18b.height, 700, 15)
                            janela.blit(texto_calculo18c, rec_texto_calculo18c)

                            texto_calculo18d = fonte.render('RT = RL + RP = '+str(Rltotal18)+' + '+str(Rp19)+' = '+str(Rt18)+' kN', True, preto)
                            rec_texto_calculo18d = pygame.Rect(rec_texto_calculo18c.x, rec_texto_calculo18c.y + rec_texto_calculo18c.height, 700, 15)
                            janela.blit(texto_calculo18d, rec_texto_calculo18d)
                        
                        if count > 18:

                            texto_calculo19 = fonte.render('Para a estaca apoiada na profundidade de 19m:', True, preto)
                            rec_texto_calculo19 = pygame.Rect(rec_texto_calculo18d.x, rec_texto_calculo18d.y + rec_texto_calculo18d.height + 5, 700, 15)
                            janela.blit(texto_calculo19, rec_texto_calculo19)

                            texto_calculo19a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13+Rl14+Rl15+Rl16+Rl17+Rl18+Rl19', True, preto)
                            rec_texto_calculo19a = pygame.Rect(rec_texto_calculo19.x, rec_texto_calculo19.y + rec_texto_calculo19.height, 700, 15)
                            janela.blit(texto_calculo19a, rec_texto_calculo19a)

                            texto_calculo19b = fonte.render('RL = '+str(Rltotal18)+' + '+'('+str(alfa19)+'*'+str(k19*1000)+'*'+NSPT19+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal19)+' kN', True, preto)
                            rec_texto_calculo19b = pygame.Rect(rec_texto_calculo19a.x, rec_texto_calculo19a.y + rec_texto_calculo19a.height, 700, 15)
                            janela.blit(texto_calculo19b, rec_texto_calculo19b)

                            texto_calculo19c = fonte.render('RP = ('+str(k20*1000)+'*'+NSPT20+'*'+str(area)+')/'+str(f1)+' = '+str(Rp20)+' kN', True, preto)
                            rec_texto_calculo19c = pygame.Rect(rec_texto_calculo19b.x, rec_texto_calculo19b.y + rec_texto_calculo19b.height, 700, 15)
                            janela.blit(texto_calculo19c, rec_texto_calculo19c)

                            texto_calculo19d = fonte.render('RT = RL + RP = '+str(Rltotal19)+' + '+str(Rp20)+' = '+str(Rt19)+' kN', True, preto)
                            rec_texto_calculo19d = pygame.Rect(rec_texto_calculo19c.x, rec_texto_calculo19c.y + rec_texto_calculo19c.height, 700, 15)
                            janela.blit(texto_calculo19d, rec_texto_calculo19d)
                        
                        if count > 19:

                            texto_calculo20 = fonte.render('Para a estaca apoiada na profundidade de 20m:', True, preto)
                            rec_texto_calculo20 = pygame.Rect(rec_texto_calculo19d.x, rec_texto_calculo19d.y + rec_texto_calculo19d.height + 5, 700, 15)
                            janela.blit(texto_calculo20, rec_texto_calculo20)

                            texto_calculo20a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13+Rl14+Rl15+Rl16+Rl17+Rl18+Rl19+Rl20', True, preto)
                            rec_texto_calculo20a = pygame.Rect(rec_texto_calculo20.x, rec_texto_calculo20.y + rec_texto_calculo20.height, 700, 15)
                            janela.blit(texto_calculo20a, rec_texto_calculo20a)

                            texto_calculo20b = fonte.render('RL = '+str(Rltotal19)+' + '+'('+str(alfa20)+'*'+str(k20*1000)+'*'+NSPT20+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal20)+' kN', True, preto)
                            rec_texto_calculo20b = pygame.Rect(rec_texto_calculo20a.x, rec_texto_calculo20a.y + rec_texto_calculo20a.height, 700, 15)
                            janela.blit(texto_calculo20b, rec_texto_calculo20b)

                            texto_calculo20c = fonte.render('RP = ('+str(k21*1000)+'*'+NSPT21+'*'+str(area)+')/'+str(f1)+' = '+str(Rp21)+' kN', True, preto)
                            rec_texto_calculo20c = pygame.Rect(rec_texto_calculo20b.x, rec_texto_calculo20b.y + rec_texto_calculo20b.height, 700, 15)
                            janela.blit(texto_calculo20c, rec_texto_calculo20c)

                            texto_calculo20d = fonte.render('RT = RL + RP = '+str(Rltotal20)+' + '+str(Rp21)+' = '+str(Rt20)+' kN', True, preto)
                            rec_texto_calculo20d = pygame.Rect(rec_texto_calculo20c.x, rec_texto_calculo20c.y + rec_texto_calculo20c.height, 700, 15)
                            janela.blit(texto_calculo20d, rec_texto_calculo20d)
                        
                        if count > 20:

                            texto_calculo21 = fonte.render('Para a estaca apoiada na profundidade de 21m:', True, preto)
                            rec_texto_calculo21 = pygame.Rect(rec_texto_calculo20d.x, rec_texto_calculo20d.y + rec_texto_calculo20d.height + 5, 700, 15)
                            janela.blit(texto_calculo21, rec_texto_calculo21)

                            texto_calculo21a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13+Rl14+Rl15+Rl16+Rl17+Rl18+Rl19+Rl20+Rl21', True, preto)
                            rec_texto_calculo21a = pygame.Rect(rec_texto_calculo21.x, rec_texto_calculo21.y + rec_texto_calculo21.height, 700, 15)
                            janela.blit(texto_calculo21a, rec_texto_calculo21a)

                            texto_calculo21b = fonte.render('RL = '+str(Rltotal20)+' + '+'('+str(alfa21)+'*'+str(k21*1000)+'*'+NSPT21+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal21)+' kN', True, preto)
                            rec_texto_calculo21b = pygame.Rect(rec_texto_calculo21a.x, rec_texto_calculo21a.y + rec_texto_calculo21a.height, 700, 15)
                            janela.blit(texto_calculo21b, rec_texto_calculo21b)

                            texto_calculo21c = fonte.render('RP = ('+str(k22*1000)+'*'+NSPT22+'*'+str(area)+')/'+str(f1)+' = '+str(Rp22)+' kN', True, preto)
                            rec_texto_calculo21c = pygame.Rect(rec_texto_calculo21b.x, rec_texto_calculo21b.y + rec_texto_calculo21b.height, 700, 15)
                            janela.blit(texto_calculo21c, rec_texto_calculo21c)

                            texto_calculo21d = fonte.render('RT = RL + RP = '+str(Rltotal21)+' + '+str(Rp22)+' = '+str(Rt21)+' kN', True, preto)
                            rec_texto_calculo21d = pygame.Rect(rec_texto_calculo21c.x, rec_texto_calculo21c.y + rec_texto_calculo21c.height, 700, 15)
                            janela.blit(texto_calculo21d, rec_texto_calculo21d)
                    
                    if pcount == 5:

                        if count > 21:

                            texto_calculo22 = fonte.render('Para a estaca apoiada na profundidade de 22m:', True, preto)
                            rec_texto_calculo22 = pygame.Rect(rec_texto_calculo2.x, rec_texto_calculo2.y, 700, 15)
                            janela.blit(texto_calculo22, rec_texto_calculo22)

                            texto_calculo22a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13+Rl14+Rl15+Rl16+Rl17+Rl18+Rl19+Rl20+Rl21+Rl22', True, preto)
                            rec_texto_calculo22a = pygame.Rect(rec_texto_calculo22.x, rec_texto_calculo22.y + rec_texto_calculo22.height, 700, 15)
                            janela.blit(texto_calculo22a, rec_texto_calculo22a)

                            texto_calculo22b = fonte.render('RL = '+str(Rltotal21)+' + '+'('+str(alfa22)+'*'+str(k22*1000)+'*'+NSPT22+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal22)+' kN', True, preto)
                            rec_texto_calculo22b = pygame.Rect(rec_texto_calculo22a.x, rec_texto_calculo22a.y + rec_texto_calculo22a.height, 700, 15)
                            janela.blit(texto_calculo22b, rec_texto_calculo22b)

                            texto_calculo22c = fonte.render('RP = ('+str(k23*1000)+'*'+NSPT23+'*'+str(area)+')/'+str(f1)+' = '+str(Rp23)+' kN', True, preto)
                            rec_texto_calculo22c = pygame.Rect(rec_texto_calculo22b.x, rec_texto_calculo22b.y + rec_texto_calculo22b.height, 700, 15)
                            janela.blit(texto_calculo22c, rec_texto_calculo22c)

                            texto_calculo22d = fonte.render('RT = RL + RP = '+str(Rltotal22)+' + '+str(Rp23)+' = '+str(Rt23)+' kN', True, preto)
                            rec_texto_calculo22d = pygame.Rect(rec_texto_calculo22c.x, rec_texto_calculo22c.y + rec_texto_calculo22c.height, 700, 15)
                            janela.blit(texto_calculo22d, rec_texto_calculo22d)
                        
                        if count > 22:

                            texto_calculo23 = fonte.render('Para a estaca apoiada na profundidade de 23m:', True, preto)
                            rec_texto_calculo23 = pygame.Rect(rec_texto_calculo22d.x, rec_texto_calculo22d.y + rec_texto_calculo22d.height + 5, 700, 15)
                            janela.blit(texto_calculo23, rec_texto_calculo23)

                            texto_calculo23a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13+Rl14+Rl15+Rl16+Rl17+Rl18+Rl19+Rl20+Rl21+Rl22+Rl23', True, preto)
                            rec_texto_calculo23a = pygame.Rect(rec_texto_calculo23.x, rec_texto_calculo23.y + rec_texto_calculo23.height, 700, 15)
                            janela.blit(texto_calculo23a, rec_texto_calculo23a)

                            texto_calculo23b = fonte.render('RL = '+str(Rltotal22)+' + '+'('+str(alfa23)+'*'+str(k23*1000)+'*'+NSPT23+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal23)+' kN', True, preto)
                            rec_texto_calculo23b = pygame.Rect(rec_texto_calculo23a.x, rec_texto_calculo23a.y + rec_texto_calculo23a.height, 700, 15)
                            janela.blit(texto_calculo23b, rec_texto_calculo23b)

                            texto_calculo23c = fonte.render('RP = ('+str(k24*1000)+'*'+NSPT24+'*'+str(area)+')/'+str(f1)+' = '+str(Rp24)+' kN', True, preto)
                            rec_texto_calculo23c = pygame.Rect(rec_texto_calculo23b.x, rec_texto_calculo23b.y + rec_texto_calculo23b.height, 700, 15)
                            janela.blit(texto_calculo23c, rec_texto_calculo23c)

                            texto_calculo23d = fonte.render('RT = RL + RP = '+str(Rltotal23)+' + '+str(Rp24)+' = '+str(Rt23)+' kN', True, preto)
                            rec_texto_calculo23d = pygame.Rect(rec_texto_calculo23c.x, rec_texto_calculo23c.y + rec_texto_calculo23c.height, 700, 15)
                            janela.blit(texto_calculo23d, rec_texto_calculo23d)
                        
                        if count > 23:

                            texto_calculo24 = fonte.render('Para a estaca apoiada na profundidade de 24m:', True, preto)
                            rec_texto_calculo24 = pygame.Rect(rec_texto_calculo23d.x, rec_texto_calculo23d.y + rec_texto_calculo23d.height + 5, 700, 15)
                            janela.blit(texto_calculo24, rec_texto_calculo24)

                            texto_calculo24a = fonte.render('RL = Rl2+Rl3+Rl4+Rl5+Rl6+Rl7+Rl8+Rl9+Rl10+Rl11+Rl12+Rl13+Rl14+Rl15+Rl16+Rl17+Rl18+Rl19+Rl20+Rl21+Rl22+Rl23+Rl24', True, preto)
                            rec_texto_calculo24a = pygame.Rect(rec_texto_calculo24.x, rec_texto_calculo24.y + rec_texto_calculo24.height, 700, 15)
                            janela.blit(texto_calculo24a, rec_texto_calculo24a)

                            texto_calculo24b = fonte.render('RL = '+str(Rltotal23)+' + '+'('+str(alfa24)+'*'+str(k24*1000)+'*'+NSPT24+'*'+str(circunferencia)+')/'+str(f2)+' = '+str(Rltotal24)+' kN', True, preto)
                            rec_texto_calculo24b = pygame.Rect(rec_texto_calculo24a.x, rec_texto_calculo24a.y + rec_texto_calculo24a.height, 700, 15)
                            janela.blit(texto_calculo24b, rec_texto_calculo24b)

                            texto_calculo24c = fonte.render('RP = ('+str(k25*1000)+'*'+NSPT25+'*'+str(area)+')/'+str(f1)+' = '+str(Rp25)+' kN', True, preto)
                            rec_texto_calculo24c = pygame.Rect(rec_texto_calculo24b.x, rec_texto_calculo24b.y + rec_texto_calculo24b.height, 700, 15)
                            janela.blit(texto_calculo24c, rec_texto_calculo24c)

                            texto_calculo24d = fonte.render('RT = RL + RP = '+str(Rltotal24)+' + '+str(Rp25)+' = '+str(Rt24)+' kN', True, preto)
                            rec_texto_calculo24d = pygame.Rect(rec_texto_calculo24c.x, rec_texto_calculo24c.y + rec_texto_calculo24c.height, 700, 15)
                            janela.blit(texto_calculo24d, rec_texto_calculo24d)

            texto_topo1 = fonte.render('Metodo:', True, preto)
            rec_texto_topo1 = pygame.Rect(recMenu_width + button_spacing, 0, cell_width, cell_height)
            janela.blit(texto_topo1, rec_texto_topo1)

            texto_topo2 = fonte.render('Diâmetro da estaca:', True, preto)
            rec_texto_topo2 = pygame.Rect(rec_texto_topo1.x + cell_width + button_spacing, 0, cell_width, cell_height)
            janela.blit(texto_topo2, rec_texto_topo2)

            texto_topo3 = fonte.render('Tipo da estaca:', True, preto)
            rec_texto_topo3 = pygame.Rect(rec_texto_topo2.x + cell_width + button_spacing, 0, cell_width, cell_height)
            janela.blit(texto_topo3, rec_texto_topo3)

            texto_diametro = fonte.render(diametro.lstrip('0') + ' mm', True, preto)
            rec_texto_diametro = texto_diametro.get_rect(center = rec_diametro.center)
            pygame.draw.rect(janela, branco, rec_diametro)
            pygame.draw.rect(janela, preto, rec_diametro, 1)
            janela.blit(texto_diametro, rec_texto_diametro)
            if diametro_select:
                pygame.draw.rect(janela, preto, (rec_texto_diametro.x + texto_diametro.get_width() - 20, rec_texto_diametro.y, 2, texto_diametro.get_height()))

            if metodo_selecionado is None:
                texto_metodo = fonte.render('Selecione um método', True, preto)
                texto_estaca = fonte.render('Selecione um método', True, preto)
            else:
                texto_metodo = fonte.render(metodo_selecionado, True, preto)
                if estaca_selecionado is None:
                    texto_estaca = fonte.render('Selecione uma estaca', True, preto)
                else:
                    texto_estaca = fonte.render(estaca_selecionado, True, preto)
            rec_texto_metodo = texto_metodo.get_rect(center = rec_metodo.center)
            pygame.draw.rect(janela, branco, rec_metodo)
            pygame.draw.rect(janela, preto, rec_metodo, 1)
            janela.blit(texto_metodo, rec_texto_metodo)
            rec_texto_estaca = texto_estaca.get_rect(center = rec_estaca.center)
            pygame.draw.rect(janela, branco, rec_estaca)
            pygame.draw.rect(janela, preto, rec_estaca, 1)
            janela.blit(texto_estaca, rec_texto_estaca)

            if metodo_aberto:
                for i, opcao in enumerate(metodos):
                    rec_opcaometodo = pygame.Rect(rec_metodo.x, rec_metodo.y + (i+1) * rec_metodo.height, rec_metodo.width, rec_metodo.height)
                    pygame.draw.rect(janela, preto, rec_opcaometodo)
                    pygame.draw.rect(janela, vermelho, rec_opcaometodo, 1)
                    texto_metodo = fonte.render(opcao, True, branco)
                    janela.blit(texto_metodo, (rec_opcaometodo.x + 10, rec_opcaometodo.y + 10))
            
            if estaca_aberto:
                if metodo_selecionado == 'DECOURT & QUARESMA':
                    for i, opcao in enumerate(estaca_quaresma):
                        rec_opcaoestaca = pygame.Rect(rec_estaca.x, rec_estaca.y + (i+1) * rec_estaca.height, rec_estaca.width, rec_estaca.height)
                        pygame.draw.rect(janela, preto, rec_opcaoestaca)
                        pygame.draw.rect(janela, vermelho, rec_opcaoestaca, 1)
                        texto_estaca = fonte.render(opcao, True, branco)
                        janela.blit(texto_estaca, (rec_opcaoestaca.x + 10, rec_opcaoestaca.y + 10))
                
                else:
                    for i, opcao in enumerate(estaca_aoki):
                        rec_opcaoestaca = pygame.Rect(rec_estaca.x, rec_estaca.y + (i+1) * rec_estaca.height, rec_estaca.width, rec_estaca.height)
                        pygame.draw.rect(janela, preto, rec_opcaoestaca)
                        pygame.draw.rect(janela, vermelho, rec_opcaoestaca, 1)
                        texto_estaca = fonte.render(opcao, True, branco)
                        janela.blit(texto_estaca, (rec_opcaoestaca.x + 10, rec_opcaoestaca.y + 10))
            
            texto_calcular = fonte.render('Calcular', True, preto)
            rec_texto_calcular = texto_calcular.get_rect(center = rec_calcular.center)
            pygame.draw.rect(janela, rec_calcular_color, rec_calcular)
            janela.blit(texto_calcular, rec_texto_calcular)

            texto_proximo = fonte.render('Proximo', True, preto)
            rec_texto_proximo = texto_proximo.get_rect(center=rec_proximo.center)
            pygame.draw.rect(janela, rec_proximo_color, rec_proximo)
            janela.blit(texto_proximo, rec_texto_proximo)

            texto_anterior = fonte.render('Anterior', True, preto)
            rec_texto_anterior = texto_anterior.get_rect(center=rec_anterior.center)
            pygame.draw.rect(janela, rec_anterior_color, rec_anterior)
            janela.blit(texto_anterior, rec_texto_anterior)

            if diametro == '':
                area = 0
                circunferencia = 0
            else:
                area = round(((int(diametro)/1000)*(int(diametro)/1000)*pi)/4, 2)
                circunferencia = round((int(diametro)/1000)*pi, 2)

        
    if perfil_sondagem:

        if count > 23:
            texto_profundidade25 = fonte.render(profundidade25, True, preto)
            rec_texto_profundidade25 = texto_profundidade25.get_rect(center = rec_profundidade25.center)
            pygame.draw.rect(janela, branco, rec_profundidade25)
            pygame.draw.rect(janela, preto, rec_profundidade25, 1)
            janela.blit(texto_profundidade25, rec_texto_profundidade25)

            texto_NSPT25 = fonte.render(NSPT25.lstrip('0'), True, preto)
            rec_texto_NSPT25 = texto_NSPT25.get_rect(center=rec_NSPT25.center)
            pygame.draw.rect(janela, branco, rec_NSPT25)
            pygame.draw.rect(janela, preto, rec_NSPT25, 1)
            janela.blit(texto_NSPT25, rec_texto_NSPT25)
            if NSPT25_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT25.x + texto_NSPT25.get_width(), rec_texto_NSPT25.y, 2, texto_NSPT25.get_height()))
            
            if solo25 is None:
                texto_solo25 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo25 = fonte.render(solo25, True, preto)
            rec_texto_solo25 = texto_solo25.get_rect(center=rec_solos25.center)
            pygame.draw.rect(janela, branco, rec_solos25)
            pygame.draw.rect(janela, preto, rec_solos25, 1)
            janela.blit(texto_solo25, rec_texto_solo25)

            if solos_select25:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao25 = pygame.Rect(rec_solos25.x, rec_solos25.y + (i+1) * rec_solos25.height, rec_solos25.width, rec_solos25.height)
                    pygame.draw.rect(janela, preto, rec_opcao25)
                    pygame.draw.rect(janela, vermelho, rec_opcao25, 1)
                    texto_solo25 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo25, (rec_opcao25.x + 10, rec_opcao25.y + 10))

        if count > 22:
            texto_profundidade24 = fonte.render(profundidade24, True, preto)
            rec_texto_profundidade24 = texto_profundidade24.get_rect(center = rec_profundidade24.center)
            pygame.draw.rect(janela, branco, rec_profundidade24)
            pygame.draw.rect(janela, preto, rec_profundidade24, 1)
            janela.blit(texto_profundidade24, rec_texto_profundidade24)

            texto_NSPT24 = fonte.render(NSPT24.lstrip('0'), True, preto)
            rec_texto_NSPT24 = texto_NSPT24.get_rect(center=rec_NSPT24.center)
            pygame.draw.rect(janela, branco, rec_NSPT24)
            pygame.draw.rect(janela, preto, rec_NSPT24, 1)
            janela.blit(texto_NSPT24, rec_texto_NSPT24)
            if NSPT24_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT24.x + texto_NSPT24.get_width(), rec_texto_NSPT24.y, 2, texto_NSPT24.get_height()))
            
            if solo24 is None:
                texto_solo24 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo24 = fonte.render(solo24, True, preto)
            rec_texto_solo24 = texto_solo24.get_rect(center=rec_solos24.center)
            pygame.draw.rect(janela, branco, rec_solos24)
            pygame.draw.rect(janela, preto, rec_solos24, 1)
            janela.blit(texto_solo24, rec_texto_solo24)

            if solos_select24:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao24 = pygame.Rect(rec_solos24.x, rec_solos24.y + (i+1) * rec_solos24.height, rec_solos24.width, rec_solos24.height)
                    pygame.draw.rect(janela, preto, rec_opcao24)
                    pygame.draw.rect(janela, vermelho, rec_opcao24, 1)
                    texto_solo24 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo24, (rec_opcao24.x + 10, rec_opcao24.y + 10))

        if count > 21:
            texto_profundidade23 = fonte.render(profundidade23, True, preto)
            rec_texto_profundidade23 = texto_profundidade23.get_rect(center = rec_profundidade23.center)
            pygame.draw.rect(janela, branco, rec_profundidade23)
            pygame.draw.rect(janela, preto, rec_profundidade23, 1)
            janela.blit(texto_profundidade23, rec_texto_profundidade23)

            texto_NSPT23 = fonte.render(NSPT23.lstrip('0'), True, preto)
            rec_texto_NSPT23 = texto_NSPT23.get_rect(center=rec_NSPT23.center)
            pygame.draw.rect(janela, branco, rec_NSPT23)
            pygame.draw.rect(janela, preto, rec_NSPT23, 1)
            janela.blit(texto_NSPT23, rec_texto_NSPT23)
            if NSPT23_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT23.x + texto_NSPT23.get_width(), rec_texto_NSPT23.y, 2, texto_NSPT23.get_height()))
            
            if solo23 is None:
                texto_solo23 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo23 = fonte.render(solo23, True, preto)
            rec_texto_solo23 = texto_solo23.get_rect(center=rec_solos23.center)
            pygame.draw.rect(janela, branco, rec_solos23)
            pygame.draw.rect(janela, preto, rec_solos23, 1)
            janela.blit(texto_solo23, rec_texto_solo23)

            if solos_select23:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao23 = pygame.Rect(rec_solos23.x, rec_solos23.y + (i+1) * rec_solos23.height, rec_solos23.width, rec_solos23.height)
                    pygame.draw.rect(janela, preto, rec_opcao23)
                    pygame.draw.rect(janela, vermelho, rec_opcao23, 1)
                    texto_solo23 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo23, (rec_opcao23.x + 10, rec_opcao23.y + 10))

        if count > 20:
            texto_profundidade22 = fonte.render(profundidade22, True, preto)
            rec_texto_profundidade22 = texto_profundidade22.get_rect(center = rec_profundidade22.center)
            pygame.draw.rect(janela, branco, rec_profundidade22)
            pygame.draw.rect(janela, preto, rec_profundidade22, 1)
            janela.blit(texto_profundidade22, rec_texto_profundidade22)

            texto_NSPT22 = fonte.render(NSPT22.lstrip('0'), True, preto)
            rec_texto_NSPT22 = texto_NSPT22.get_rect(center=rec_NSPT22.center)
            pygame.draw.rect(janela, branco, rec_NSPT22)
            pygame.draw.rect(janela, preto, rec_NSPT22, 1)
            janela.blit(texto_NSPT22, rec_texto_NSPT22)
            if NSPT22_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT22.x + texto_NSPT22.get_width(), rec_texto_NSPT22.y, 2, texto_NSPT22.get_height()))
            
            if solo22 is None:
                texto_solo22 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo22 = fonte.render(solo22, True, preto)
            rec_texto_solo22 = texto_solo22.get_rect(center=rec_solos22.center)
            pygame.draw.rect(janela, branco, rec_solos22)
            pygame.draw.rect(janela, preto, rec_solos22, 1)
            janela.blit(texto_solo22, rec_texto_solo22)

            if solos_select22:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao22 = pygame.Rect(rec_solos22.x, rec_solos22.y + (i+1) * rec_solos22.height, rec_solos22.width, rec_solos22.height)
                    pygame.draw.rect(janela, preto, rec_opcao22)
                    pygame.draw.rect(janela, vermelho, rec_opcao22, 1)
                    texto_solo22 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo22, (rec_opcao22.x + 10, rec_opcao22.y + 10))

        if count > 19:
            texto_profundidade21 = fonte.render(profundidade21, True, preto)
            rec_texto_profundidade21 = texto_profundidade21.get_rect(center = rec_profundidade21.center)
            pygame.draw.rect(janela, branco, rec_profundidade21)
            pygame.draw.rect(janela, preto, rec_profundidade21, 1)
            janela.blit(texto_profundidade21, rec_texto_profundidade21)

            texto_NSPT21 = fonte.render(NSPT21.lstrip('0'), True, preto)
            rec_texto_NSPT21 = texto_NSPT21.get_rect(center=rec_NSPT21.center)
            pygame.draw.rect(janela, branco, rec_NSPT21)
            pygame.draw.rect(janela, preto, rec_NSPT21, 1)
            janela.blit(texto_NSPT21, rec_texto_NSPT21)
            if NSPT21_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT21.x + texto_NSPT21.get_width(), rec_texto_NSPT21.y, 2, texto_NSPT21.get_height()))
            
            if solo21 is None:
                texto_solo21 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo21 = fonte.render(solo21, True, preto)
            rec_texto_solo21 = texto_solo21.get_rect(center=rec_solos21.center)
            pygame.draw.rect(janela, branco, rec_solos21)
            pygame.draw.rect(janela, preto, rec_solos21, 1)
            janela.blit(texto_solo21, rec_texto_solo21)

            if solos_select21:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao21 = pygame.Rect(rec_solos21.x, rec_solos21.y + (i+1) * rec_solos21.height, rec_solos21.width, rec_solos21.height)
                    pygame.draw.rect(janela, preto, rec_opcao21)
                    pygame.draw.rect(janela, vermelho, rec_opcao21, 1)
                    texto_solo21 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo21, (rec_opcao21.x + 10, rec_opcao21.y + 10))

        if count > 18:
            texto_profundidade20 = fonte.render(profundidade20, True, preto)
            rec_texto_profundidade20 = texto_profundidade20.get_rect(center = rec_profundidade20.center)
            pygame.draw.rect(janela, branco, rec_profundidade20)
            pygame.draw.rect(janela, preto, rec_profundidade20, 1)
            janela.blit(texto_profundidade20, rec_texto_profundidade20)

            texto_NSPT20 = fonte.render(NSPT20.lstrip('0'), True, preto)
            rec_texto_NSPT20 = texto_NSPT20.get_rect(center=rec_NSPT20.center)
            pygame.draw.rect(janela, branco, rec_NSPT20)
            pygame.draw.rect(janela, preto, rec_NSPT20, 1)
            janela.blit(texto_NSPT20, rec_texto_NSPT20)
            if NSPT20_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT20.x + texto_NSPT20.get_width(), rec_texto_NSPT20.y, 2, texto_NSPT20.get_height()))
            
            if solo20 is None:
                texto_solo20 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo20 = fonte.render(solo20, True, preto)
            rec_texto_solo20 = texto_solo20.get_rect(center=rec_solos20.center)
            pygame.draw.rect(janela, branco, rec_solos20)
            pygame.draw.rect(janela, preto, rec_solos20, 1)
            janela.blit(texto_solo20, rec_texto_solo20)

            if solos_select20:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao20 = pygame.Rect(rec_solos20.x, rec_solos20.y + (i+1) * rec_solos20.height, rec_solos20.width, rec_solos20.height)
                    pygame.draw.rect(janela, preto, rec_opcao20)
                    pygame.draw.rect(janela, vermelho, rec_opcao20, 1)
                    texto_solo20 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo20, (rec_opcao20.x + 10, rec_opcao20.y + 10))

        if count > 17:
            texto_profundidade19 = fonte.render(profundidade19, True, preto)
            rec_texto_profundidade19 = texto_profundidade19.get_rect(center = rec_profundidade19.center)
            pygame.draw.rect(janela, branco, rec_profundidade19)
            pygame.draw.rect(janela, preto, rec_profundidade19, 1)
            janela.blit(texto_profundidade19, rec_texto_profundidade19)

            texto_NSPT19 = fonte.render(NSPT19.lstrip('0'), True, preto)
            rec_texto_NSPT19 = texto_NSPT19.get_rect(center=rec_NSPT19.center)
            pygame.draw.rect(janela, branco, rec_NSPT19)
            pygame.draw.rect(janela, preto, rec_NSPT19, 1)
            janela.blit(texto_NSPT19, rec_texto_NSPT19)
            if NSPT19_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT19.x + texto_NSPT19.get_width(), rec_texto_NSPT19.y, 2, texto_NSPT19.get_height()))
            
            if solo19 is None:
                texto_solo19 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo19 = fonte.render(solo19, True, preto)
            rec_texto_solo19 = texto_solo19.get_rect(center=rec_solos19.center)
            pygame.draw.rect(janela, branco, rec_solos19)
            pygame.draw.rect(janela, preto, rec_solos19, 1)
            janela.blit(texto_solo19, rec_texto_solo19)

            if solos_select19:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao19 = pygame.Rect(rec_solos19.x, rec_solos19.y + (i+1) * rec_solos19.height, rec_solos19.width, rec_solos19.height)
                    pygame.draw.rect(janela, preto, rec_opcao19)
                    pygame.draw.rect(janela, vermelho, rec_opcao19, 1)
                    texto_solo19 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo19, (rec_opcao19.x + 10, rec_opcao19.y + 10))

        if count > 16:
            texto_profundidade18 = fonte.render(profundidade18, True, preto)
            rec_texto_profundidade18 = texto_profundidade18.get_rect(center = rec_profundidade18.center)
            pygame.draw.rect(janela, branco, rec_profundidade18)
            pygame.draw.rect(janela, preto, rec_profundidade18, 1)
            janela.blit(texto_profundidade18, rec_texto_profundidade18)

            texto_NSPT18 = fonte.render(NSPT18.lstrip('0'), True, preto)
            rec_texto_NSPT18 = texto_NSPT18.get_rect(center=rec_NSPT18.center)
            pygame.draw.rect(janela, branco, rec_NSPT18)
            pygame.draw.rect(janela, preto, rec_NSPT18, 1)
            janela.blit(texto_NSPT18, rec_texto_NSPT18)
            if NSPT18_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT18.x + texto_NSPT18.get_width(), rec_texto_NSPT18.y, 2, texto_NSPT18.get_height()))
            
            if solo18 is None:
                texto_solo18 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo18 = fonte.render(solo18, True, preto)
            rec_texto_solo18 = texto_solo18.get_rect(center=rec_solos18.center)
            pygame.draw.rect(janela, branco, rec_solos18)
            pygame.draw.rect(janela, preto, rec_solos18, 1)
            janela.blit(texto_solo18, rec_texto_solo18)

            if solos_select18:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao18 = pygame.Rect(rec_solos18.x, rec_solos18.y + (i+1) * rec_solos18.height, rec_solos18.width, rec_solos18.height)
                    pygame.draw.rect(janela, preto, rec_opcao18)
                    pygame.draw.rect(janela, vermelho, rec_opcao18, 1)
                    texto_solo18 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo18, (rec_opcao18.x + 10, rec_opcao18.y + 10))

        if count > 15:
            texto_profundidade17 = fonte.render(profundidade17, True, preto)
            rec_texto_profundidade17 = texto_profundidade17.get_rect(center = rec_profundidade17.center)
            pygame.draw.rect(janela, branco, rec_profundidade17)
            pygame.draw.rect(janela, preto, rec_profundidade17, 1)
            janela.blit(texto_profundidade17, rec_texto_profundidade17)

            texto_NSPT17 = fonte.render(NSPT17.lstrip('0'), True, preto)
            rec_texto_NSPT17 = texto_NSPT17.get_rect(center=rec_NSPT17.center)
            pygame.draw.rect(janela, branco, rec_NSPT17)
            pygame.draw.rect(janela, preto, rec_NSPT17, 1)
            janela.blit(texto_NSPT17, rec_texto_NSPT17)
            if NSPT17_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT17.x + texto_NSPT17.get_width(), rec_texto_NSPT17.y, 2, texto_NSPT17.get_height()))
            
            if solo17 is None:
                texto_solo17 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo17 = fonte.render(solo17, True, preto)
            rec_texto_solo17 = texto_solo17.get_rect(center=rec_solos17.center)
            pygame.draw.rect(janela, branco, rec_solos17)
            pygame.draw.rect(janela, preto, rec_solos17, 1)
            janela.blit(texto_solo17, rec_texto_solo17)

            if solos_select17:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao17 = pygame.Rect(rec_solos17.x, rec_solos17.y + (i+1) * rec_solos17.height, rec_solos17.width, rec_solos17.height)
                    pygame.draw.rect(janela, preto, rec_opcao17)
                    pygame.draw.rect(janela, vermelho, rec_opcao17, 1)
                    texto_solo17 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo17, (rec_opcao17.x + 10, rec_opcao17.y + 10))

        if count > 14:
            texto_profundidade16 = fonte.render(profundidade16, True, preto)
            rec_texto_profundidade16 = texto_profundidade16.get_rect(center = rec_profundidade16.center)
            pygame.draw.rect(janela, branco, rec_profundidade16)
            pygame.draw.rect(janela, preto, rec_profundidade16, 1)
            janela.blit(texto_profundidade16, rec_texto_profundidade16)

            texto_NSPT16 = fonte.render(NSPT16.lstrip('0'), True, preto)
            rec_texto_NSPT16 = texto_NSPT16.get_rect(center=rec_NSPT16.center)
            pygame.draw.rect(janela, branco, rec_NSPT16)
            pygame.draw.rect(janela, preto, rec_NSPT16, 1)
            janela.blit(texto_NSPT16, rec_texto_NSPT16)
            if NSPT16_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT16.x + texto_NSPT16.get_width(), rec_texto_NSPT16.y, 2, texto_NSPT16.get_height()))
            
            if solo16 is None:
                texto_solo16 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo16 = fonte.render(solo16, True, preto)
            rec_texto_solo16 = texto_solo16.get_rect(center=rec_solos16.center)
            pygame.draw.rect(janela, branco, rec_solos16)
            pygame.draw.rect(janela, preto, rec_solos16, 1)
            janela.blit(texto_solo16, rec_texto_solo16)

            if solos_select16:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao16 = pygame.Rect(rec_solos16.x, rec_solos16.y + (i+1) * rec_solos16.height, rec_solos16.width, rec_solos16.height)
                    pygame.draw.rect(janela, preto, rec_opcao16)
                    pygame.draw.rect(janela, vermelho, rec_opcao16, 1)
                    texto_solo16 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo16, (rec_opcao16.x + 10, rec_opcao16.y + 10))

        if count > 13:
            texto_profundidade15 = fonte.render(profundidade15, True, preto)
            rec_texto_profundidade15 = texto_profundidade15.get_rect(center = rec_profundidade15.center)
            pygame.draw.rect(janela, branco, rec_profundidade15)
            pygame.draw.rect(janela, preto, rec_profundidade15, 1)
            janela.blit(texto_profundidade15, rec_texto_profundidade15)

            texto_NSPT15 = fonte.render(NSPT15.lstrip('0'), True, preto)
            rec_texto_NSPT15 = texto_NSPT15.get_rect(center=rec_NSPT15.center)
            pygame.draw.rect(janela, branco, rec_NSPT15)
            pygame.draw.rect(janela, preto, rec_NSPT15, 1)
            janela.blit(texto_NSPT15, rec_texto_NSPT15)
            if NSPT15_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT15.x + texto_NSPT15.get_width(), rec_texto_NSPT15.y, 2, texto_NSPT15.get_height()))
            
            if solo15 is None:
                texto_solo15 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo15 = fonte.render(solo15, True, preto)
            rec_texto_solo15 = texto_solo15.get_rect(center=rec_solos15.center)
            pygame.draw.rect(janela, branco, rec_solos15)
            pygame.draw.rect(janela, preto, rec_solos15, 1)
            janela.blit(texto_solo15, rec_texto_solo15)

            if solos_select15:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao15 = pygame.Rect(rec_solos15.x, rec_solos15.y + (i+1) * rec_solos15.height, rec_solos15.width, rec_solos15.height)
                    pygame.draw.rect(janela, preto, rec_opcao15)
                    pygame.draw.rect(janela, vermelho, rec_opcao15, 1)
                    texto_solo15 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo15, (rec_opcao15.x + 10, rec_opcao15.y + 10))

        if count > 12:
            texto_profundidade14 = fonte.render(profundidade14, True, preto)
            rec_texto_profundidade14 = texto_profundidade14.get_rect(center = rec_profundidade14.center)
            pygame.draw.rect(janela, branco, rec_profundidade14)
            pygame.draw.rect(janela, preto, rec_profundidade14, 1)
            janela.blit(texto_profundidade14, rec_texto_profundidade14)

            texto_NSPT14 = fonte.render(NSPT14.lstrip('0'), True, preto)
            rec_texto_NSPT14 = texto_NSPT14.get_rect(center=rec_NSPT14.center)
            pygame.draw.rect(janela, branco, rec_NSPT14)
            pygame.draw.rect(janela, preto, rec_NSPT14, 1)
            janela.blit(texto_NSPT14, rec_texto_NSPT14)
            if NSPT14_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT14.x + texto_NSPT14.get_width(), rec_texto_NSPT14.y, 2, texto_NSPT14.get_height()))
            
            if solo14 is None:
                texto_solo14 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo14 = fonte.render(solo14, True, preto)
            rec_texto_solo14 = texto_solo14.get_rect(center=rec_solos14.center)
            pygame.draw.rect(janela, branco, rec_solos14)
            pygame.draw.rect(janela, preto, rec_solos14, 1)
            janela.blit(texto_solo14, rec_texto_solo14)

            if solos_select14:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao14 = pygame.Rect(rec_solos14.x, rec_solos14.y + (i+1) * rec_solos14.height, rec_solos14.width, rec_solos14.height)
                    pygame.draw.rect(janela, preto, rec_opcao14)
                    pygame.draw.rect(janela, vermelho, rec_opcao14, 1)
                    texto_solo14 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo14, (rec_opcao14.x + 10, rec_opcao14.y + 10))

        if count > 11:
            texto_profundidade13 = fonte.render(profundidade13, True, preto)
            rec_texto_profundidade13 = texto_profundidade13.get_rect(center = rec_profundidade13.center)
            pygame.draw.rect(janela, branco, rec_profundidade13)
            pygame.draw.rect(janela, preto, rec_profundidade13, 1)
            janela.blit(texto_profundidade13, rec_texto_profundidade13)

            texto_NSPT13 = fonte.render(NSPT13.lstrip('0'), True, preto)
            rec_texto_NSPT13 = texto_NSPT13.get_rect(center=rec_NSPT13.center)
            pygame.draw.rect(janela, branco, rec_NSPT13)
            pygame.draw.rect(janela, preto, rec_NSPT13, 1)
            janela.blit(texto_NSPT13, rec_texto_NSPT13)
            if NSPT13_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT13.x + texto_NSPT13.get_width(), rec_texto_NSPT13.y, 2, texto_NSPT13.get_height()))
            
            if solo13 is None:
                texto_solo13 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo13 = fonte.render(solo13, True, preto)
            rec_texto_solo13 = texto_solo13.get_rect(center=rec_solos13.center)
            pygame.draw.rect(janela, branco, rec_solos13)
            pygame.draw.rect(janela, preto, rec_solos13, 1)
            janela.blit(texto_solo13, rec_texto_solo13)

            if solos_select13:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao13 = pygame.Rect(rec_solos13.x, rec_solos13.y + (i+1) * rec_solos13.height, rec_solos13.width, rec_solos13.height)
                    pygame.draw.rect(janela, preto, rec_opcao13)
                    pygame.draw.rect(janela, vermelho, rec_opcao13, 1)
                    texto_solo13 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo13, (rec_opcao13.x + 10, rec_opcao13.y + 10))

        if count > 10:
            texto_profundidade12 = fonte.render(profundidade12, True, preto)
            rec_texto_profundidade12 = texto_profundidade12.get_rect(center = rec_profundidade12.center)
            pygame.draw.rect(janela, branco, rec_profundidade12)
            pygame.draw.rect(janela, preto, rec_profundidade12, 1)
            janela.blit(texto_profundidade12, rec_texto_profundidade12)

            texto_NSPT12 = fonte.render(NSPT12.lstrip('0'), True, preto)
            rec_texto_NSPT12 = texto_NSPT12.get_rect(center=rec_NSPT12.center)
            pygame.draw.rect(janela, branco, rec_NSPT12)
            pygame.draw.rect(janela, preto, rec_NSPT12, 1)
            janela.blit(texto_NSPT12, rec_texto_NSPT12)
            if NSPT12_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT12.x + texto_NSPT12.get_width(), rec_texto_NSPT12.y, 2, texto_NSPT12.get_height()))
            
            if solo12 is None:
                texto_solo12 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo12 = fonte.render(solo12, True, preto)
            rec_texto_solo12 = texto_solo12.get_rect(center=rec_solos12.center)
            pygame.draw.rect(janela, branco, rec_solos12)
            pygame.draw.rect(janela, preto, rec_solos12, 1)
            janela.blit(texto_solo12, rec_texto_solo12)

            if solos_select12:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao12 = pygame.Rect(rec_solos12.x, rec_solos12.y + (i+1) * rec_solos12.height, rec_solos12.width, rec_solos12.height)
                    pygame.draw.rect(janela, preto, rec_opcao12)
                    pygame.draw.rect(janela, vermelho, rec_opcao12, 1)
                    texto_solo12 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo12, (rec_opcao12.x + 10, rec_opcao12.y + 10))

        if count > 9:
            texto_profundidade11 = fonte.render(profundidade11, True, preto)
            rec_texto_profundidade11 = texto_profundidade11.get_rect(center = rec_profundidade11.center)
            pygame.draw.rect(janela, branco, rec_profundidade11)
            pygame.draw.rect(janela, preto, rec_profundidade11, 1)
            janela.blit(texto_profundidade11, rec_texto_profundidade11)

            texto_NSPT11 = fonte.render(NSPT11.lstrip('0'), True, preto)
            rec_texto_NSPT11 = texto_NSPT11.get_rect(center=rec_NSPT11.center)
            pygame.draw.rect(janela, branco, rec_NSPT11)
            pygame.draw.rect(janela, preto, rec_NSPT11, 1)
            janela.blit(texto_NSPT11, rec_texto_NSPT11)
            if NSPT11_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT11.x + texto_NSPT11.get_width(), rec_texto_NSPT11.y, 2, texto_NSPT11.get_height()))
            
            if solo11 is None:
                texto_solo11 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo11 = fonte.render(solo11, True, preto)
            rec_texto_solo11 = texto_solo11.get_rect(center=rec_solos11.center)
            pygame.draw.rect(janela, branco, rec_solos11)
            pygame.draw.rect(janela, preto, rec_solos11, 1)
            janela.blit(texto_solo11, rec_texto_solo11)

            if solos_select11:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao11 = pygame.Rect(rec_solos11.x, rec_solos11.y + (i+1) * rec_solos11.height, rec_solos11.width, rec_solos11.height)
                    pygame.draw.rect(janela, preto, rec_opcao11)
                    pygame.draw.rect(janela, vermelho, rec_opcao11, 1)
                    texto_solo11 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo11, (rec_opcao11.x + 10, rec_opcao11.y + 10))

        if count > 8:
            texto_profundidade10 = fonte.render(profundidade10, True, preto)
            rec_texto_profundidade10 = texto_profundidade10.get_rect(center = rec_profundidade10.center)
            pygame.draw.rect(janela, branco, rec_profundidade10)
            pygame.draw.rect(janela, preto, rec_profundidade10, 1)
            janela.blit(texto_profundidade10, rec_texto_profundidade10)

            texto_NSPT10 = fonte.render(NSPT10.lstrip('0'), True, preto)
            rec_texto_NSPT10 = texto_NSPT10.get_rect(center=rec_NSPT10.center)
            pygame.draw.rect(janela, branco, rec_NSPT10)
            pygame.draw.rect(janela, preto, rec_NSPT10, 1)
            janela.blit(texto_NSPT10, rec_texto_NSPT10)
            if NSPT10_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT10.x + texto_NSPT10.get_width(), rec_texto_NSPT10.y, 2, texto_NSPT10.get_height()))
            
            if solo10 is None:
                texto_solo10 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo10 = fonte.render(solo10, True, preto)
            rec_texto_solo10 = texto_solo10.get_rect(center=rec_solos10.center)
            pygame.draw.rect(janela, branco, rec_solos10)
            pygame.draw.rect(janela, preto, rec_solos10, 1)
            janela.blit(texto_solo10, rec_texto_solo10)

            if solos_select10:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao10 = pygame.Rect(rec_solos10.x, rec_solos10.y + (i+1) * rec_solos10.height, rec_solos10.width, rec_solos10.height)
                    pygame.draw.rect(janela, preto, rec_opcao10)
                    pygame.draw.rect(janela, vermelho, rec_opcao10, 1)
                    texto_solo10 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo10, (rec_opcao10.x + 10, rec_opcao10.y + 10))

        if count > 7:
            texto_profundidade9 = fonte.render(profundidade9, True, preto)
            rec_texto_profundidade9 = texto_profundidade9.get_rect(center = rec_profundidade9.center)
            pygame.draw.rect(janela, branco, rec_profundidade9)
            pygame.draw.rect(janela, preto, rec_profundidade9, 1)
            janela.blit(texto_profundidade9, rec_texto_profundidade9)

            texto_NSPT9 = fonte.render(NSPT9.lstrip('0'), True, preto)
            rec_texto_NSPT9 = texto_NSPT9.get_rect(center=rec_NSPT9.center)
            pygame.draw.rect(janela, branco, rec_NSPT9)
            pygame.draw.rect(janela, preto, rec_NSPT9, 1)
            janela.blit(texto_NSPT9, rec_texto_NSPT9)
            if NSPT9_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT9.x + texto_NSPT9.get_width(), rec_texto_NSPT9.y, 2, texto_NSPT9.get_height()))
            
            if solo9 is None:
                texto_solo9 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo9 = fonte.render(solo9, True, preto)
            rec_texto_solo9 = texto_solo9.get_rect(center=rec_solos9.center)
            pygame.draw.rect(janela, branco, rec_solos9)
            pygame.draw.rect(janela, preto, rec_solos9, 1)
            janela.blit(texto_solo9, rec_texto_solo9)

            if solos_select9:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao9 = pygame.Rect(rec_solos9.x, rec_solos9.y + (i+1) * rec_solos9.height, rec_solos9.width, rec_solos9.height)
                    pygame.draw.rect(janela, preto, rec_opcao9)
                    pygame.draw.rect(janela, vermelho, rec_opcao9, 1)
                    texto_solo9 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo9, (rec_opcao9.x + 10, rec_opcao9.y + 10))

        if count > 6:
            texto_profundidade8 = fonte.render(profundidade8, True, preto)
            rec_texto_profundidade8 = texto_profundidade8.get_rect(center = rec_profundidade8.center)
            pygame.draw.rect(janela, branco, rec_profundidade8)
            pygame.draw.rect(janela, preto, rec_profundidade8, 1)
            janela.blit(texto_profundidade8, rec_texto_profundidade8)

            texto_NSPT8 = fonte.render(NSPT8.lstrip('0'), True, preto)
            rec_texto_NSPT8 = texto_NSPT8.get_rect(center=rec_NSPT8.center)
            pygame.draw.rect(janela, branco, rec_NSPT8)
            pygame.draw.rect(janela, preto, rec_NSPT8, 1)
            janela.blit(texto_NSPT8, rec_texto_NSPT8)
            if NSPT8_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT8.x + texto_NSPT8.get_width(), rec_texto_NSPT8.y, 2, texto_NSPT8.get_height()))
            
            if solo8 is None:
                texto_solo8 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo8 = fonte.render(solo8, True, preto)
            rec_texto_solo8 = texto_solo8.get_rect(center=rec_solos8.center)
            pygame.draw.rect(janela, branco, rec_solos8)
            pygame.draw.rect(janela, preto, rec_solos8, 1)
            janela.blit(texto_solo8, rec_texto_solo8)

            if solos_select8:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao8 = pygame.Rect(rec_solos8.x, rec_solos8.y + (i+1) * rec_solos8.height, rec_solos8.width, rec_solos8.height)
                    pygame.draw.rect(janela, preto, rec_opcao8)
                    pygame.draw.rect(janela, vermelho, rec_opcao8, 1)
                    texto_solo8 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo8, (rec_opcao8.x + 10, rec_opcao8.y + 10))

        if count > 5:
            texto_profundidade7 = fonte.render(profundidade7, True, preto)
            rec_texto_profundidade7 = texto_profundidade7.get_rect(center = rec_profundidade7.center)
            pygame.draw.rect(janela, branco, rec_profundidade7)
            pygame.draw.rect(janela, preto, rec_profundidade7, 1)
            janela.blit(texto_profundidade7, rec_texto_profundidade7)

            texto_NSPT7 = fonte.render(NSPT7.lstrip('0'), True, preto)
            rec_texto_NSPT7 = texto_NSPT7.get_rect(center=rec_NSPT7.center)
            pygame.draw.rect(janela, branco, rec_NSPT7)
            pygame.draw.rect(janela, preto, rec_NSPT7, 1)
            janela.blit(texto_NSPT7, rec_texto_NSPT7)
            if NSPT7_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT7.x + texto_NSPT7.get_width(), rec_texto_NSPT7.y, 2, texto_NSPT7.get_height()))
            
            if solo7 is None:
                texto_solo7 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo7 = fonte.render(solo7, True, preto)
            rec_texto_solo7 = texto_solo7.get_rect(center=rec_solos7.center)
            pygame.draw.rect(janela, branco, rec_solos7)
            pygame.draw.rect(janela, preto, rec_solos7, 1)
            janela.blit(texto_solo7, rec_texto_solo7)

            if solos_select7:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao7 = pygame.Rect(rec_solos7.x, rec_solos7.y + (i+1) * rec_solos7.height, rec_solos7.width, rec_solos7.height)
                    pygame.draw.rect(janela, preto, rec_opcao7)
                    pygame.draw.rect(janela, vermelho, rec_opcao7, 1)
                    texto_solo7 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo7, (rec_opcao7.x + 10, rec_opcao7.y + 10))

        if count > 4:
            texto_profundidade6 = fonte.render(profundidade6, True, preto)
            rec_texto_profundidade6 = texto_profundidade6.get_rect(center = rec_profundidade6.center)
            pygame.draw.rect(janela, branco, rec_profundidade6)
            pygame.draw.rect(janela, preto, rec_profundidade6, 1)
            janela.blit(texto_profundidade6, rec_texto_profundidade6)

            texto_NSPT6 = fonte.render(NSPT6.lstrip('0'), True, preto)
            rec_texto_NSPT6 = texto_NSPT6.get_rect(center=rec_NSPT6.center)
            pygame.draw.rect(janela, branco, rec_NSPT6)
            pygame.draw.rect(janela, preto, rec_NSPT6, 1)
            janela.blit(texto_NSPT6, rec_texto_NSPT6)
            if NSPT6_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT6.x + texto_NSPT6.get_width(), rec_texto_NSPT6.y, 2, texto_NSPT6.get_height()))
            
            if solo6 is None:
                texto_solo6 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo6 = fonte.render(solo6, True, preto)
            rec_texto_solo6 = texto_solo6.get_rect(center=rec_solos6.center)
            pygame.draw.rect(janela, branco, rec_solos6)
            pygame.draw.rect(janela, preto, rec_solos6, 1)
            janela.blit(texto_solo6, rec_texto_solo6)

            if solos_select6:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao6 = pygame.Rect(rec_solos6.x, rec_solos6.y + (i+1) * rec_solos6.height, rec_solos6.width, rec_solos6.height)
                    pygame.draw.rect(janela, preto, rec_opcao6)
                    pygame.draw.rect(janela, vermelho, rec_opcao6, 1)
                    texto_solo6 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo6, (rec_opcao6.x + 10, rec_opcao6.y + 10))

        if count > 3:
            texto_profundidade5 = fonte.render(profundidade5, True, preto)
            rec_texto_profundidade5 = texto_profundidade5.get_rect(center = rec_profundidade5.center)
            pygame.draw.rect(janela, branco, rec_profundidade5)
            pygame.draw.rect(janela, preto, rec_profundidade5, 1)
            janela.blit(texto_profundidade5, rec_texto_profundidade5)

            texto_NSPT5 = fonte.render(NSPT5.lstrip('0'), True, preto)
            rec_texto_NSPT5 = texto_NSPT5.get_rect(center=rec_NSPT5.center)
            pygame.draw.rect(janela, branco, rec_NSPT5)
            pygame.draw.rect(janela, preto, rec_NSPT5, 1)
            janela.blit(texto_NSPT5, rec_texto_NSPT5)
            if NSPT5_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT5.x + texto_NSPT5.get_width(), rec_texto_NSPT5.y, 2, texto_NSPT5.get_height()))
            
            if solo5 is None:
                texto_solo5 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo5 = fonte.render(solo5, True, preto)
            rec_texto_solo5 = texto_solo5.get_rect(center=rec_solos5.center)
            pygame.draw.rect(janela, branco, rec_solos5)
            pygame.draw.rect(janela, preto, rec_solos5, 1)
            janela.blit(texto_solo5, rec_texto_solo5)

            if solos_select5:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao5 = pygame.Rect(rec_solos5.x, rec_solos5.y + (i+1) * rec_solos5.height, rec_solos5.width, rec_solos5.height)
                    pygame.draw.rect(janela, preto, rec_opcao5)
                    pygame.draw.rect(janela, vermelho, rec_opcao5, 1)
                    texto_solo5 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo5, (rec_opcao5.x + 10, rec_opcao5.y + 10))

        if count > 2:
            texto_profundidade4 = fonte.render(profundidade4, True, preto)
            rec_texto_profundidade4 = texto_profundidade4.get_rect(center = rec_profundidade4.center)
            pygame.draw.rect(janela, branco, rec_profundidade4)
            pygame.draw.rect(janela, preto, rec_profundidade4, 1)
            janela.blit(texto_profundidade4, rec_texto_profundidade4)

            texto_NSPT4 = fonte.render(NSPT4.lstrip('0'), True, preto)
            rec_texto_NSPT4 = texto_NSPT4.get_rect(center=rec_NSPT4.center)
            pygame.draw.rect(janela, branco, rec_NSPT4)
            pygame.draw.rect(janela, preto, rec_NSPT4, 1)
            janela.blit(texto_NSPT4, rec_texto_NSPT4)
            if NSPT4_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT4.x + texto_NSPT4.get_width(), rec_texto_NSPT4.y, 2, texto_NSPT4.get_height()))
            
            if solo4 is None:
                texto_solo4 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo4 = fonte.render(solo4, True, preto)
            rec_texto_solo4 = texto_solo4.get_rect(center=rec_solos4.center)
            pygame.draw.rect(janela, branco, rec_solos4)
            pygame.draw.rect(janela, preto, rec_solos4, 1)
            janela.blit(texto_solo4, rec_texto_solo4)

            if solos_select4:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao4 = pygame.Rect(rec_solos4.x, rec_solos4.y + (i+1) * rec_solos4.height, rec_solos4.width, rec_solos4.height)
                    pygame.draw.rect(janela, preto, rec_opcao4)
                    pygame.draw.rect(janela, vermelho, rec_opcao4, 1)
                    texto_solo4 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo4, (rec_opcao4.x + 10, rec_opcao4.y + 10))

        if count > 1:
            texto_profundidade3 = fonte.render(profundidade3, True, preto)
            rec_texto_profundidade3 = texto_profundidade3.get_rect(center = rec_profundidade3.center)
            pygame.draw.rect(janela, branco, rec_profundidade3)
            pygame.draw.rect(janela, preto, rec_profundidade3, 1)
            janela.blit(texto_profundidade3, rec_texto_profundidade3)

            texto_NSPT3 = fonte.render(NSPT3.lstrip('0'), True, preto)
            rec_texto_NSPT3 = texto_NSPT3.get_rect(center=rec_NSPT3.center)
            pygame.draw.rect(janela, branco, rec_NSPT3)
            pygame.draw.rect(janela, preto, rec_NSPT3, 1)
            janela.blit(texto_NSPT3, rec_texto_NSPT3)
            if NSPT3_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT3.x + texto_NSPT3.get_width(), rec_texto_NSPT3.y, 2, texto_NSPT3.get_height()))
            
            if solo3 is None:
                texto_solo3 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo3 = fonte.render(solo3, True, preto)
            rec_texto_solo3 = texto_solo3.get_rect(center=rec_solos3.center)
            pygame.draw.rect(janela, branco, rec_solos3)
            pygame.draw.rect(janela, preto, rec_solos3, 1)
            janela.blit(texto_solo3, rec_texto_solo3)

            if solos_select3:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao3 = pygame.Rect(rec_solos3.x, rec_solos3.y + (i+1) * rec_solos3.height, rec_solos3.width, rec_solos3.height)
                    pygame.draw.rect(janela, preto, rec_opcao3)
                    pygame.draw.rect(janela, vermelho, rec_opcao3, 1)
                    texto_solo3 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo3, (rec_opcao3.x + 10, rec_opcao3.y + 10))

        if count > 0:
            texto_profundidade2 = fonte.render(profundidade2, True, preto)
            rec_texto_profundidade2 = texto_profundidade2.get_rect(center = rec_profundidade2.center)
            pygame.draw.rect(janela, branco, rec_profundidade2)
            pygame.draw.rect(janela, preto, rec_profundidade2, 1)
            janela.blit(texto_profundidade2, rec_texto_profundidade2)

            texto_NSPT2 = fonte.render(NSPT2.lstrip('0'), True, preto)
            rec_texto_NSPT2 = texto_NSPT2.get_rect(center=rec_NSPT2.center)
            pygame.draw.rect(janela, branco, rec_NSPT2)
            pygame.draw.rect(janela, preto, rec_NSPT2, 1)
            janela.blit(texto_NSPT2, rec_texto_NSPT2)
            if NSPT2_select:
                pygame.draw.rect(janela, preto, (rec_texto_NSPT2.x + texto_NSPT2.get_width(), rec_texto_NSPT2.y, 2, texto_NSPT2.get_height()))
            
            if solo2 is None:
                texto_solo2 = fonte.render("Selecione um solo", True, preto)
            else:
                texto_solo2 = fonte.render(solo2, True, preto)
            rec_texto_solo2 = texto_solo2.get_rect(center=rec_solos2.center)
            pygame.draw.rect(janela, branco, rec_solos2)
            pygame.draw.rect(janela, preto, rec_solos2, 1)
            janela.blit(texto_solo2, rec_texto_solo2)

            if solos_select2:
                for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                    rec_opcao2 = pygame.Rect(rec_solos2.x, rec_solos2.y + (i+1) * rec_solos2.height, rec_solos2.width, rec_solos2.height)
                    pygame.draw.rect(janela, preto, rec_opcao2)
                    pygame.draw.rect(janela, vermelho, rec_opcao2, 1)
                    texto_solo2 = fonte.render(opcao, True, branco)
                    janela.blit(texto_solo2, (rec_opcao2.x + 10, rec_opcao2.y + 10))

        texto_coluna1 = fonte.render(coluna1, True, preto)
        rec_texto_coluna1 = texto_coluna1.get_rect(center=rec_coluna1.center)
        pygame.draw.rect(janela, cinza_claro, rec_coluna1)
        pygame.draw.rect(janela, preto, rec_coluna1, 1)
        janela.blit(texto_coluna1, rec_texto_coluna1)

        texto_coluna2 = fonte.render(coluna2, True, preto)
        rec_texto_coluna2 = texto_coluna2.get_rect(center=rec_coluna2.center)
        pygame.draw.rect(janela, cinza_claro, rec_coluna2)
        pygame.draw.rect(janela, preto, rec_coluna2, 1)
        janela.blit(texto_coluna2, rec_texto_coluna2)
        
        texto_coluna3 = fonte.render(coluna3, True, preto)
        rec_texto_coluna3 = texto_coluna3.get_rect(center=rec_coluna3.center)
        pygame.draw.rect(janela, cinza_claro, rec_coluna3)
        pygame.draw.rect(janela, preto, rec_coluna3, 1)
        janela.blit(texto_coluna3, rec_texto_coluna3)

        texto_profundidade = fonte.render(profundidade, True, preto)
        rec_texto_profundidade = texto_profundidade.get_rect(center=rec_profundidade.center)
        pygame.draw.rect(janela, branco, rec_profundidade)
        pygame.draw.rect(janela, preto, rec_profundidade, 1)
        janela.blit(texto_profundidade, rec_texto_profundidade)

        texto_NSPT = fonte.render(NSPT.lstrip('0'), True, preto)
        rec_texto_NSPT = texto_NSPT.get_rect(center=rec_NSPT.center)
        pygame.draw.rect(janela, branco, rec_NSPT)
        pygame.draw.rect(janela, preto, rec_NSPT, 1)
        janela.blit(texto_NSPT, rec_texto_NSPT)

        if solo is None:
            texto_solo = fonte.render("Selecione um solo", True, preto)
        else:
            texto_solo = fonte.render(solo, True, preto)
        rec_texto_solo = texto_solo.get_rect(center=rec_solos.center)
        pygame.draw.rect(janela, branco, rec_solos)
        pygame.draw.rect(janela, preto, rec_solos, 1)
        janela.blit(texto_solo, rec_texto_solo)

        if NSPT_select:
            pygame.draw.rect(janela, preto, (rec_texto_NSPT.x + texto_NSPT.get_width(), rec_texto_NSPT.y, 2, texto_NSPT.get_height()))

        if solos_select:
            for i, opcao in enumerate(solos[scroll_position:scroll_position+itens_visiveis]):
                rec_opcao = pygame.Rect(rec_solos.x, rec_solos.y + (i+1) * rec_solos.height, rec_solos.width, rec_solos.height)
                pygame.draw.rect(janela, preto, rec_opcao)
                pygame.draw.rect(janela, vermelho, rec_opcao, 1)
                texto_solo = fonte.render(opcao, True, branco)
                janela.blit(texto_solo, (rec_opcao.x + 10, rec_opcao.y + 10))
        
        texto_add = fonte.render('Adicionar', True, preto)
        rec_texto_add = texto_add.get_rect(center=rec_add.center)
        pygame.draw.rect(janela, rec_add_color, rec_add)
        janela.blit(texto_add, rec_texto_add)

        texto_remove = fonte.render('Remover', True, preto)
        rec_texto_remove = texto_remove.get_rect(center = rec_remove.center)
        pygame.draw.rect(janela, rec_remove_color, rec_remove)
        janela.blit(texto_remove, rec_texto_remove)

    pygame.display.flip()
    clock.tick(60)