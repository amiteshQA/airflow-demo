from datetime import date, datetime, timedelta
from os.path import join
import os


reading_date = open(join(os.getcwd(), './xml_api/date_sheet.txt'), 'r')
my_day = reading_date.read()
float_day = int(my_day)
yesterday = date(2022, 4, 22) - timedelta(days=float_day)
print(yesterday)

# float_day-=1
# file_output = open(join(os.getcwd(), '../xml_api/date_sheet.txt'), 'w')
# file_output.write(str(float_day))