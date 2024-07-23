from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'contact_email', 'birth_date', 'student_usn']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'contact_email': forms.EmailInput(attrs={'placeholder': 'example@example.com'}),
        }
        labels = {
            'birth_date': 'Date of Birth',
            'student_usn': 'Student USN',
            }