from tkinter import *
from tkinter.messagebox import askokcancel
from tkinter import font as tkFont
from PIL import ImageTk, Image

window = Tk()
window.title('Blidenschrift')
window.geometry('640x1136')
window.configure(bg='#ffffff')
window.resizable(width=True, height=True)

# Created a base font for the whole application
BL36 = tkFont.Font(family='Bahnschrift light', size=36)
BL20 = tkFont.Font(family='Bahnschrift light', size=20)

label1 = Label(window, text='Blidenschrift', font=BL36, fg='black', bg='#ffffff')
label1.pack(pady=15)

frame = Frame(window, width=360, height=360, borderwidth=0, highlightthickness=0)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.45)

img = ImageTk.PhotoImage(Image.open("img_asset/blindenschrift.jpg"))

label = Label(frame, image=img)
label.pack()

# Global is_on
is_on = True

def Switch():

    global is_on

    if is_on:

        switch.config(image=off)
        is_on = False
        
    else:
        switch.config(image=on)
        is_on = True

on = PhotoImage(file="img_asset/on-switch.png")
off = PhotoImage(file="img_asset/off-switch.png")

def openSetting():

    global switch  # Declare switch as global
    
    newWindow = Toplevel(window)
    newWindow.title("Settings")
    newWindow.geometry("640x1136")
    setting_1 = Label(newWindow, text="Change theme", font=BL20)
    setting_1.pack()
    setting_1.place(anchor='nw')

    switch = Button(newWindow, image=off, bd=0, command=Switch)
    switch.pack(pady=50)
    switch.place(anchor='ne', relx=0.95, rely=0.01)

# Created a button to scan
scan_b = Button(window, width=5, height=1, text="Scan", font=BL20, fg='#bcb531', bg='#3476ae')
scan_b.pack()
scan_b.place(anchor='center', relx=0.5, rely=0.8)

img_b = ImageTk.PhotoImage(file='img_asset/setting.jpg')
img_label = Label(window, image=img_b)
setting_b = Button(window, image=img_b, command=openSetting)
setting_b.pack()
setting_b.place(relx=0.85, rely=0.85)

window.mainloop()