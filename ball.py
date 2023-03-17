class ball(object):
    def __init__(self,pos,dire,vel):
        self.pos = pos
        self.dire = dire
        self.vel = vel

    
    def updatePos(self):
        x,y = self.pos
        xd,yd = self.dire
        x = x+xd*self.vel
        y = y+yd*self.vel
        self.pos = (x,y)

    def updateDire(self,dire):
        self.dire = dire


