#Coin collecter
from random import randint

#variables
WIDTH = 1000
HEIGHT = 500
score = 0
game_over = False

#actors
player = Actor("player.png")
player.pos = 100,100
coin = Actor("coin.png")
coin.pos = 200,200
#backround = Actor("bg.png")
def draw():
    screen.fill("white")
    #backround.draw()
    player.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black",topleft=(10,10))

    if game_over:
        screen.fill("red")
        screen.draw.text("Score: " + str(score), color="black",topleft=(10,10))
def place_coin():
    coin.x = randint(20,(WIDTH - 30))
    coin.y = randint(20,(HEIGHT - 30))


def time_up():
    global game_over
    game_over = True

def update():
    global score

    if keyboard.a:
        player.x = player.x -5
    if keyboard.d:
        player.x = player.x +5
    if keyboard.w:
        player.y = player.y -5
    if keyboard.s:
        player.y = player.y +5

    coin_collected = player.colliderect(coin)
    if coin_collected:
        sounds.coin_collected.play()
        score = score + 10
        place_coin()

clock.schedule(time_up, 60.0)
place_coin()


