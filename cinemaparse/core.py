import requests
  ''
'Этот класс создан для работы с hnml'
''
class CinemaParser():
  ''
'Самый полезный класс'
''
def __init__(self, city = 'msk'):
  ''
'"Это функция получает на вход город (Москва или Санкт-Петербург)'
''
self.city = city
def extract_raw_content():
  self.content = requests.get('https://msk.subscity.ru')
def print_raw_content():
  print(self.content)
