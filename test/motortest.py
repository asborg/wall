import time
import board
from adafruit_motorkit import MotorKit
 
kit = MotorKit(i2c=board.I2C())
 
kit.motor2.throttle = 1.0
time.sleep(1)
kit.motor2.throttle = 0.5
time.sleep(1)
kit.motor2.throttle = -1.0
time.sleep(1)
kit.motor2.throttle = 0
