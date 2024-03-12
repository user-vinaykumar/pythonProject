class DataModel:

    kannada = {'kgf', 'kantara', 'natasaarvabhouma', 'james', 'kaatera', 'kranthi'}
    tamil = {'leo', 'jai bheem', 'jailer', 'thunivu'}
    telugu = {'pushpa', 'bahubali', 'rrr', 'og'}

    def selectMovies(self):
        self.movieLanguage = input('Enter the Language you are interested in : ')
        self.moviename = input('Enter the movie name : ')
        if self.moviename in self.selectLanguage(self, self.movieLanguage):
            tickets = input(f'')



    def selectLanguage(self, item):
        if item.upper() == 'KANNADA':
            return self.kannada
        elif item.upper() == 'TAMIL':
            return self.tamil
        elif item.upper() == 'TELUGU':
            return self.telugu

