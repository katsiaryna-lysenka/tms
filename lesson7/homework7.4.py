def json(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
    return wrapper

@json
def fetch_webpage():
    import requests
    webpage = requests.get('https://yandex.by/')


@json
def get_webpage():
    import requests
    webpage = requests.get('https://teachmeskills.by/')

fetch_webpage()
get_webpage()
