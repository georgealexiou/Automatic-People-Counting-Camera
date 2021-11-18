import os.path
from datetime import datetime
from random import randint as rand
from datetime import datetime
import csv

'''
file_exists
Checks if the file for the current date exists in the database

:returns: boolean (does file exist)
'''
def file_exists(date):
    if (os.path.isfile('data/{}.csv'.format(date))):
        return True
    else:
        return False

'''
save
Writes population to csv file

:param count: amount of people in the space (int)
'''
def save(count):
    date = datetime.now().strftime('%d_%m_%Y')
    time = datetime.now().strftime('%H:%M:%S')

    #! need to figure out a device id
    if file_exists(date):
        with open('data/{}.csv'.format(date), mode='a', newline='') as f:
            csv.writer(f).writerow([time, 'mbp', count])
            f.close()
    else:
        with open('data/{}.csv'.format(date), mode='w', newline='') as f:
            csv.writer(f).writerow([time, 'mbp', count])
            f.close()

'''
dummy
Creates dummy data (UNUSED)
'''
def dummy():
    file = open('test.csv', 'w')

    while True:
        to_write = "{date},{output}\n".format(date = datetime.now().strftime("%d/%m/%Y %H:%M:%S"), output = rand(0,20))
        file.write(to_write)

'''
get_date_data
Returns data for a given date

:param date: date that we wish to look for
:return: String of data in the csv file for :param date:
'''
def get_date_data(date):
    date = datetime.now().strftime('%d_%m_%Y')
    if file_exists(date):
        file = open('data/{date}.csv'.format(date=date))
        str = file.read()
        file.close()
        return str
        
    else:
        return 'The data that you have requested is unavailable'

for i in range (1,10):
    save(i)