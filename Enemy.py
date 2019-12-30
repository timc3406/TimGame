import random
import sys
class Enemy():
    print(sys.version_info)
    pos = None
    vel = PVector(1,0)

    turnTo = PVector(-1,0)
    turn = False

    pause = True
    rect_width = 400
    rect_height = 400
    enemy_size = 10

    def __init__(self,pos_x,pos_y,speed=1):
        self.pos = PVector(pos_x, pos_y)
        self.speed_list = [1]*speed + [0]

    def show(self):
        fill(0,255,0)
        stroke(255,255,0)
        ellipse(self.pos.x,self.pos.y,self.enemy_size*2,self.enemy_size*2)

    def checkPosition(self,enemies=[]):
        self.vel = PVector(self.turnTo.x,self.turnTo.y)
        if self.turnTo.x + self.pos.x < 50+self.enemy_size or self.turnTo.x + self.pos.x > 50+self.rect_width-self.enemy_size \
        or self.turnTo.y + self.pos.y < 50+self.enemy_size or self.turnTo.y + self.pos.y > 50+self.rect_width-self.enemy_size:
            return False
        else:
#             for e in enemies:
#                 print('h',enemies)
# #                 dif_x = self.pos.x - e.pos.x
# #                 dif_y = self.pos.y - e.pos.y
#                 distance = dist(self.pos.x, self.pos.y, e.pos.x, e.pos.y)
# #                 print(distance)
#                 if distance < 20:
#                     self.pos.add(e.vel)
#                     return False
#                     if dif_x > 0:
#                         self.turnTo = PVector(-1,0)
#                     elif dif_x <= 0:
#                         self.turnTo = PVector(1,0)
#                     elif dif_y > 0:
#                         self.turnTo = PVector(0,1)
#                     else:
#                         self.turnTo = PVector(0,-1)
#                     self.vel = PVector(self.turnTo.x,self.turnTo.y)

            return True

    def move(self,enemies=[]):
        if self.checkPosition(enemies) and bool(random.choice(self.speed_list)):
            for e in enemies:
                distance = dist(self.pos.x, self.pos.y, e.pos.x, e.pos.y)
                while (distance < 21):
                    distance = dist(self.pos.x, self.pos.y, e.pos.x, e.pos.y)
                    if self.pos.x < e.pos.x and self.checkPosition(e):
                        self.pos.add(PVector(-1,0))
                    if self.pos.x >= e.pos.x and self.checkPosition(e):
                        self.pos.add(PVector(1,0))
                    if self.pos.y < e.pos.y and self.checkPosition(e):
                        self.pos.add(PVector(0,1))
                    if self.pos.y >= e.pos.y and self.checkPosition(e):
                        self.pos.add(PVector(0,-1))
                    self.show()
#                     self.pos.add(self.vel*random.choice([-1,1]))
#                     e.pos.add(e.vel*random.choice([-1,1]))
            else:
                self.pos.add(self.vel)
