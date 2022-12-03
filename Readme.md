# Proyecto Backend de Subastas con Django

## Instalar dependencias del proyecto
```
pip install pipenv
pipenv install -r requirements.txt
```

## Correr el proyecto
```
pipenv shell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Abrir [http://localhost:8000](http://localhost:8000) para ver en el navegador.

## Agregar categorías de productos

Abrir [http://localhost:8000/admin](http://localhost:8000/admin) para acceder al portal administrativo.\
Iniciar sesión con el super usuario creado.\
Seleccionar Categorys y agregar algunas.