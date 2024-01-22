import random
from tkinter import *
import pandas as pd
import random
from tkinter import messagebox
import os

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except:
    org_data = pd.read_csv("./data/french_words.csv")
    to_learn = org_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_word():
    global current_card, update_timer
    window.after_cancel(update_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{current_card['French']}", fill="black")
    canvas.itemconfig(image, image=front_img)
    update_timer = window.after(3000, func=update)


def update():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{current_card['English']}", fill="white")
    canvas.itemconfig(image, image=back_img)


def remove():
    global to_learn
    if len(to_learn) == 2:
        messagebox.showinfo(message="You've learned all the words,Congrats")
        os.remove("data/words_to_learn.csv")
        return ""
    to_learn.remove(current_card)
    to_learn_list = pd.DataFrame(to_learn)
    to_learn_list.to_csv("data/words_to_learn.csv", index=False)
    next_word()


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

update_timer = window.after(3000, func=update)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
image = canvas.create_image(400, 263, image=front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong = PhotoImage(file="./images/wrong.png")
right = PhotoImage(file="./images/right.png")

unknown_word = Button(image=wrong, highlightthickness=0, command=next_word)
unknown_word.grid(row=1, column=0)

known_word = Button(image=right, highlightthickness=0, command=remove)
known_word.grid(row=1, column=1)

next_word()

window.mainloop()
