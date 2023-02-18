from faker import Faker
fake = Faker()

wybor_kontaktu = int(input("Wbierz numer kontaktu, króry chcesz wybrac: 1 - prywatny, 2 - służbowy, wybierz 3 jeśli chcesz zobaczyć efekt funkcji create_contacts"))

        
class Adressbook:
    def __init__(self, name, email, phone_number):
       self.name = name
       self.email = email
       self.phone_number = phone_number

if wybor_kontaktu == 1:

    class BaseContact(Adressbook):
        def __init__(self, name, email, phone_number):
            super().__init__(name, email, phone_number)
            self.__LabelLength = 0
    
    Base = int(input("wybierz numer od 1 do 5, osoby z którą chcesz się skontaktować: "))

    Card1 = Adressbook('Jordan Robinson','annanelson@example.org', '001-055-964-3457x233')  
    Card2 = Adressbook('Michelle Adkins', 'mmiranda@example.net', '3526149867')    
    Card3 = Adressbook('Gregory Gonzalez', 'mcgrathroger@example.com', '478-462-1576x31034')
    Card4 = Adressbook('Timothy Ramos', 'carterbrian@example.com', '974.393.9479x73979')
    Card5 = Adressbook('Elaine Quinn', 'juanortiz@example.org', '468.645.7187')
    
    def contact(Base):
        if Base== 1:
            print("Wybieram numer:", Card1.phone_number, "i dzwonię do", Card1.name )
        elif Base == 2:
            print("Wybieram numer:", Card2.phone_number, "i dzwonię do", Card2.name )
        elif Base == 3:
            print("Wybieram numer:", Card3.phone_number, "i dzwonię do", Card3.name )
        elif Base == 4:
            print("Wybieram numer:", Card4.phone_number, "i dzwonię do", Card4.name )
        elif Base == 5:
            print("Wybieram numer", Card5.phone_number, "i dzwonię do", Card5.name )
    contact(Base)

    @property
    def LabelLength(self):
        return self.__LabelLength
    @LabelLength.setter
    def LabelLength(self,value):
        self.__LabelLength = value

    if Base == 1:
        Card1.LabelLength = len(Card1.name)
        print(Card1.LabelLength)
    elif Base == 2:
        Card2.LabelLength = len(Card2.name)
        print(Card2.LabelLength)
    elif Base == 3:
        Card3.LabelLength = len(Card3.name)
        print(Card3.LabelLength)
    elif Base == 4:
        Card4.LabelLength = len(Card4.name)
        print(Card4.LabelLength)
    elif Base == 2:
        Card5.LabelLength = len(Card5.name)
        print(Card5.LabelLength)

elif wybor_kontaktu == 2:
    class BusinessContact(Adressbook):
    
        def __init__(self, name, email, phone_number,job, company, business_number):
            super().__init__(name, email, phone_number)
            self.job = job
            self.company = company
            self.business_number = business_number
            self.__LabelLength = 0
    Business = int(input("wybierz numer służbowy od 1 do 5, osoby z którą chcesz się skontaktować: "))
    
    BCard1 = BusinessContact('Jordan Robinson','annanelson@example.org', '001-055-964-3457x233', 'Soil scientist', 'Miller, Jackson and Jones', '(681)104-8602')
    BCard2 = BusinessContact('Michelle Adkins', 'mmiranda@example.net', '3526149867', 'Merchant navy officer', 'Kelley, Harrison and Hancock', '+1-712-112-7989x22016')       
    BCard3 = BusinessContact('Gregory Gonzalez', 'mcgrathroger@example.com', '478-462-1576x31034', 'IT technical support officer', 'Lindsey, Day and Booth', '+1-817-907-8929x14720')
    BCard4 = BusinessContact('Timothy Ramos', 'carterbrian@example.com', '974.393.9479x73979', 'Information officer', 'Thompson Group', '225-317-2051x77660')
    BCard5 = BusinessContact('Elaine Quinn', 'juanortiz@example.org', '468.645.7187', 'Product/process development scientist', 'Patterson Ltd', '(193)182-0777')
    
    def contact(Business):

        if Business == 1:
            print("Wybieram numer służbowy:", BCard1.business_number, "i dzwonię do", BCard1.name)
        elif Business == 2:
            print("Wybieram numer służbowy:", BCard2.business_number, "i dzwonię do", BCard2.name)
        elif Business == 3:
            print("Wybieram numer służbowy:", BCard3.business_number, "i dzwonię do", BCard3.name)
        elif Business == 4:
            print("Wybieram numer służbowy:", BCard4.business_number, "i dzwonię do", BCard4.name)
        elif Business == 5:
            print("Wybieram numer służbowy:", BCard5.business_number, "i dzwonię do", BCard5.name)

    contact(Business)

    @property
    def LabelLength(self):
        return self.__LabelLength
    @LabelLength.setter
    def LabelLength(self,value):
        self.__LabelLength = value

    if Business == 1:
        BCard1.LabelLength = len(BCard1.name)
        print(BCard1.LabelLength)
    elif Business == 2:
        BCard2.LabelLength = len(BCard2.name)
        print(BCard2.LabelLength)
    elif Business == 3:
        BCard3.LabelLength = len(BCard3.name)
        print(BCard3.LabelLength)
    elif Business == 4:
        BCard4.LabelLength = len(BCard4.name)
        print(BCard4.LabelLength)
    elif Business == 5:
        BCard5.LabelLength = len(BCard5.name)
        print(BCard5.LabelLength)
elif wybor_kontaktu == 3:

    liczba = int(input("Podaj, ile chcesz mieć wizytówek: "))
    rodzaj = int(input("Podaj typ wizytowek, 1 - prywatny / 2 - służbowy"))
    
    def create_contacts():
        if rodzaj == 1:
            print("Oto Twoja lista prywatnych wizytówek:")
            for i in range (liczba):
                contacts = (fake.name(), fake.email(), fake.phone_number())
                print(contacts)
        elif rodzaj == 2:
            print("Oto Twoja lista służbowych wizytówek:")
            for i in range (liczba):
                contacts = (fake.name(), fake.email(), fake.phone_number(), fake.job(), fake.company())
                print(contacts)
    create_contacts()





        





    



       




