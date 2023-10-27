import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT_NAME = "Arial"
BG_COLOR = "#2B2730"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_entry.delete(0, END)
    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    emails = email_entry.get()
    passwords = password_entry.get()
    user_dict = {
        website: {
            "Email": emails,
            "Password": passwords,
        }
    }

    if website == "" or passwords == "" or emails == "":
        messagebox.showwarning(title="Oops!", message="Please make sure you haven't left any fields empty!")
    else:
        try:
            with open("password_cache.json", mode="r") as pass_file:
                # Reading and storing old data from "Password Cache.json" into update_data.
                update_data = json.load(pass_file)
                # Adding the new data entered by the user to update_data.
                update_data.update(user_dict)
        except FileNotFoundError:
            with open("password_cache.json", mode="w") as pass_file:
                json.dump(user_dict, pass_file, indent=4)
        else:
            with open("password_cache.json", mode="w") as pass_file:
                # Storing the new update_data to "Password Cache.json"
                json.dump(update_data, pass_file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(0, "mailme.Meowya@proton.me")
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    search_query = website_entry.get()
    try:
        with open("password_cache.json", mode="r") as search_file:
            search_data = json.load(search_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found.")
    else:
        if search_query in search_data.keys():
            messagebox.showinfo(title=f"{search_query}",
                                message=f"Email: {search_data[search_query]['Email']}\nPassword: {search_data[search_query]['Password']}")
        else:
            messagebox.showwarning(title="Error", message=f"No detail for {search_query} website exists.")


# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Password Manager")
windows.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
pass_manager_img = PhotoImage(file="logo.png")
canvas.create_image((100, 100), image=pass_manager_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=(FONT_NAME, 10, "bold italic"))
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, sticky="EW", pady=5)

search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2, sticky="EW", padx=3, pady=5)

email_label = Label(text="Email/Username:", font=(FONT_NAME, 10, "bold italic"))
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.insert(0, "mailme.Meowya@proton.me")
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW", pady=5)

password_label = Label(text="Password:", font=(FONT_NAME, 10, "bold italic"))
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, padx=3, pady=5)

add_password_button = Button(text="Add", width=36, command=save)
add_password_button.grid(row=4, column=1, columnspan=2, sticky="EW")

windows.mainloop()
