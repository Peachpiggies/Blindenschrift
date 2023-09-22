import braille as b
import cv2
import numpy as np
from tkinter import *
from tkinter.messagebox import askokcancel
from PIL import ImageTk, Image
import csv

window = Tk()
window.title('Blidenschrift')
window.geometry('400x480')
window.resizable(width = True, height = True)

label1 = Label(window, text = 'Blidenschrift', font = ('Bahnschrift light', 20), fg = 'black').pack(pady = 15)

frame = Frame(window, width=360, height=360)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open("img_asset/blindenschrift.jpg"))

label = Label(frame, image = img)
label.pack()

window.mainloop()