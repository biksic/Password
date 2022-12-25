from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters)for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols)for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers)for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_pass.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = entry_web.get()
    email = entry_email.get()
    password = entry_pass.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")

    else:
        try:
            with open("data.json", "r") as data_file:
                #reading
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        except json.decoder.JSONDecodeError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #updating
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            entry_web.delete(0, END)
            entry_pass.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = entry_web.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}\n")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label_web = Label(text="Website:")
label_web.grid(row=1, column=0)

entry_web = Entry(width=21)
entry_web.grid(row=1, column=1, sticky="EW")
entry_web.focus()

button_web = Button(text="Search", width=15, command=find_password)
button_web.grid(row=1, column=2, sticky="EW")

label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)

entry_email = Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2, sticky="EW")
entry_email.insert(END, "darko.tomljanovic@gmail.com")

label_pass = Label(text="Password:")
label_pass.grid(row=3, column=0)

entry_pass = Entry(width=21)
entry_pass.grid(row=3, column=1,sticky="EW")

button_pass = Button(text="Generate Password", width=15, command=generate_password)
button_pass.grid(row=3, column=2,sticky="EW")

button_add = Button(text="Add", width=36, command=save)
button_add.grid(row=4, column=1,columnspan=2, sticky="EW")





window.mainloop()