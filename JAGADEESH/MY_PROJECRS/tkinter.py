# import tkinter as tk                                 #1
#
# import label
#
# kd_root = tk.Tk()                                    #2
#
# kd_root.geometry("300x500")
#
# kd_root.minsize(100, 100)
#
# kd_root.maxsize(800, 700)
#
# label = tk.Label( text="Opening with 250 discount")
# label.pack()
#
# kd_root.mainloop()                                      #3

import tkinter as tk

from PIL import Image
import os

kd = Image.open(r"C:/Users/SIC/Desktop/neww/photo.png")
kd_root = tk.Tk()


import label

kd_root = tk.Tk()                                    #2

kd_root.geometry("300x500")

kd = ImageTk.PhotoImage(kd)

label = Label(root,image = kd)
label.pack




kd_root.minsize(100, 100)

kd_root.maxsize(800, 700)

label = tk.Label( text="Opening with 250 discount")
label.pack()

kd_root.mainloop()    




