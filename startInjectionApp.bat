@echo off

if exist "%cd%\venv\Scripts\activate" (
    call venv\Scripts\activate
    pip install -r requirements.txt
) else (
    pip install virtualenv
    python -m virtualenv venv
    call venv\Scripts\activate
    pip install -r requirements.txt
)

python %cd%\InjectApp\manage.py runserver 127.0.0.1:8090