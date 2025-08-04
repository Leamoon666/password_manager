from tkinter import *
import pyperclip
from func import save_data, generate_password, find_password


def password_button():
    random_password = generate_password()

    password_entry.delete(0, END)
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)

def search_website():
    find_password(website_entry.get())



def save():
    if save_data(website_entry.get(), email_entry.get(), password_entry.get()):
        website_entry.delete(0, END)
        password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=33)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_entry.insert(0, "example@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3, sticky="w")

generate_button = Button(text="Generate Password", command=password_button)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command=search_website)
search_button.grid(column=2, row=1)


window.mainloop()
