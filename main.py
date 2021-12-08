from ursina import *
import numpy as np
import math




class Player(Entity):
    def __init__(self):
        super().__init__()
        self.model='quad'
        self.scale=(1,1)
        self.position=(0,0)
        self.color=color.white50

class Bullet(Entity):
    def __init__(self):
        super().__init__()
        self.model='quad'
        self.color=color.green
        self.scale=(.25,.25)
        self.position=player.position
        self.dx = .8*math.sin(player.rotation_z/180*math.pi)
        self.dy = .8*math.cos(player.rotation_z/180*math.pi)

def input(key):
    global bullets
    if key == "space":
        bullet = Bullet()
        bullets.append(bullet)


def update():
    player.y += held_keys['w'] * time.dt * 8
    player.y -= held_keys['s'] * time.dt * 8
    player.x += held_keys['d'] * time.dt * 8
    player.x -= held_keys['a'] * time.dt * 8


    global bullets
    for bullet in bullets:
        bullet.x+=time.dt*bullet.dx
        bullet.y+=time.dt*bullet.dy
        

        

app = Ursina()









player = Player()
bullets=[]


app.run()
