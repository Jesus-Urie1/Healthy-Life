# -*- coding: utf-8 -*-
#enconding: utf-8
import pygame, sys
import time
import random
from pygame.locals import *

pygame.init()
pygame.mixer.init()

# R,G,B - SomeColors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (17, 124, 47)
green2 = (27, 102, 3)
gold = (255, 191, 0)
red = (255, 0, 0)
gold = (239,184,16)

#Constants
lives = 3
score = 0
musica = True

cont=0
direc=True
i=0
fondopause=0
xixf={}#xinicial y xfinal
Rxixf={}
#LoadImages (Food Healthy)
manzanaImg = pygame.image.load("./Assets/Image/Comida/manzana.png")
brocoliImg = pygame.image.load("./Assets/Image/Comida/Brocoli.png")
zanahoriaImg = pygame.image.load("./Assets/Image/Comida/Zanahoria.png")
platanoImg = pygame.image.load("./Assets/Image/Comida/Platano.png")
sandiaImg = pygame.image.load("./Assets/Image/Comida/Sandia.png")
naranjaImg = pygame.image.load("./Assets/Image/Comida/Naranja.png")
tomateImg = pygame.image.load("./Assets/Image/Comida/Tomate.png")
cerezaImg = pygame.image.load("./Assets/Image/Comida/Cereza.png")
#LoadImages (Food No Healthy)
maruchanImg = pygame.image.load("./Assets/Image/Comida/Maruchan.png")
hamburImg = pygame.image.load("./Assets/Image/Comida/Hamburgesa.png")
donaImg = pygame.image.load("./Assets/Image/Comida/Dona.png")
polloImg = pygame.image.load("./Assets/Image/Comida/Pollo.png")
hotdogImg = pygame.image.load("./Assets/Image/Comida/Hotdog.png")
pizzaImg = pygame.image.load("./Assets/Image/Comida/Pizza.png")
papasImg = pygame.image.load("./Assets/Image/Comida/Papas.png")
cupcakeImg = pygame.image.load("./Assets/Image/Comida/Cupcake.png")

#Backgrounds
fondoCasa = pygame.image.load("./Assets/Image/Fondos/fondocasa.jpeg")
fondoInicio = pygame.image.load("./Assets/Image/Fondos/FondoInicio.png")
fondoParque = pygame.image.load("./Assets/Image/Fondos/fondoParque.png")
fondoPueblo = pygame.image.load("./Assets/Image/Fondos/fondoPueblo.png")
fondoPlaya = pygame.image.load("./Assets/Image/Fondos/FondoPlaya.png")
fondoTuto = pygame.image.load("./Assets/Image/Fondos/FondoTuto.jpeg")
marcoPausa = pygame.image.load("./Assets/Animacion/Botones/MarcoPausa.png")
selectLevelImg = pygame.image.load("./Assets/Image/Fondos/SelectLevel.png")
#player
blueImg = pygame.image.load("./Assets/Animacion/Personaje/Blue_Sprite.png")
blueplayaImg = pygame.image.load("./Assets/Animacion/Personaje/BlueBeach.png")
blue2Img = pygame.image.load("./Assets/Animacion/Personaje/Blue.png")
#Buttons
logo = pygame.image.load("./Assets/Image/Logo/logo.png")
manzanaB = pygame.image.load("./Assets/Animacion/Botones/btn_PlayDesativado.png")
manzanaClick = pygame.image.load("./Assets/Animacion/Botones/btn_PlayActivado.png")
corazonImg = pygame.image.load("./Assets/Image/Vida/corazon_lleno.png")
pauseImg = pygame.image.load("./Assets/Animacion/Botones/Pausa.png")
pause2Img = pygame.image.load("./Assets/Animacion/Botones/Pausa_Activo.png")
casaImg = pygame.image.load("./Assets/Animacion/Botones/BotonCasa.png")
casa2Img = pygame.image.load("./Assets/Animacion/Botones/BotonCasa_Activo.png")
reanudarImg = pygame.image.load("./Assets/Animacion/Botones/BotonReanudar.png")
reanudar2Img = pygame.image.load("./Assets/Animacion/Botones/BotonReanudar2.png")
FlechaiImg = pygame.image.load("./Assets/Animacion/Botones/FlechaI.png")
FlechadImg = pygame.image.load("./Assets/Animacion/Botones/FlechaD.png")
ControlImg = pygame.image.load("./Assets/Animacion/Botones/Controles.png")
ControlAImg = pygame.image.load("./Assets/Animacion/Botones/Controles_Activo.png")
FlechaRImg = pygame.image.load("./Assets/Animacion/Botones/FlechaR.png")
FlechaR2Img = pygame.image.load("./Assets/Animacion/Botones/Flecha_Activo.png")

#Screen Inicialization
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("HealthyLife")

#SettingClock
clock = pygame.time.Clock()

