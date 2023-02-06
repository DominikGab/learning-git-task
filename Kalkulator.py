

dzialanie  = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))



def liczenie (dzialanie):
    if dzialanie == 1:
        n = list(map(int, input("wprowadź wartości dodawania: ").split()))
        print("podane wartości: ", n)
        wynik = sum(n)
        print("wynik dodawania to: ", wynik)
    elif dzialanie == 2:
        num1 = int(input("Podaj składnik 1: "))
        num2 = int(input("Podaj składnik 2: "))
        print("Odejmuję", num1, "i", num2)
        print("wynik to:", num1-num2)
    elif dzialanie == 3:
        n = list(map(int, input("wprowadź wartości mnożenia: ").split()))
        print("podane wartości: ", n)
        wynik = 1
        for number in n:
            wynik = wynik * number 
        print("wynik mnożenia to: ", wynik)
    elif dzialanie == 4:
        num1 = int(input("Podaj składnik 1: "))
        num2 = int(input("Podaj składnik 2: "))
        print("Dzielę", num1, "i", num2)
        print("wynik to:", num1/num2)
    else:
        print("Wybrałeś zły numer działania")
        exit(1)

liczenie(dzialanie)   

