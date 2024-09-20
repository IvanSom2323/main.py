import random
import time
bot = 0
Passwords = {}
def RandomPassword():
    RandomPasswordNew = random.randint(1, 10000)
    print('Можно использовать пароль ', RandomPasswordNew)
def RandomNotBot():
    q=0
    Random = random.randint(1,5)
    if Random == 2:
        print('Яблоко это что? (фрукт  овощ  напиток) ')
        YouAreReady = input()
        if YouAreReady != 'фрукт':
            print(' Ты бот! >:( ')
            bot = 1
        else:
            bot = 0
    if Random == 3:
        print('Чай это что? (овощ  погода  напиток) ')
        YouAreReady = input()
        if YouAreReady != 'напиток':
            print(' Ты бот! >:( ')
            bot = 1
        else:
            bot = 0
    if Random == 4:
        print('Огурец это что? (фрукт  погода  овощ) ')
        YouAreReady = input()
        if YouAreReady != 'овощ':
            print(' Ты бот! >:( ')
            bot = 1
        else:
            bot = 0
    if Random == 5:
        print('Дождливая(ый)... (погода  овощ  напиток) ')
        YouAreReady = input()
        if YouAreReady != 'погода':
            print(' Ты бот! >:( ')
            bot = 1
        else:
            bot = 0
    q=1
def DeletePassword(name):                                 # CrownPassword - Главный пароль
    if CrownPassword == CrownPasswordVVOD:
        YouAreReady = input('Вы уверены что хотите удалить пароль который вы напишите? (да или нет)')
        if YouAreReady == 'да':
            del Passwords[name]
            print('Пароль успешно удалён!')
def ShowPasswords():
    if CrownPassword == CrownPasswordVVOD:
        print('Вы не бот? ')
        RandomNotBot()
        if bot == 1:
            print('УХОДИ БОТ!!!')
        else:
            print(Passwords) 
def AddPassword(name, intValue):
    if CrownPasswordVVOD == CrownPassword:
        Passwords[name] = intValue
        print('Пароль успешно добавлен!')
print('*'*20, 'Менеджер паролей', '*'*20)
CrownPassword = input('Для начала напишите главный пароль')
print('Вам доступны следующие команды: ')
while True:
    print()
    print('1 - Показать список паролей  ', end='')
    time.sleep(1)
    print('2 - Удалить/Добавить пароль ')
    time.sleep(1)
    print('3 - Показать случайный пароль ')
    time.sleep(1)
    print()
    Command = int(input())
    if Command == 1:
        CrownPasswordVVOD = input('Главный пароль для подтверждения: ')
        ShowPasswords()
    if Command == 2:
        AddOrDelete = int(input('1 - добавить, 2 - удалить (написать цифру)  '))
        if AddOrDelete == 1:
            CrownPasswordVVOD = input('Главный пароль для подтверждения: ')
            nameVVOD = input('Как будет называться заголовок пароля? ')
            intValueVVOD = input('Напишите ваш пароль: ')
            AddPassword(nameVVOD, intValueVVOD)
        if AddOrDelete == 2:
            CrownPasswordVVOD = input('Главный пароль для подтверждения: ')
            nameVVOD = input('Как называется заголовок пароля? ')
            DeletePassword(nameVVOD)
    if Command == 3:
        RandomPassword()
