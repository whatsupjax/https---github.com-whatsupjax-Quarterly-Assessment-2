import sqlite3

connect = sqlite3.connect('QUIZKEY.db')
cursor = connect.cursor()

DS3850 = cursor.execute("""create table if not exists DS3850
                        (Id INTEGER PRIMARY KEY,
                        Question varchar,
                        Answer varchar)""")

ECON3320 = cursor.execute("""create table if not exists ECON3320
                        (Id INTEGER PRIMARY KEY,
                        Question varchar,
                        Answer varchar)""")

DS3841 = cursor.execute("""create table if not exists DS3841
                        (Id INTEGER PRIMARY KEY,
                        Question varchar,
                        Answer varchar)""")

DS3865 = cursor.execute("""create table if not exists DS3865
                        (Id INTEGER PRIMARY KEY,
                        Question varchar,
                        Answer varchar)""")

FIN3210 = cursor.execute("""create table if not exists FIN3210
                        (Id INTEGER PRIMARY KEY,
                        Question varchar,
                        Answer varchar)""")

connect.commit()
connect.close()