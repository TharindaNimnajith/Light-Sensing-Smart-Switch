import RPi.GPIO as GPIO
import time
from Tkinter import *
root = Tk()
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
def on():
    GPIO.output(18,GPIO.HIGH)
def off():
    GPIO.output(18,GPIO.LOW)
tob = Button(root, text = "Press to activate", command = on)
tob.grid(row = 0, column = 0)
tofb = Button(root, text = "Press to deactivate", command = off)
tofb.grid(row = 0, column = 1)

root.mainloop()
