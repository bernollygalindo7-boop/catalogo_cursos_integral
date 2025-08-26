from django.test import TestCase
from .models import Curso

class CursoModelTest(TestCase):
    def test_crear_curso(self):
        c = Curso.objects.create(
            nombre="Python Básico",
            duracion="10 horas",
            plataforma="Udemy",
            dificultad="Básico",
        )
        self.assertEqual(Curso.objects.count(), 1)
        self.assertIn("Python Básico", str(c))
