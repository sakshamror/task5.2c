# Import necessary modules
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

# Set GPIO mode to BCM
RPi.GPIO.setmode(RPi.GPIO.BCM)

# Initialize LED objects for Red, White, and Green LEDs
Red = LED(14)
White = LED(10)
Green = LED(6)

# Create a Tkinter window
win = Tk()
win.title("LED BLINK")

# Define a custom font for buttons
myFont = tkinter.font.Font(family='Arial', size=12, weight="bold")

# Function to toggle the state of the Red LED
def RED_LED():
    # Check if Red LED is currently lit
    if Red.is_lit:
        # If lit, turn off and update button text
        Red.off()
        redButton["text"] = "TURN RED LED ON"
    else:
        # If not lit, turn on and update button text
        Red.on()
        redButton["text"] = "TURN RED LED OFF"

# Function to toggle the state of the Green LED
def GREEN_LED():
    if Green.is_lit:
        Green.off()
        greenButton["text"] = "TURN GREEN LED ON"
    else:
        Green.on()
        greenButton["text"] = "TURN GREEN LED OFF"

# Function to toggle the state of the White LED
def WHITE_LED():
    if White.is_lit:
        White.off()
        whiteButton["text"] = "TURN WHITE LED ON"
    else:
        White.on()
        whiteButton["text"] = "TURN WHITE LED OFF"

# Function to clean up GPIO and close the window
def close():
    RPi.GPIO.cleanup()
    win.destroy()

# Create buttons for controlling LEDs and exit
redButton = Button(win, text="TURN RED LED ON", font=myFont, command=RED_LED)
redButton.grid(row=0, column=1)

whiteButton = Button(win, text="TURN WHITE LED ON", font=myFont, command=WHITE_LED)
whiteButton.grid(row=0, column=3)

greenButton = Button(win, text="TURN GREEN LED ON", font=myFont, command=GREEN_LED)
greenButton.grid(row=0, column=6)

exitButton = Button(win, text="EXIT WINDOW", font=myFont, command=close, bg='red')
exitButton.grid(row=2, column=3)

# Bind the close function to the window close button
win.protocol("WM_DELETE_WINDOW", close)

# Start the Tkinter event loop
win.mainloop()
