print('VALIIDAR SI UN AÑO ES BISIESTO')

year = int(input('Ingrese el año '))


def bisist_years(year):

    if (year % 4 == 0 and year % 100) == 0 and year % 400 == 0:
        print(' El año {} es bisiesto'.format(year))

    else:
        print(' El año {}  no es bisiesto'.format(year))


bisist_years(year)
