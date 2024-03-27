# notes

Notes - это мощный инструмент для управления вашими заметками прямо из командной строки. Никогда не теряйте важные мысли или вдохновение!


## Установка и запуск

1. Скачайте проект с репозитория.
2. Установите зависимости: `pip install -r requirements.txt`.
3. Запустите проект: `python main.py`.

## Использование

### Команда create
Создает новую заметку.

1. С передачей только заголовка: `python main.py -c "Заголовок заметки"`.
2. С передачей заголовка и текста: `python main.py -с "Заголовок заметки" "Текст заметки"`.

<img width="764" alt="Снимок экрана 2024-03-27 в 09 57 11" src="https://github.com/Misha-creato/notes/assets/84848013/54179182-a355-446e-bba8-467f5ae42d31">

### Команда list
Выводит список заметок.

`python main.py -l`.

<img width="569" alt="Снимок экрана 2024-03-27 в 09 59 42" src="https://github.com/Misha-creato/notes/assets/84848013/20fa0594-a952-40e8-94f6-37e65533959f">

### Команда edit
Редактирует конкретную заметку.

`python main.py -e {номер заметки}`.

<img width="511" alt="Снимок экрана 2024-03-27 в 10 01 01" src="https://github.com/Misha-creato/notes/assets/84848013/7a94670d-f34f-45d9-80ed-4ecb4b3db95e">

### Команда delete
Удаляет конкретную заметку.

`python main.py -d {номер заметки}`.

<img width="466" alt="Снимок экрана 2024-03-27 в 10 02 15" src="https://github.com/Misha-creato/notes/assets/84848013/1299fef2-91d8-4110-84c2-4adefdbb999f">

### Команда show
Показывает информацию о конкретной заметке.

`python main.py -s {номер заметки}`.

<img width="465" alt="Снимок экрана 2024-03-27 в 10 02 59" src="https://github.com/Misha-creato/notes/assets/84848013/4d025816-df09-48ec-a440-3c2f2ec1d0e8">

### Команда help
Выводить справку о программе.

`python main.py -h`.
