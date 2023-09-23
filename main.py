import braille as b
import cv2
import numpy as np
from tkinter import *
from tkinter.messagebox import askokcancel
from tkinter import font as tkFont
from PIL import ImageTk, Image
import csv

window = Tk()
window.title('Blidenschrift')
window.geometry('500x600')
window.resizable(width = True, height = True)

# Created a base font for the whole application
BL36 = tkFont.Font(family='Bahnschrift light', size=36)
BL20 = tkFont.Font(family='Bahnschrift light', size=20)

label1 = Label(window, text = 'Blidenschrift', font = BL36, fg = 'black').pack(pady = 15)

frame = Frame(window, width=360, height=360)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open("img_asset/blindenschrift.jpg"))

label = Label(frame, image = img)
label.pack()

# Created a button to scan the
scan_b = Button(window, width = 5, height = 1, text = "Scan", font = BL20, fg = '#bcb531', bg = '#3476ae')
scan_b.pack()
scan_b.place(anchor = 'center', relx = 0.5, rely = 0.9)

window.mainloop()