import tts
import motor
import time

if __name__ == "__main__":
    motor.fwd()
    tts.say("Hola culeritos! Soy un furby de barrio.")
    motor.stop()

