class Tim():
    pos = None
    vel = PVector(1,0)
    
    turnTo = PVector(-1,0)
    turn = False

    rect_width = 400
    rect_height = 400
    enemy_size = 10
    def __init__(self):
        self.pos = PVector(150, 150)
        
    def show(self):
        fill(255,255,0)
        stroke(255,255,0)
        ellipse(self.pos.x,self.pos.y,20,20)
    
    def checkPosition(self):
        self.vel = PVector(self.turnTo.x,self.turnTo.y)
        if self.turnTo.x + self.pos.x < 50+self.enemy_size or self.turnTo.x + self.pos.x > 50+self.rect_width-self.enemy_size \
        or self.turnTo.y + self.pos.y < 50+self.enemy_size or self.turnTo.y + self.pos.y > 50+self.rect_width-self.enemy_size:
            return False
        else:
            return True
    
    def move(self):
        if self.checkPosition():
            self.pos.add(self.vel)
