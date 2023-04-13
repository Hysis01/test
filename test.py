import datetime


def choose_plural(n, k):
    if n % 10 == 1 and n % 100 != 11:
        return f'{n} {k[0]}'
    elif n % 10 in [2, 3, 4] and n % 100 not in [12, 13, 14]:
        return f'{n} {k[1]}'
    else:
        return f'{n} {k[2]}'


try:
    how = input('Введите дату/время в формате ДД.ММ.ГГГГ ЧЧ:ММ ')
    date_x = datetime.datetime.strptime(how, '%d.%m.%Y %H:%M')
    date_now = datetime.datetime.now().replace(second=0, microsecond=0)
    if date_x >= date_now:
        delta = date_x - date_now
        hours = delta.seconds // 3600
        minutes = (delta.seconds - hours * 3600) // 60
        days = delta.days
        match (True):
            case True if days == 0 and hours == 0:
                print('До часа "Икс" ' + choose_plural(minutes, ["минута", "минуты", "минут"]))
            case True if days == 0 and hours != 0:
                print('До часа "Икс" ' + choose_plural(hours,["час", "часа", "часов"]) + " и " +
                      choose_plural(minutes, ["минута", "минуты", "минут"]))
            case True if days != 0 and minutes == 0:
                print('До часа "Икс" ' + choose_plural(days, ["день", "дня", "дней"]) + " и " +
                      choose_plural(hours, ["час", "часа", "часов"]))
            case _:
                print('До часа "Икс" ' + choose_plural(days, ["день", "дня", "дней"]) + " " +
                      choose_plural(hours, ["час", "часа", "часов"]) + " " +
                      choose_plural(minutes, ["минута", "минуты", "минут"]))
    else:
        print('Ошибка')
except:
    print('Ошибка')
