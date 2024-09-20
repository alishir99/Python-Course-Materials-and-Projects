from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
from random import choice, randint, shuffle
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = [choice(letters) for _ in range(randint(8, 10))]\
                    +[choice(symbols) for _ in range(randint(2, 5))] \
                    + [choice(symbols) for _ in range(randint(2,5))]
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_name.get()
    email = email_or_username.get()
    password = password_input.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }
    if len(website)== 0 or len(password)==0 or len(email)==0:
        messagebox.showinfo(title="Opps", message="Make sure you have't left any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                #Saving updated data
                json.dump(new_data,file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
                web_name.delete(0, END)
                email_or_username.delete(0, END)
                password_input.delete(0,END)
                lazy()

#----------------------------search for details -----------------------#

def find_password():
    search_for=web_name.get()
    try:
        with open ("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found.")
    else:
        if search_for in data:
            messagebox.showinfo(title=search_for, message=f"Email: {data[search_for]['email']}\nPassword: {data[search_for]['password']}")
        else:
            messagebox.showinfo(title="Opps", message="The file doesn't exist")

# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Password Manager")
windows.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = image)
canvas.grid(row=0, column=1)

#labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
user_name_label = Label(text="Email/Username:")
user_name_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


#Entery

web_name = Entry(width=36)
web_name.grid(row=1, column=1)

email_or_username = Entry(width=55)
email_or_username.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=36)
password_input.grid(row=3, column=1)


#Buttons
generate_button = Button(text="Generate Password", command= generate)
generate_button.grid(row=3, column=2)

add_button = Button(width=46, text= "Add", command= save)
add_button.grid(row=4, column=1, columnspan=3)

search_button = Button(text="Search", width=14, command= find_password)
search_button.grid(row=1, column=2)


def lazy():
    web_name.focus()
    email_or_username.insert(0, "alishirzad444@gmail.com")

lazy()


windows.mainloop()