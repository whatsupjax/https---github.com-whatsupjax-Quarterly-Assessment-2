import sqlite3

connect = sqlite3.connect('QUIZKEY.db')
cursor = connect.cursor()

DS3850 = [
    ('1', 'What time does DS3850-500 begin?', '9:00 AM'),
    ('2', 'Who is the professor?', 'Dr. Clary'),
    ('3', 'How many exams does this course have?', 'Four'),
    ('4', 'Is this class in a computer lab?', 'Yes'),
    ('5', 'What is the primary programming language used?', 'Python'),
    ('6', 'What code editor is used in class?', 'Visual Studio'),
    ('7', 'Is SQL a programming language?', 'No'),
    ('8', 'Do I need to pass this course?', 'Absolutly'),
    ('9', 'I enjoy this course.', 'True'),
    ('10', 'Is this a prerequisite?', 'Yes'),
]

ECON3320 = [
    ('1', 'How confusing is this class?', 'Money is confusing'),
    ('2', 'What is money?', 'An item that is accepted as payment.'),
    ('3', 'What is bartering?', 'Trading'),
    ('4', 'What problem did money fix in bartering?', 'Double Coincidence of Wants'),
    ('5', 'Money is divisible.', 'True'),
    ('6', 'What is Monetary Policy set by?', 'Federal Reserve Bank'),
    ('7', 'Medium of Exchange.', 'Characteristic of money'),
    ('8', 'Unit of Account.', 'Characteristic of money'),
    ('9', 'Store of Value.', 'Characteristic of money'),
    ('10', 'Standard of Defered Payment.', 'Characteristic of money'),]

DS3841 = [
    ('1', 'Computer.', 'Hardware'),
    ('2', 'Program', 'Software'),
    ('3', 'Information', 'Data'),
    ('4', 'People', 'User'),
    ('5', 'GPU', 'Graphics Processing Unit'),
    ('6', 'OS', 'Operating System'),
    ('7', 'LAN', 'Local Area Network'),
    ('8', 'HDD', 'Hard Disk Drive'),
    ('9', 'SSD', 'Solid State Drive'),
    ('10', 'Taking in information is called?', 'Input'),
]

DS3865 = [
    ('1', 'Right Join', 'Type of join'),
    ('2', 'Left Join', 'Type of join'),
    ('3', 'Do you normalize database tables?', 'Yes'),
    ('4', 'Is SQL a programming language?', 'Yes'),
    ('5', 'Commonly used notation.', "Crow's Foot Notation"),
    ('6', 'What is a primary key?', 'A unique identifier'),
    ('7', 'A weak entity can exist on its own.', 'False'),
    ('8', 'How many exams does this class have?', '3'),
    ('9', 'What is the primary SQL editor?', 'MySQL'),
    ('10', '_____ is the primary SQL editor.', 'SSMS'),
]

FIN3210 = [
    ('1', 'Number of Periods', 'N'),
    ('2', 'Interest Rate', 'I/Y'),
    ('3', 'Payment', 'PMT'),
    ('4', 'Present Value', 'PV'),
    ('5', 'Future Value', 'FV'),
    ('6', 'Net Present Value', 'NPV'),
    ('7', 'What time does this class start?', '2:30 PM'),
    ('8', 'Are taxes taught in this class?', 'Yes'),
    ('9', 'Are finacial reports taught in class?', 'Yes'),
    ('10', 'Who teaches this class?', 'Matthew Hall'),
]

for value in DS3850:
    cursor.execute("""INSERT INTO DS3850 (Id, Question, Answer) VALUES (?, ?, ?)""", value)

for value in ECON3320:
    cursor.execute("""INSERT INTO ECON3320 (Id, Question, Answer) VALUES (?, ?, ?)""", value)

for value in DS3841:
    cursor.execute("""INSERT INTO DS3841 (Id, Question, Answer) VALUES (?, ?, ?)""", value)

for value in DS3865:
    cursor.execute("""INSERT INTO DS3865 (Id, Question, Answer) VALUES (?, ?, ?)""", value)

for value in FIN3210:
    cursor.execute("""INSERT INTO FIN3210 (Id, Question, Answer) VALUES (?, ?, ?)""", value)

connect.commit()
connect.close()