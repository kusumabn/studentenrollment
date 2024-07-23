from django.db import models
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_email = models.EmailField(unique=True)
    birth_date = models.DateField()
    student_usn = models.CharField(max_length=20, unique=True)

    def _str_(self):
        return f"{self.first_name} {self.last_name}"