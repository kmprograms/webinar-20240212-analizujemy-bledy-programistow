from collections import Counter
# Nieefektywne wykorzystanie kontenerow.

# ----------------------------------------------------------------------------------------------------------------
# Nadużywanie list zamiast set lub dict
# Listy są idealne do przechowywania uporządkowanych kolekcji elementów, ale wyszukiwanie elementów
# w liście może być nieefektywne dla dużych danych. Używanie set lub dict, które zapewniają szybsze wyszukiwanie
# jest lepszym wyborem dla operacji, które wymagają częstego sprawdzania obecności elementu.

# [1] Okazuje sie ze znowu wazna jest teoria - ZLOZONOSC OBLICZENIOWA ALGORYTMOW!

# ----------------------------------------------------------------------------------------------------------------
# Użycie pętli do przeszukiwania wartości zamiast metod wbudowanych: Python oferuje wiele metod wbudowanych
# i funkcji, takich jak in dla zbiorów i słowników, które są zazwyczaj znacznie szybsze niż ręczne iterowanie
# po kolekcji. Należy korzystać z tych metod, gdy tylko jest to możliwe.

# Ręczne przeszukiwanie dict-a
pairs = {"a": 1, "b": 2, "c": 3}
key_to_find = "b"
for key in pairs:
    if key == key_to_find:
        print("Znaleziono!")
        break

# Wykorzystanie 'in' do sprawdzenia klucza
if key_to_find in pairs:
    print("Znaleziono!")

# [2] Uwaga do, po co nam pokazujesz te wszystkie metody podczas spotkan ??!!

# ----------------------------------------------------------------------------------------------------------------

# Modyfikowanie listy podczas iteracji: Modyfikowanie kolekcji, po której aktualnie iterujemy, może prowadzić
# do nieoczekiwanych błędów. Zamiast tego lepiej jest używać składni list comprehensions lub tworzyć nową kolekcję.

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number % 2 == 0:
        numbers.remove(number)

# Lepsze podejście: list comprehension
# UWAGA NA DUZE ILOSC ELEMENTOW W LISCIE
numbers = [1, 2, 3, 4, 5]
numbers = [number for number in numbers if number % 2 != 0]

# ----------------------------------------------------------------------------------------------------------------
# Nadmierne kopiowanie danych
# Tworzenie niepotrzebnych kopii kolekcji: Python pozwala na łatwe kopiowanie kolekcji, ale niezamierzone tworzenie
# kopii, zwłaszcza w przypadku dużych zbiorów danych, może być kosztowne pod względem wydajności. Należy unikać
# niepotrzebnego kopiowania, chyba że jest to absolutnie konieczne.

# ----------------------------------------------------------------------------------------------------------------
# Ignorowanie zaawansowanych struktur danych z modułów collections lub heapq: Python oferuje zaawansowane
# struktury danych, takie jak defaultdict, Counter, deque, czy heapq, które mogą znacznie poprawić wydajność dla
# specyficznych zastosowań. Używanie tych struktur zamiast prostych list czy słowników, gdy są one odpowiednie,
# może znacznie poprawić wydajność.

# Zliczanie elementow
# Nieefektywny sposób
lista = ['a', 'b', 'c', 'a', 'b', 'c', 'a']
licznik = {}
for element in set(lista):
    licznik[element] = lista.count(element)

# Efektywny sposób z użyciem Counter
licznik = Counter(lista)
print(licznik)
