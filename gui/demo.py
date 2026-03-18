from tkinter import *
root=Tk()
root.title("GIET FORM")
root.geometry("400x400")
root.configure(bg="yellow")
e1=Entry(root)
e1.pack(side=TOP, pady=10, padx=10)
lb1=Label(root, text="Enter your name", bg="yellow", fg="blue")
lb1.pack(side=TOP, pady=10, padx=10)

root.mainloop()