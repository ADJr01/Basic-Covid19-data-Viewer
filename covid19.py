import requests
import time, calendar
import urllib.request


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def readable_date_format(date):
    dayy = str(date).split('-')
    main_day = f"{dayy[2]}-{calendar.month_name[int(dayy[1])]}-{dayy[0]}"
    return main_day


def is_connected():
    try:
        urllib.request.urlopen('https://www.google.com/')  # Python 3.x
        return True
    except:
        return False


def confirmed(message: str):
    return f'{bcolors.FAIL}{message}{bcolors.ENDC}'


def warn(message: str):
    return f'{bcolors.WARNING}{message}{bcolors.ENDC}'


def get_world_info(data_set: dict, country_name, wait=0):
    try:
        for i in data_set[country_name]:
            print(f"Country: {country_name}")
            print('-' * 15)
            print(f"Date: {readable_date_format(i['date'])} ")
            print(warn(f"Confirmed: {i['confirmed']}"))
            print(confirmed(f"Deaths {i['deaths']}"))
            print('=' * 20)
            if wait > 0:
                time.sleep(wait)
    except Exception as e:
        print('Failed To load data \e{}'.format(e))


def input_format(string):
    string = str(string).split()
    if 0 < len(string) <= 2:
        if len(string) == 1:
            return string[0], 0
        else:
            return string[0], float(string[1])
    else:
        raise str('Invalid Input')


if __name__ == '__main__':
    if not is_connected():
        print("Sorry No Internet Connection :(")
        exit(0)
    uri = 'https://pomber.github.io/covid19/timeseries.json'
    result = requests.get(uri)
    data = dict(result.json())
    country, Wait = input_format(input('Please Enter Country Name [press q to exit]: '))
    while country.lower()[0] != 'q':
        get_world_info(data, country.capitalize(), wait=Wait)
        country, Wait = input_format(input('Please Enter Country Name [press q to exit]: '))
    print('Done')
    exit(0)
