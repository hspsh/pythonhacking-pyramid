# Pyramid HS

## 1. Wystartowanie projektu

- Załóż/Aktywuj virtualenva
    
    W przypadku `virtualenv wrappera`:

    `mkvirtualenv -p python3 <your_venv_name>`
    
    `workon <your_venv_name>`

- Zainstaluj zależności jeśli dopiero utworzyłeś venva:

    `pip install --upgrade pip setuptools`

    `pip install -e ".[testing]"`

- Zainicjuj bazę danych:

    `initialize_pyramid_hs_db development.ini`

- Wystartowanie testów:

    `pytest`

- Wystartowanie projektu.

    `pserve development.ini`

## 2. Spotkania

### Pierwsze

#### Wygenerowaliśmy projekt

Skorzystaliśmy z [cookicuttera](https://github.com/Pylons/pyramid-cookiecutter-alchemy)

#### Widoki HTML

Stworzyliśmi przykładowy widok do serwowania odpowiedzi z html.
Widok dostępny pod adresem `/hello_h/`

#### JSON

Stworzyliśmy przykładowy widok do serwowania odpowiedzi z jsonem.
Widok dostępny pod adresem `/hello_j/`

### Drugie

#### Formularze

Przygotowaliśmy przykładową obsługę formularza html.
Widok dostępny pod adresem `/form/`
