import hashlib
import glob

def get_hash_sha(filename):
    """ Ф-я рассчитывает хэш файла """

    with open(filename, 'rb') as f:
        m = hashlib.sha256()
        while True:
            data = f.read(256)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

def check(): # разбиваем на список, сравниваем название файла в папке, берём его хеш и сверяем 3й элемент,

    """ 1. Получаем список файлов из папки
        2. Считываем данные из файла data.txt
        3. Сравниваем название файлов и их хэш """


    spisok = glob.glob("*.txt")
    data = 'D:\PITON\Heshuryem\data\data.txt'
    with open(data, 'r') as f:
        a = [[_ for _ in line.split()] for line in f.readlines()]
    # a[0][0]...a[3][0] == data[0]  БЕРЁМ НАИМЕНОВАНИЕ ИЗ ДАТА.ТХТ ИЩЕМ ЕЁ Ф ПАПКЕ ПОЛУЧАЕМ ЕЁ ХЭШ И СРАВНИВАЕМ С ТЕМ ЧТО ЕСТЬ В ФАЙЛЕ
    # A[0][2] - ХЭШ
    for sp in spisok:
        x = 0
        try:
            while not sp == a[x][0]:
                x += 1
                if x == len(a):
                    print(sp.ljust(12, ' '), 'NOT FOUND')
        except IndexError:
            pass
        hesh = get_hash_sha(sp)
        try:
            if hesh == a[x][2]:
                print(sp.ljust(12, ' '), 'OK')
            else:
                print(sp.ljust(12, ' '), "FAIL")
        except IndexError:
            pass

check()