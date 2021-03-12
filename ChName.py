from os import listdir as ls, rename as rn, chdir
from re import search
chdir("C:\\Users\\moahamadhosseyn313\\Downloads\\Video")
listDir = ls()

for name in listDir:
    print(name)
    if search(r"قسمت\+\d{2}-\d+-\d+-\d+\+\d+-\d+-\d+", name):
        rn(name, name.split('-')[0].split("+")[1] + ".mp4")
