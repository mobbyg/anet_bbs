#!/usr/bin/env python3

"""
ANet Control Panel : This code creates the GUI for the BBS and is also the telnet server.

I will slowly move over the code from the BBSCORE module I have already done some coding on.
"""

from tkinter import *
from tkinter import ttk

root = Tk() #Create Master Window
root.title("ANet Control Panel") #Give Master Window a title

#Make some buttons and place them. Commands come after..
sysinfoButton = ttk.Button(root, text = "Sys Info")
sysinfoButton.grid(row = 0, column = 0)
sysinfoButton.pack()

userinfoButton = ttk.Button(root, text = "User Info")
userinfoButton.grid(row = 0, column = 1)

configButton = ttk.Button(root, text = "Config")
configButton.grid(row = 0, column = 2)

mailButton = ttk.Button(root, text = "Mail")
mailButton.grid(row = 0, column = 3)

filesButton = ttk.Button(root, text = "Files")
filesButton.grid(row = 0, column = 4)

yanksButton = ttk.Button(root, text = "Yanks")
yanksButton.grid(row = 0, column = 5)

newsButton = ttk.Button(root, text = "News")
newsButton.grid(row = 0, column = 6)

editButton = ttk.Button(root, text = "Edit")
editButton.grid(row = 0, column = 7)

quitButton = ttk.Button(root, text = "Quit")
quitButton.grid(row = 0, column = 8)

root.mainloop()
