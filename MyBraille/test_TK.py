import braille
import cv2
from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image

window = Tk()
window.title('Blidenschrift')
window.geometry('640x1136')
window.configure(bg='white')
window.resizable(width=True, height=True)

# Created a base font for the whole application
BL36 = tkFont.Font(family='Bahnschrift light', size=36)
BL20 = tkFont.Font(family='Bahnschrift light', size=20)

label1 = Label(window, text='Blidenschrift', font=BL36, fg='black', bg='white')
label1.pack()

logo_frame = Frame(window, width=360, height=360, borderwidth=0, highlightthickness=0)
logo_frame.pack()
logo_frame.place(anchor='center', relx=0.5, rely=0.45)

img_logo = ImageTk.PhotoImage(Image.open("img_asset/blindenschrift.jpg"))
img_logo_dark = ImageTk.PhotoImage(Image.open("img_asset/invert_blindenschrift.jpg"))

on = PhotoImage(file = "img_asset/on-switch.png")
off = PhotoImage(file = "img_asset/off-switch.png")

TH = PhotoImage(file = "img_asset/TH.png")
ENG = PhotoImage(file = "img_asset/ENG.png")

back = PhotoImage(file = "img_asset/back.png")
back_dark = PhotoImage(file = "img_asset/back_dark.png")

pic = Label(logo_frame, image=img_logo)
pic.pack()

# Global theme_default and lang_default
theme_default = True
lang_default = True
scan_b = None
setting_window = None  # Initialize the setting window as None

def switch_theme():
    global theme_default
    if theme_default:
        switch.config(image=off)
        theme_default = False
        window.configure(bg='black')
        label1.config(fg='white', bg='black')
        pic.config(image=img_logo_dark)
        setting_button.config(image=img_setting_dark)
    else:
        switch.config(image=on)
        theme_default = True
        window.configure(bg='white')
        label1.config(fg='black', bg='white')
        pic.config(image=img_logo)
        setting_button.config(image=img_setting)

def switch_language():
    global lang_default
    if lang_default:
        lang.config(image=TH)
        lang_default = False
        setting_1.config(text='เปลี่ยนสีธีม')
        setting_2.config(text='เปลี่ยนภาษา')
    else:
        lang.config(image=ENG)
        lang_default = True
        setting_1.config(text='Change Theme')
        setting_2.config(text='Change Language')

def close_setting():
    global setting_window
    if setting_window:
        setting_window.destroy()
        label1.pack()
        pic.pack()
        scan_b.pack()
        setting_button.pack()
        setting_window = None  # Reset the reference to None

def open_setting():
    global setting_window
    global switch
    global setting_1
    global setting_2
    global lang
    if setting_window:
        return  # If the settings window is already open, do nothing
    label1.pack_forget()
    pic.pack_forget()
    scan_b.pack_forget()
    setting_button.pack_forget()
    setting_window = Toplevel(window)
    setting_window.title("Settings")
    setting_window.geometry("640x1136")
    setting_window.configure(bg='white')
    setting_1 = Label(setting_window, text="Change Theme", font=BL20)
    setting_1.configure(bg='white')
    setting_1.pack()
    setting_1.place(anchor='nw')
    setting_2 = Label(setting_window, text="Change Language", font=BL20)
    setting_2.configure(bg='white')
    setting_2.pack()
    setting_2.place(anchor='nw', rely=0.1)
    switch = Button(setting_window, image=off, bd=0, command=switch_theme)
    switch.pack(pady=50)
    switch.place(anchor='ne', relx=0.95, rely=0.01)
    lang = Button(setting_window, image=ENG, bd=0, command=switch_language)
    lang.pack()
    lang.place(anchor='ne', relx=0.95, rely=0.1)
    close_button = Button(setting_window, image=back, font=BL20, command=close_setting)
    close_button.pack()
    close_button.place(anchor='sw', rely=0.9)

def scan():
    cam = cv2.VideoCapture(0)
    while True:
        check, scanned = cam.read()
        cv2.imshow('Scan', scanned)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            print("<<<SCANNED>>>")
            cv2.imwrite("save/scan.jpg", scanned)
            scanned_braille = braille.imageToBraille("save/scan.jpg")
            print(scanned_braille)
            if not scanned_braille:
                print("Image not recognized")
            break
    cam.release()
    cv2.destroyAllWindows()

scan_b = Button(window, width=5, height=1, text="Scan", font=BL20, fg='#bcb531', bg='#3476ae', command=scan)
scan_b.pack()
scan_b.place(anchor='center', relx=0.5, rely=0.8)

# Created an Image Button
img_setting = ImageTk.PhotoImage(file='img_asset/setting.jpg')
img_setting_dark = ImageTk.PhotoImage(file='img_asset/invert_setting.jpg')
setting_button = Button(window, image=img_setting, command=open_setting)
setting_button.pack()
setting_button.place(relx=0.85, rely=0.85)

window.mainloop()