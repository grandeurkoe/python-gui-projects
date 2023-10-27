from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    french_words_data = pandas.read_csv(filepath_or_buffer="data/words_to_learn.csv")
except FileNotFoundError:
    french_words_data = pandas.read_csv(filepath_or_buffer="data/french_words.csv")
else:
    pass
finally:
    french_word_list = french_words_data.to_dict(orient="records")


def pick_a_card():
    global flipping_the_card, current_card
    windows.after_cancel(flipping_the_card)
    current_card = random.choice(french_word_list)
    canvas.itemconfig(canvas_image, image=front_card_image)
    canvas.itemconfigure(tagOrId=canvas_title_text, text="French", fill="black")
    canvas.itemconfigure(tagOrId=canvas_word_text, text=current_card["French"], fill="black")
    flipping_the_card = windows.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_card_image)
    canvas.itemconfigure(tagOrId=canvas_title_text, text="English", fill="white")
    canvas.itemconfigure(tagOrId=canvas_word_text, text=current_card["English"], fill="white")


def right_card():
    french_word_list.remove(current_card)
    pick_a_card()
    words_to_learn_data = pandas.DataFrame(french_word_list)
    words_to_learn_data.to_csv(path_or_buf="data/words_to_learn.csv", index=0)


windows = Tk()
windows.title("Flash Card App")
windows.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flipping_the_card = windows.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card_image = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image((400, 263), image=front_card_image)
back_card_image = PhotoImage(file="images/card_back.png")

canvas_title_text = canvas.create_text((400, 150), text="Title", font=("Arial", 40, "italic"))
canvas_word_text = canvas.create_text((400, 263), text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, borderwidth=0, bg=BACKGROUND_COLOR, command=right_card)
right_button.grid(row=1, column=0)

wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, borderwidth=0, bg=BACKGROUND_COLOR, command=pick_a_card)
wrong_button.grid(row=1, column=1)

pick_a_card()

windows.mainloop()
