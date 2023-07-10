# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from datetime import datetime as dt
from calendar import isleap
import sys


__all__ = ['check_date']

def check_date(current_date):
    try:
        day, month, year = map(int, current_date.split('.'))
        dt(year=year, month=month, day=day)
    except:
        return [False, False]
    if isleap(year):
        return [True, True]
    else:
        return [True, False]


if __name__ == '__main__':
    match check_date(sys.argv[1]):
        case [True, True]:
            print('Такая дата существует. Год високосный')
        case [True, False]:
            print('Такая дата существует. Год не високосный')
        case [False, False]:
            print('Даты не существует')