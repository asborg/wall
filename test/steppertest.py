"""Simple test for using adafruit_motorkit with a stepper motor"""
import time
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit = MotorKit(i2c=board.I2C())

for i in range(200):
    step= kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
    print(step)
    time.sleep(0.01)

for i in range(500):
    step= kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
    print(step)
    time.sleep(0.01)


kit.stepper2.release()
