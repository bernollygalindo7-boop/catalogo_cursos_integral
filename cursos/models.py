from django.db import models

class Curso(models.Model):
    DIFICULTAD_CHOICES = [
        ('Básico', 'Básico'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
    ]

    nombre = models.CharField(max_length=200)
    duracion = models.CharField(max_length=50)   # Ej: "10 horas", "6 semanas"
    plataforma = models.CharField(max_length=100)
    dificultad = models.CharField(max_length=20, choices=DIFICULTAD_CHOICES)

    def __str__(self):
        return f"{self.nombre} ({self.plataforma})"

#Para estudiantes
class Estudiante(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    contraseña=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
