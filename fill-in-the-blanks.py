# coding: utf-8
print "welcome to kids Genral quiz"
"""
a quiz where you are asked to select from three difficulty levels, with each level
"""
level = None
blanks = ['__1___','__2___', '__3___', '__4___']
"""
The program is required to have 4 blanks .
All paragraph 4 main blanks, I ask the user input until all of the blanks are filled.
"""
quistions_easy = 'What color is the sky __1___ ,The color of the sun __2___ Color Clouds __3___ Moon color __4___'
answers_easy = ['blue','yellow','white','gray']
"""
 The levels of the quiz are given below:
 This is the easy fill in the blank quiz, questions and answers.
"""
quistions_medium = ' What color fruit bananas __1___ fruit orange __2___ fruit tomato __3___ fruit Lemon __4___'
answers_medium = ['yellow','orange','red','yellow']
"""
 This is the medium fill in the blank quiz, questions and answers.
"""
quistions_hard = 'What are milk products __1___ and __2___ and __3___ and __4___'
answers_hard = ['milk','yogurt','cream','butter']
"""
This is the hard fill in the blank quiz, questions and answers.
"""

"""
This will ask the user to chose a level:easy,medium,or hard.
"""
while level not in ['easy', 'medium', 'hard']:
    level = raw_input ('Please select a difficulty (easy, medium, or hard): ').lower()



def replace(old,new,text):
    """
    Behavior replaces with correct answers
    input:text
    output:return new (correct answers)
    """
    return text.replace(old,new)

def chooseLevel(level):
    """
    Behavior Player selects level of quiz
    the level choice function takes as input the
    raw_input from the user and return as output according to the game difficlty.
    """
    if level == "easy":
        return quistions_easy, answers_easy
    elif level =="medium":
        return quistions_medium,answers_medium
    else:
        return quistions_hard,answers_hard

def quiz():
    """
    Asks user for answer, if correct moves to next question if wrong Incorrect
    This method ask gamer for answers to fill the blank , when answer the
    question it will be move to the next question.
    Input : answers in blank.
    output:if the answers correct or not.
    Return : new question.
    """
    question,answers=chooseLevel(level)
    print question
    blank_number =0
    length = len(answers)
    question.replace(blanks[blank_number],answers[blank_number])
    while blank_number < length:
        user_answer=raw_input("fill the blank"+blanks[blank_number])
        if user_answer == answers[blank_number]:
            question = question.replace(blanks[blank_number],answers[blank_number])
            print ("Correct \n" + question.replace(blanks[blank_number],answers[blank_number]) )
            blank_number += 1
        else:
            print "Incorrect"
quiz()
print ('Congratulations')
