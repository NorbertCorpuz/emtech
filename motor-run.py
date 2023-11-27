from motor import motor
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

cred = credentials.Certificate('/home/norbie/Desktop/emtech/credentials.json')

options = {
    "databaseURL": "https://emtech-1ac6b-default-rtdb.asia-southeast1.firebasedatabase.app/"
}
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred,options)

motor = motor(Ena=25, In1=24, In2=23)



while True:
    run_ref = db.reference("/motor_run")
    run_data = run_ref.get()


    if run_data == True:


        motor.move_forward(speed=100, t=.3)
        motor.stop(.5)
        motor.stop(5)
        motor.move_backward(speed=100, t=.3)
        motor.stop()


    else:
        continue

                                               