import datetime


def choose_plural(n, k):
    if n % 10 == 1 and n % 100 != 11:
        return (f'{n} {k[0]}')
    elif n % 10 in [2, 3, 4] and n % 100 not in [12, 13, 14]:
        return (f'{n} {k[1]}')
    else:
        return (f'{n} {k[2]}')


try:
    how = input('Введите дату/время в формате ДД.ММ.ГГГГ ЧЧ:ММ ')
    date_x = datetime.datetime.strptime(how, '%d.%m.%Y %H:%M')
    date_now = datetime.datetime.now().replace(second=0, microsecond=0)
    if date_x >= date_now:
        delta = date_x - date_now

    else:
        print('Ошибка')
except:
    print('Ошибка')
