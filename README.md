# Nowa Era Downloader

Jakiś tam gówno kod napisany przez AI do pobierania zdjęć stron ebooków Nowej Ery i zrobienia z nich pdfa.

## Użycie

Aby użyć skryptu należy zmienić nazwę pliku `config.json.example` na `config.json` i wypełnić go prawidłowymi danymi:

-   `url` - link do zdjęcia strony (numer strony należy zamienić na `XXX`)
-   `number_of_pages` - liczba stron ebooka
-   `download_folder` - folder, gdzie będą pobierane zdjęcia
-   `output_pdf` - ścieżka pdfa, który zostanie utworzony
-   `cookies` - ciasteczka, należy umieścić zawartość ciasteczka `ne-authidsrv`

Po przygotowaniu configu możemy odpalić skrypt przy pomocy `python index.py`

## Ostrzeżenie

Skrypt należy wykorzystywać tylko w celach edukacyjnych i nie należy rozprzestrzeniać pobranych plików, gdyż może to łamać prawa autorskie Nowej Ery.
