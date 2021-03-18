import os

def sozp (name):
    os.mkdir(name)
def delp (name):
    os.rmdir(name)
def kud (name):
    print('текущая директория ', os.getcwd())
    os.chdir(name)
    print('директория после команды ', os.getcwd())
def sozf (name, text=False):
    file = open(name, 'w')
    if text:
        file.write(' '.join(text))
def delf (name):
    os.remove(name)
def sod (name):
    print(open(name).read())
def per (name,kuda):
    os.replace(name, '/'.join((kuda,name)))
def rename (name, rname):
    os.rename(name,rname)
    
kom = input('введите команду ').split(' ')
if kom[0]=='sozp':
    try: 
        sozp(kom[1])
    except FileExistsError:
        print('папка с таким именем уже существует ')
elif kom[0]=='delp':
    try:
        delp(kom[1])
    except FileNotFoundError:
        print('папки с таким именем нет ')
elif kom[0]=='kud':
    try:
        kud(kom[1])
    except FileNotFoundError:
        print('в данную дирректорию нельзя перейти ')
elif kom[0]=='sozf':
    sozf(kom[1])
elif kom[0]=='delf':
    try:
        delf(kom[1])
    except FileNotFoundError:
        print('файла с таким именем нет ')
elif kom[0]=='zap':
    sozf(kom[1],kom[2:])
elif kom[0]=='sod':
    try:
        sod(kom[1])
    except FileNotFoundError:
        print('данного файла не существует ')
elif kom[0]=='per':
    try:
        per(kom[1],kom[2])
    except FileNotFoundError:
        print('перемещение невозможно ')
elif kom[0]=='rename':
    try:
        rename(kom[1],kom[2])
    except FileNotFoundError:
        print('данного файла не существует ')