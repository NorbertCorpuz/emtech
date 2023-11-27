import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class motor():
    def __init__(self, Ena, In1, In2):
        self.Ena = Ena
        self.In1 = In1
        self.In2 = In2

        GPIO.setup(self.Ena, GPIO.OUT)
        GPIO.setup(self.In1, GPIO.OUT)
        GPIO.setup(self.In2, GPIO.OUT)

        self.pwm = GPIO.PWM(self.Ena,100)
        self.pwm.start(0)


    def move_forward(self, speed=50, t=.5):

        GPIO.output(self.In1, GPIO.LOW)
        GPIO.output(self.In2, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(speed)
        sleep(t)

    
    def move_backward(self, speed=50, t=1):

        GPIO.output(self.In1, GPIO.HIGH)
        GPIO.output(self.In2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(speed)
        sleep(t)


    def stop(self, t=0):
        self.pwm.ChangeDutyCycle(0)
        sleep(t)

    
