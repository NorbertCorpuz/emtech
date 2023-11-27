import tkinter as tk
from tkinter import ttk
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

def update_values():
    # Fetch values from Firebase
    diseased_value = db.reference("/diseased").get()
    healthy_value = db.reference("/healthy").get()
    harvest_value = db.reference("/total_harvest").get()
    percentage_value = db.reference("/percentages").get()

    # Update labels with fetched values
    diseased_label.config(text=f"Diseased: {diseased_value}")
    healthy_label.config(text=f"Healthy: {healthy_value}")
    harvest_label.config(text=f"Total Harvest: {harvest_value}")
    percentage_label.config(text=f"Healthy Potatoes: {percentage_value}%")

    # Schedule the function to run again after 1000 milliseconds (1 second)
    root.after(1000, update_values)

# Function to reset the database
def reset_database():
    # Set default values or clear the data in the database
    db.reference("/diseased").set(0)
    db.reference("/healthy").set(0)
    db.reference("/total_harvest").set(0)
    db.reference("/percentages").set(0)

root = tk.Tk()
root.title("Firebase Real-Time Database GUI")

# Set the background color to black
root.configure(bg="green")

# Labels to display values
diseased_label = tk.Label(root, text="Diseased: ", bd=5, relief="groove", bg="#FC6600", fg="white", font=("Arial", 20))
diseased_label.pack(pady=10)

healthy_label = tk.Label(root, text="Healthy: ", bd=5, relief="groove", bg="#FC6600", fg="white", font=("Arial", 20))
healthy_label.pack(pady=10)

harvest_label = tk.Label(root, text="Total Harvest: ", bd=5, relief="groove", bg="#FC6600", fg="white", font=("Arial", 20))
harvest_label.pack(pady=10)

percentage_label = tk.Label(root, text="Healthy Percentage: ", bd=5, relief="groove", bg="#FC6600", fg="white", font=("Arial", 20))
percentage_label.pack(pady=10)

# Label for seasonal information
season_label = tk.Label(root, text="Optimal Harvests Per Seasons", bd=5, relief="groove", bg="#FC6600", fg="white", font=("Arial", 20))
season_label.pack(pady=20)

# Labels for each season
seasons = ["January - April: 75%", "May - August: 70%", "September - December: 80%"]
for season in seasons:
    season_frame = tk.Frame(root, bg="green")
    season_frame.pack()

    season_label = tk.Label(season_frame, text=f"{season}", bd=5, relief="groove", bg="#FC6600", fg="white", font=("Arial", 16))
    season_label.pack(side=tk.LEFT, padx=10)

# Button to reset the database
reset_button = tk.Button(root, text="Reset Database", command=reset_database, bd=5, relief="raised", bg="blue", fg="white", font=("Arial", 12))
reset_button.pack(pady=10, side=tk.LEFT, anchor=tk.CENTER)

# Button to quit the application
quit_button = tk.Button(root, text="Quit", command=root.destroy, bd=5, relief="raised", bg="gray", fg="white", font=("Arial", 12))
quit_button.pack(pady=10, side=tk.RIGHT, anchor=tk.CENTER)

# Start updating values from Firebase
update_values()

# Start the Tkinter main loop
root.mainloop()