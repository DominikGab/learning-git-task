

dzialanie  = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))

def liczenie (dzialanie):
    if dzialanie == 1:
        numbers = input("Podaj liczby, które chcesz do siebie dodać, oddziel je przecinkiem: ").split(",")
        print("Podane liczby to :", numbers)
        for number in numbers:
            wynik = sum(number)
    print(wynik)

