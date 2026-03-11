# Laboratorium 01 – Tworzenie modelu ML w Pythonie. Zapisywanie i wersjonowanie modelu

## 1. Cel ćwiczenia
Celem ćwiczenia było:
- stworzenie prostego modelu uczenia maszynowego w Pythonie
- zapisanie go do pliku
- sprawdzenie poprawności wczytywania
- omówienie podstaw wersjonowania modelu
- różnic między środowiskiem deweloperskim a produkcyjnym


## Zadanie 1. Przygotowanie środowiska i danych

### Utworzenie środowiska wirtualnego

```bash
python3 -m venv venv
pip3 install -r requirements.txt
```

### Użyty zbiór danych
W ćwiczeniu użyto wbudowanego zbioru **Iris** z biblioteki scikit-learn.

### Krótka analiza danych

Przykładowe pierwsze wiersze danych:
| sepal length (cm) | sepal width (cm) | petal length (cm) | petal width (cm) | target |
|---:|---:|---:|---:|---:|
| 5.1 | 3.5 | 1.4 | 0.2 | 0 |
| 4.9 | 3.0 | 1.4 | 0.2 | 0 |


Informacje o danych:
- rozmiar: **150 wierszy x 5 kolumn**
- wszystkie kolumny cech mają typ `float64`
- kolumna `target` ma typ `int64`
- nazwy klas: 0 - setosa, 1 - versicolor, 2 - virginica

## Zadanie 2. Stworzenie prostego modelu ML – wariant A (scikit-learn)

### Podział danych
Dane zostały podzielone na:
- zbiór treningowy: **70%**
- zbiór testowy: **30%**

### Wytrenowanie modelu
Model **LogisticRegression** został wytrenowany na zbiorze treningowym.

### Metryki oceny modelu
Model został oceniony na zbiorze testowym przy użyciu następujących metryk:
- accuracy
- precision
- recall
- macierz pomyłek (confusion matrix)
- F1-score


## Zadanie 3. Zapisanie i ładowanie modelu


### Zapis modelu
Do zapisania modelu użyto biblioteki **joblib**.

### Wczytanie modelu i predykcja
Utworzono osobny skrypt `load_model.py`, który:
- wczytuje model z pliku
- pobiera przykładowy rekord
- wykonuje predykcję
- wyświetla wynik


## Zadanie 4. Wersjonowanie modelu w praktyce

### Dodanie modelu do repozytorium Git
Po wytrenowaniu modelu można dodać go do repozytorium:

```bash
git init
nano .gitignore
git add .
git status
git commit -m "init"

gh repo create NTPD_LAB01 --public --source=. --remote=origin --push
git remote -v
```



### Utworzenie tagu
Do oznaczenia wersji modelu można użyć tagu:

```bash
git tag -a v1.0.0 -m "Pierwsza wersja modelu ML"
git push origin v1.0.0
```

### Wykorzystany system wersjonowania modelu
W projekcie zastosowano prostą politykę wersjonowania opartą na konwencji **Semantic Versioning (SemVer)**. Wersje modeli zapisywane są w formacie:


W projekcie zastosowano prostą politykę wersjonowania opartą na konwencji **Semantic Versioning (SemVer)**. Wersje modeli zapisywane są w formacie:
`vMAJOR.MINOR.PATCH`

Przykładowa nazwa pliku modelu: `model_v1.0.0.joblib`

oraz odpowiadający jej tag w repozytorium Git: `v1.0.0`

Znaczenie poszczególnych elementów wersji:

- **MAJOR** – zwiększany w przypadku dużych zmian wpływających na działanie modelu lub jego kompatybilność, np. zmiana algorytmu uczenia maszynowego, zmiana zestawu cech wejściowych lub istotna modyfikacja procesu przygotowania danych.

- **MINOR** – zwiększany w przypadku ulepszeń modelu bez zmiany sposobu jego użycia, np. zmiana hiperparametrów, poprawa jakości modelu, rozszerzenie zbioru treningowego lub ulepszony preprocessing danych.

- **PATCH** – zwiększany przy drobnych poprawkach technicznych, które nie wpływają znacząco na działanie modelu, np. poprawki w kodzie, niewielkie zmiany w preprocessingu lub ponowne wytrenowanie modelu na bardzo podobnych danych.


## Zadanie 5. Różnice między środowiskiem deweloperskim a produkcyjnym


