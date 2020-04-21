from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#define pins
redled = LED(17)
blueled = LED(18)
greenled = LED(27)

#define Gui
win = Tk()
win.title("Control LED Lights")
myfont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

#function toggle
def toggleRedLight():
	if redled.is_lit:
		redled.off()
		RedButton["text"]="Turn Red Led On"
	else:
		redled.on()
		RedButton["text"]="Turn Red Led Off" 

def toggleBlueLight():
        if blueled.is_lit:
                blueled.off()
                BlueButton["text"]="Turn Blue Led On"
        else:
                blueled.on()
                BlueButton["text"]="Turn Blue Led Off" 

def toggleGreenLight():
        if greenled.is_lit:
                greenled.off()
                GreenButton["text"]="Turn Green Led On"
        else:
                greenled.on()
                GreenButton["text"]="Turn Green Led Off" 

def close():

	GPIO.cleanup()
	win.destroy()


#widgets
RedButton = Button(win, text = 'Turn Red Led On', font = myfont, command = toggleRedLight, bg = 'red', height = 1, width = 24)
RedButton.grid(row = 1, column = 0)

BlueButton = Button(win, text = 'Turn Blue Led On', font = myfont, command = toggleBlueLight, bg = 'sky blue', height = 1, width = 24)
BlueButton.grid(row = 1, column = 1)

GreenButton = Button(win, text = 'Turn Green Led on', font = myfont, command = toggleGreenLight, bg = 'green', height = 1, width = 24)
GreenButton.grid(row = 1, column = 2)

ExitButton = Button(win, text = 'Exit', font = myfont, command = close, bg = 'red', height = 1, width = 5)
ExitButton.grid(row = 2, column = 1)

win.protocol("WM_DELETE_WINDOW")
win.mainloop()





