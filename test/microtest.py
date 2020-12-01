import speech_recognition as sr
import time
import board
from adafruit_motorkit import MotorKit

def stop(kit):
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0

def forward(kit):
    kit.motor1.throttle = 1
    kit.motor2.throttle = 1

def reverse(kit):
    kit.motor1.throttle = -1
    kit.motor2.throttle = -1

# obtain audio from the microphone
r = sr.Recognizer()

audio_input = ""

while(audio_input != "fin"):
    with sr.Microphone() as source:
        print("J'ecoute")
        audio = r.listen(source)

# recognize speech using Google Speech Recognition
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        audio_input =  r.recognize_google(audio, language="fr-FR")
        print("j'ai entendu " + audio_input)
        if (audio_input == "avance"):
            #avancer
            print("En avant!")
            kit = MotorKit(i2c=board.I2C())
            forward(kit)
            time.sleep(2)
            stop(kit)
        if (audio_input == "recule"):
           print("En arriere!")
           kit = MotorKit(i2c=board.I2C())
           reverse(kit)
           time.sleep(2)
           stop(kit)

    except sr.UnknownValueError:
        print("Je comprends pas :(")
    except sr.RequestError as e:
        print("Allo google ? ; {0}".format(e))

print("Au revoir!")
