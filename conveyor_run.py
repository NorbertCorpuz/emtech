import RPi._GPIO as GPIO
from time import sleep

in3 = 27
in4 = 17
enb = 4
temp1 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p=GPIO.PWM(enb,1000)

p.start(25)
print("\n")
print("the default speed and direction of motor is low n forward")
print("r-run s- stop f - forward l - low m- medium")
print("\n")


while(1):

    x=input("")

    if x=='r':
        if (temp1==1):
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)
            print("forward")
            x='z'
        else:
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)
            print("backward")
            x='z'

    
    elif x=='s':
        print("stop")
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)
        x='z'
    elif x=='f':
        print("forward")
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        x='z'

    elif x == 'l':
        print("low")
        p.ChangeDutyCycle(25)
        x=='z'
    
    elif x == 'm':
        print("medium")
        p.ChangeDutyCycle(50)
        x=='z'
    
    elif x == 'h':
        print("high")
        p.ChangeDutyCycle(100)
        x=='z'

    elif x=='e':
        GPIO.cleanup()
        print("GPIO cleanup")

    else:
        print("wrong input")
        
