import RPi.GPIO as GPIO

IN1 = 23 # GPIO23 -> PIN 16
IN2 = 24 # GPIO24 -> PIN 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

def fwd():
    print("motor_fwd")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

def bwd():
    print("motor_bwd")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)

def stop():
    print("motor_stop")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

