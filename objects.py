from pygame import Rect

class Brick:
    def __init__( self, texture, colorIndex = 0, position = [0,0], difficulty = 1, height = 25, width = 25):
        self.color = colorIndex
        self.pos = position
        self.health = difficulty
        self.h = height
        self.w = width
        self.rect = Rect(self.pos[0], self.pos[1], self.w, self.h)
        self.tex = texture
        self.texPos = Rect(152, 49+(self.color*52), self.w, self.h)

         #152, 49 top left purple
    #182, 80

    def hit(self):
        if self.health <= 2:
            del self
        else:
            self.health = self.health - 1

class Ball:
    w = 20
    h = 20
    texPos = Rect(196, 414, w, h)
    def __init__(self, texture, moveSpeed = [-2,2], loc = [0,0]):
        self.speed = moveSpeed
        self.pos = loc
        self.rect = Rect(self.pos[0], self.pos[1], self.w, self.h)
        self.tex = texture

    def move(self, speed):
        #self.pos = self.pos + self.speed
        if not speed:
            self.rect.left = self.rect.left + self.speed[0]
            self.rect.top = self.rect.top + self.speed[1]
            self.pos = [self.rect.left, self.rect.top]
        else:
            self.rect.left = self.rect.left + speed[0]
            self.rect.top = self.rect.top + speed[1]
            self.pos = [self.rect.left, self.rect.top]