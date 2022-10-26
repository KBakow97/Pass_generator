from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
from win32api import GetSystemMetrics


def pass_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(6, 8)
    nr_numbers = randint(2, 5)
    nr_symbols = randint(2, 5)

    p_lett = [choice(letters) for _ in range(nr_letters)]
    p_num = [choice(numbers) for _ in range(nr_numbers)]
    p_sym = [choice(symbols) for _ in range(nr_symbols)]

    password_list = p_lett + p_num + p_sym
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


def save():
    site = site_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(site) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Error", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(
            title=site, message=f"These are the detail entered: \n Email: {email}\n Password: {password} \n Do you wanna save this?")

        if is_ok:
            with open("data.txt", 'a') as fi:
                print(f"{site} | {email} | {password}", file=fi)
                site_entry.delete(0, END)
                password_entry.delete(0, END)


# Window setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
width = GetSystemMetrics(0)//4
height = GetSystemMetrics(1)//3
x = (width*1.5)
y = (height)
window.geometry('%dx%d+%d+%d' % (width, height, x, y))


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
site_entry = Entry(width=39)
site_entry.grid(row=1, column=1, columnspan=2)
site_entry.focus()
email_entry = Entry(width=39)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "kacperbakow97@gmail.com")
password_entry = Entry(width=19)
password_entry.grid(row=3, column=1)

# Buttons

generate_password_button = Button(
    text="Generate Password", command=pass_generate)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=34, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
