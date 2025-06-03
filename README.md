# Nowa Era Downloader

Skrypt do pobierania zdjęć stron ebooków Nowej Ery i zrobienia z nich pdfa.

## Użycie

Aby użyć skryptu należy wypełnić `config.json` prawidłowymi danymi:

-   `url` - link do zdjęcia strony (numer strony należy zamienić na `XXX` lub `XX`)
-   `number_of_pages` - liczba stron ebooka (Nowa Era podaje złą liczbę stron, poprawna liczba znajduje się w url do jpg ostatniej strony)
-   `download_folder` - folder, gdzie będą pobierane zdjęcia
-   `cookies` - ciasteczka, należy umieścić zawartość ciasteczka `ne-authidsrv`

Po przygotowaniu configu możemy odpalić skrypt przy pomocy `python index.py`

## Ostrzeżenie

Skrypt należy wykorzystywać tylko w celach edukacyjnych i nie należy rozprzestrzeniać pobranych plików, gdyż może to łamać prawa autorskie Nowej Ery.
