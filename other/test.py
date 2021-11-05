from random import randint as rand
from datetime import datetime
from time import sleep as pause

file = open('test.csv', 'w')

while True:
    to_write = "{date} | {output}\n".format(date = datetime.now().strftime("%d/%m/%Y %H:%M:%S"), output = rand(0,20))
    file.write(to_write)

