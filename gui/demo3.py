from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Login Form")

# window size
root.geometry("500x500+0+0")

# background color
root.configure(background="#FF8C00")


bg_img = Image.open("rss1.png") 
bg_img = bg_img.resize((1920, 1080))
bg = ImageTk.PhotoImage(bg_img)

bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# image
img = Image.open("rss.png")
resize_img = img.resize((100, 70))
img = ImageTk.PhotoImage(resize_img)

img_label = Label(root, image=img, bg="#706100")
img_label.pack(pady=10)

# title text
text_label = Label(root,
                   text="Rashtriya Swayamsevak Sangh worker loginC",
                   font=('Arial', 18, 'bold'),
                   bg="#704500",
                   fg="white")
text_label.pack(pady=10)

# email label
email_label = Label(root,
                    text="Email",
                    font=('Arial', 18, 'bold'),
                    bg="#704700",
                    fg="white")
email_label.pack(pady=(20, 5))

# email entry
email_entry = Entry(root,
                    font=('Arial', 18),
                    fg="white",
                    bg="grey")
email_entry.pack(pady=(5, 10))

# password label
password_label = Label(root,
                       text="Password",
                       font=('Arial', 18, 'bold'),
                       bg="#B56D0A",
                       fg="white")
password_label.pack(pady=(20, 5))

# password entry
password_entry = Entry(root,
                       font=('Arial', 18),
                       fg="white",
                       bg="grey",
                       show="*")
password_entry.pack(pady=(5, 10))

# login button
login_btn = Button(root,
                   text="Login",
                   font=('Arial', 16, 'bold'),
                   bg="#000000",
                   fg="white")
login_btn.pack(pady=20)

root.mainloop()