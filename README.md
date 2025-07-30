# Instap Box

Prosta aplikacja Python z modułami Instap Box i Modbus.

## Struktura projektu

```
instap-box/
├── main.py                 # Główny plik aplikacji
├── run.sh                  # Skrypt uruchamiający
├── requirements.txt        # Zależności Python
├── README.md              # Ten plik
└── instap/                # Pakiet główny
    ├── __init__.py
    ├── box.py             # Główny moduł Instap Box
    ├── item.py            # Moduł do pobierania danych z API
    ├── logger.py          # Konfiguracja globalnego loggera
    └── modbus/            # Pakiet Modbus
        ├── __init__.py
        ├── register.py    # Moduł rejestrów Modbus
        └── processor.py   # Moduł procesora Modbus
```

## Uruchamianie

### Metoda 1: Używając skryptu shell
```bash
# Ustaw zmienną środowiskową
export INSTAP_BOX=twoja_wartosc

# Uruchom aplikację
./run.sh
```

### Metoda 2: Bezpośrednio przez Python
```bash
# Uruchom aplikację z wymaganym argumentem
python3 main.py --instap-box twoja_wartosc

# Lub z dodatkowymi opcjami logowania
python3 main.py --instap-box twoja_wartosc --log-level DEBUG
python3 main.py --instap-box twoja_wartosc --log-level INFO --log-file app.log
```

### Metoda 3: Inline z zmienną środowiskową
```bash
INSTAP_BOX=twoja_wartosc ./run.sh
```

## Opcje logowania

Aplikacja obsługuje zaawansowane opcje logowania:

### Poziomy logowania
- `DEBUG` - Szczegółowe informacje debugowania
- `INFO` - Informacje ogólne (domyślny)
- `WARNING` - Ostrzeżenia
- `ERROR` - Błędy

### Przykłady użycia
```bash
# Domyślny poziom INFO
python3 main.py --instap-box test-box

# Szczegółowe logowanie debug
python3 main.py --instap-box test-box --log-level DEBUG

# Tylko błędy i ostrzeżenia
python3 main.py --instap-box test-box --log-level WARNING

# Logowanie do pliku
python3 main.py --instap-box test-box --log-file app.log

# Kombinacja opcji
python3 main.py --instap-box test-box --log-level DEBUG --log-file debug.log
```

## Wymagania

- Python 3.6+
- Zależności (jeśli potrzebne) - patrz `requirements.txt`

## Instalacja zależności

```bash
pip install -r requirements.txt
``` 