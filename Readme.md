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
Abrir navegador en http://127.0.0.1:8000/
```

## Agregar categorías de productos
```
Abrir navegador en http://127.0.0.1:8000/admin
Iniciar sesión con el super usuario creado
Seleccionar Categorys y agregar algunas
```