#ButtonClass
class Button:
    def __init__(self, x, y, width, height, x_act, y_act, text, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        font = pygame.font.Font("04B_30__.TTF", 25)
        textb1 = font.render(text, True, green2)
        textb2 = font.render(text, True, gold)  
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(textb2,(x_act, y_act))
            if click[0] and action != None:
                action()
        else:
            gameDisplay.blit(textb1, (x, y))
class Button2:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(img_act, (x_act, y_act))
            if click[0] and action != None:
                action()
        else:
            gameDisplay.blit(img_in, (x, y))

# BackgroundClass
class Background:
    def __init__(self, bg_img, bg_x, bg_y):
        self.bg_x = bg_x
        self.bg_y = bg_y
        gameDisplay.blit(bg_img, (bg_x, bg_y))

# PlayerClass
class Player:
    def __init__(self,p_img,speedIn,blue_x,blue_y,hitbox_x,hitbox_y,speedmultiplier):
        self.speed = speedIn
        self.blue_x = blue_x
        self.blue_y = blue_y
        self.p_img = p_img
        self.hitbox_x = hitbox_x
        self.hitbox_y = hitbox_y
        self.speedmult = speedmultiplier

# GameObjectsClass
class Gameobject:
    def __init__(self, b_image, speed, coord_x, coord_y, hitbox_x, hitbox_y):
        self.b_image = b_image
        self.speed = speed
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.hitbox_x = hitbox_x
        self.hitbox_y = hitbox_y
#Livesreturn
class levelreturn:
    def __init__(self,menu,lives,level):
        if lives == 0:
            menu()
        elif lives == 3:
            level()
        elif lives == 2:
            level()
        elif lives == 1:
            level()
#PauseFunction
def Pause():
    global fondopause
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 740 + 50 > mouse[0] > 740 and -1 + 50 > mouse[1] > -1:
        gameDisplay.blit(pause2Img, (740, -1))
        if click[0]:
            pygame.mixer.music.pause()
            if fondopause == 1:
                PauseAction(fondoCasa)
            elif fondopause == 2:
                PauseAction(fondoPueblo)
            if fondopause == 3:
                PauseAction(fondoParque)
            if fondopause == 4:
                PauseAction(fondoPlaya)
            
    else:
        gameDisplay.blit(pauseImg, (740, -1))

def PauseAction(fondo):
    font = pygame.font.Font("04B_30__.TTF", 25)
    text = font.render("Pausa", True, black)  
    pausa = True
    while pausa:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()                    
        gameDisplay.blit(fondo,(0,0))
        gameDisplay.blit(marcoPausa,(0,0))
        gameDisplay.blit(text, (345, 130))
        #Returnmainmenu
        if 355 + 80 > mouse[0] > 355 and 180 + 60 > mouse[1] > 180:
            gameDisplay.blit(casa2Img,(355,180))
            if click[0]:
                pausa = False
                mainmenu()
        else:
            gameDisplay.blit(casaImg, (355,180))
        #Controles
        if 355 + 80 > mouse[0] > 355 and 260 + 60 > mouse[1] > 260:
            gameDisplay.blit(ControlAImg,(355,260))
            if click[0]:
                instruccions()
        else:
            gameDisplay.blit(ControlImg, (355,260))
        #ReanudarGame
        if 355 + 80 > mouse[0] > 355 and 340 + 60 > mouse[1] > 340:
            gameDisplay.blit(reanudar2Img,(355,340))
            if click[0]:
                pausa = False
                if musica == True:
                    pygame.mixer.music.unpause()
        else:
            gameDisplay.blit(reanudarImg, (355,340))
        
        
        pygame.display.update()
        clock.tick(30)
#Musica
def MusicaStart():
    global musica
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    font = pygame.font.Font("04B_30__.TTF", 25)
    text1 = font.render("Musica", True, green2)
    text2 = font.render("Musica", True, gold)
    gameDisplay.blit(text1, (350, 415))
    if 350 + 120 > mouse[0] > 350 and 415 + 20 > mouse[1] > 415:
        if click[0] and musica == True:
            musica = False
            mainmenu()
               
def MusicaPause():
    global musica
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    font = pygame.font.Font("04B_30__.TTF", 25)
    text2 = font.render("Musica", True, gold)
    text3 = font.render("Musica", True, red)
    gameDisplay.blit(text3, (350, 415))
    if 350 + 120 > mouse[0] > 350 and 415 + 20 > mouse[1] > 415:
        if click[0] and musica == False:
            musica = True
            mainmenu()

# ScoreFunction
def scorecounter(count):
    font = pygame.font.Font("04B_30__.TTF", 25)
    text = font.render("Puntos:" + str(count), True, black)  
    gameDisplay.blit(text, (1, 30))

# Sprite
def sprite():
    
    global cont

    xixf[0]=(0,0,46,52)
    xixf[1]=(48,0,48,52)
    xixf[2]=(50,0,50,52)
    xixf[3]=(52,0,52,52)
    
    Rxixf[0]=(52,0,52,52)
    Rxixf[1]=(50,0,50,52)
    Rxixf[2]=(48,0,48,52)
    Rxixf[3]=(0,0,46,52)
    
    p=2
    
    global i
    
    if cont==p:
        i=0
    if cont==p*2:
        i=1
    if cont==p*3:
        i=2
    if cont==p*4:
        i=3
        cont=0

    return
# CrashFunction/MessageDisplay)
def text_objects(text, font):
    textscreen = font.render(text, True, red)
    return textscreen, textscreen.get_rect()


def message_display(text):
    largeText = pygame.font.Font("8-BIT WONDER.TTF", 46)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
def crash(message):
    message_display(message)

#QuitFunction
def quitgame():
    pygame.quit()
    quit()
#==================================================

def mainmenu():
    global lives
    global score
    global musica
    select = True
    if lives == 0:
        lives = 3
    if score > 0:
        score = 0
    if musica == True:
        pygame.mixer.music.load("./Assets/Music/Level0.wav")
        pygame.mixer.music.play(3)
    if musica == False:
        pygame.mixer.music.pause()
    while select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
           
        gameDisplay.blit(fondoInicio,(0,0))
        gameDisplay.blit(logo,(0,0))
        if musica == True:
            MusicaStart()
        if musica == False:
            MusicaPause()
        Button2(manzanaB,330,230,150,150,manzanaClick,330,230,selectlevel)
        Button(290,380,250,20,290,380,"Instrucciones",instruccions)
        Button(360,445,100,20,360,445,"Salir",quitgame)

        pygame.display.update()
        clock.tick(30)

#MenuInstruccions
def instruccions():
    ciclo = True
    while ciclo:
        font = pygame.font.Font("04B_30__.TTF", 25)
        font2 = pygame.font.Font("04B_30__.TTF", 20)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #Background
        gameDisplay.blit(fondoTuto,(0,0))
        #Lives
        gameDisplay.blit(corazonImg, (580,2))
        gameDisplay.blit(corazonImg, (630,2))
        gameDisplay.blit(corazonImg, (680,2))
        #Barlife
        red_bar = pygame.Surface((300, 40))
        red_bar.fill((255, 0, 0))
        gameDisplay.blit(red_bar,(250, 2))
        pygame.draw.rect(gameDisplay, white, (250, 2, 300, 40), 5)
        pygame.draw.rect(gameDisplay, green, (250, 2, 150, 40))
        #Score and level
        text3 = font.render("Nivel", True, white)
        text = font.render("Puntos: 0", True, black)  
        gameDisplay.blit(text, (1, 30))
        gameDisplay.blit(text3, (1, 1))
        #Blue
        gameDisplay.blit(blue2Img,(400,450))
        #Controles
        controles = font.render("Controles", True, black)  
        gameDisplay.blit(controles, (333,330))
        gameDisplay.blit(FlechaiImg,(330,350))
        gameDisplay.blit(FlechadImg,(440,350))
        #Text 
        resumen = font2.render("No dejes que la barra termine en rojo", True, red)
        resumen2 = font2.render("O perderas una VIDA", True, black)
        resumen3 = font2.render("Atrapa comida saludable para ganar puntos", True, black)
        resumen4 = font2.render("Saludable", True, red)
        resumen5 = font2.render("No saludable", True, red)  
        gameDisplay.blit(resumen, (150,100))
        gameDisplay.blit(resumen2, (250,120))
        gameDisplay.blit(resumen3, (100,180))
        gameDisplay.blit(resumen4, (100,220))
        gameDisplay.blit(resumen5, (500,220))
        gameDisplay.blit(manzanaImg,(140, 235))
        gameDisplay.blit(donaImg,(580, 240))
        #ReturnMainmenu        
        if 730 + 80 > mouse[0] > 730 and 1 + 60 > mouse[1] > 1:
            gameDisplay.blit(FlechaR2Img,(730,1))
            if click[0]:
                ciclo = False
        else:
            gameDisplay.blit(FlechaRImg, (730,1))

        
        pygame.display.update()
        clock.tick(30)

#MenuSelectLevel
def selectlevel():
    ciclo = True
    while ciclo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(selectLevelImg,(0,0))
        Button(130,130,115,20,130,130,"Nivel1",level1)
        Button(520,130,115,20,520,130,"Nivel2",level2)
        Button(130,370,115,20,130,370,"Nivel3",level3)
        Button(520,370,115,20,520,370,"Nivel4",level4)
        
        pygame.display.update()
        clock.tick(30)

def level1():
#Music
    global musica
    if musica == True:
        pygame.mixer.music.load("./Assets/Music/Level1.wav")
        pygame.mixer.music.play(3)
#CreatingObjects
    blue = Player(blueImg, 4, 377, 450, 55, 30, 1.1)
    manzana = Gameobject(manzanaImg, 3, random.randrange(0, display_width - 20,),-500,50,50)
    dona = Gameobject(donaImg, 3, random.randrange(0, display_width - 20),-600,50,50)
    hamburgesa = Gameobject(hamburImg, 3, random.randrange(0, display_width - 20),-700,50,50)
    brocoli = Gameobject(brocoliImg, 3, random.randrange(0, display_width - 20),-800,50,50)

#Constants
    x_change = 0
    global cont, direc, lives, fondopause, score
    bar = 300
    aux = 1
    aux2 = 1
    fondopause = 1
    gameexit = False
    font = pygame.font.Font("04B_30__.TTF", 25)
#GameLoop
    while not gameexit:

#TimeBar
        Time_Bar = pygame.time.get_ticks()/1000
        
        if aux <= Time_Bar:
            aux = Time_Bar
        if aux == Time_Bar:
            aux += 1
            bar -= 5
#Background
        bg = Background(fondoCasa, 0, 0)
        text = font.render("Nivel 1", True, white)
        text2 = font.render("Siguiente nivel:20", True, black)
        gameDisplay.blit(text, (1, 1))
        gameDisplay.blit(text2, (230, 45))
# Objects
        gameDisplay.blit(manzana.b_image, (manzana.coord_x, manzana.coord_y))
        gameDisplay.blit(dona.b_image, (dona.coord_x, dona.coord_y))
        gameDisplay.blit(hamburgesa.b_image, (hamburgesa.coord_x, hamburgesa.coord_y))
        gameDisplay.blit(brocoli.b_image, (brocoli.coord_x, brocoli.coord_y))
#Life bar
        red_bar = pygame.Surface((300, 40))
        red_bar.fill((255, 0, 0))
        gameDisplay.blit(red_bar,(250, 2))
        pygame.draw.rect(gameDisplay, white, (250, 2, 300, 40), 5)
        pygame.draw.rect(gameDisplay, green, (250, 2, bar, 40))

#Pause
        Pause()
#Events
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and blue.blue_x > 0:
                    x_change = blue.speed*-1 + -1*blue.speedmult
                    direc=False
                elif event.key == pygame.K_RIGHT and blue.blue_x < display_width - 45:
                    x_change = blue.speed + blue.speedmult
                    direc=True
                elif event.key == pygame.K_ESCAPE:
                    quit()
        blue.blue_x += x_change
        direct = blue.blue_x
        if blue.blue_x !=  377:
            if direct == blue.blue_x:
                cont += 1
#Sprite
        blue_inv=pygame.transform.flip(blue.p_img,True,False)
        sprite()
        if direc==True:
            gameDisplay.blit(blue.p_img,(blue.blue_x,450),(xixf[i]))
        if direc==False:
            gameDisplay.blit(blue_inv,(blue.blue_x,450),(Rxixf[i]))
#Objects Speed
        fast = 0
        fast2 = 0
        if score >= 10:
            fast = fast + 1
            fast2 = fast2 + 1
        manzana.coord_y += manzana.speed + fast2
        brocoli.coord_y += brocoli.speed + fast2
        dona.coord_y += dona.speed + fast
        hamburgesa.coord_y += hamburgesa.speed + fast     
#Boundaries
        if blue.blue_x > 745 or blue.blue_x < 0:
            x_change = 0
            cont = 0         
#Reload Objects
        if manzana.coord_y > display_height:
            manzana.coord_y = -10
            manzana.coord_x = random.randrange(0, display_width - 25)
        if brocoli.coord_y > display_height - 10:
            brocoli.coord_y = -20
            brocoli.coord_x = random.randrange(0, display_width - 25)
        if dona.coord_y > display_height:
            dona.coord_y = -300
            dona.coord_x = random.randrange(0, display_width - 55)
        if hamburgesa.coord_y > display_height:
            hamburgesa.coord_y = -100
            hamburgesa.coord_x = random.randrange(0, display_width - 65)
# Score
        scorecounter(score)
#Colissions
    # Donut
        if blue.blue_y < dona.coord_y + dona.hitbox_y and blue.blue_y > dona.coord_y or blue.blue_y + blue.hitbox_y > dona.coord_y and blue.blue_y + blue.hitbox_y < dona.coord_y + dona.hitbox_y:
            if blue.blue_x > dona.coord_x and blue.blue_x < dona.coord_x + dona.hitbox_x or blue.blue_x + blue.hitbox_x > dona.coord_x and blue.blue_x + blue.hitbox_x < dona.coord_x + dona.hitbox_x:
                dona.coord_y = -10
                dona.coord_x = random.randrange(0, display_width - 30)
                bar -= 10

    # hamburgesa
        if blue.blue_y < hamburgesa.coord_y + hamburgesa.hitbox_y and blue.blue_y > hamburgesa.coord_y or blue.blue_y + blue.hitbox_y > hamburgesa.coord_y and blue.blue_y + blue.hitbox_y < hamburgesa.coord_y + hamburgesa.hitbox_y:
            if blue.blue_x > hamburgesa.coord_x and blue.blue_x < hamburgesa.coord_x + hamburgesa.hitbox_x or blue.blue_x + blue.hitbox_x > hamburgesa.coord_x and blue.blue_x + blue.hitbox_x < hamburgesa.coord_x + hamburgesa.hitbox_x:
                hamburgesa.coord_y = -10
                hamburgesa.coord_x = random.randrange(0, display_width - 30)
                bar -= 10
    #Apple
        if blue.blue_y < manzana.coord_y + manzana.hitbox_y and blue.blue_y > manzana.coord_y or blue.blue_y + blue.hitbox_y > manzana.coord_y and blue.blue_y + blue.hitbox_y < manzana.coord_y + manzana.hitbox_y:
            if blue.blue_x > manzana.coord_x and blue.blue_x < manzana.coord_x + manzana.hitbox_x or blue.blue_x + blue.hitbox_x > manzana.coord_x and blue.blue_x + blue.hitbox_x < manzana.coord_x + manzana.hitbox_x:
                manzana.coord_y = -10
                manzana.coord_x = random.randrange(0, display_width - 30)
                score += 1
                bar += 5
    #Broccoli
        if blue.blue_y < brocoli.coord_y + brocoli.hitbox_y and blue.blue_y > brocoli.coord_y or blue.blue_y + blue.hitbox_y > brocoli.coord_y and blue.blue_y + blue.hitbox_y < brocoli.coord_y + brocoli.hitbox_y:
            if blue.blue_x > brocoli.coord_x and blue.blue_x < brocoli.coord_x + brocoli.hitbox_x or blue.blue_x + blue.hitbox_x > brocoli.coord_x and blue.blue_x + blue.hitbox_x < brocoli.coord_x + brocoli.hitbox_x:
                brocoli.coord_y = -10
                brocoli.coord_x = random.randrange(0, display_width - 30)
                score += 1
                bar += 5

        if bar <= 0:
            bar = 0
            lives = lives - 1
            pygame.mixer.music.stop()
            if score > 0:
                score = 0
            crash("Perdiste")
            levelreturn(mainmenu,lives,level1)
        if bar >= 300:
            bar = 300
        
    #LivesPlayer
        
        if lives == 3:
            gameDisplay.blit(corazonImg, (580,2))
            gameDisplay.blit(corazonImg, (630,2))
            gameDisplay.blit(corazonImg, (680,2))
        if lives == 2:
            gameDisplay.blit(corazonImg, (680,2))
            gameDisplay.blit(corazonImg, (630,2))
        if lives == 1:
            gameDisplay.blit(corazonImg, (680,2))        
        if score == 20:
            crash("Ganaste")
            score = 0
            lives = 3
            level2()
            
        pygame.display.update()
        clock.tick(70)

def level2():
#Music
    global musica
    if musica == True:
        pygame.mixer.music.load("./Assets/Music/Level2.wav")
        pygame.mixer.music.play(3)
#CreatingObjects
    blue = Player(blueImg, 4, 377, 450, 55, 30, 1.1)
    manzana = Gameobject(manzanaImg, 3, random.randrange(0, display_width - 20,),-500,50,50)
    dona = Gameobject(donaImg, 3, random.randrange(0, display_width - 20),-600,50,50)
    maruchan = Gameobject(maruchanImg, 3, random.randrange(0, display_width - 20),-900,50,50)
    zanahoria = Gameobject(zanahoriaImg, 3, random.randrange(0, display_width - 20),-1000,50,50)
    platano = Gameobject(platanoImg, 3, random.randrange(0, display_width - 20),-700,50,50)
    pollo = Gameobject(polloImg, 3, random.randrange(0, display_width - 20),-800,50,50)
#Constants
    x_change = 0
    global score
    global fondopause
    global lives
    bar = 300
    aux = 1
    aux2 = 1
    fondopause = 2
    gameexit = False
    font = pygame.font.Font("04B_30__.TTF", 25)
#GameLoop
    while not gameexit:
#TimeBar
        Time_Bar = pygame.time.get_ticks()/1000
        
        if aux <= Time_Bar:
            aux = Time_Bar
        if aux == Time_Bar:
            aux += 1
            bar -= 10

#Background
        bg = Background(fondoPueblo, 0, 0)
        text = font.render("Nivel 2", True, white)
        text2 = font.render("Siguiente nivel:30", True, black)
        gameDisplay.blit(text, (1, 1))
        gameDisplay.blit(text2, (230, 45))
# Objects
        gameDisplay.blit(manzana.b_image, (manzana.coord_x, manzana.coord_y))
        gameDisplay.blit(dona.b_image, (dona.coord_x, dona.coord_y))
        gameDisplay.blit(maruchan.b_image, (maruchan.coord_x, maruchan.coord_y))
        gameDisplay.blit(zanahoria.b_image, (zanahoria.coord_x, zanahoria.coord_y))
        gameDisplay.blit(pollo.b_image, (pollo.coord_x, pollo.coord_y))
        gameDisplay.blit(platano.b_image, (platano.coord_x, platano.coord_y))
#Life bar
        red_bar = pygame.Surface((300, 40))
        red_bar.fill((255, 0, 0))
        gameDisplay.blit(red_bar,(250, 2))
        pygame.draw.rect(gameDisplay, white, (250, 2, 300, 40), 5)
        pygame.draw.rect(gameDisplay, green, (250, 2, bar, 40))
#Pause
        Pause()
#Events
        global cont, direc
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and blue.blue_x > 0:
                    x_change = blue.speed*-1 + -1*blue.speedmult
                    direc=False
                elif event.key == pygame.K_RIGHT and blue.blue_x < display_width - 45:
                    x_change = blue.speed + blue.speedmult
                    direc=True
                elif event.key == pygame.K_ESCAPE:
                    quit()
        blue.blue_x += x_change
        direct = blue.blue_x
        if blue.blue_x !=  377:
            if direct == blue.blue_x:
                cont += 1
#Sprite
        blue_inv=pygame.transform.flip(blue.p_img,True,False)
        sprite()
        if direc==True:
            gameDisplay.blit(blue.p_img,(blue.blue_x,450),(xixf[i]))
        if direc==False:
            gameDisplay.blit(blue_inv,(blue.blue_x,450),(Rxixf[i]))
#Objects Speed
        fast = 1
        fast2 = 0
        if score >= 10:
            fast = fast + 1
            fast2 = fast2 + 1
        if score >= 20:
            fast = fast + 1
            fast2 = fast2 + 1
        manzana.coord_y += manzana.speed + fast2
        zanahoria.coord_y += zanahoria.speed + fast2
        platano.coord_y += platano.speed + fast2
        dona.coord_y += dona.speed + fast
        pollo.coord_y += pollo.speed + fast
        maruchan.coord_y += maruchan.speed + fast      
#Boundaries
        if blue.blue_x > 745 or blue.blue_x < 0:
            x_change = 0
            cont = 0          
#Reload Objects
        if manzana.coord_y > display_height:
            manzana.coord_y = -10
            manzana.coord_x = random.randrange(0, display_width - 25)
        if zanahoria.coord_y > display_height - 5:
            zanahoria.coord_y = -10
            zanahoria.coord_x = random.randrange(0, display_width - 25)
        if platano.coord_y > display_height - 10:
            platano.coord_y = -20
            platano.coord_x = random.randrange(0, display_width - 25)
        if dona.coord_y > display_height:
            dona.coord_y = -300
            dona.coord_x = random.randrange(0, display_width - 55)
        if pollo.coord_y > display_height:
            pollo.coord_y = -100
            pollo.coord_x = random.randrange(0, display_width - 65)
        if maruchan.coord_y > display_height:
            maruchan.coord_y = -200
            maruchan.coord_x = random.randrange(0, display_width - 75)
# Score
        scorecounter(score)
#Colissions
    # Donut
        if blue.blue_y < dona.coord_y + dona.hitbox_y and blue.blue_y > dona.coord_y or blue.blue_y + blue.hitbox_y > dona.coord_y and blue.blue_y + blue.hitbox_y < dona.coord_y + dona.hitbox_y:
            if blue.blue_x > dona.coord_x and blue.blue_x < dona.coord_x + dona.hitbox_x or blue.blue_x + blue.hitbox_x > dona.coord_x and blue.blue_x + blue.hitbox_x < dona.coord_x + dona.hitbox_x:
                dona.coord_y = -10
                dona.coord_x = random.randrange(0, display_width - 30)
                bar -= 20

    # Pollo
        if blue.blue_y < pollo.coord_y + pollo.hitbox_y and blue.blue_y > pollo.coord_y or blue.blue_y + blue.hitbox_y > pollo.coord_y and blue.blue_y + blue.hitbox_y < pollo.coord_y + pollo.hitbox_y:
            if blue.blue_x > pollo.coord_x and blue.blue_x < pollo.coord_x + pollo.hitbox_x or blue.blue_x + blue.hitbox_x > pollo.coord_x and blue.blue_x + blue.hitbox_x < pollo.coord_x + pollo.hitbox_x:
                pollo.coord_y = -10
                pollo.coord_x = random.randrange(0, display_width - 30)
                bar -= 20
    # Maruchan
        if blue.blue_y < maruchan.coord_y + maruchan.hitbox_y and blue.blue_y > maruchan.coord_y or blue.blue_y + blue.hitbox_y > maruchan.coord_y and blue.blue_y + blue.hitbox_y < maruchan.coord_y + maruchan.hitbox_y:
            if blue.blue_x > maruchan.coord_x and blue.blue_x < maruchan.coord_x + maruchan.hitbox_x or blue.blue_x + blue.hitbox_x > maruchan.coord_x and blue.blue_x + blue.hitbox_x < maruchan.coord_x + maruchan.hitbox_x:
                maruchan.coord_y = -10
                maruchan.coord_x = random.randrange(0, display_width - 30)
                bar -= 20
    #Apple
        if blue.blue_y < manzana.coord_y + manzana.hitbox_y and blue.blue_y > manzana.coord_y or blue.blue_y + blue.hitbox_y > manzana.coord_y and blue.blue_y + blue.hitbox_y < manzana.coord_y + manzana.hitbox_y:
            if blue.blue_x > manzana.coord_x and blue.blue_x < manzana.coord_x + manzana.hitbox_x or blue.blue_x + blue.hitbox_x > manzana.coord_x and blue.blue_x + blue.hitbox_x < manzana.coord_x + manzana.hitbox_x:
                manzana.coord_y = -10
                manzana.coord_x = random.randrange(0, display_width - 30)
                score += 1
                bar += 10
    #Carrot
        if blue.blue_y < zanahoria.coord_y + zanahoria.hitbox_y and blue.blue_y > zanahoria.coord_y or blue.blue_y + blue.hitbox_y > zanahoria.coord_y and blue.blue_y + blue.hitbox_y < zanahoria.coord_y + zanahoria.hitbox_y:
            if blue.blue_x > zanahoria.coord_x and blue.blue_x < zanahoria.coord_x + zanahoria.hitbox_x or blue.blue_x + blue.hitbox_x > zanahoria.coord_x and blue.blue_x + blue.hitbox_x < zanahoria.coord_x + zanahoria.hitbox_x:
                zanahoria.coord_y = -10
                zanahoria.coord_x = random.randrange(0, display_width - 30)
                score += 1
                bar += 10
    #Platano
        if blue.blue_y < platano.coord_y + platano.hitbox_y and blue.blue_y > platano.coord_y or blue.blue_y + blue.hitbox_y > platano.coord_y and blue.blue_y + blue.hitbox_y < platano.coord_y + platano.hitbox_y:
            if blue.blue_x > platano.coord_x and blue.blue_x < platano.coord_x + platano.hitbox_x or blue.blue_x + blue.hitbox_x > platano.coord_x and blue.blue_x + blue.hitbox_x < platano.coord_x + platano.hitbox_x:
                platano.coord_y = -10
                platano.coord_x = random.randrange(0, display_width - 30)
                score += 1
                bar += 10

        if bar <= 0:
            bar = 0
            lives = lives - 1
            pygame.mixer.music.stop()
            if score > 0:
                score = 0
            crash("Perdiste")
            levelreturn(mainmenu,lives,level2)
        if bar >= 300:
            bar = 300
        
    #LivesPlayer
        
        if lives == 3:
            gameDisplay.blit(corazonImg, (580,2))
            gameDisplay.blit(corazonImg, (630,2))
            gameDisplay.blit(corazonImg, (680,2))
        if lives == 2:
            gameDisplay.blit(corazonImg, (680,2))
            gameDisplay.blit(corazonImg, (630,2))
        if lives == 1:
            gameDisplay.blit(corazonImg, (680,2))         
        if score == 30:
            crash("Ganaste")
            score = 0
            lives = 3
            level3()
            
        pygame.display.update()
        clock.tick(70) 

def level3():
#Music
    global musica
    if musica == True:
        pygame.mixer.music.load("./Assets/Music/Level3.wav")
        pygame.mixer.music.play(3)

#CreatingObjects
    blue = Player(blueImg, 4, 377, 450, 55, 30, 1.1)
    manzana = Gameobject(manzanaImg, 3, random.randrange(0, display_width - 20,),-300,50,50)
    dona = Gameobject(donaImg, 3, random.randrange(0, display_width - 20),-400,50,50)
    zanahoria = Gameobject(zanahoriaImg, 3, random.randrange(0, display_width - 20),-500,50,50)
    pollo = Gameobject(polloImg, 3, random.randrange(0, display_width - 20),-600,50,50)

    sandia = Gameobject(sandiaImg, 3, random.randrange(0, display_width - 20),-700,50,50)
    naranja = Gameobject(naranjaImg, 3, random.randrange(0, display_width - 20),-800,50,50)
    hotdog = Gameobject(hotdogImg, 3, random.randrange(0, display_width - 20),-900,50,50)
    pizza = Gameobject(pizzaImg, 3, random.randrange(0, display_width - 20),-1000,50,50)
#Constants
    x_change = 0
    global score
    global fondopause
    global lives
    bar = 300
    aux = 1
    aux2 = 1
    fondopause = 3
    gameexit = False
    font = pygame.font.Font("04B_30__.TTF", 25)
#GameLoop
    while not gameexit:
#TimeBar
        Time_Bar = pygame.time.get_ticks()/1000
        
        if aux <= Time_Bar:
            aux = Time_Bar
        if aux == Time_Bar:
            aux += 1
            bar -= 10
#Background
        bg = Background(fondoParque, 0, 0)
        text = font.render("Nivel 3", True, white)
        text2 = font.render("Siguiente nivel:40", True, black)
        gameDisplay.blit(text, (1, 1))
        gameDisplay.blit(text2, (230, 45))
#Objects
        gameDisplay.blit(manzana.b_image, (manzana.coord_x, manzana.coord_y))
        gameDisplay.blit(dona.b_image, (dona.coord_x, dona.coord_y))
        gameDisplay.blit(zanahoria.b_image, (zanahoria.coord_x, zanahoria.coord_y))
        gameDisplay.blit(pollo.b_image, (pollo.coord_x, pollo.coord_y))

        gameDisplay.blit(sandia.b_image, (sandia.coord_x, sandia.coord_y))
        gameDisplay.blit(naranja.b_image, (naranja.coord_x, naranja.coord_y))
        gameDisplay.blit(hotdog.b_image, (hotdog.coord_x, hotdog.coord_y))
        gameDisplay.blit(pizza.b_image, (pizza.coord_x, pizza.coord_y))
#Life bar
        red_bar = pygame.Surface((300, 40))
        red_bar.fill((255, 0, 0))
        gameDisplay.blit(red_bar,(250, 2))
        pygame.draw.rect(gameDisplay, white, (250, 2, 300, 40), 5)
        pygame.draw.rect(gameDisplay, green, (250, 2, bar, 40))
#Pause
        Pause()
#Events
        global cont, direc
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and blue.blue_x > 0:
                    x_change = blue.speed*-1 + -1*blue.speedmult
                    direc=False
                elif event.key == pygame.K_RIGHT and blue.blue_x < display_width - 45:
                    x_change = blue.speed + blue.speedmult
                    direc=True
                elif event.key == pygame.K_ESCAPE:
                    quit()
        blue.blue_x += x_change
        direct = blue.blue_x
        if blue.blue_x !=  377:
            if direct == blue.blue_x:
                cont += 1
#Sprite
        blue_inv=pygame.transform.flip(blue.p_img,True,False)
        sprite()
        if direc==True:
            gameDisplay.blit(blue.p_img,(blue.blue_x,450),(xixf[i]))
        if direc==False:
            gameDisplay.blit(blue_inv,(blue.blue_x,450),(Rxixf[i]))
#Objects Speed
        fast = 0
        fast2 = 0
        if score >= 10:
            fast = fast + 1
            fast2 = fast2 + 1
        if score >= 20:
            fast = fast + 1
            fast2 = fast2 + 1
        if score >= 30:
            fast = fast + 1
            fast2 = fast2 + 1
        
        manzana.coord_y += manzana.speed + fast2
        zanahoria.coord_y += zanahoria.speed + fast2
        dona.coord_y += dona.speed + fast
        pollo.coord_y += pollo.speed + fast

        sandia.coord_y += sandia.speed + fast2
        naranja.coord_y += naranja.speed + fast2
        hotdog.coord_y += hotdog.speed + fast
        pizza.coord_y += pizza.speed + fast      
#Boundaries
        if blue.blue_x > 745 or blue.blue_x < 0:
            x_change = 0
            cont = 0          
#Reload Objects
        if manzana.coord_y > display_height:
            manzana.coord_y = -10
            manzana.coord_x = random.randrange(0, display_width - 25)
        if zanahoria.coord_y > display_height - 5:
            zanahoria.coord_y = -10
            zanahoria.coord_x = random.randrange(0, display_width - 25)
        if sandia.coord_y > display_height - 10:
            sandia.coord_y = -20
            sandia.coord_x = random.randrange(0, display_width - 25)
        if naranja.coord_y > display_height - 10:
            naranja.coord_y = -20
            naranja.coord_x = random.randrange(0, display_width - 25)
        if dona.coord_y > display_height:
            dona.coord_y = -300
            dona.coord_x = random.randrange(0, display_width - 55)
        if pollo.coord_y > display_height:
            pollo.coord_y = -100
            pollo.coord_x = random.randrange(0, display_width - 65)
        if hotdog.coord_y > display_height:
            hotdog.coord_y = -200
            hotdog.coord_x = random.randrange(0, display_width - 75)
        if pizza.coord_y > display_height:
            pizza.coord_y = -150
            pizza.coord_x = random.randrange(0, display_width - 75)
# Score
        scorecounter(score)
#Colissions
    # Donut
        if blue.blue_y < dona.coord_y + dona.hitbox_y and blue.blue_y > dona.coord_y or blue.blue_y + blue.hitbox_y > dona.coord_y and blue.blue_y + blue.hitbox_y < dona.coord_y + dona.hitbox_y:
            if blue.blue_x > dona.coord_x and blue.blue_x < dona.coord_x + dona.hitbox_x or blue.blue_x + blue.hitbox_x > dona.coord_x and blue.blue_x + blue.hitbox_x < dona.coord_x + dona.hitbox_x:
                dona.coord_y = -10
                dona.coord_x = random.randrange(0, display_width - 30)
                bar -= 25

    # Pollo
        if blue.blue_y < pollo.coord_y + pollo.hitbox_y and blue.blue_y > pollo.coord_y or blue.blue_y + blue.hitbox_y > pollo.coord_y and blue.blue_y + blue.hitbox_y < pollo.coord_y + pollo.hitbox_y:
            if blue.blue_x > pollo.coord_x and blue.blue_x < pollo.coord_x + pollo.hitbox_x or blue.blue_x + blue.hitbox_x > pollo.coord_x and blue.blue_x + blue.hitbox_x < pollo.coord_x + pollo.hitbox_x:
                pollo.coord_y = -10
                pollo.coord_x = random.randrange(0, display_width - 30)
                bar -= 25
    # Hotdog
        if blue.blue_y < hotdog.coord_y + hotdog.hitbox_y and blue.blue_y > hotdog.coord_y or blue.blue_y + blue.hitbox_y > hotdog.coord_y and blue.blue_y + blue.hitbox_y < hotdog.coord_y + hotdog.hitbox_y:
            if blue.blue_x > hotdog.coord_x and blue.blue_x < hotdog.coord_x + hotdog.hitbox_x or blue.blue_x + blue.hitbox_x > hotdog.coord_x and blue.blue_x + blue.hitbox_x < hotdog.coord_x + hotdog.hitbox_x:
                hotdog.coord_y = -10
                hotdog.coord_x = random.randrange(0, display_width - 30)
                bar -= 25
    # Pizza
        if blue.blue_y < pizza.coord_y + pizza.hitbox_y and blue.blue_y > pizza.coord_y or blue.blue_y + blue.hitbox_y > pizza.coord_y and blue.blue_y + blue.hitbox_y < pizza.coord_y + hotdog.hitbox_y:
            if blue.blue_x > pizza.coord_x and blue.blue_x < pizza.coord_x + pizza.hitbox_x or blue.blue_x + blue.hitbox_x > pizza.coord_x and blue.blue_x + blue.hitbox_x < pizza.coord_x + hotdog.hitbox_x:
                pizza.coord_y = -10
                pizza.coord_x = random.randrange(0, display_width - 30)
                bar -= 25
    #Apple
        if blue.blue_y < manzana.coord_y + manzana.hitbox_y and blue.blue_y > manzana.coord_y or blue.blue_y + blue.hitbox_y > manzana.coord_y and blue.blue_y + blue.hitbox_y < manzana.coord_y + manzana.hitbox_y:
            if blue.blue_x > manzana.coord_x and blue.blue_x < manzana.coord_x + manzana.hitbox_x or blue.blue_x + blue.hitbox_x > manzana.coord_x and blue.blue_x + blue.hitbox_x < manzana.coord_x + manzana.hitbox_x:
                manzana.coord_y = -10
                manzana.coord_x = random.randrange(0, display_width - 30)
                score += 1
                bar += 10
    #Carrot
        if blue.blue_y < zanahoria.coord_y + zanahoria.hitbox_y and blue.blue_y > zanahoria.coord_y or blue.blue_y + blue.hitbox_y > zanahoria.coord_y and blue.blue_y + blue.hitbox_y < zanahoria.coord_y + zanahoria.hitbox_y:
            if blue.blue_x > zanahoria.coord_x and blue.blue_x < zanahoria.coord_x + zanahoria.hitbox_x or blue.blue_x + blue.hitbox_x > zanahoria.coord_x and blue.blue_x + blue.hitbox_x < zanahoria.coord_x + zanahoria.hitbox_x:
                zanahoria.coord_y = -10
                zanahoria.coord_x = random.randrange(0, display_width - 30)
                score += 1
                bar += 10
    #Sandia
        if blue.blue_y < sandia.coord_y + sandia.hitbox_y and blue.blue_y > sandia.coord_y or blue.blue_y + blue.hitbox_y > sandia.coord_y and blue.blue_y + blue.hitbox_y < sandia.coord_y + sandia.hitbox_y:
            if blue.blue_x > sandia.coord_x and blue.blue_x < sandia.coord_x + sandia.hitbox_x or blue.blue_x + blue.hitbox_x > sandia.coord_x and blue.blue_x + blue.hitbox_x < sandia.coord_x + sandia.hitbox_x:
                sandia.coord_y = -10
                sandia.coord_x = random.randrange(0, display_width - 30)
                score += 1
                bar += 10
    #Naranja
        if blue.blue_y < naranja.coord_y + naranja.hitbox_y and blue.blue_y > naranja.coord_y or blue.blue_y + blue.hitbox_y > naranja.coord_y and blue.blue_y + blue.hitbox_y < naranja.coord_y + naranja.hitbox_y:
            if blue.blue_x > naranja.coord_x and blue.blue_x < naranja.coord_x + naranja.hitbox_x or blue.blue_x + blue.hitbox_x > naranja.coord_x and blue.blue_x + blue.hitbox_x < naranja.coord_x + naranja.hitbox_x:
                naranja.coord_y = -10
                naranja.coord_x = random.randrange(0, display_width - 30)
                score += 1
                bar += 10

        if bar <= 0:
            bar = 0
            lives = lives - 1
            pygame.mixer.music.stop()
            if score > 0:
                score = 0
            crash("Perdiste")
            levelreturn(mainmenu,lives,level3)
        if bar >= 300:
            bar = 300
        
    #LivesPlayer
        if lives == 3:
            gameDisplay.blit(corazonImg, (580,2))
            gameDisplay.blit(corazonImg, (630,2))
            gameDisplay.blit(corazonImg, (680,2))
        if lives == 2:
            gameDisplay.blit(corazonImg, (680,2))
            gameDisplay.blit(corazonImg, (630,2))
        if lives == 1:
            gameDisplay.blit(corazonImg, (680,2))         
        if score == 40:
            crash("Ganaste")
            score = 0
            lives = 3
            level4()
            
        pygame.display.update()
        clock.tick(70) 

def level4():
#Music
    global musica
    if musica == True:
        pygame.mixer.music.load("./Assets/Music/Level4.wav")
        pygame.mixer.music.play(3)
#CreatingObjects
    blue = Player(blueplayaImg, 4, 377, 478, 55, 30, 1.1)
    dona = Gameobject(donaImg, 3, random.randrange(0, display_width - 20),-100,50,50)
    zanahoria = Gameobject(zanahoriaImg, 3, random.randrange(0, display_width - 20),-200,50,50)

    cereza = Gameobject(cerezaImg, 3, random.randrange(0, display_width - 20,),-300,50,50)
    cupcake = Gameobject(cupcakeImg, 3, random.randrange(0, display_width - 20),-400,50,50)
    tomate = Gameobject(tomateImg, 3, random.randrange(0, display_width - 20),-500,50,50)
    papas = Gameobject(papasImg, 3, random.randrange(0, display_width - 20),-600,50,50)

    sandia = Gameobject(sandiaImg, 3, random.randrange(0, display_width - 20),-700,50,50)
    naranja = Gameobject(naranjaImg, 3, random.randrange(0, display_width - 20),-800,50,50)
    hotdog = Gameobject(hotdogImg, 3, random.randrange(0, display_width - 20),-900,50,50)
    pizza = Gameobject(pizzaImg, 3, random.randrange(0, display_width - 20),-1000,50,50)
#Constants
    x_change = 0
    global score
    global fondopause
    global lives
    bar = 300
    aux = 1
    aux2 = 1
    fondopause = 4
    gameexit = False
    font = pygame.font.Font("04B_30__.TTF", 25)
#GameLoop
    while not gameexit:
        
#TimeBar
        Time_Bar = pygame.time.get_ticks()/1000
        
        if aux <= Time_Bar:
            aux = Time_Bar
        if aux == Time_Bar:
            aux += 1
            bar -= 15

#Background
        bg = Background(fondoPlaya, 0, 0)
        text = font.render("Nivel 4", True, white)
        text2 = font.render("Final:50", True, black)
        gameDisplay.blit(text, (1, 1))
        gameDisplay.blit(text2, (330, 45))
# Objects
        gameDisplay.blit(dona.b_image, (dona.coord_x, dona.coord_y))
        gameDisplay.blit(zanahoria.b_image, (zanahoria.coord_x, zanahoria.coord_y))

        gameDisplay.blit(cereza.b_image, (cereza.coord_x, cereza.coord_y))
        gameDisplay.blit(cupcake.b_image, (cupcake.coord_x, cupcake.coord_y))
        gameDisplay.blit(tomate.b_image, (tomate.coord_x, tomate.coord_y))
        gameDisplay.blit(papas.b_image, (papas.coord_x, papas.coord_y))

        gameDisplay.blit(sandia.b_image, (sandia.coord_x, sandia.coord_y))
        gameDisplay.blit(naranja.b_image, (naranja.coord_x, naranja.coord_y))
        gameDisplay.blit(hotdog.b_image, (hotdog.coord_x, hotdog.coord_y))
        gameDisplay.blit(pizza.b_image, (pizza.coord_x, pizza.coord_y))
#Life bar
        red_bar = pygame.Surface((300, 40))
        red_bar.fill((255, 0, 0))
        gameDisplay.blit(red_bar,(250, 2))
        pygame.draw.rect(gameDisplay, white, (250, 2, 300, 40), 5)
        pygame.draw.rect(gameDisplay, green, (250, 2, bar, 40))
#Pause
        Pause()
#Events
        global cont, direc
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and blue.blue_x > 0:
                    x_change = blue.speed*-1 + -1*blue.speedmult
                    direc=False
                elif event.key == pygame.K_RIGHT and blue.blue_x < display_width - 45:
                    x_change = blue.speed + blue.speedmult
                    direc=True
                elif event.key == pygame.K_ESCAPE:
                    quit()
        blue.blue_x += x_change
        direct = blue.blue_x
        if blue.blue_x !=  377:
            if direct == blue.blue_x:
                cont += 1
#Sprite
        blue_inv=pygame.transform.flip(blue.p_img,True,False)
        sprite()
        if direc==True:
            gameDisplay.blit(blue.p_img,(blue.blue_x,blue.blue_y),(xixf[i]))
        if direc==False:
            gameDisplay.blit(blue_inv,(blue.blue_x,blue.blue_y),(Rxixf[i]))
#Objects Speed
        fast = 0
        fast2 = 0
        if score >= 10:
            fast = fast + 1
            fast2 = fast2 + 1
        if score >= 20:
            fast = fast + 1
            fast2 = fast2 + 1
        if score >= 30:
            fast = fast + 1
            fast2 = fast2 + 1
        if score >= 40:
            fast = fast + 1
            fast2 = fast2 + 1
        zanahoria.coord_y += zanahoria.speed + fast2
        dona.coord_y += dona.speed + fast

        cupcake.coord_y += cupcake.speed + fast
        papas.coord_y += papas.speed + fast
        cereza.coord_y += cereza.speed + fast2
        tomate.coord_y += tomate.speed + fast2

        sandia.coord_y += sandia.speed + fast2
        naranja.coord_y += naranja.speed + fast2
        hotdog.coord_y += hotdog.speed + fast
        pizza.coord_y += pizza.speed + fast      
#Boundaries
        if blue.blue_x > 745 or blue.blue_x < 0:
            x_change = 0
            cont = 0          
#Reload Objects
        if cereza.coord_y > display_height:
            cereza.coord_y = -10
            cereza.coord_x = random.randrange(0, display_width - 25)
        if tomate.coord_y > display_height:
            tomate.coord_y = -10
            tomate.coord_x = random.randrange(0, display_width - 25)
        if zanahoria.coord_y > display_height - 5:
            zanahoria.coord_y = -10
            zanahoria.coord_x = random.randrange(0, display_width - 25)
        if sandia.coord_y > display_height - 10:
            sandia.coord_y = -20
            sandia.coord_x = random.randrange(0, display_width - 25)
        if naranja.coord_y > display_height - 10:
            naranja.coord_y = -20
            naranja.coord_x = random.randrange(0, display_width - 25)
        if dona.coord_y > display_height:
            dona.coord_y = -300
            dona.coord_x = random.randrange(0, display_width - 55)
        if cupcake.coord_y > display_height:
            cupcake.coord_y = -100
            cupcake.coord_x = random.randrange(0, display_width - 65)
        if hotdog.coord_y > display_height:
            hotdog.coord_y = -200
            hotdog.coord_x = random.randrange(0, display_width - 75)
        if pizza.coord_y > display_height:
            pizza.coord_y = -150
            pizza.coord_x = random.randrange(0, display_width - 75)
        if papas.coord_y > display_height:
            papas.coord_y = -150
            papas.coord_x = random.randrange(0, display_width - 75)
# Score
        scorecounter(score)
#Colissions
    ## Donut
        if blue.blue_y < dona.coord_y + dona.hitbox_y and blue.blue_y > dona.coord_y or blue.blue_y + blue.hitbox_y > dona.coord_y and blue.blue_y + blue.hitbox_y < dona.coord_y + dona.hitbox_y:
            if blue.blue_x > dona.coord_x and blue.blue_x < dona.coord_x + dona.hitbox_x or blue.blue_x + blue.hitbox_x > dona.coord_x and blue.blue_x + blue.hitbox_x < dona.coord_x + dona.hitbox_x:
                dona.coord_y = -10
                dona.coord_x = random.randrange(0, display_width - 30)
                bar -= 25
    
    ## Papas
        if blue.blue_y < papas.coord_y + papas.hitbox_y and blue.blue_y > papas.coord_y or blue.blue_y + blue.hitbox_y > papas.coord_y and blue.blue_y + blue.hitbox_y < papas.coord_y + papas.hitbox_y:
            if blue.blue_x > papas.coord_x and blue.blue_x < papas.coord_x + papas.hitbox_x or blue.blue_x + blue.hitbox_x > papas.coord_x and blue.blue_x + blue.hitbox_x < papas.coord_x + papas.hitbox_x:
                papas.coord_y = -10
                papas.coord_x = random.randrange(0, display_width - 30)
                bar -= 25

    ## Cupcake
        if blue.blue_y < cupcake.coord_y + cupcake.hitbox_y and blue.blue_y > cupcake.coord_y or blue.blue_y + blue.hitbox_y > cupcake.coord_y and blue.blue_y + blue.hitbox_y < cupcake.coord_y + cupcake.hitbox_y:
            if blue.blue_x > cupcake.coord_x and blue.blue_x < cupcake.coord_x + cupcake.hitbox_x or blue.blue_x + blue.hitbox_x > cupcake.coord_x and blue.blue_x + blue.hitbox_x < cupcake.coord_x + cupcake.hitbox_x:
                cupcake.coord_y = -10
                cupcake.coord_x = random.randrange(0, display_width - 30)
                bar -= 25
    ## Hotdog
        if blue.blue_y < hotdog.coord_y + hotdog.hitbox_y and blue.blue_y > hotdog.coord_y or blue.blue_y + blue.hitbox_y > hotdog.coord_y and blue.blue_y + blue.hitbox_y < hotdog.coord_y + hotdog.hitbox_y:
            if blue.blue_x > hotdog.coord_x and blue.blue_x < hotdog.coord_x + hotdog.hitbox_x or blue.blue_x + blue.hitbox_x > hotdog.coord_x and blue.blue_x + blue.hitbox_x < hotdog.coord_x + hotdog.hitbox_x:
                hotdog.coord_y = -10
                hotdog.coord_x = random.randrange(0, display_width - 30)
                bar -= 25
    ## Pizza
        if blue.blue_y < pizza.coord_y + pizza.hitbox_y and blue.blue_y > pizza.coord_y or blue.blue_y + blue.hitbox_y > pizza.coord_y and blue.blue_y + blue.hitbox_y < pizza.coord_y + hotdog.hitbox_y:
            if blue.blue_x > pizza.coord_x and blue.blue_x < pizza.coord_x + pizza.hitbox_x or blue.blue_x + blue.hitbox_x > pizza.coord_x and blue.blue_x + blue.hitbox_x < pizza.coord_x + hotdog.hitbox_x:
                pizza.coord_y = -10
                pizza.coord_x = random.randrange(0, display_width - 30)
                bar -= 25
    ## Cereza
        if blue.blue_y < cereza.coord_y + cereza.hitbox_y and blue.blue_y > cereza.coord_y or blue.blue_y + blue.hitbox_y > cereza.coord_y and blue.blue_y + blue.hitbox_y < cereza.coord_y + cereza.hitbox_y:
            if blue.blue_x > cereza.coord_x and blue.blue_x < cereza.coord_x + cereza.hitbox_x or blue.blue_x + blue.hitbox_x > cereza.coord_x and blue.blue_x + blue.hitbox_x < cereza.coord_x + cereza.hitbox_x:
                cereza.coord_y = -10
                cereza.coord_x = random.randrange(0, display_width - 30)
                score += 1
                bar += 15
    ## Tomate
        if blue.blue_y < tomate.coord_y + tomate.hitbox_y and blue.blue_y > tomate.coord_y or blue.blue_y + blue.hitbox_y > tomate.coord_y and blue.blue_y + blue.hitbox_y < tomate.coord_y + tomate.hitbox_y:
            if blue.blue_x > tomate.coord_x and blue.blue_x < tomate.coord_x + tomate.hitbox_x or blue.blue_x + blue.hitbox_x > tomate.coord_x and blue.blue_x + blue.hitbox_x < tomate.coord_x + tomate.hitbox_x:
                tomate.coord_y = -10
                tomate.coord_x = random.randrange(0, display_width - 30)
                score += 1
                bar += 15
    ## Carrot
        if blue.blue_y < zanahoria.coord_y + zanahoria.hitbox_y and blue.blue_y > zanahoria.coord_y or blue.blue_y + blue.hitbox_y > zanahoria.coord_y and blue.blue_y + blue.hitbox_y < zanahoria.coord_y + zanahoria.hitbox_y:
            if blue.blue_x > zanahoria.coord_x and blue.blue_x < zanahoria.coord_x + zanahoria.hitbox_x or blue.blue_x + blue.hitbox_x > zanahoria.coord_x and blue.blue_x + blue.hitbox_x < zanahoria.coord_x + zanahoria.hitbox_x:
                zanahoria.coord_y = -10
                zanahoria.coord_x = random.randrange(0, display_width - 30)
                score += 1
                bar += 15
    ## Sandia
        if blue.blue_y < sandia.coord_y + sandia.hitbox_y and blue.blue_y > sandia.coord_y or blue.blue_y + blue.hitbox_y > sandia.coord_y and blue.blue_y + blue.hitbox_y < sandia.coord_y + sandia.hitbox_y:
            if blue.blue_x > sandia.coord_x and blue.blue_x < sandia.coord_x + sandia.hitbox_x or blue.blue_x + blue.hitbox_x > sandia.coord_x and blue.blue_x + blue.hitbox_x < sandia.coord_x + sandia.hitbox_x:
                sandia.coord_y = -10
                sandia.coord_x = random.randrange(0, display_width - 30)
                score += 1
                bar += 15
    ## Naranja
        if blue.blue_y < naranja.coord_y + naranja.hitbox_y and blue.blue_y > naranja.coord_y or blue.blue_y + blue.hitbox_y > naranja.coord_y and blue.blue_y + blue.hitbox_y < naranja.coord_y + naranja.hitbox_y:
            if blue.blue_x > naranja.coord_x and blue.blue_x < naranja.coord_x + naranja.hitbox_x or blue.blue_x + blue.hitbox_x > naranja.coord_x and blue.blue_x + blue.hitbox_x < naranja.coord_x + naranja.hitbox_x:
                naranja.coord_y = -10
                naranja.coord_x = random.randrange(0, display_width - 30)
                score += 1
                bar += 15

        if bar <= 0:
            bar = 0
            lives = lives - 1
            pygame.mixer.music.stop()
            if score > 0:
                score = 0
            crash("Perdiste")
            levelreturn(mainmenu,lives,level4)
        if bar >= 300:
            bar = 300
        
    #LivesPlayer
        if lives == 3:
            gameDisplay.blit(corazonImg, (580,2))
            gameDisplay.blit(corazonImg, (630,2))
            gameDisplay.blit(corazonImg, (680,2))
        if lives == 2:
            gameDisplay.blit(corazonImg, (680,2))
            gameDisplay.blit(corazonImg, (630,2))
        if lives == 1:
            gameDisplay.blit(corazonImg, (680,2))         
        if score == 50:
            crash("Felicidades")
            score = 0
            lives = 3
            mainmenu()
            
        pygame.display.update()
        clock.tick(80)
        
mainmenu()
instruccions()
selectlevel()
level1()
level2()
level3()
level4()
quit()
