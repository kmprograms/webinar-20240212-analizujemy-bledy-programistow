import math

# [1] Nazewnictwo zmiennych i inne konwencje.
# Przestrzeganie konwencji dla konkretnego jezyka (dobre IDE wspiera konwencje, dlatego takie uzywamy):
# https://peps.python.org/pep-0008/

# [2] Zmienne globalne - NIE STOSOWAC

# [3] Nazewnictwo funkcji, loggers
# [4] Type hints, pyright (jakie jeszcze)
def divide_and_square(a: int | float, b: int | float) -> float:
    """

    :param a:
    :param b:
    :return:
    """
    # [5] WALIDACJA ARGUMENTOW I ICH TYPOW
    if b == 0:
        raise ValueError('By zero')
    # [5.1] Nie stosuj niepotrzebnych fragmentow kodu
    # [5.2] Uzywac debuggera
    # x = a / b
    print(x)
    # return x

    # [6] Naduzywanie bibliotek / zewnetrznych bibliotek - brak znajomosci
    # standardow, chyba ze musisz pracowac w starszej wersji
    # return math.pow(a / b, 2)
    return (a / b) ** 2

# [6] Brak prawidlowej struktury kodu - czy zastosowales podzial na funkcje?
# [7] Brak prawidlowej struktury kodu - gdzie jest main?

# [8] Testowanie kodu !!!

# [9] Brak środowiska wirtualnego lub narzędzia do zarzadzania dependencies
# Webinar o wirtualnych środowiskach w Python: https://km-programs.pl/e-learning/webinary/lessons/modul-2-webinar-3/
def main() -> None:
    """

    :return:
    """
    a = 100
    b = 200
    print(divide_and_square(a, b))
    # Kategoria
    # kategoria
    # kategora


if __name__ == '__main__':
    main()

# [10] Dokumentowanie kodu
