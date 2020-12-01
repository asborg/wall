# -*- coding: utf-8 -*-
import xbox
import RPi.GPIO as gpio

def init():
  gpio.setmode(gpio.BOARD)
  gpio.setup(7, gpio.OUT)
  gpio.setup(11, gpio.OUT)
  gpio.setup(13,gpio.OUT)
  gpio.setup(15, gpio.OUT)

def stop():
    gpio.output(13, False)
    gpio.output(15, False)
    gpio.output(7, False)
    gpio.output(11, False)

def forward():
    #init()
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(7, False)
    gpio.output(11, True)
    #time.sleep(tf)
    #gpio.cleanup()

def reverse():
    #init()
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(7, True)
    gpio.output(11, False)
    #time.sleep(tf)
    #gpio.cleanup()


def pivot_left():
    #init()
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(7, True)
    gpio.output(11, False)
    #time.sleep(tf)
    #gpio.cleanup()

def pivot_right():
    #init()
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(7, False)
    gpio.output(11, True)
    #time.sleep(tf)
    #gpio.cleanup()



def turn_left():
    #init()
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    #time.sleep(tf)
    #gpio.cleanup()


def turn_right():
    #init()
    gpio.output(7, False)
    gpio.output(13, False)
    gpio.output(15, False)
    gpio.output(11, True)
    #time.sleep(tf)
    #gpio.cleanup()



# Instantiate the controller and gpio
joy = xbox.Joystick()
init()

print("Wall-B : Appuyez sur Back pour arrêter")
print("A pour avancer, B pour reculer, gauche et droite avec le Dpad")
gauchepressed = False
droitepressed = False
avantpressed = False
arrierepressed = False
while not joy.Back():
  #Gauche
  if(joy.dpadLeft()):
    if not gauchepressed :
      print("A gauche")
      pivot_left()
      gauchepressed = True
  else:
    if gauchepressed:
      print("Stop à gauche")
      stop()
      gauchepressed = False
  #Droite
  if(joy.dpadRight()):
    if not droitepressed:
      print("A droite")
      pivot_right()
      droitepressed = True
  else:
    if droitepressed:
      print("Stop à droite")
      stop()
      droitepressed = False
  #Avant
  if(joy.A()):
    #tester si on peut avancer
    if not avantpressed:
      print("En avant")
      forward()
      avantpressed = True
  else:
    if avantpressed:
      print("Stop en avant")
      stop()
      avantpressed = False
  #Arriere
  if(joy.B()):
    if not arrierepressed:
      print("En arrière")
      reverse()
      arrierepressed = True
  else:
    if arrierepressed:
      print("Stop en arrière")
      stop()
      arrierepressed = False
#Fin
joy.close()
gpio.cleanup()
