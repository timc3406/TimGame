import Tim
import Enemy
import random
import time
import sys
import httplib

tim = Tim.Tim()
enemies = []

for i in range(10):
    x_rand = random.randint(200,400)
    y_rand = random.randint(200,400)
    speed = random.randint(1,10)
    enemy = Enemy.Enemy(x_rand,y_rand,1)
    enemies.append(enemy)

gameover_bool = False

def setup():
    size(500,500)

def draw():


    if gameover_bool:
        time.sleep(1)
        exit()

    background(51)
    noFill()
    stroke(255)
    rect(50, 50, 400, 400)
    tim.show()
    tim.move()

    for e in enemies:
        chase(e)
        e.show()
        e.move([en for en in enemies if en not in [e]])
        gameover(e)

def keyPressed():
    conn = httplib.HTTPConnection('localhost:3000')
    conn.request("GET","/tim/generate_thought")
    response = conn.getresponse()
    d1 = response.read()
    print(d1)
    print(keyCode)
    if keyCode == 37:
        #Left
        tim.turnTo = PVector(-1,0)
        tim.turn = True
    elif keyCode == 38:
        #Up
        tim.turnTo = PVector(0,-1)
        tim.turn = True
    elif keyCode == 39:
        #right
        tim.turnTo = PVector(1,0)
        tim.turn = True
    elif keyCode ==40:
        #down
        tim.turnTo = PVector(0,1)
        tim.turn = True

def chase(enemy):
    dif_x = tim.pos.x - enemy.pos.x
    dif_y = tim.pos.y - enemy.pos.y

    if abs(dif_x) > abs(dif_y):
        vertical_direction = False
    elif abs(dif_x) < abs(dif_y):
        vertical_direction = True
    else:
        vertical_direction = bool(random.getrandbits(1))

    if vertical_direction:
        if dif_y < 0:
            enemy.turnTo = PVector(0,-1)
            enemy.turn = True
        else:
            enemy.turnTo = PVector(0,1)
            enemy.turn = True
    else:
        if dif_x > 0:
            enemy.turnTo = PVector(1,0)
            enemy.turn = True
        else:
            enemy.turnTo = PVector(-1,0)
            enemy.turn = True

def gameover(enemy):
    dif_x = tim.pos.x - enemy.pos.x
    dif_y = tim.pos.y - enemy.pos.y
    global gameover_bool
    if abs(dif_x) < 5 and abs(dif_y) < 5:
        textSize(32)
        fill(255, 102, 153)
        text('you suck',175,225)
        gameover_bool = True

def mousePressed():
  print("Opening Process_4")
  launch("data/test")
