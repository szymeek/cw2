# Zad. 1
# Napisz skrypt, w którym tworzysz listę ulubionych sportów, odwróć ją a następnie dodaj mniej lubiane sporty
# na sam koniec.
def zadanie1():
    lista = ['F1', 'NBA', 'NHL']
    print('ulubione sporty: ', lista)
    lista.reverse()
    print('odwrócona lista ', lista)
    mniej_lubiane_sporty = ('NFL', 'WWE')
    lista.extend(mniej_lubiane_sporty)
    print('mniej lubiane sporty na końcu ', lista)


# zadanie1()


# Zad. 2
# Stwórz słownik skrótów powszechnie używanych w gazetach lub artykułach internetowych.
# Jako klucz przyjmij skrót danego słowa, wartość to rozwinięcie tego skrótu.
def zadanie2():
    skroty = {'wp': 'Wirtualna Polska', 'zw': 'zaraz wracam', 'jw': 'jak wyżej', 'itp': 'i tym podobne'}
    print(skroty['zw'])


# zadanie2()


# Zad 3.
# Stwórz słownik z ulubionymi grami komputerowymi. Pomyśl, co może być kluczem a co wartością w takim słowniku.
# Policz liczbę elementów w słowniku.
def zadanie3():
    gry = {
        'tytul': 'ocena',
        'fifa': 9,
        'nba': 9,
        'mgs': 10
    }
    print('dlugosc slownika to ', len(gry))


# zadanie3()


# Zad 4.
# Napisz skrypt, który pobiera od użytkownika zdanie i liczy wystąpienia litery a. Użyj funkcji input
def zadanie4():
    a = input("podaj zdanie zawierające literę a:")
    print(a)
    print('litera a powtarza sie', a.count('a'), 'razy')


# zadanie4()


# Zad 5.
# Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie wykonasz obliczenia: ab + c.
# Użyj instrukcji readline() i write()).
def zadanie5():
    import sys
    print('podaj liczbe 1')
    a = sys.stdin.readline()
    print('liczba 1 to: ' + a)

    print('podaj liczbe 2')
    b = sys.stdin.readline()
    print('liczba 2 to: ' + b)

    print('podaj liczbe 3')
    c = sys.stdin.readline()
    print('liczba 3 to: ' + c)

    a = int(a)
    b = int(b)
    c = int(c)
    wynik = a * b + c
    wynik = str(wynik)
    sys.stdout.write('ab + c = ' + wynik)


# zadanie5()


# Zad 6.
# Wczytaj trzy liczby całkowite a,b,c i sprawdź, która z nich jest największa. W zależności od wyniku wyświetl
# odpowiedni komunikat. Użyj zagnieżdżeń.
def zadanie6():
    a = input('podaj liczbe 1:')
    b = input('podaj liczbe 2:')
    c = input('podaj liczbe 3:')
    a, b, c = int(a), int(b), int(c)

    if (a >= b) and (a >= c):
        najw = a
    elif (b >= a) and (b >= c):
        najw = b
    else:
        najw = c

    print('najwieksza liczba to', najw)


# zadanie6()


# Zad 7.
# Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float.
# Następnie za pomocą użycia pętli for podnieś każdą liczbę do kwadratu.
def zadanie7():
    lista = []
    lista.append(int(input('podaj liczbe int:')))
    lista.append(int(input('podaj liczbe int:')))
    lista.append(float(input('podaj liczbe float:')))
    lista.append(float(input('podaj liczbe float:')))
    # a = input('podaj liczbe int:')
    # b = input('podaj liczbe int:')
    # c = input('podaj liczbe float:')
    # d = input('podaj liczbe float:')
    # a, b = int(a), int(b)
    # c, d = float(c), float(d)
    print(lista)
    for x in lista:
        print(x * x)


# zadanie7()


# Zad 8. Napisz skrypt, który za pomocą pętli while pobiera 10 liczb, następnie dodaje do listy tylko parzyste liczby.
def zadanie8():
    lista = []
    z = 0
    while z != 10:
        x = int(input('podaj liczbe int:'))
        if x % 2 == 0:
            lista.append(x)
        z += 1
    print(lista)


# zadanie8()


# Zad. 9.
# Napisz skrypt, który liczy pierwiastek z liczby podanej przez użytkownika
# jeśli użytkownik poda wartość ujemną to powinien być wyłapany błąd.
def zadanie9():
    import math
    liczba = float(input('prosze podaj liczbe z ktorej oblicze pierwiastek '))
    try:
        wynik = math.sqrt(liczba)
        print(wynik)
    except ValueError:
        print('pierwiastek tylko z liczb dodatnich!')


# zadanie9()
