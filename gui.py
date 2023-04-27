import serial
import time
from datetime import datetime

from BLL.ConveyorBelt import ConveyorBelt

def command(ser, command):
  start_time = datetime.now()
  ser.write(str.encode(command))
  time.sleep(1)

  while True:
    line = ser.readline()
    print(line)

    if line == b'ok\n':

      return()

ser = serial.Serial('/dev/ttyUSB1', 115200)
time.sleep(2)
command(ser, "G28\r\n")



import tkinter as tk

# Create the tkinter window
root = tk.Tk()

root.attributes('-fullscreen', True)
root.title("Big Buttons Example")

# Set the window size
root.geometry("400x300")

# Create the button functions
def button1_click():
    command(ser, "G0 Y0 F18000 \r\n")

def button2_click():
    command(ser, "G0 Y72 F18000 \r\n")

def button3_click():
  conb = ConveyorBelt()
  conb.start()
  



# Create the buttons
button1 = tk.Button(root, text="Position 1", font=("Arial", 24), command=button1_click)
button2 = tk.Button(root, text="Position 2", font=("Arial", 24), command=button2_click)

button3 = tk.Button(root, text="Run conveyer belt", font=("Arial", 24), command=button3_click)


# Place the buttons on the window
button1.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
button2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
button3.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# Start the main event loop
root.mainloop()