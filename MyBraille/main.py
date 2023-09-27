import braille
import cv2
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
BL36 = tkFont.Font(family = 'Bahnschrift light', size = 36)
BL20 = tkFont.Font(family = 'Bahnschrift light', size = 20)

label1 = Label(window, text = 'Blidenschrift', font = BL36, fg = 'black', bg = 'white')
label1.pack()

logo_frame = Frame(window, width = 360, height = 360, borderwidth = 0, highlightthickness = 0)
logo_frame.pack()
logo_frame.place(anchor = 'center', relx = 0.5, rely = 0.45)

img_logo = ImageTk.PhotoImage(Image.open("img_asset/blindenschrift.jpg"))
img_logo_dark = ImageTk.PhotoImage(Image.open("img_asset/invert_blindenschrift.jpg"))

pic = Label(logo_frame, image = img_logo)
pic.pack()

# Global theme_defult and lang_defult
theme_defult = True
lang_defult = True
newWindow = None  # Initialize newWindow as None
setting_1 = None
setting_2 = None
scan_b = None

def Switch():

    global theme_defult, newWindow, setting_1, setting_2

    if theme_defult:
        
        switch.config(image = on)
        theme_defult = False

        window.configure(bg = 'black')

        if newWindow:
            newWindow.configure(bg = 'black')
        
        label1.config(fg = 'white', bg = 'black')
        pic.config(image = img_logo_dark)
        setting_button.config(image = img_setting_dark)

        if setting_1:
            setting_1.config(fg = 'white', bg = 'black')

        if setting_2:
            setting_2.config(fg = 'white', bg = 'black')

    else:

        switch.config(image = off)
        theme_defult = True

        window.configure(bg = 'white')

        if newWindow:
        
            newWindow.configure(bg = 'white')
        
        label1.config(fg = 'black', bg = 'white')
        pic.config(image = img_logo)
        setting_button.config(image = img_setting)

        if setting_1:
            
            setting_1.config(fg = 'black', bg = 'white')

        if setting_2:

            setting_2.config(fg = 'black', bg = 'white')

on = PhotoImage(file = "img_asset/on-switch.png")
off = PhotoImage(file = "img_asset/off-switch.png")

TH = PhotoImage(file = "img_asset/TH.png")
ENG = PhotoImage(file = "img_asset/ENG.png")

def Language():

    global lang_defult
    global setting_1
    global setting_2

    if lang_defult:

        lang.config(image = TH)
        lang_defult = False

        if setting_1:
            
            setting_1.config(text = 'เปลี่ยนสีธีม')

        if setting_2:

            setting_2.config(text = 'เปลี่ยนภาษา')

    else:

        lang.config(image = ENG)
        lang_defult = True

        if setting_1:

            setting_1.config(text = 'Change Theme')

        if setting_2:

            setting_2.config(text = 'Change Language')

def OpenSetting():

    global switch  # Declare switch as global
    global newWindow
    global setting_1
    global setting_2
    global lang

    newWindow = Toplevel(window)
    newWindow.title("Settings")
    newWindow.geometry("640x1136")
    newWindow.configure(bg = 'white')

    setting_1 = Label(newWindow, text = "Change Theme", font = BL20)
    setting_1.configure(bg = 'white')
    setting_1.pack()
    setting_1.place(anchor = 'nw')

    setting_2 = Label(newWindow, text = "Change Language", font = BL20)
    setting_2.configure(bg = 'white')
    setting_2.pack()
    setting_2.place(anchor = 'nw', rely = 0.1)

    switch = Button(newWindow, image = off, bd = 0, command = Switch)
    switch.pack(pady = 50)
    switch.place(anchor='ne', relx = 0.95, rely = 0.01)

    lang = Button(newWindow, image = ENG, bd = 0, command = Language)
    lang.pack()
    lang.place(anchor = 'ne', relx = 0.95, rely = 0.1)

def Scan():

    global scan_b

    if scan_b:

        cam = cv2.VideoCapture(0)

        while (True):

            check, scaned = cam.read()
            cv2.imshow('Scan', scaned)

            if cv2.waitKey(1) & 0xFF == ord('s'):

                print("<<<SCANED>>>")
                cv2.imwrite("save/scan.jpg", scaned)

                scanned_braille = braille.brailleImgToText("save/scan.jpg")
                print(scanned_braille)

                if not scanned_braille:
                    print("Image not recognized")

                break
    
        cam.release()
        cv2.destroyAllWindows()

Scan()

# Created a button to scan
scan_b = Button(window, width = 5, height = 1, text = "Scan", font = BL20, fg = '#bcb531', bg = '#3476ae', command = Scan)
scan_b.pack()
scan_b.place(anchor = 'center', relx = 0.5, rely = 0.8)

# Created an Image Button
img_setting = ImageTk.PhotoImage(file = 'img_asset/setting.jpg')
img_setting_dark = ImageTk.PhotoImage(file = 'img_asset/invert_setting.jpg')
img_label = Label(window, image = img_setting)
setting_button = Button(window, image = img_setting, command = OpenSetting)
setting_button.pack()
setting_button.place(relx = 0.85, rely = 0.85)

window.mainloop()