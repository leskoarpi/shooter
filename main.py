from ursina import *
import numpy as np
import math

from ursina.prefabs.platformer_controller_2d import CollisionBox




class Player(Entity):
    def __init__(self):
        super().__init__()
        self.model='quad'
        self.collider='box'
        self.scale=(1,1)
        self.position=(0,0,0)
        self.color=color.white50
        self.health=500

class Bullet(Entity):
    def __init__(self):
        super().__init__()
        self.model='quad'
        self.color=color.green
        self.scale=(.25,.25)
        self.position=player.position
        self.collider="box"
        self.dx = .8*math.sin(player.rotation_z/180*math.pi)
        self.dy = .8*math.cos(player.rotation_z/180*math.pi)

def input(key):
    global bullets
    if key == "space":
        bullet = Bullet()
        bullets.append(bullet)

class Enemy(Entity):
    def __init__(self):
        super().__init__()
        self.model= 'circle'
        self.hp=100
        self.color=color.azure
        self.position =(0,5.5)
        self.collider="box"

collide = Enemy().intersects()

def update():
    player.y += held_keys['w'] * time.dt * 8
    player.y -= held_keys['s'] * time.dt * 8
    player.x += held_keys['d'] * time.dt * 8
    player.x -= held_keys['a'] * time.dt * 8


    global bullets
    for bullet in bullets:
        bullet.x+=time.dt*bullet.dx*15
        bullet.y+=time.dt*bullet.dy*15

app = Ursina()
camera.z=-35

ground=Entity(model='quad',color=color.green, scale=(40,1), position=(0,-7.5, 0))

player = Player()


enemy=Enemy()



bullets=[]


app.run()
