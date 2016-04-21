# -*- encoding: utf-8 -*-
import os
import glob
OpenFile = open(r'/dir/result.txt', 'w') #Открываем файл для записи

for file in glob.glob(r'/dir/*.txt'): #Перебор слов
    Opfile = open(file)
    Opfile = Opfile.read()
    number = Opfile.count('python')
    numstr = str(number)
    print(file)
    print(numstr)
    OpenFile.write(' В файле: ' + file + ' слово Python содержится ' + numstr + ' раз\n')
OpenFile.close()