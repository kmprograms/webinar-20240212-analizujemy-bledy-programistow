# [1] Brak stosowania albo nieoptymalne uzywanie algorytmow
#     ale tez zeby nie przesadzic.
# [2] Zwroc uwage ze nie zawsze nazwy musza byc rozwlekle, niekiedy moga byc to skroty
# ale musi to wszystko miec sens

# TODO O czym zaponialem?

import random

# Przeszukiwanie liniowe
def linear_search(lst, value):
    for i, item in enumerate(lst):
        if item == value:
            return i
    return -1

# Sortowanie i przeszukiwanie binarne
# [1 2 3 4 5]
def binary_search(sorted_lst, value):
    left, right = 0, len(sorted_lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_lst[mid] == value:
            return mid
        elif sorted_lst[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main() -> None:
    # Załóżmy, że mamy listę i szukamy wartości
    lst = [random.randint(0, 100) for _ in range(1000)]  # Generujemy losową listę
    value = lst[random.randint(0, 999)]  # Wybieramy losową wartość do znalezienia
    sorted_lst = sorted(lst)
    # Teraz możemy zastosować przeszukiwanie binarne
    index = binary_search(sorted_lst, value)
    print(value)
    print(sorted_lst[index])

if __name__ == '__main__':
    main()

# Wybór algorytmu zależy od kontekstu. Przeszukiwanie liniowe może być bardziej odpowiednie
# dla jednorazowych wyszukań w nieposortowanych listach, zwłaszcza gdy lista jest krótka.
# Sortowanie listy połączone z przeszukiwaniem binarnym jest lepszym wyborem, gdy mamy do
# czynienia z wielokrotnymi wyszukiwaniami w tej samej liście i koszt początkowego sortowania
# rozkłada się na wiele operacji wyszukiwania.