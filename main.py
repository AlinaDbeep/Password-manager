#pip install pyperclip is needed for copying the password automatically

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_numbers+password_symbols+password_letters
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)



def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Ooops",
                            message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        if is_ok == True:
            try:
                with open("data.json", "r") as data_file:
                    #read new data
                    data = json.load(data_file)

            except FileNotFoundError:
                # add first data
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # update data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    #save updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)



def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            website = website_entry.get()
            email = email_username_entry.get()
            existing_password = data[website]["password"]
            messagebox.showinfo(title="Your password", message=f"Your password to {website} is {existing_password}\nThe email/username you used was {email}")
    except KeyError:
        messagebox.showinfo(title="Nothing Found", message="It seems like you're using this site for the first time")




window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="password_stars.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_l = Label(text="Website", bg="white")
website_l.grid(row=1, column=0)

email_username_l = Label(text="Email/Username", bg="white")
email_username_l.grid(row=2, column=0)

password_l = Label(text="Password", bg="white")
password_l.grid(row=3, column=0)

website_entry = Entry()
website_entry.grid(row=1, column=1)
website_entry.focus()

email_username_entry = Entry(width=30)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "my_dummy_email@gmail.com")

password_entry = Entry()
password_entry.grid(row=3, column=1)

search_button = Button(text="  Search  ", bd=1, bg="white", pady=0.7, command=find_password)
search_button.grid(row=1, column=2)

generate_password = Button(text="Generate", bd=1, bg="white", pady=0.7, command=generate)
generate_password.grid(row=3, column=2)


add_button = Button(text="Add", bd=1, bg="white", width=28, pady=0.7, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()


