import random

Biblioteka = (("The Green Mile", 1999, "Drama"),
("The Shawshank Redemption", 1994, "Drama"),
("Kiler", 1997, "Comedy"),
("Breaking Bad", 2008, "Drama","S1", "E1"),
("Family Guy", 1999, "Animation", 1, 1),
("Pitbull", 2005, "Crime", 1, 1))

print("Oto biblioteka naszych multimediów: ", Biblioteka)

film_or_serial = input("Wpisz hasło filmy aby wyświetlić filmy lub seriale aby wyświetlić seriale: ")
Filmy = []
Seriale = []

for i in Biblioteka:
    if len(i) == 3:
        Filmy.append(i)
print(Filmy)
for i in Biblioteka:
    if len(i) == 5:
        Seriale.append(i)
print(Seriale)


class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.view = 0
        
    def play(self):
        self.view += 1
        
    def __str__(self):
        return f'{self.title} {self.year} {self.genre}'

Movie1 = Movie( title="The Green Mile", year=1999, genre="Drama")
Movie2 = Movie(title="The Shawshank Redemption", year=1994, genre = "Drama")
Movie3 = Movie(title= "Kiler",year=  1997, genre= "Comedy")

library = [Movie(title="The Green Mile", year=1999, genre="Drama"),
           Movie(title="The Shawshank Redemption", year=1994, genre="Drama"),
           Movie(title="Kiler", year=1997, genre="Comedy")]


class Series(Movie):
    def __init__(self, title, year, genre, sezon, episode):
        super().__init__(title, year, genre)
        self.sezon = sezon
        self.episode = episode
        self.view_count = 0    
    
    def play(self):
        self.view_count += 1

    def __str__(self):
        return f'{self.title} {self.year} {self.genre} {self.sezon} {self.episode}'

Serial1 = Series(title="Breaking Bad",year= 2008,genre= "Drama",sezon="S1", episode= "E1")
Serial2 = Series(title="Family Guy",year= 1999,genre= "Animation",sezon ="S1", episode= "E1")
Serial3 = Series(title="Pitbull",year= 2005,genre= "Crime",sezon= "S1",episode= "E1")


Tytuł = input("Wyszukaj film lub serial, wpisując jego tytuł: ")

def search():
    if Tytuł == Movie1.title:
        print(Movie1)
    elif Tytuł == Movie2.title:
        print(Movie2)
    elif Tytuł == Movie3.title:
        print(Movie3)
    elif Tytuł == Serial1.title:
        print(Serial1)
    elif Tytuł == Serial2.title:
        print(Serial2)
    elif Tytuł == Serial3.title:
        print(Serial3)              
search()





