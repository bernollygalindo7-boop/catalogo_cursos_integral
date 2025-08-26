# 📚 Catálogo de Cursos Online (Django)
Mini proyecto **CRUD** con **Django**: curso, duración, plataforma, dificultad.  
Metodologías: **Scrum + XP**, repositorio en **GitHub** y **CI** con GitHub Actions.

## 🚀 Requisitos
- Python 3.11 (o 3.10)
- pip

## 🔧 Instalación y ejecución
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Abrir: http://127.0.0.1:8000

## 🧪 Tests
```bash
python manage.py test
```

## 🤖 CI con GitHub Actions
Workflow en `.github/workflows/django.yml`: instala deps, migra y corre tests en cada push/PR a `main`.
