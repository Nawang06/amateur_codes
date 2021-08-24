from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_input.delete(0, "end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(symbols) for char in range(randint(8, 10))]
    password_list += [choice(letters) for letter in range(randint(2, 4))]
    password_list += [choice(numbers) for num in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Empty Fields", message="There are empty field/s. Please do fill them!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nUsername/Email: "
                                                              f"{username}\nPassword: {password}\n"
                                                              f"Do You Want To Save? ")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {username} | {password}\n")
            website_input.delete(0, "end")
            # username_input.delete(0, "end")
            password_input.delete(0, "end")
            messagebox.showinfo(title="Success", message="Information Saved")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=60, width=400, height=400)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ", font=(FONT_NAME, 10, "bold"))
website_label.grid(column=0, row=1)
website_input = Entry(width=35, borderwidth=1)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")

username_label = Label(text="Email/Username: ", font=(FONT_NAME, 10, "bold"))
username_label.grid(column=0, row=2)
username_input = Entry(width=35, borderwidth=1)
username_input.insert(0, "abc09@gmail.com")
username_input.grid(column=1, row=2, columnspan=2, sticky="EW")

password_label = Label(text="Password: ", font=(FONT_NAME, 10, "bold"))
password_label.grid(column=0, row=3)
password_input = Entry(width=21, borderwidth=1)
password_input.grid(column=1, row=3, sticky="EW")

generate_button = Button(text="Generate Password", borderwidth=1, command=generate_password)
generate_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", borderwidth=1, width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
