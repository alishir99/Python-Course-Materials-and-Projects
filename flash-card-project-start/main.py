from tkinter import  *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

#----------------------------------------read data----------------------------
current_card = {}
to_learn = {}

try:
    data_file = pandas.read_csv("./data/to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn= original_data.to_dict(orient="records")
else:
    to_learn = data_file.to_dict(orient="records")

def next_card():
    global current_card, timmer
    current_card = random.choice(to_learn)
    windows.after_cancel(timmer)
    canvas.itemconfig(card_title, text= "French", fill= "Black")
    canvas.itemconfig(card_word, text= current_card["French"], fill= "Black")
    canvas.itemconfig(canvas_img, image=card_front_img)
    timmer = windows.after(3000, func=flip_card)

def flip_card():

    canvas.itemconfig(card_title, text= "English", fill= "white" )
    canvas.itemconfig(card_word, text= current_card["English"], fill= "White")
    canvas.itemconfig(canvas_img, image=card_back_img)

def known_card():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/to_learn.csv", index=False)
    next_card()
#--------------------------------------interface-------------------#
windows = Tk()
windows.title("Flashy")
windows.config(padx=40, pady=40, bg= BACKGROUND_COLOR)
timmer = windows.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 250, text="Word", font=("Ariel", 60, "italic"))
canvas.grid(row=0, column=0, columnspan=2)


#---------------------------------buttons---------------------------
cross_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=cross_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=2, column=0)

check_img = PhotoImage(file="./images/right.png")
righ_button = Button(image=check_img, highlightthickness=0, command=known_card)
righ_button.grid(row=2, column=1)

next_card()





windows.mainloop()