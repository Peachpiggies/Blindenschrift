import braille as b
import cv2
import numpy as np
from tkinter import *
from tkinter.messagebox import askokcancel
from PIL import ImageTk, Image
import csv

window = Tk()
window.title('Blidenschrift')
window.geometry('300x350')
window.resizable(width = True, height = True)

label1 = Label(window, text = 'Blidenschrift', font = ('Bahnschrift light', 20), fg = 'black').pack(pady = 15)

window.mainloop()