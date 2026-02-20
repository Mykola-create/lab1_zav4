1. Створення віртуального оточення:

python -m venv venv

2. Активація віртуального середовища для Windows:

source venv/Scripts/activate

3. Встановлення бібліотеки:

pip install requests

4. Для запуску простої програми:

python main.py

4. Збереження списку залежностей:

pip freeze > requirements.txt

5. Встановлення залежностей із файлу:

pip install -r requirements.txt

6. Перевірка вразливостей:
АБО через  pip-audit:

pip-audit -r requirements.txt

АБО через safety:

safety check -r equirements.txt