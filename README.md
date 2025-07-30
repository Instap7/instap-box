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
# Ustaw zmienną środowiskową
export INSTAP_BOX=twoja_wartosc

# Uruchom aplikację
python3 main.py
```

### Metoda 3: Inline z zmienną środowiskową
```bash
INSTAP_BOX=twoja_wartosc ./run.sh
```

## Wymagania

- Python 3.6+
- Zależności (jeśli potrzebne) - patrz `requirements.txt`

## Instalacja zależności

```bash
pip install -r requirements.txt
``` 