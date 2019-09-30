#code broken fix ASAP
#import a .py file as commands and such to clean up code
import tkinter
from tkinter import *
from guiCommands import pathgame, dndgame
from algorithmn import algorithmn

game = tkinter.Tk()
game.title("TTRPG Encounters")
game.geometry('500x500')

lbl = Label(window, text = "Chose Your TTRPG", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

pathfinder = Button (game, bg = "red", text ="Pathfinder", command = pathgame).grid(row=2, column=1)
pathfinder.pack()

dnd5e = Button (game, bg = "blue", text ="D&D 5e", command = dndgame).grid(row=2, column=4)
dnd5e.pack()

tk.Button(game, text='Quit', command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)




#pls dont touch this
window.mainloop()
