import hashlib
import glob


def get_hash_for_chk(filename, a, x):
    """
    Ф-я рассчитывает хэш файла
    1. смотрим каким методом был захэширан файл
    2. таким же методом повторяем процедуру
    """
    with open(filename, 'rb') as f:
        method = a[x][1]
        if method == 'md5':
            m = hashlib.md5()
        if method == 'sha1':
            m = hashlib.sha1()
        if method == 'sha256':
            m = hashlib.sha256()
        while True:
            data = f.read(256)
            if not data:
                break
            m.update(data)
        return m.hexdigest()


def check():
    """
    1. Получаем список файлов из папки
    2. Считываем данные из файла data.txt
    3. Сравниваем название файлов и их хэши
    """

    spisok = glob.glob("*.*")
    data = 'D:\PITON\Heshuryem\data\data.txt'
    with open(data, 'r') as f:
        a = [[_ for _ in line.split()] for line in f.readlines()]
    for sp in spisok:
        x = 0
        try:
            while not sp == a[x][0]:
                x += 1
                if x == len(a):
                    print(sp.ljust(14, ' '), 'NOT FOUND')
        except IndexError:
            pass
        if not x == len(a):
            hesh = get_hash_for_chk(sp, a, x)

            if hesh == a[x][2]:
                print(sp.ljust(14, ' '), 'OK')
            else:
                print(sp.ljust(14, ' '), "FAIL")


if __name__ == '__main__':
    check()
