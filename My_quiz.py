#This program is a program that proses a quiz and allows the user to answer
questions = ("what is the capital of New Zealand?",
             "what is the capital of Colombia?",
             "what is the capital of Malaysia?",
             "what is the capital of Turkey?",
             "what is the capital of India?")

options = (("A. Wellington", "B. Christchurch", "C. Queenstwon", "D. Auckland", "E. Rotorua"),
           ("A. Medellín", "B. Santa Marta", "C. Bogotá", "D. Cartagena", "E. Barranquilla"),
           ("A. George Town", "B. Malacca", "C. Kuala Terengganu", "D. Ipoh", "E. Kulara Lumpur"),
           ("A. Istanbul", "B. Ankara", "C. Izmir", "D. Bursa", "E. Antalya"),
           ("A. Mumbai", "B. Kolkata", "C. jaipur", "D. New Delhi", "E. Bengaluru"))

answers = ("A", "C", "E", "B", "D")
guesses = []
score = 0
question_num = 0
name = str()
age = int()
from easygui import*


def user_details():
    name = enterbox("enter your name : ")
    if name == "":
        msgbox("name can not be blank")
    else:
        msgbox("fill the next field")
    age = enterbox("enter your age : ")
    if age == "":
        msgbox("you must fill this field")
    else:
        msgbox("thank you for entering your details")
        ready_yet()
        
def ready_yet():
    quiz = enterbox("are you ready to start quiz? press Y or N : ").upper()
    if quiz == ["Y", "Yes", "y", "yes"]:
        msgbox("Now answer as many questions as you can")
        quiz_start()
    else:
        msgbox("see you next time")

def quiz_start():
    answers = ("A", "C", "E", "B", "D")
    guesses = []
    score = 0
    question_num = 0
    for question in questions:
        msgbox(question)
        for option in options[question_num]:
            msgbox(option)

        guess = enterbox("enter A,B,C,D,E ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            msgbox("Correct")

        else:
            msgbox("Incorrect" f" {answers[question_num]} is the correct answer")
        question_num += 1

    msgbox("your results")

    print("answer: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    print("guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int(score / len (question) * 585)
    msgbox(f"your score is: {score}% congrats {name}!" )
    quiz = enterbox("do you want to do quiz again? press Y or N : ").upper()
    if quiz == ["Y", "Yes", "y", "yes"]:
        quiz_start()
    else:
        msgbox("see you next time")

user_details()