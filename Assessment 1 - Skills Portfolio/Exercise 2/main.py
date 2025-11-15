from tkinter import*
from pathlib import Path
import random

root = Tk()

root.title("Alexa Joke")

root.geometry("500x400")

txt_path = Path(__file__).with_name("randomJokes.txt") #Reads text file
with txt_path.open('r') as file:
    txt_content = file.read() #Stores text file in variable

jokes = txt_content.split('\n') #Splits text file by new line
joke = []
punchline = []

for x in jokes:
    joke_item, punch_item = x.split('?') 
    joke.append(joke_item + "?")
    punchline.append(punch_item)

item = random.randint(0, len(joke))

joke_label = Label(root, text="", font=20)
joke_label.pack(pady=25)

punchline_label = Label(root, text="", font=20)
punchline_label.pack()

buttons = Frame(root)
buttons.pack(pady=25)

joke_button = Button(buttons, text="Alexa tell me a joke", command=lambda:setup_joke(), font=40)
joke_button.pack(side=LEFT)

punchline_button = Button(buttons, text="Show punchline", command=lambda:show_punchline(), font=40)
punchline_button.pack(side=RIGHT)

next_button = Button(root, text="Next joke", command=lambda:next_joke(), font= 30)
next_button.pack()

def setup_joke():
    joke_label.config(text=joke[item])

def show_punchline():
    punchline_label.config(text=punchline[item])

def next_joke():
    global item
    item = random.randint(0, len(joke)-1)
    joke_label.config(text="")
    punchline_label.config(text="")

root.mainloop()