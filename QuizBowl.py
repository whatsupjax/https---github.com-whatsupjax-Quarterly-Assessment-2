import sqlite3
import random

green = '\033[38;2;0;225;0m'
red = '\033[38;2;225;0;0m'
white = '\033[38;2;225;225;225m'

connection = sqlite3.connect('QUIZKEY.db')
cursor = connection.cursor()
cursor.execute('SELECT * FROM DS3850')
print(cursor.fetchall())

def returnQuestions():
    cursor.execute('SELECT * FROM DS3850')
    cursor.execute('SELECT * FROM ECON3320')
    cursor.execute('SELECT * FROM DS3841')
    cursor.execute('SELECT * FROM DS3865')
    cursor.execute('SELECT * FROM FIN3210')
    return cursor.fetchall()

questionBank = returnQuestions()

random.shuffle(questionBank)

correct = 0
incorrect = 0

print('Lets start the game.')

for row in questionBank:
    question = row[1]
    answer = row[2]

    print(question)
    userAnswer = input('ANSWER: ')

    if userAnswer.lower() == answer.lower():
        print('That is ', green + 'correct!')
        print(white)
        correct += 1

    else:
        print('That is ', red + 'incorrect!')
        print(white)
        incorrect += 1

print('Final results:', green + str(correct), white, "/", red + str(incorrect), white)

connection.commit()
connection.close()
