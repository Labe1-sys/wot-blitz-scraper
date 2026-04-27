@echo off
:: 1. Active l'environnement virtuel
call .venv\Scripts\activate
:: 2. Lance le script python
python main.py
:: 3. Reste ouvert pour voir le résultat
pause