import requests
from bs4 import BeautifulSoup

class CinemaParser:
    ''' Самый нужный класс'''

    def __init__(self, city='msk'):
        ''' Принемаем город'''
        self.city = city
        self.content = ''
        self.number = 0
        self.station = []
        self.name = []
        self.film = []
        self.site = []
        self.name = []

    def extract_raw_content(self):
        ''' Скачиваем HTML содержимое сайта '''
        url = 'https://{}.subscity.ru'.format(self.city)
        self.content = requests.get(url)

    def print_raw_content(self):
        '''Печатаем HTML содержимое(красиво)'''
        soup = BeautifulSoup(self.content.text, 'html.parser')
        return soup.prettify()
 
    def get_films_list(self):
        '''Поиск всех тегов с фильмами и очистка'''
        self.film.clear()
        soup = BeautifulSoup(self.content.text, 'html.parser')
        for i in soup.find_all("div", class_='movie-plate'):
            self.film.append(i["attr-title"])
        return self.film

    def get_film_nearest_session(self, name):
        '''Ищем ближайший сеанс фильма'''
        f_0 = 0
        day = []
        t_str = ''
        time = []
        cinema_name = []
        for i in range(len(self.film)):
            if str(self.film[i]).upper() == str(name).upper():
                self.number = i
                f_0 = 1
        if f_0 == 0:
            raise TypeError("Фильм не найден")
        url = 'https://{}.subscity.ru'.format(self.city)

        soup = BeautifulSoup(self.content.text, 'html.parser')
        for i in soup.find_all('div', class_="movie-titles"):
            for j in i.find_all('div', class_="movie-title"):
                for c in j.find_all("a", class_="underdashed"):
                    self.site.append(url + c['href'])

        self.content = requests.get(self.site[self.number])
        print(self.site[self.number])
        soup = BeautifulSoup(self.content.text, 'html.parser')
        for i in soup.find_all('h3', class_='header-day text-center'):
            for j in i.find_all('a', class_='underdashed'):
                day.append(j.text)
        t_str = "table table-bordered table-condensed table-curved table-striped table-no-inside-"
        for i in soup.find('table', class_=t_str+'borders'):
            for j in i.find_all("td", class_="text-center cell-screenings"):
                time.append(str(j.text)[:5].replace(':', '.'))

        for i in soup.find_all('div', class_='cinema-name'):
            for j in i.find_all('a', class_="underdashed"):
                cinema_name.append(j.text)


        f_0 = min(range(len(time)), key=time.__getitem__)
        return time[f_0], day[f_0], cinema_name[f_0]
      
