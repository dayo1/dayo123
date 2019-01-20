"""
import os
print(os.name)

"""

"""
import os
os.getcwd()

"""

"""
import os
os.mkdir("pract1")
"""

"""
import os
os.chdir("pract1")
print(os.getcwd())

print(os.listdir())


for dirpath, dirnames, filenames in os.walk("C:/Users/User/PycharmProjects"):
    print ('Current path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

"""

import os

from datetime import datetime
print(os.stat("text3.txt"))
time = os.stat("text3.txt").st_mtime
print(datetime.fromtimestamp(time))

import os
os.mkdir("pract2")

os.chdir("pract2")
print(os.getcwd())