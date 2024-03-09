# create a movie class and its instances.
import datetime

class Movies:
    def __init__(self, movie, hero, heroine, director, releaseDate, boxOffice,
                 language, panIndia, dubbed):
        self.movie = movie
        self.hero = hero
        self.heroine = heroine
        self.director = director
        self.releasedate = releaseDate
        self.boxOffice = boxOffice
        self.language = language
        self.panIndia = panIndia
        self.dubbed = dubbed

    def movielanguage(self, item1):
        if item1 != 'Mungaru Male':
            return 'Kannada'
        else:
            return 'Non-Kannada'


    def movieinfo(self):
        print(f'the name of the movie : {self.movie}')
        print(f'the Hero of the movie : {self.hero}')
        print(f'the Heroine of the movie : {self.heroine}')
        print(f'the director of the movie : {self.director}')
        print(f'Movie released on : {self.releasedate}')
        print(f'Box Office collections : {self.boxOffice}')
        print(f'language of the movie : {self.movielanguage(self.movie)}')
        print(f'is the movie panIndia : {self.panIndia}')
        print(f'the movie dubbed to other languages : {self.dubbed}')

KGF = Movies('KGF', 'Yash', 'Srinidhi', 'Prashanth Neel',
             datetime.datetime.now(), '100cr', 'Kannada',
             True, True)

KGF.movieinfo()