#code broken fix ASAP
#import a .py file as commands and such to clean up code
import tkinter
from tkinter import *
from guiCommands import pathgame, dndgame


window = tkinter.Tk()
window.title("TTRPG Encounters")
window.geometry('500x500')

lbl = Label(window, text = "Chose Your TTRPG", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

pathfinder = Button (window, bg = "red", text ="Pathfinder", command = pathgame).grid(row=2, column=1)
dnd5e = Button (window, bg = "blue", text ="D&D 5e", command = dndgame).grid(row=2, column=4)

tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)


pathfinder.pack()
dnd5e.pack()
#pls dont touch this
window.mainloop()
