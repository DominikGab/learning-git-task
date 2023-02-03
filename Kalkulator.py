dzialanie  = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")

num1 = int(input("Podaj składnik 1: "))
num2 = int(input("Podaj składnik 2: "))

def liczenie (dzialanie):
    if dzialanie == "1":
        print("Dodaję", num1, "i", num2)
        print("wynik to:", num1+num2)
    elif dzialanie == "2":
        print("Odejmuję", num1, "i", num2)
        print("wynik to:", num1-num2)
    elif dzialanie == "3":
        print("Mnożę", num1, "i", num2)
        print("wynik to:", num1*num2)
    elif dzialanie == "4":
        print("Dzielę", num1, "i", num2)
        print("wynik to:", num1/num2) 
   
liczenie(dzialanie)