class player(object):
    def __init__(self,pos):
        self.pos = pos

    def up(self):
        x,y = self.pos
        y = y-1
        self.pos = x,y

    def down(self):
        x,y = self.pos
        y = y+1
        self.pos = x,y

    def updatepos(self,pos):
        self.pos = pos
