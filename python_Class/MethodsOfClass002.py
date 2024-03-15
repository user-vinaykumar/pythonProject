# regular methods / instance methods, class methods, static methods.
from datetime import timedelta
class Movies:

    movieQuality = '4K'

    def __init__(self, title, duration, language, hero, heroine, director):
        self.title = title
        self.duration = duration
        self.language = language
        self.hero = hero
        self.heroine = heroine
        self.director = director


    def MovieDirector(self):
        return f'Director of the movie : {self.director}'

    def MovieHero(self):
        return f'Main lead of the movie Male is : {self.hero}'

    def MovieHeroine(self):
        return f'Main lead of the movie Female is : {self.heroine}'

    def MovieDuration(self):
        return f'Duration of the movie is : {self.duration}'

    @classmethod
    def setMovieQuality(cls, item):
        cls.movieQuality = item

    @classmethod
    def movieInstance(cls, item1, item2, item3, item4, item5, item6, item7):
        moviename = item1
        movieduration = item2
        movielanguage = item3
        moviehero = item4
        movieheroine = item5
        moviedirector = item6
        randomvariable = item7
        return cls(moviename, movieduration, movielanguage, moviehero, movieheroine,
                   moviedirector)
    @staticmethod
    def CompleteMovieInfo(item):
        print(f'Movie name : {item.title}')
        print(f'Movie language : {item.language}')
        print(f'Movie duration : {item.duration}')
        print(f'Movie hero : {item.hero}')
        print(f'Movie heroine : {item.heroine}')
        print(f'Movie director : {item.director}')


rajahuli = Movies('Rajahuli', timedelta(0,56, 0,
                                        0, 23, 2, 0),
                  'Kannada', 'Yash', 'Meghana Raj', 'Madesh')
rajahuli.setMovieQuality('8K')
print(rajahuli.movieQuality)
print(Movies.movieQuality)

print(rajahuli.MovieHero())
print(rajahuli.duration)
name = 'Blink'
durat = timedelta(0, 42, 0, 0, 32,
                  2, 0)
lang = 'Kannada'
actor = 'Deekshith Shetty'
actress = 'Chaitra J Achar'
directo = 'Srinidhi'
unknown = 'unknown'
blink = Movies.movieInstance(name, durat, lang, actor, actress, directo, unknown)
print(blink.MovieHeroine())
blink2 = rajahuli.movieInstance(name, durat, lang, actor, actress, directo, unknown)
blink2.CompleteMovieInfo(blink2)
rajahuli.CompleteMovieInfo(rajahuli)
name1 = 'jackie'
durat1 = timedelta(0, 11, 0, 0, 21,
                  2, 0)
lang1 = 'Kannada'
actor1 = 'Puneeth Rajkumar'
actress1 = 'Bhavana'
directo1 = 'Soori'
unknown1 = 'unknown1'
jackie = Movies.movieInstance(name1, durat1, lang1, actor1, actress1, directo1, unknown1)
print(f'-----------------')
blink.CompleteMovieInfo(jackie)