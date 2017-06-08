from time import sleep
from picamera import PiCamera
from os import system
"curry.te.roba"
camera = PiCamera()
print "Hola tomi, que queres hoy??"
rta = raw_input("x= timelapse o v=colorswap:  ")

if rta == "x":
    camera.start_preview()
    for x in [0,1,2,3]:
        sleep(0.2)
        camera.capture("curry.te.roba"+str(x)+".jpg")
    camera.stop_preview()
    system ("convert -delay 5 -loop 0 curry.te.roba*.jpg pumagif.gif")
    

if rta == "v":
    camera.start_preview()
    camera.image_effect = 'colorswap'
    camera.capture("curry.te.roba.jpg")
    camera.stop_preview()
    

print "la rompimos, tomi. vamos por el 10!. espero que te haya gustado \n muchisimo esta pieza exquisita de programacion avanzada"



