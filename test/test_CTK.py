import os
import json
import customtkinter as ctk
import cv2
from tkinter import *
from PIL import ImageTk, Image

app = ctk.CTk()
app.title("Main Menu")
app.geometry("640x980")
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

theme_label = None
combobox1 = None
setting_frame = None
scan_window = None

# Global variable to store the theme setting
theme_setting = 'light'

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

    setting_button.pack_forget()
    name.pack_forget()
    logo_lable.pack_forget()
    scan_button.pack_forget()

    app.title("Settings")
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("test/test_custom.json")

    # Create a frame to hold the label and combobox
    setting_frame = ctk.CTkFrame(master = app, width = 600, height = 900)
    setting_frame.pack(pady=10)

    theme_label = ctk.CTkLabel(setting_frame, text='Color Theme', bg_color = "transparent", font = bl20)
    theme_label.pack()

    combobox1 = ctk.CTkComboBox(setting_frame, values=['light', 'dark'], command=lambda choice: set_theme(choice))
    combobox1.pack()

    back_button = ctk.CTkButton(setting_frame, width = 58, height = 29, bg_color = "transparent", image=back, text="", command=close_setting)
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

        setting_button.pack(anchor = "nw", padx = 0, pady = 0)
        name.pack(anchor = "center")
        logo_lable.pack(padx = 0, pady = 50)
        scan_button.pack(padx = 0, pady = 80)

def scan():
    setting_button.pack_forget()
    name.pack_forget()
    logo_lable.pack_forget()
    scan_button.pack_forget()

    # Create a new window to display the camera feed
    scan_window = Toplevel(app)
    scan_window.title("Scanning")
    scan_window.geometry("640x480")
    scan_window.protocol("WM_DELETE_WINDOW", close_scan_window)  # Handle window close event

    cam = cv2.VideoCapture(0)

    while True:
        ret, scanned = cam.read()

        if ret:
            cv2.imshow("Scan Window", scanned)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            cv2.imwrite("save/scan2.jpg", scanned)
            # Perform further processing on the saved image if needed

        if key == ord('q'):  # Press 'q' to exit the scanning window
            break

    cam.release()
    cv2.destroyAllWindows()

def close_scan_window():

    global scan_window

    if scan_window:

        scan_window.pack_forget()
        setting_button.pack(anchor="nw", padx=0, pady=0)
        name.pack(anchor="center")
        logo_lable.pack(padx=0, pady=50)
        scan_button.pack(padx=0, pady=80)


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

scan_button = ctk.CTkButton(app, text="SCAN", command = scan)
scan_button.configure(font = bl36, width = 360, height = 60)
scan_button.anchor("center")
scan_button.pack(padx = 0, pady = 80)

app.mainloop() 