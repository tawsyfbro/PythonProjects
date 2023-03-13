from tkinter import *
from datetime import datetime
import time
import random

window = Tk()
window.title("TYPING TEST")
window.minsize(width=1500, height=1200)
window.config(background="light blue")

test_text = Canvas(window, width=800, height=300, bg="cyan")

list_of_texts = ["The quick brown fox jumps over the lazy dog. Did you know that this sentence contains all the letters of the English alphabet? It's a great sentence for practicing typing because it's short and easy to remember. Typing quickly and accurately is an important skill in today's digital age. Whether you're writing emails, reports, or just chatting with friends, being able to type quickly and without mistakes can save you a lot of time and hassle. So, take a deep breath, relax your fingers, and let's begin! Remember to keep your eyes on the screen, not your fingers, and try to keep a steady pace. Good luck!",
                 "The rain was pouring down in sheets, drenching everything in its path. The streets were empty and silent, save for the sound of the raindrops hitting the pavement. Thunder rumbled in the distance, a low and steady growl that seemed to vibrate the very air. Lightning flashed across the sky, illuminating the darkness for a split second. A car drove by, its headlights cutting through the rain like knives. The driver looked tired and stressed, their eyes fixed on the road ahead. A few moments later, the car was gone, disappearing into the darkness. The rain continued to fall, relentless and unforgiving. It was as if the sky had opened up and was pouring out all of its fury. But even in the midst of the storm, there was a certain beauty to be found. The rain washed away the dirt and grime, leaving everything fresh and clean. It was a reminder that sometimes, even in the midst of chaos, there was still hope.",
                 "The sun was setting over the horizon, casting a warm golden glow across the sky. The birds were flying back to their nests, chirping happily as they went. The trees rustled softly in the gentle breeze, and the leaves shimmered in the fading light. A few clouds drifted lazily across the sky, painting the sky with shades of pink and purple. The air was filled with the scent of flowers and freshly-cut grass. As the darkness crept in, the stars began to twinkle in the sky, one by one. The night was peaceful and calm, and it was the perfect time to reflect on the day. I felt grateful for everything I had experienced and for everyone who had been a part of my life.",
                 "The waves crashed against the shore, sending sprays of salty water into the air. The seagulls circled overhead, calling out to each other. The sand was warm under my feet, and I felt the sun beating down on my skin. I closed my eyes and took a deep breath, savoring the salty ocean air. The beach was crowded with people of all ages, playing in the water, building sandcastles, or simply lounging on towels. Children were laughing and running around, their parents watching over them. The sound of music drifted over from a nearby beach bar, adding to the festive atmosphere. I smiled to myself, feeling grateful for this moment of relaxation.",
                 "The city was bustling with activity, the streets filled with cars and pedestrians. The buildings towered overhead, their windows reflecting the bright sunlight. The sound of car horns and chatter filled the air, creating a chaotic symphony of sound. I walked down the street, dodging people and trying to keep pace with the crowd. The smell of coffee and pastries wafted over from a nearby cafe, making my stomach growl. I stopped for a moment to watch a street performer juggling flaming torches, eliciting cheers from the crowd. Despite the chaos, I felt energized and alive, grateful to be a part of this vibrant city.",
                 "The mountains rose majestically in the distance, their peaks shrouded in clouds. The air was crisp and cool, and I could feel the breeze blowing through my hair. The trees were a riot of colors, their leaves turning bright shades of orange, red, and yellow. I took a deep breath, savoring the scent of pine and earth. A nearby stream babbled softly, adding to the peaceful atmosphere. I hiked through the woods, enjoying the quiet solitude of nature. It was a beautiful day, and I felt grateful for the opportunity to experience this stunning landscape.",
                 "The stadium was filled with cheering fans, their voices echoing through the air. The players ran across the field, their movements quick and precise. The ball bounced back and forth, the tension building with each pass. The sun beat down on the field, making the players sweat. The referee blew his whistle, and the game began anew. The score was tied, and everyone was on the edge of their seats. I cheered along with the crowd, feeling the excitement and energy of the moment. It was a thrilling game, and I felt grateful to be a part of it.",
                 "The library was quiet and peaceful, the shelves lined with books. The smell of paper and ink filled the air, making me feel right at home. I browsed the shelves, running my fingers over the spines of the books. There were books on every topic imaginable, from history to science to fiction. I settled into a comfortable chair and opened a book, getting lost in the story. The only sounds were the rustling of pages and the occasional cough or whisper. Time seemed to stand still as I read, and I felt grateful for the escape that books provided. When I finished the book, I returned it to its place on the shelf, feeling a sense of satisfaction. The library was a treasure trove of knowledge and stories, and I was grateful to have access to it.",
                 "The market was a riot of color and noise, the stalls overflowing with fruits, vegetables, and other goods. Vendors shouted out their prices and offerings, trying to attract customers. The smell of spices and herbs wafted over from a nearby stall, making my mouth water. I sampled some fruit, savoring the sweetness of the ripe mango. I haggled with a vendor over the price of a necklace, feeling a sense of satisfaction when I got a good deal. The market was a bustling hub of activity, and I felt grateful for the opportunity to experience it.",
                 "The park was filled with families and friends, enjoying the sunshine and fresh air. Children ran around, playing tag and chasing each other. Couples walked hand in hand, enjoying the peaceful atmosphere. A group of friends played frisbee, their laughter echoing through the park. The sound of a nearby fountain added to the serene ambiance. I sat on a bench, watching the people go by and feeling grateful for this moment of relaxation.",
                 "The museum was a treasure trove of art and history, the walls adorned with masterpieces and artifacts. I wandered through the galleries, admiring the beauty and skill of the artists. There were paintings, sculptures, and installations from all eras and genres. I learned about history and culture, gaining a deeper appreciation for the world around me. The museum was a sanctuary of knowledge and inspiration, and I felt grateful to have access to it.",
                 "The cafe was cozy and inviting, the smell of coffee and pastries filling the air. The chatter of customers and the sound of soft music created a warm and welcoming atmosphere. I ordered a cappuccino and a croissant, enjoying the indulgence. I sat at a table, watching the people go by and feeling the stress of the day melt away. The cafe was a sanctuary of comfort and relaxation, and I felt grateful for the opportunity to unwind."]

chosen_text = random.choice(list_of_texts)

test_text.create_text(
    400, 150, font=("Arial", "15"), text=chosen_text, width=800, justify="left")

user_input = ""


def retrieve_input():
    global user_input, typing_stop, right_words, wrong_words, typing_speed

    typing_stop = datetime.now()

    user_input = input_text.get("1.0", END)

    typed_text = user_input

    demo_text_split = chosen_text.split(" ")
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

    right_words = right_counter

    wrong_words = wrong_coutner
    total_seconds_typing = (typing_stop - typing_start).total_seconds()
    print(total_seconds_typing)

    typing_speed = right_counter/(total_seconds_typing/60)

    result_text = Label(
        window, text=f"You typed {right_words} correctly, and {wrong_words} incorrectly. \n Your typing speed is {typing_speed} wpm!", padx=5, pady=5)
    result_text.config(background="light blue", font=("Arial", "20"))
    result_text.pack()


def start_typing():

    global typing_start

    input_text.config(state="normal")

    typing_start = datetime.now()


heading_text = Label(window, text="THE TYPING SPEED TEST", padx=5, pady=5)
heading_text.config(background="light blue", font=("Arial", "35"))
heading_text.pack()

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


window.mainloop()

