#code broken fix ASAP

import tkinter
from tkinter import *



window = tkinter.Tk()
window.title("TTRPG Encounters")
window.geometry('500x500')

lbl = Label(window, text = "Chose Your TTRPG", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
def pathgame():
	game = "Pathfinder"
	lbl.configure(text = "Pathfinder")
	print (game)
def dndgame():
	game = "DnD5e"
	lbl.configure(text = "Dungeons and Dragons: 5e")
	print (game)

pathfinder = Button (window, bg = "red", text ="Pathfinder", command = pathgame)
pathfinder.grid(column=1, row=0)
dnd5e = Button (window, bg = "blue", text ="D&D 5e", command = dndgame)
dnd5e.grid(column=1, row=0)


pathfinder.pack()
dnd5e.pack()
#pls dont touch this
window.mainloop()
