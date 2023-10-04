import cv2
from PIL import Image, ImageTk
import tkinter as tk
import requests

#service AIFORTHAI
def TL():
    global a, b, c

    cv2.imwrite("car.jpeg", frame)

    url = "https://api.aiforthai.in.th/lpr-v2"
    payload = {"crop": "1", "rotate": "1"}
    files = {"image": open("car.jpeg", "rb")}

    headers = {
        "Apikey": "FsV5qaAnO2GN6vsiDiMZDQhQ501bkEhO",
    }

    try:

        response = requests.post(url, files=files, data=payload, headers=headers)

        print(response.json())
        a = response.json()
        b = a[0]
        c = b["lpr"]
        license.set(c)

    except Exception:
        return


# 6.2 ฟังก์ชันปุ่ม ออกจากโปรแกรม
def stop():
    cap.release()
    window.destroy()


# 1. การกำหนดขนาดกล้อง และฟังก์ชันการอ่านค่าจากกล้อง โดยใช้ library openCV และ Pillow
wcam, hcam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)


def show_frame():

    global imgtk
    global frame

    check, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)


# 2. การสร้าง GUI โดยใช้ tkinter
# 2.1 สร้างหน้าต่างและกำหนดค่าหน้าต่าง
window = tk.Tk()  # Makes main window

window.wm_title("โปรแกรมอ่านป้ายทะเบียนรถ")
window.geometry('800x700')
window.option_add("*font", "PSL-omyim 30")
window.config(background="#242526")

# 2.2 สร้าง frame กำหนดขนาด Graphics window
imageFrame = tk.Frame(window)
imageFrame.configure(width = 600, height = 500)
imageFrame.grid_propagate(False)
imageFrame.pack()
# .grid(row=0, column=0, columnspan=2, padx=10, pady=2)

# 2.3 การกำหนดตัวแปรข้อความที่เปลี่ยนแปลงได้เพื่อนำไปแสดงผล และการแสดงค่าเริ่มต้น (แถวที่ 2)
license = tk.StringVar()
license.set("รอการกดปุ่มอ่านเลขทะเบียนรถขาเข้า")

# 2.4 การนำภาพจากกล้อง Capture video มาใส่ใน frames (imageFrame) ที่กำหนดไว้
lmain = tk.Label(imageFrame)
lmain.pack(pady = 3)

# 2.7 การสร้าง label เพื่อนำค่าที่ได้มาอ่านค่าลงตัวแปรข้อความ license ป้ายทะเบียนขาเข้า แถวที่ 2
label20 = tk.Label(textvariable=license, bg="gold", fg="white", font="PSL-omyim 50")
label20.pack()

# 2.5 การสร้างปุ่ม button เพื่อให้เรียกใช้ฟังก์ชัน อ่านป้ายทะเบียนขาเข้า TL แถวที่ 1 แนวที่ 0
btn10 = tk.Button(text="กดปุ่มเพื่ออ่านเลขทะเบียน", fg='black', command=TL)
btn10.pack()

# 2.9 การสร้างปุ่ม เพื่อออกจากโปรแกรม แถวที่ 4 แนวที่ 0
btn40 = tk.Button(text="หยุดการทำงาน", fg="red", command=stop)
btn40.pack()
show_frame()  # การเรียกใช้ฟังก์ show_frame ของ openCV บรรท้ดที่ 88
window.mainloop()  # การเรียกใช้หน้าต่าง GUI ที่สร้างขึ้น