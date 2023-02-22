import random

Biblioteka1 = (("The Green Mile", 1999, "Drama"),
("The Shawshank Redemption", 1994, "Drama"),
("Kiler", 1997, "Comedy"),
("Breaking Bad", 2008, "Drama","S1", "E1"),
("Family Guy", 1999, "Animation", 1, 1),
("Pitbull", 2005, "Crime", 1, 1))

print("Oto biblioteka naszych multimediów: ", Biblioteka1)

class Movie:
    def __init__(self, title, year, genre, type):
        self.title = title
        self.year = year
        self.genre = genre
        self.type = type
        self.view = 0
        
    def play(self):
        self.view += 1
        
    def __str__(self):
        return f'{self.title} {self.year} {self.genre} {self.type}'

class Series(Movie):
    def __init__(self, title, year, genre, sezon, episode, type):
        super().__init__(title, year, genre, type)
        self.sezon = sezon
        self.episode = episode
        self.view_count = 0    
    
    def play(self):
        self.view_count += 1

    def __str__(self):
        return f'{self.title} {self.year} {self.genre} {self.sezon} {self.episode} {self.type}'



Biblioteka = [Movie(title="The Green Mile", year=1999, genre="Drama", type = "film"),
              Movie(title="The Shawshank Redemption", year=1994, genre="Drama", type = "film"),
              Movie(title="Kiler", year=1997, genre="Comedy", type = "film"),
              Series(title="Breaking Bad", year=2008, genre="Drama", sezon="S1", episode="E1", type = "serial"),
              Series(title="Family Guy", year=1999, genre="Animation", sezon="S1", episode="E1", type = "serial"),
              Series(title="Pitbull", year=2005, genre="Crime", sezon="S1", episode="E1", type = "serial")]

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

film_or_serial = input("Wpisz hasło filmy aby wyświetlić filmy lub seriale aby wyświetlić seriale: ")
Seriale = []

def get_movies():
    Filmy = []
    if film_or_serial == "filmy":
        if Biblioteka[0].type == "film":
                Filmy.append(Biblioteka[0])
        elif Biblioteka[1].type == "film":
                Filmy.append(Biblioteka[1])
        elif Biblioteka[2].type == "film":
                Filmy.append(Biblioteka[2])
        elif Biblioteka[3].type == "film":
                Filmy.append(Biblioteka[3])
        elif Biblioteka[4].type == "film":
                Filmy.append(Biblioteka[4])
        elif Biblioteka[5].type == "film":
                Filmy.append(Biblioteka[5])
        elif film_or_serial == "pomiń":
            pass
        print(Filmy)
get_movies()

def get_series():
    Seriale = []
    if film_or_serial == "seriale":
        if Biblioteka[0].type == "serial":
                Seriale.append(Biblioteka[0])
        elif Biblioteka[1].type == "serial":
                Seriale.append(Biblioteka[1])
        elif Biblioteka[2].type == "serial":
                Seriale.append(Biblioteka[2])
        elif Biblioteka[3].type == "serial":
                Seriale.append(Biblioteka[3])
        elif Biblioteka[4].type == "serial":
                Seriale.append(Biblioteka[4])
        elif Biblioteka[5].type == "serial":
                Seriale.append(Biblioteka[5])
        elif film_or_serial == "pomiń":
            pass
        print(Seriale)
get_series()

Library1 = []
Library2 = []

def generate_views(library):
    element = random.choice(library)
    element.play()
    views = random.randint(1, 100)
    for i in range(views):
        element.play()
    Library1.append(element.title)
    Library2.append(element.view)
    print(f"{element.title} odtworzono {element.view} razy.")

    

def run_generate_views(library):
    for i in range(10):
        generate_views(library)
    print(Library1, Library2)

    Lista_dict = dict(zip(Library1, Library2))

    sorted_dict = dict(sorted(Lista_dict.items(), key=lambda item: item[1], reverse=True))

    print("Oto lista wszystkich wyświetleń naszych tytułów: ",Lista_dict)
    print("Oto lista naszych top wyświetleń: ",sorted_dict)

    


chce = input("Wpisz hasło: statystyki, aby zobaczyć wyświetlenia pozycji z biblioteki:")

if chce == "statystyki":
    run_generate_views(Biblioteka)







