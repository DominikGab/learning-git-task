import random

class Movie:
    def __init__(self, title, year, genre, type):
        self.title = title
        self.year = year
        self.genre = genre
        self.type = type
        self.view = 0
        
    def play(self):
        self.view += 1
        
    def show(self):
        return f'{self.title} {self.year} {self.genre} {self.type}'

class Series(Movie):
    def __init__(self, title, year, genre, sezon, episode, type):
        super().__init__(title, year, genre, type)
        self.sezon = sezon
        self.episode = episode
        self.view_count = 0    
    
    def play(self):
        self.view_count += 1

    def show(self):
        return f'{self.title} {self.year} {self.genre} {self.sezon} {self.episode} {self.type}'



Biblioteka = [Movie(title="The Green Mile", year=1999, genre="Drama", type = "film"),
              Movie(title="The Shawshank Redemption", year=1994, genre="Drama", type = "film"),
              Movie(title="Kiler", year=1997, genre="Comedy", type = "film"),
              Series(title="Breaking Bad", year=2008, genre="Drama", sezon="S1", episode="E1", type = "serial"),
              Series(title="Family Guy", year=1999, genre="Animation", sezon="S1", episode="E1", type = "serial"),
              Series(title="Pitbull", year=2005, genre="Crime", sezon="S1", episode="E1", type = "serial")]

print("Oto nasza biblioteka: ")
for element in Biblioteka: 
    print(element.show())


# Selekcja filmów i seriali z listy ogólnej
type = input("Wpisz hasło film aby wyświetlić filmy lub serial aby wyświetlić seriale: ")
def movie_or_series():
    for element in Biblioteka:
        if element.type == type: 
            print(element.show())
movie_or_series()

# Wyszukiwanie elementu po tytule
title = input("Wpisz tytuł filmu lub serialu aby wyświetlićinformacje o nim: ")
def search():
        if element.title == title: 
            print(element.show())
search()

# Generowanie i sortowanie wyświetleń

stats = input("Wpisz hasło: statystyki, aby zobaczyć wyświetlenia pozycji z biblioteki:")

Library1 = []
Library2 = []

#generowanie wyświetleń
def generate_views(library):
    element = random.choice(library)
    element.play()
    views = random.randint(1, 100)
    for i in range(views):
        element.play()
    Library1.append(element.title)
    Library2.append(element.view)
    print(f"{element.title} odtworzono {element.view} razy.")

# włączanie funkcji 10 razy
def run_generate_views(library):
    for i in range(10):
        generate_views(library)
    print(Library1, Library2)

    Lista_dict = dict(zip(Library1, Library2))

    sorted_dict = dict(sorted(Lista_dict.items(), key=lambda item: item[1], reverse=True))

    print("Oto lista wszystkich wyświetleń naszych tytułów: ",Lista_dict)
    print("Oto lista naszych top wyświetleń: ",sorted_dict)

if stats == "statystyki":
    run_generate_views(Biblioteka)   