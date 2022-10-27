from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import json


def pass_generate():
    lett = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', ]
    numb = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symb = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '>', '<', '?']

    nr_lett = randint(6, 8)
    nr_numb = randint(2, 5)
    nr_symb = randint(2, 5)

    p_lett = [choice(lett) for _ in range(nr_lett)]
    p_num = [choice(numb) for _ in range(nr_numb)]
    p_sym = [choice(symb) for _ in range(nr_symb)]

    password_list = p_lett + p_num + p_sym
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


def pass_find():
    site = site_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data File not found, add some records first.")
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Error", message="Data File empty, add some records first.")
    else:
        if len(site) == 0:
            messagebox.showinfo(title="Error", message=" You did not give website name.")
        elif site in data:
            email = data[site]["email"]
            password = data[site]["password"]
            messagebox.showinfo(title=site, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Sorry", message=f"data for {site} does not exist.")


def data_writing(new_data):
    with open("data.json", "w") as data_file:
        return json.dump(new_data, data_file, indent=4)


def save():
    site = site_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {site: {"email": email, "password": password}}
    if len(site) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Error", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            data_writing(new_data)
        except json.decoder.JSONDecodeError:
            data_writing(new_data)
        else:
            old_email = data[site]["email"]
            old_password = data[site]["password"]
            is_ok = messagebox.askokcancel(
                title=site,
                message=f"Old details: \n Email: {old_email}\n Password: {old_password} \n\n New details entered: \n Email: {email}\n Password: {password} \n Do you wanna upload?")
            if is_ok:
                data.update(new_data)
                data_writing(data)
        finally:
            site_entry.delete(0, END)
            password_entry.delete(0, END)


# Window setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
site_entry = Entry(width=19)
site_entry.grid(row=1, column=1)
site_entry.focus()
email_entry = Entry(width=39)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "kacperbakow97@gmail.com")
password_entry = Entry(width=19)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=15, command=pass_find)
search_button.grid(row=1, column=2)
generate_password_button = Button(
    text="Generate Password", command=pass_generate)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=34, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
