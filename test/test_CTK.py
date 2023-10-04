import os
import json
import customtkinter as ctk
import cv2
import time
from tkinter import *
from PIL import ImageTk, Image

app = ctk.CTk()
app.title("Main Menu")
app.geometry("640x800")
app.resizable(width=0, height=0)
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("test/test_custom.json")

# declare the font for the app
bl36 = ctk.CTkFont(family='Bahnschrift light', size=36)
bl20 = ctk.CTkFont(family='Bahnschrift light', size=20)
bb72 = ctk.CTkFont(family='Bahnschrift SemiBold', size=72)
pkm_unk_36 = ctk.CTkFont(family='Pokemon Unown GB', size=36)

back = ctk.CTkImage(light_image=Image.open("img_asset/back.png"),
                    dark_image=Image.open("img_asset/back_dark.png"),
                    size=(58, 29))

cap = None
theme_label = None
combobox1 = None
setting_frame = None
scan_frame = None
label = None

# Global variable to store the theme setting
theme_setting = 'light'

def close_main():

    setting_button.pack_forget()
    name.pack_forget()
    logo_lable.pack_forget()
    scan_button.pack_forget()

def pack_main():

        app.title("Main Menu")
        setting_button.pack(anchor="nw", padx=0, pady=0)
        name.pack(anchor="center")
        logo_lable.pack(padx=0, pady=50)
        scan_button.pack(padx=0, pady=40)   

def load_settings() -> dict:

    if not os.path.exists('./test/settings.json'):

        with open('./test/settings.json', 'w') as file:

            json.dump({'theme': 'system'}, file)

    with open('./test/settings.json') as file:
        
        return json.load(file)

def write_settings(settings: dict) -> None:

    with open('./test/settings.json', 'w') as file:

        json.dump(settings, file)

def set_theme(theme):

    global theme_setting  # Declare the variable as global
    theme_setting = theme
    ctk.set_appearance_mode(theme)
    write_settings({'theme': theme})

def open_setting():

    global setting_frame
    global combobox1
    global theme_label

    close_main()

    app.title("Settings")
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("test/test_custom.json")

    # Create a frame to hold the label and combobox
    setting_frame = ctk.CTkFrame(master = app, width = 600, height = 700)
    setting_frame.pack(pady=10)

    theme_label = ctk.CTkLabel(setting_frame, text = 'Color Theme', bg_color = "transparent", font = bl20)
    theme_label.pack()

    combobox1 = ctk.CTkComboBox(setting_frame, values = ['light', 'dark'], command = lambda choice: set_theme(choice))
    combobox1.pack()

    back_button = ctk.CTkButton(setting_frame, width = 58, height = 29, bg_color = "transparent", image=back, text = "", command = close_setting)
    back_button.anchor("sw")
    back_button.pack()

def close_setting():

    global setting_frame
    global combobox1
    global theme_label

    if setting_frame:

        theme_label.pack_forget()
        combobox1.pack_forget()
        setting_frame.pack_forget()

        pack_main()

def open_scan():

    global cap
    global label
    global scan_frame  # Declare scan_frame as global

    if cap is None:
        cap = cv2.VideoCapture(0)  # Reinitialize the cap if it's None

    close_main()

    # Create a new window to display the camera feed
    app.title("Scanning")
    scan_frame = ctk.CTkFrame(master = app, width = 600, height = 750)
    scan_frame.pack(pady = 10)

    back_button2 = ctk.CTkButton(scan_frame, width = 58, height = 29, image = back, text = "", command = close_scan)
    back_button2.pack(side = "top", anchor = "nw")

    label = ctk.CTkLabel(scan_frame, text = "", width = 600, height = 600)
    label.pack(side = "top", fill = "both", expand = True)

    confirm_button = ctk.CTkButton(scan_frame, width = 72, height = 72, text = "O", font = bb72, command = confirm_scan)
    confirm_button.pack(side = "top", padx = (600-72)//2, pady = 10)  # Centered below the label

    scan()

def confirm_scan():

    if cap is not None and cap.isOpened():

        ret, frame = cap.read()

        if ret:

            cv2.imwrite("./save/scaned.png", frame)
    
    close_scan()

def scan():

    global imgtk
    global frame
    global label

    if label is None:  # Check if label is None, and if so, create it

        label = ctk.CTkLabel(scan_frame, text="", width=600, height=800)
        label.pack()

    if cap is not None and cap.isOpened():

        check, frame = cap.read()

        if check:

            cv2img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2img)
            imgtk = ctk.CTkImage(light_image=img, dark_image=img, size=(600, 600))

            label.configure(image=imgtk)

    # print("hi")

    # Schedule the scan function and store the ID
    global scan_id
    scan_id = label.after(1, scan)

def close_scan():

    global scan_frame
    global label
    global cap

    if scan_frame:

        # Cancel the scheduled scan function
        label.after_cancel(scan_id)
        scan_frame.pack_forget()

        pack_main()

setting_button = ctk.CTkButton(app, text = "n", command = open_setting)
setting_button.configure(width = 58, height = 58, font = pkm_unk_36)
setting_button.pack(anchor = "nw", padx = 0, pady = 0)

name = ctk.CTkLabel(app, text = "Blidenschrift", fg_color = "transparent", font = bb72)
name.anchor("center")
name.pack()

logo = ctk.CTkImage(light_image = Image.open("img_asset/blindenschrift.png"),
                              dark_image = Image.open("img_asset/invert_blindenschrift.png"),
                              size = (360, 360))

logo_lable = ctk.CTkLabel(app, image = logo, text = "")
logo_lable.anchor("center")
logo_lable.pack(padx = 0, pady = 50)

scan_button = ctk.CTkButton(app, text="SCAN", command = open_scan)
scan_button.configure(font = bl36, width = 360, height = 60)
scan_button.anchor("center")
scan_button.pack(padx = 0, pady = 40)

app.mainloop() 