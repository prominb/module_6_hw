import re

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

for cyri, lati in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cyri)] = lati
    TRANS[ord(cyri.upper())] = lati.upper()


def normalize(name: str) -> str: # приймає на вхід рядок та повертає рядок
    """normalize
    приймає на вхід рядок та повертає рядок;
    проводить транслітерацію кириличних символів на латиницю;
    замінює всі символи, крім літер латинського алфавіту та цифр, на символ '_';
    транслітерація може не відповідати стандарту, але бути читабельною;
    великі літери залишаються великими, а маленькі — маленькими після транслітерації.
    """
    name, *extension = name.split('.')
    name_translit = name.translate(TRANS) # transliteration
    name_translit = re.sub(r"\W", "_", name_translit) # normalize word
    return f"{name_translit}.{'.'.join(extension)}"


if __name__ == '__main__':
    print(normalize('Z9ЙoJaPм.tar.gz')) # WORK
