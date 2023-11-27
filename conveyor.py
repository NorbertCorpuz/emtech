import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class motor():
    def __init__(self, Enb, In3, In4):
        self.Enb = Enb
        self.In3 = In3
        self.In4 = In4

        GPIO.setup(self.Enb, GPIO.OUT)
        GPIO.setup(self.In3, GPIO.OUT)
        GPIO.setup(self.In4, GPIO.OUT)

        self.pwm = GPIO.PWM(self.Enb,100)
        self.pwm.start(0)


    def move_forward(self, speed=100):

        GPIO.output(self.In3, GPIO.LOW)
        GPIO.output(self.In4, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(speed)
        