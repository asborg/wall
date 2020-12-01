# -*- coding: utf-8 -*-
import xbox
import time
import board
import mesure
from adafruit_motorkit import MotorKit

#TODO
#1 corriger le sens des moteurs -> OK
#2 utiliser le stick pour le niveau de throttle -> ok . attention les autres boutons ne marchent plus
#3 caméra : https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/4
#video stream https://randomnerdtutorials.com/video-streaming-with-raspberry-pi-camera/
#face recognition : https://www.pyimagesearch.com/2018/06/25/raspberry-pi-face-recognition/

def stop(kit):
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0

def forward(kit):
    if (mesure.distance()) > 3:
        kit.motor1.throttle = 1
        kit.motor2.throttle = 1
    else:
        print("Obstacle droit devant! Stop!")

def reverse(kit):
    kit.motor1.throttle = -1
    kit.motor2.throttle = -1

def pivot_left(kit):
    kit.motor1.throttle = 1
    kit.motor2.throttle = -1

def pivot_right(kit):
    kit.motor1.throttle = -1
    kit.motor2.throttle = 1

def turn_left(kit):
    kit.motor1.throttle = 1
    kit.motor2.throttle = 0

def turn_right(kit):
    kit.motor1.throttle = 0
    kit.motor2.throttle = 1

# run motor on analogic stick
def analogic_run(kit, amountX, amountY):
    LM = amountY
    RM = amountY
    if (amountX != 0):
      LM = LM - amountX
      RM = RM + amountX
    if (LM > 1) :
      LM = 1
    if (RM > 1):
      RM = 1
    if (LM < -1):
      LM = -1
    if (RM < -1):
      RM = -1 
    #print("motors - left :", LM, " - Right :", RM, end="")
    if (LM>0 and RM>0 and mesure.distance() < 3):
        #if we go forward but close object, stop
        print("Obstacle devant, j'avance pas")
        LM = 0
        RM = 0
    kit.motor1.throttle = LM
    kit.motor2.throttle = RM

# Format floating point number to string format -x.xxx
def fmtFloat(n):
    return '{:6.1f}'.format(n)


# Instantiate the controller and gpio
joy = xbox.Joystick()
#instantiate the motors
kit = MotorKit(i2c=board.I2C())
stop(kit)

print("Wall-C : Appuyez sur Back pour arrêter")
print("A pour avancer, B pour reculer, gauche et droite avec le Dpad")
gauchepressed = False
droitepressed = False
avantpressed = False
arrierepressed = False
stick = False
while not joy.Back():
  #Gauche
  if(joy.dpadLeft()):
    if not gauchepressed :
      print("A gauche")
      pivot_left(kit)
      gauchepressed = True
  else:
    if gauchepressed:
      print("Stop à gauche")
      stop(kit)
      gauchepressed = False
  #Droite
  if(joy.dpadRight()):
    if not droitepressed:
      print("A droite")
      pivot_right(kit)
      droitepressed = True
  else:
    if droitepressed:
      print("Stop à droite")
      stop(kit)
      droitepressed = False
  #Avant
  if(joy.A()):
    #tester si on peut avancer
    if not avantpressed:
      print("En avant")
      forward(kit)
      avantpressed = True
  else:
    if avantpressed:
      print("Stop en avant")
      stop(kit)
      avantpressed = False
  #Arriere
  if(joy.B()):
    if not arrierepressed:
      print("En arrière")
      reverse(kit)
      arrierepressed = True
  else:
    if arrierepressed:
      print("Stop en arrière")
      stop(kit)
      arrierepressed = False
  # stick left
  #if(fmtFloat(joy.leftX()) != fmtFloat(0) or fmtFloat(joy.leftY()) != fmtFloat(0)):
  if(joy.leftX() != 0 or joy.leftY() != 0):
    if not stick:
      print("Stick left")
      analogic_run(kit, joy.leftX(), joy.leftY())
      stick = True
    else:
      if stick:
        print("stop stick left")
        stop(kit)
        stick = False
  else:
    stop(kit)
#Fin
joy.close()
