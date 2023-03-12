from tkinter import *
from datetime import datetime
import time

window = Tk()
window.title("TYPING TEST")
window.minsize(width=1500, height=800)
window.config(background="light blue")

test_text = Canvas(window, width=800, height=300, bg="cyan")

demo_text = "The quick brown fox jumps over the lazy dog. Did you know that this sentence contains all the letters of the English alphabet? It's a great sentence for practicing typing because it's short and easy to remember. Typing quickly and accurately is an important skill in today's digital age. Whether you're writing emails, reports, or just chatting with friends, being able to type quickly and without mistakes can save you a lot of time and hassle. So, take a deep breath, relax your fingers, and let's begin! Remember to keep your eyes on the screen, not your fingers, and try to keep a steady pace. Good luck!"
demo_text1 = "Hello World, how are you doing today? Ar kilan soler te shobta"
demo_text2 = "The rain was pouring down in sheets, drenching everything in its path. The streets were empty and silent, save for the sound of the raindrops hitting the pavement. Thunder rumbled in the distance, a low and steady growl that seemed to vibrate the very air. Lightning flashed across the sky, illuminating the darkness for a split second. A car drove by, its headlights cutting through the rain like knives. The driver looked tired and stressed, their eyes fixed on the road ahead. A few moments later, the car was gone, disappearing into the darkness. The rain continued to fall, relentless and unforgiving. It was as if the sky had opened up and was pouring out all of its fury. But even in the midst of the storm, there was a certain beauty to be found. The rain washed away the dirt and grime, leaving everything fresh and clean. It was a reminder that sometimes, even in the midst of chaos, there was still hope."

test_text.create_text(
    400, 150, font=("Arial", "15"), text=demo_text1, width=800, justify="left")

user_input = ""


def retrieve_input():
    global user_input, typing_stop

    typing_stop = datetime.now()

    user_input = input_text.get("1.0", END)

    typed_text = user_input

    demo_text_split = demo_text1.split(" ")
    user_input_split = typed_text.split(" ")

    if len(user_input_split) != len(demo_text_split):
        user_input_split.extend(
            [" "]*(len(demo_text_split) - len(user_input_split)))

    right_counter = 0
    wrong_coutner = 0

    for i in range(len(demo_text_split) - 1):

        if demo_text_split[i] != user_input_split[i]:
            wrong_coutner += 1
            # print(f"{demo_text_split[i]} and {user_input_split[i]}")
        else:
            right_counter += 1
            # print(f"{demo_text_split[i]} and {user_input_split[i]}")

    print(right_counter)
    print(wrong_coutner)
    total_seconds_typing = (typing_stop - typing_start).total_seconds()
    print(total_seconds_typing)
    print(right_counter/(total_seconds_typing/60))


def start_typing():

    global typing_start

    input_text.config(state="normal")

    typing_start = datetime.now()


input_text = Text(window, height=15,
                  width=150,
                  bg="light yellow", state="disabled")
buttonSubmit = Button(window, height=1, width=10, text="Submit",
                      command=lambda: retrieve_input())

buttonStart = Button(window, height=1, width=10, text="Start Typing",
                     command=lambda: start_typing())

spacer = Label(window, text="", padx=5, pady=5)
spacer.config(background="light blue")
spacer.pack()


test_text.pack()

spacer = Label(window, text="", padx=10, pady=10)
spacer.config(background="light blue")
spacer.pack()

buttonStart.pack()

spacer = Label(window, text="", padx=5, pady=5)
spacer.config(background="light blue")
spacer.pack()

input_text.pack()

spacer = Label(window, text="", padx=5, pady=5)
spacer.config(background="light blue")
spacer.pack()

buttonSubmit.pack()


# buttonShow.pack()
window.mainloop()
