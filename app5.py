# Wyrazenia regularne
# Czasami dobrze je uzyc, ale czasami mozesz przedobrzyc

# --------------------------------------------------------------------------------
# Przykład: Sprawdzanie, czy string zawiera pewien podciąg
# --------------------------------------------------------------------------------

# Nieefektywny sposob
import re

text = "This is an example string."
if re.search("example", text):
    print("Znaleziono słowo 'example'.")

# W tym przypadku użycie wyrażeń regularnych jest nadmiernym komplikowaniem,
# ponieważ re.search jest potężnym narzędziem przeznaczonym do bardziej złożonych
# wzorców i operacji na stringach, co może wprowadzać dodatkowy narzut wydajnościowy
# dla prostych sprawdzeń.

# Efektywny sposob

text = "This is an example string."
if "example" in text:
    print("Znaleziono słowo 'example'.")