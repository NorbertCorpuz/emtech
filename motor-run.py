from motor import motor
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

# Setuo Database
cred = credentials.Certificate('/home/norbie/Desktop/emtech/credentials.json')

options = {
    "databaseURL": "https://emtech-1ac6b-default-rtdb.asia-southeast1.firebasedatabase.app/"
}
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred,options)


# Define motor
motor = motor(Ena=25, In1=24, In2=23)
while True:
    
    # Get value of run (True of False)
    run = db.reference("/motor_run")
    
    if run == True:
        motor.move_forward(speed=100, t=.8)
        motor.stop(.5)
        motor.move_forward(speed=100, t=.2)
        motor.move_backward(speed=100, t=1.05)
        motor.stop()
        # Update database to stop motor
        db.reference("/").update({"motor_run": False}) 

    
        
    else:
        continue

                                               
