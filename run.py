from tkinter import Tk, Label
import cv2
import time
from PIL import Image, ImageDraw, ImageFont, ImageTk
import numpy as np
from tensorflow.keras.models import load_model
import tensorflow as tf
import os
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials


cred = credentials.Certificate("credentials.json")

options = { 
    "databaseURL": "https://emtech-1ac6b-default-rtdb.asia-southeast1.firebasedatabase.app/"
}

# Check if the app is already initialized
if not firebase_admin._apps:
    # Initialize the Firebase app
    firebase_admin.initialize_app(cred, options)

ref_diseased = db.reference("/diseased")
ref_diseased.get()
ref_healthy = db.reference("/healthy")
ref_healthy.get()
ref_harvest = db.reference("/total_harvest")
ref_harvest.get()

diseased_value = 0
healthy_value = 0
harvest_value = 0

new_model = load_model(os.path.join('models','new50epoch.h5'))
font = ImageFont.load_default()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret:
        # Converting into RGB
        frame_array = Image.fromarray(frame, 'RGB')

        # Resizing
        frame_array = frame_array.resize((256, 256))
        frame_array = np.array(frame_array)
        

        # 4-Dimensional Tensor
        frame_array = np.expand_dims(frame_array / 255, 0)


        # Make prediction using model
        prediction = new_model.predict(frame_array)

        # Process the prediction and update the frame
        if prediction > 0.65:
           
            img_pil = Image.fromarray(frame)
            draw = ImageDraw.Draw(img_pil)
            draw.rectangle(((8, 50), (110, 100)), fill="green")
            draw.text((10, 50), "Healthy", font=font, fill=(255, 255, 255))
            frame = np.array(img_pil)
            def increment_transaction(healthy_val):
                return healthy_val + 1
            db.reference("/healthy").transaction(increment_transaction)
            
            
            def increment_transaction(harvest_val):
                return harvest_val + 1
            db.reference("/total_harvest").transaction(increment_transaction)
            
            
            total_count = db.reference("/total_harvest").get()
            healthy_count = db.reference("/healthy").get()
              

        # Calculate percentage
            if total_count > 0:
                percentage_value = (healthy_count / total_count) * 100
                # Update the '/percentages' database
                db.reference("/percentages").set(percentage_value)
            
            db.reference("/").update({"motor_run": False})
            
            
            


        elif 0.39 <= prediction <= 0.55:
            
            img_pil = Image.fromarray(frame)
            draw = ImageDraw.Draw(img_pil)
            draw.rectangle(((8, 50), (140, 100)), fill=(0, 0, 255))
            draw.text((10, 50), "Diseased", font=font, fill=(255, 255, 255))
            def increment_transaction(diseased_val):
                return diseased_val + 1
            db.reference("/diseased").transaction(increment_transaction)
          
            
            
            def increment_transaction(harvest_val):
                return harvest_val + 1
            db.reference("/total_harvest").transaction(increment_transaction)
            
            
            total_count = db.reference("/total_harvest").get()
            healthy_count = db.reference("/healthy").get()
              

        # Calculate percentage
            if total_count > 0:
                percentage_value = (healthy_count / total_count) * 100
                # Update the '/percentages' database
                db.reference("/percentages").set(percentage_value)

                
            
            
            db.reference("/percentages")
            db.reference("/").update({"motor_run": True})
            
            
          
        else:
            # NO POTATO
            img_pil = Image.fromarray(frame)
            draw = ImageDraw.Draw(img_pil)
            draw.rectangle(((8, 50), (170, 100)), fill=(0, 165, 255))
            draw.text((10, 50), "NO POTATO", font=font, fill=(255, 255, 255))
            frame = np.array(img_pil)

            db.reference("/percentages")
            db.reference("/").update({"motor_run": False})

        # Show the frame
        cv2.imshow("Potato Disease Detection", frame)
        time.sleep(0.1)
       

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        print("Error reading frame from webcam.")

cap.release()
cv2.destroyAllWindows()