import tkinter
import time

def update_label(root, label):
    label1.config(text=time.ctime())
    root.after(1000, update_label, root, label1)

root = tkinter.Tk()
label1 = tkinter.Label(root, text="Loading")
label1.pack()
root.after(1, update_label, root, label1)
root.mainloop()