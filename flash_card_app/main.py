from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"


# Data conversion and usage using Pandas

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    word_dict = data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records")
    current_card = {}


# Picking Random Word from the dictionary (converted from the pandas dataframe)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_dict)
    random_word_f = current_card["French"]
    canvas.itemconfig(canvas_text_2, text=random_word_f, fill="black")
    canvas.itemconfig(canvas_text_1, text="French", fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, flip_card)


# If user doesn't know the word

def is_known():
    word_dict.remove(current_card)
    next_card()
    new_data = pandas.DataFrame(word_dict)
    new_data.to_csv("./data/words_to_learn.csv", index=False)

# Flipping Of Card


def flip_card():
    canvas.itemconfig(canvas_text_1, text="English", fill="white")
    canvas.itemconfig(canvas_text_2, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)

# Basic UI of the Application


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 260, image=card_front)
canvas_text_1 = canvas.create_text(400, 150, font=(FONT_NAME, 40, "italic"))
canvas_text_2 = canvas.create_text(400, 263, font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
cross_button = Button(image=wrong_img, relief="flat", bg=BACKGROUND_COLOR, command=next_card)
cross_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, relief="flat", bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()

