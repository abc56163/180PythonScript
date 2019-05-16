import MySQLdb
import os

db = MySQLdb.connect("localhost", "root", "Abcd520025@", "58dh", charset='utf8')

cursor = db.cursor()


with open(os.path.dirname(__file__)+'/1.txt', 'r') as text:
    new_text = text.read()

for t in new_text.split():
    text_list = []
    for x in t.split(','):
        text_list.append(x)
        try:
            cursor.execute('INSERT INTO `58_robot_2` (`id`, `keyword`, `description`) '
                           'VALUES ("{}", "{}" , "{}");'.format(int(text_list[0]), text_list[1], text_list[2]))
            db.commit()
        except:
            db.rollback()

