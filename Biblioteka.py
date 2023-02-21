import random

Biblioteka1 = (("The Green Mile", 1999, "Drama"),
("The Shawshank Redemption", 1994, "Drama"),
("Kiler", 1997, "Comedy"),
("Breaking Bad", 2008, "Drama","S1", "E1"),
("Family Guy", 1999, "Animation", 1, 1),
("Pitbull", 2005, "Crime", 1, 1))

#print("Oto biblioteka naszych multimediów: ", Biblioteka1)

film_or_serial = input("Wpisz hasło filmy aby wyświetlić filmy lub seriale aby wyświetlić seriale: ")
Filmy = []
Seriale = []

if film_or_serial == "filmy":
    for i in Biblioteka1:
        if len(i) == 3:
            Filmy.append(i)
    print(Filmy)
if film_or_serial == "seriale":
    for i in Biblioteka1:
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

Biblioteka = [Movie(title="The Green Mile", year=1999, genre="Drama"),
              Movie(title="The Shawshank Redemption", year=1994, genre="Drama"),
              Movie(title="Kiler", year=1997, genre="Comedy"),
              Series(title="Breaking Bad", year=2008, genre="Drama", sezon="S1", episode="E1"),
              Series(title="Family Guy", year=1999, genre="Animation", sezon="S1", episode="E1"),
              Series(title="Pitbull", year=2005, genre="Crime", sezon="S1", episode="E1")]

Tytuł = input("Wyszukaj film lub serial, wpisując jego tytuł, wpisz pomiń jeśli chesz pominąć funkcję: ")

def search():
    if Tytuł == Biblioteka[0].title:
        print(Biblioteka[0])
    elif Tytuł == Biblioteka[1].title:
        print(Biblioteka[1])
    elif Tytuł == Biblioteka[2].title:
        print(Biblioteka[2])
    elif Tytuł == Biblioteka[3].title:
        print(Biblioteka[3])
    elif Tytuł == Biblioteka[4].title:
        print(Biblioteka[4])
    elif Tytuł == Biblioteka[5].title:
        print(Biblioteka[5])
    elif Tytuł == "pomiń":
        pass              
search()

libraryV = []

def generate_views(library):
    element = random.choice(library)
    element.play()
    views = random.randint(1, 100)
    for i in range(views):
        element.play()
    print(f"{element.title} odtworzono {element.view} razy.")
    
    #libraryV.append(element.title)
    #libraryV.append(element.view)
    #print(libraryV)

def run_generate_views(library):
    for i in range(10):
        generate_views(library)

chce = input("Wpisz hasło: statystyki, aby zobaczyć wyświetlenia pozycji z biblioteki:")

if chce == "statystyki":
    run_generate_views(Biblioteka)


