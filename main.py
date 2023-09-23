import braille
from tkinter import *
from tkinter.messagebox import askokcancel
from tkinter import font as tkFont
from PIL import ImageTk, Image

window = Tk()
window.title('Blidenschrift')
window.geometry('640x1136')
window.configure(bg = 'white')
window.resizable(width = True, height = True)

# Created a base font for the whole application
BL36 = tkFont.Font(family = 'Bahnschrift light', size=36)
BL20 = tkFont.Font(family = 'Bahnschrift light', size=20)

label1 = Label(window, text = 'Blidenschrift', font = BL36, fg='black', bg = '#ffffff')
label1.pack()

frame = Frame(window, width = 360, height = 360, borderwidth = 0, highlightthickness = 0)
frame.pack()
frame.place(anchor = 'center', relx = 0.5, rely = 0.45)

img_logo = ImageTk.PhotoImage(Image.open("img_asset/blindenschrift.jpg"))
img_logo_dark = ImageTk.PhotoImage(Image.open("img_asset/invert_blindenschrift.jpg"))

pic = Label(frame, image = img_logo)
pic.pack()

# Global is_on
is_on = True

def Switch():

    global is_on
    global newWindow

    if is_on:

        switch.config(image = on)
        is_on = False

        window.configure(bg = 'black')
        #newWindow.configure(bg = 'black')
        label1.config(fg = 'white', bg = 'black')
        pic.config(image = img_logo_dark)
        setting_button.config(image = img_setting_dark)
        
    else:

        switch.config(image = off)
        is_on = True

        window.configure(bg = 'white')
        #newWindow.configure(bg = 'white')
        label1.config(fg='black', bg='white')
        pic.config(image = img_logo)
        setting_button.config(image = img_setting)  # Change text color of label1

on = PhotoImage(file = "img_asset/on-switch.png")
off = PhotoImage(file = "img_asset/off-switch.png")

def OpenSetting():

    global switch  # Declare switch as global
    
    newWindow = Toplevel(window)
    newWindow.title("Settings")
    newWindow.geometry("640x1136")
    newWindow.configure(bg = 'white')
    setting_1 = Label(newWindow, text = "Change theme", font = BL20)
    setting_1.pack()
    setting_1.place(anchor = 'nw')

    switch = Button(newWindow, image = off, bd = 0, command = Switch)
    switch.pack(pady = 50)
    switch.place(anchor = 'ne', relx = 0.95, rely = 0.01)

# Created a button to scan
scan_b = Button(window, width = 5, height = 1, text = "Scan", font = BL20, fg = '#bcb531', bg = '#3476ae')
scan_b.pack()
scan_b.place(anchor = 'center', relx = 0.5, rely = 0.8)


# Created a Image Button
img_setting = ImageTk.PhotoImage(file = 'img_asset/setting.jpg')
img_setting_dark = ImageTk.PhotoImage(file = 'img_asset\invert_setting.jpg')
img_label = Label(window, image = img_setting)
setting_button = Button(window, image=img_setting, command = OpenSetting)
setting_button.pack()
setting_button.place(relx = 0.85, rely = 0.85)

window.mainloop()