### Środowisko deweloperskie
Cechy:
- swobodne eksperymentowanie
- ręczne uruchamianie skryptów
- częste zmiany kodu i parametrów
- mała liczba użytkowników lub brak użytkowników końcowych
- nacisk na szybkość tworzenia rozwiązania

### Środowisko produkcyjne
Cechy:
- stabilność i niezawodność
- przewidywalność działania
- kontrola wersji modelu i danych
- bezpieczeństwo
- monitorowanie jakości działania
- możliwość automatycznego wdrażania i retrainingu


### Główne różnice i wyzwania

Podczas pracy nad modelem ML w środowisku deweloperskim model jest zwykle uruchamiany lokalnie, na mniejszych zbiorach danych i w kontrolowanych warunkach. W środowisku produkcyjnym model musi działać stabilnie, automatycznie oraz obsługiwać rzeczywiste dane i użytkowników. Powoduje to kilka dodatkowych wyzwań.

#### Zarządzanie zależnościami
W środowisku deweloperskim model może działać na różnych wersjach bibliotek. W produkcji różnice wersji mogą powodować błędy lub inne wyniki działania modelu.

Jak sobie radzić:
- używać pliku `requirements.txt`
- korzystać ze środowisk wirtualnych (`venv`, `conda`)
- w większych projektach stosować kontenery Docker

#### Powtarzalność wyników
Ważne jest, aby trening modelu był możliwy do odtworzenia w przyszłości. Ten sam kod i dane powinny prowadzić do podobnych wyników.

Jak sobie radzić:
- ustawiać parametr `random_state`
- wersjonować modele i dane
- zapisywać konfigurację treningu

#### Monitoring modelu
W środowisku produkcyjnym dane wejściowe mogą się zmieniać w czasie, co może powodować spadek jakości modelu (tzw. data drift).

Jak sobie radzić:
- monitorować metryki jakości modelu
- analizować rozkład danych wejściowych (cech)
- wykrywać spadki jakości predykcji

#### Retraining modelu
Model w produkcji może wymagać ponownego trenowania, gdy pojawią się nowe dane lub gdy jakość modelu zacznie spadać.

Jak sobie radzić:
- trenować model na nowych danych
- testować nową wersję przed wdrożeniem

#### Automatyzacja wdrożeń
W dewelopmencie model często uruchamia się ręcznie. W produkcji wdrożenia powinny być zautomatyzowane, aby zmniejszyć ryzyko błędów.

Jak sobie radzić:
- stosować pipeline CI/CD
- wdrażać model jako API lub usługę
- wykonywać testy przed publikacją nowej wersji modelu

#### Skalowalność i wydajność
W środowisku produkcyjnym model może obsługiwać dużą liczbę zapytań i większe ilości danych.

Jak sobie radzić:
- mierzyć czas odpowiedzi modelu
- optymalizować pipeline przetwarzania danych

#### Bezpieczeństwo
W produkcji model może przetwarzać dane wrażliwe lub prywatne.

Jak sobie radzić:
- ograniczać dostęp do danych i modelu
- stosować szyfrowanie transmisji
- prowadzić logowanie dostępu i audyt


## 7. Wnioski

- Zastosowanie algorytmu `LogisticRegression` z biblioteki `scikit-learn` pokazało, że nawet prosty model może osiągać dobre wyniki klasyfikacji dla odpowiednio przygotowanych danych.

- Obliczenie metryk takich jak accuracy, precision, recall i F1-score umożliwiło ocenę jakości modelu oraz lepsze zrozumienie jego skuteczności dla poszczególnych klas.

- Macierz pomyłek pozwoliła zauważyć, że model może mylić niektóre klasy częściej niż inne, co jest ważne przy analizie wyników klasyfikacji.

- Zapisanie modelu do pliku przy użyciu biblioteki joblib umożliwia jego ponowne wykorzystanie bez konieczności ponownego trenowania.

- Wersjonowanie modelu przy użyciu systemu Git i konwencji Semantic Versioning pozwala łatwiej zarządzać kolejnymi wersjami modelu i śledzić wprowadzone zmiany.

- Ćwiczenie pokazało również, że istnieją istotne różnice między środowiskiem deweloperskim a produkcyjnym, szczególnie w zakresie stabilności, monitorowania działania modelu, zarządzania zależnościami oraz automatyzacji wdrożeń.
