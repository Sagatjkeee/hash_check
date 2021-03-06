import hashlib
import glob
import random


def find_files():
    """
    Находим необходимые файлы в указанной директории по нужнымм нам параметрам
    """
    data = glob.glob('*.*')
    for i in data:
        get_hash(i)

        
def get_hash(filename):
    """ 
    Ф-я рассчитывает хэш файла случайным образом выбирая алгоритм
    после чего записывает  в отдельный файл:
    имя файла, метод и сам хэш
    """
    nb = random.random()
    if nb < 0.33:
        m = hashlib.md5()
        method = 'md5'
    elif 0.33 < nb < 0.66:
        m = hashlib.sha1()
        method = 'sha1'
    else:
        m = hashlib.sha256()
        method = 'sha256'
        
    with open(filename, 'rb') as f:
        while True:
            data = f.read(256)
            if not data:
                break
            m.update(data)
        hesh = m.hexdigest()
        
    with open('D:\PITON\Heshuryem\data\data.txt', 'a') as f:
        print('{} {} {}'.format(filename.ljust(14, ' '), method.ljust(7, ' '), hesh), file=f)


if __name__ == '__main__':
    find_files()
