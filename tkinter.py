raspberry_Tkinter
=================
from Tkinter import*
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17,GPIO.LOW)
GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)

def check_button():
    if (GPIO.input(22)==GPIO.LOW):
        labelText.set("Button Pressed")
    else:
        labelText.set(" ")
        root.after(10,check_button)
def toggle():
    if GPIO.input(17):
        GPIO.output(17, GPIO.LOW)
        toggleButton["text"]="Turn LED On"
    else:
        GPIO.output(17, GPIO.HIGH)
        toggleButton["text"]="Turn LED Off"
        
root = Tk()

toggleButton = Button(root, text="Turn LED On", command=toggle)
toggleButton.pack(side=LEFT)

quitButton = Button(root, text="Quit", command=exit)
quitButton.pack(side=LEFT)

labelText = StringVar()
labelText.set("Button Pressed.")
label1 = Label(root, textvariable=labelText, height=4)
label1.pack(side=LEFT)

root.geometry('500x300+200+200')

root.after(10,check_button)
root.mainloop()

creating a Graphical User interface with python for a raspberry pi GPIO input pin interface
