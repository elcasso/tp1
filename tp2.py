from mcpi.minecraft import Minecraft
import picamera
from mcpi import block
from time import sleep
import os
camera = picamera.PiCamera()
mc = Minecraft.create()


mc.postToChat("press j for ice, k for lava, AND C FOR THE VIRREYS CASTLE")


comando = raw_input("j o k?") 
print mc.player.getTilePos()

while True:
    if comando == "j":
        x,y,z= mc.player.getPos()
        mc.setBlock (x,y-1,z, 79)
        mc.setBlock (x+1,y-1,z, 79)
        
    elif comando == "k":
        x,y,z= mc.player.getPos()
        mc.setBlock (x,y-1,z, 46)
        mc.setBlock (x+1,y-1,z, 46)

    elif comando=="c":
        os.system ("python castle.py")

    pos = mc.player.getTilePos()
    
    if pos.x == 42 and pos.y==7 and pos.z == -101 :
        camera.capture ("minecraft.jpg")
        mc.postToChat("Photo taken")
        sleep (0.5)

        
