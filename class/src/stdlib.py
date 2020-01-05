import os
import shutil
import glob
import sys
import argparse
import re       # regular expressions.
import math
import random
from urllib.request import urlopen
import smtplib
from datetime import date

print(os.getcwd())

# shutil.copyfile('source','dest')

print(glob.glob("*.py"))    # gets all .py files.

print(sys.argv)


parser = argparse.ArgumentParser(prog='top',
                                 description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
#args = parser.parse_args()
#print(args)

sys.stderr.write('error message')

print(random.randrange(10))

# internet acess
with urlopen('http://www.google.com') as response:
     for line in response:
         print(line)
# sending email

#server = smtplib.SMTP('localhost')
#server.sendmail('sairamaj@gmail.com','sairamaj@hotmail.com','test')

print(date.today())