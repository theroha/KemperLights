# Kemper Lighting Control
# by Jared Strain
# In emergency:
# jared.strain@yahoo.com
# (316) 452-9561

import pyxhook
import pygame, sys
import time

# Import necessary functions from pygame
from pygame import midi
from pygame.locals import *

# Set up midi functionality
midi.init()

for x in range(midi.get_count()):
    device_info = midi.get_device_info(x)
    if device_info[1] != 'Midi Through Port-0' and device_info[3] == 1:
        output = midi.Output(x)
#output = midi.Output(2)


Go = 0xc0 # Midi go command used by ETC
Play = 0x90 # Midi note pressed command used by ETC
Unplay = 0x80 # Midi note note pressed command ued by ETC
Applause = False # Track whether the applause lights are running

def OnKeyPress(event):

    # Declare global variables inside function
    fun = False
    global output
    global Go
    global Play
    global Unplay
    global Applause

    # Print key for error checking
    print(event.Key)
    
    # if event.Key == "Event Key":                  # Number Pad Key
    # output.write_short(Go, Cue in light board)    # Lighting Design
    
    if event.Key == "Right" or event.Key == "Next": # Arrow Keys
        output.write_short(Go, 0)           # Go to next cue
    
    if event.Key == "P_Insert":             # 0
        output.write_short(Go, 93)      # Lights Off

    if event.Key == "P_End":                # 1
        output.write_short(Go, 95)      # PPT Lecture lights
        
    if event.Key == "P_Down":               # 2
        output.write_short(Go, 97)      # Movie Lights

    if event.Key == "P_Next":               # 3
        print("nothing here yet")

    if event.Key == "P_Left":               # 4
        output.write_short(Go, 99)          #Full Lights

    if event.Key == "P_Begin":              # 5
        output.write_short(Go, 89)        # Lecture

    if event.Key == "P_Right":              # 6
        output.write_short(Go, 11)          # Full Show

    if event.Key == "P_Home":               # 7
        output.write_short(Go, 55)          # Butler Gingerbread House

    if event.Key == "P_Up":                 # 8
        print('Nothing here yet')

    if event.Key == "P_Page_Up":            # 9
        print('Nothing here yet')

    if event.Key == "Num_Lock":            # Number Lock
        if Applause == False:
            output.write_short(Play, 0x53, 0x7F) #Applause Lights
            Applause = True
        else:
            output.write_short(Unplay, 0x53, 0x7F)
            Applause = False
        
    if event.KeyID == 39:
        output.write_short(Go, 87)

    # Switch between lecture lights and movie lights
    if event.Key == "B":
        print(fun)
        fun = not fun
        if fun:
            output.write_short(Go, 1)
        elif not fun:
            output.write_short(Go, 97)

    # Turn all lights off and close program safely
    if event.Key == "Escape":
                output.write_short(Go, 93)
                midi.quit()
                pygame.quit()
                new_hook.cancel()
                sys.exit()
                return False
                
    return True

# Pygame Window - Displays to indicate code is running
DISPLAYSURF = pygame.display.set_mode((400,300))

# Keyboard hook
new_hook=pyxhook.HookManager()

new_hook.KeyDown=OnKeyPress # Function runs when a key is pressed

new_hook.HookKeyboard()

new_hook.start()

running = True
while running:
    time.sleep(0.1)
