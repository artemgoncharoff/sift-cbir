# Photologue app powered by CBIR library




## Структура проекта
- `cbir_main` - entrypoint to `cbir`'s commands
- `cbir` - module providing core class `CBIRCore` to manage indexes.
- `cbir_evaluation` - scripts for evalution of algortithms of Oxford Paris datasets.
- `cbir_pretratined` - pretrained weights
- `cbir_tests` - tests for `cbir` module
- `project` - django project
- `photologue` - django project's app


## Установка и настройка виртуального окружения
```
pipenv shell
pipenv install
python cbir_main.py prepare_cbir_directory_structure
python manage.py makemigrations
python manage.py migrate
```

## Запуска бэкенда и фортенда
```
python cbir_main.py --log_prefix logs/server run_server --port 8701
python manage.py runserver
```
## Перезагрузка: Очистка от предыдущих файлов
```
yes | rm db.sqlite3;
    rm -rf photologue/migrations/*; touch photologue/migrations/__init__.py && \
    python manage.py makemigrations && cp backup/0002_photosize_data.py photologue/migrations && \
    python manage.py migrate && \
    ./createsuper.sh && \
    ./clean_content.sh && \
    ./clean_cbir_state.sh
```
