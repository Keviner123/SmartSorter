import tkinter as tk
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2
import requests # request img from web
import shutil # save img locally


model = YOLO("diy2.pt")

# Create the tkinter window
root = tk.Tk()

# Set the window title
root.title("Big Buttons Example")

# Set the window size
root.geometry("400x300")

# Create the button functions
def button_click():
    # Get the text in the text box

    url = "http://192.168.1.109:8080/photoaf.jpg" #prompt user for img url
    file_name = "img.jpg"

    res = requests.get(url, stream = True)

    with open(file_name,'wb') as f:
        shutil.copyfileobj(res.raw, f)


    results = model.predict(source="img.jpg", show=True)


    # Append the text "Button clicked!" to the existing text
    text = results

    # Set the text of the text box to the updated text
    textbox.delete("1.0", tk.END)
    textbox.insert("1.0", text)

# Create the buttons
button = tk.Button(root, text="Click Me", font=("Arial", 24), command=button_click)

# Place the button on the window
button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# Create the text box
textbox = tk.Text(root, font=("Arial", 16), height=5, width=30)

# Place the text box on the window
textbox.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# Start the main event loop
root.mainloop()
