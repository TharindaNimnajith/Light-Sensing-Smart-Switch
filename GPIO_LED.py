import RPi.GPIO
import time as t

GPIO.setmode(g.BOARD)
GPIO.setup(7,g.OUT)

while(1):
    GPIO.output(7,GPIO.HIGH)
    t.sleep(0.5)				#delay of 500ms
    GPIO.output(7,GPIO.LOW)
    t.sleep(0.5)
