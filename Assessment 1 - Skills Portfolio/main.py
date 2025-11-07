from tkinter import *
import random


root = Tk()

root.title("Math Quiz")

root.geometry("500x400")

def clear_screen(): #Function to clear widgets and wipe screen
    for widget in root.winfo_children():
        widget.destroy()

Big = ("Helvetica", 30, "bold")
Mid = ("Helvetica", 20)

selected_lvl = "" 
score = 0
attempts = 0



def title_screen(): #Function to show title screen
    clear_screen()

    title = Label(root, text="Math Quiz!!!", font=Big) #Title text
    title.pack()

    lvl_frame = Frame(root) #Group for buttons
    lvl_frame.pack(pady=50)

    lvl_1 = Button(lvl_frame, text="Easy", font=Mid, bg="#7DDA58", width=20, command=lambda:quiz("lvl1")) #Button for easy difficulty
    lvl_1.pack(fill=X) #Fills entire width of frame

    lvl_2 = Button(lvl_frame, text="Intermediate", font=Mid, bg="yellow", command=lambda:quiz("lvl2")) #Button for medium difficulty
    lvl_2.pack(fill=X)

    lvl_3 = Button(lvl_frame, text="Advanced", font=Mid, bg="#FF552A", command=lambda:quiz("lvl3")) #Button for hard difficulty
    lvl_3.pack(fill=X)

def quiz(lvl): #Function to show quiz
    clear_screen()
    global selected_lvl #Avoids accidentally using variable locally
    global question_num
    global score

    selected_lvl = lvl #Sets current level to button user selected
    score = 0 #Resets score
    
    lvl_text = { #Sets text to difficulty
        "lvl1": "Easy", "lvl2": "Intermediate", "lvl3": "Advanced"
    }
    question_num = 0 #Resets question number
    
    lvl_label = Label(root, text=lvl_text[selected_lvl], font=Big)
    lvl_label.pack(pady=20)

    global question_label 
    question_label = Label(root, text="", font=Mid)
    question_label.pack()

    global user_entry
    user_entry = Entry(root, font=Mid, justify="center")
    user_entry.pack(pady=20)
    user_entry.bind("<Return>", check_ans)

    global score_label
    score_label = Label(root, text="Score:", font=Mid)
    score_label.pack()

    global attempts_label
    attempts_label = Label(root, text="", font=Mid)
    attempts_label.pack(pady=10)

    menu_button = Button(root, text="Main Menu", font=Mid, bg="lightblue", command=lambda:title_screen())
    menu_button.pack(pady=10)

    update_question()

def update_question(): #Function to update question information
    global question #Variable to store question
    global answer #Variable to store answer
    global attempts #Variable to store number of attempts
    global question_num #Variable to store index of question 
    global attempts_label
    global point_gain #Variable to store number of points gained
    global user_entry 

    attempts = 3 #Sets amount of attempts to 3
    point_gain = 3 #Sets amount of points gained per correct answer
    questions = { #Stores random arithmetic questions in a dictionary
            "lvl1": [ (f"{a} {oper} {b}", eval(f"{a} {oper} {b}")) for x in range(10) #Generates 10 questions and answers in a key as variables, for each difficulty
                        for a in [random.randint(1, 9)] #Randomizes single digit first number
                        for b in [random.randint(1, 9)] #Randomizes single digit second number
                        for oper in [random.choice(['+', '-'])] #Randomizes operator
                ],
            "lvl2": [ (f"{a} {oper} {b}", eval(f"{a} {oper} {b}")) for x in range(10) 
                        for a in [random.randint(10, 99)] #Randomizes double digit first number
                        for b in [random.randint(10, 99)] #Randomizes double digit first number
                        for oper in [random.choice(['+', '-'])] 
                ],
            "lvl3": [ (f"{a} {oper} {b}", eval(f"{a} {oper} {b}")) for x in range(10) 
                        for a in [random.randint(100, 999)] #Randomizes triple digit first number
                        for b in [random.randint(100, 999)] #Randomizes triple digit first number
                        for oper in [random.choice(['+', '-'])] 
                ]
        }
    if question_num > 9: #Check if there are no more questions
        end_screen() #Show results
        return()
    question, answer = questions[selected_lvl][question_num] #Stores a single question and answer of selected difficulty in variables
    question_label.config(text=question) #Displays question
    attempts_label.config(text="") #Clears attempts text
    

def check_ans(event): #Checks if user answer is correct
    global score
    global attempts
    global question_num
    global attempts_label
    global point_gain
    global user_entry
           
    user_ans = user_entry.get() #Stores user input into variable
    try:
        
        if int(user_ans) == answer: #Adds score if user is correct
            score += point_gain
            attempts_label.config(text=(f"+ {point_gain} Points!"), fg="green")
        else: #Reduces attempts and points gained if user is wrong
            attempts -= 1
            point_gain -= 1

            if attempts == 1: #Changes grammar to fit number of attempts
                attempts_label.config(text=(f"WRONGGGG!!!! {attempts} attempt left!"), fg="red")
            else:
                attempts_label.config(text=(f"WRONGGGG!!!! {attempts} attempts left!"), fg="red")

            user_entry.delete(0, "end") #Clears user entry

            if attempts < 1: #Loads nexts question if user is out of attempts
                attempts_label.config(text=(f"Too bad, the answer was {answer}")) #Displays correct answer
                user_entry.delete(0, "end") #Clears user entry
                question_num+=1
                root.after(600, update_question) #Delays screen change
            return
        
    except ValueError: #Checks if user input is valid
        attempts_label.config(text="Please enter a number.", fg="red")
        user_entry.delete(0, "end")
        return

    score_label.config(text=(f"Score: {score}")) #Displays score
        
    question_num += 1 #Selects the next question to load
    user_entry.delete(0, "end") #Clears user entry
    root.after(600, update_question) #Delays screen change

def end_screen(): #Function to show results
    clear_screen()

    score_label = Label(root, text=(f"Score: {score}"), font=Big)
    score_label.pack(pady=50)

    comment_label = Label(root,text="", font=Big)
    comment_label.pack()

    if score == 30:
        comment_label.config(text="Perfect! Great job!")
    elif score < 30 and score > 15:
        comment_label.config(text="Could be worse!")
    elif score == 0:
        comment_label.config(text="You CANNOT be worse!!", fg="red")
    else:
        comment_label.config(text="You are BUNS!!!")

    menu_button = Button(root, text="Main Menu", font=Mid, bg="lightblue", command=lambda:title_screen()) #Button to go back to title screen
    menu_button.pack(pady=30)


title_screen() #Loads title screen

root.mainloop()

