from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .forms import StudentRegistrationForm
from .models import Student
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def register_student(request):
    form = StudentRegistrationForm()
    return render(request, 'register.html', {'form': form})

def ajax_register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False})

def export_students_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="student_list.csv"'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Lastname', 'Email', 'Birth Date', 'USN'])

    students = Student.objects.all().values_list('first_name', 'last_name', 'contact_email', 'birth_date', 'student_usn')
    for student in students:
        writer.writerow(student)

    return response

def export_students_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="student_list.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 750, "Student List")
    p.setFont("Helvetica", 12)
    p.drawString(100, 735, "==================")

    p.setFont("Helvetica-Bold", 10)
    headers = ["First Name", "Last name", "Email", "Birth Date", "USN"]
    y = 710
    x = 50
    x_offsets = [50, 110, 200, 340, 450]  # Adjusted column positions

    for index, header in enumerate(headers):
        p.drawString(x_offsets[index], y, header)

    p.setFont("Helvetica", 10)
    y = 690
    students = Student.objects.all()
    for student in students:
        p.drawString(x_offsets[0], y, student.first_name)
        p.drawString(x_offsets[1], y, student.last_name)
        p.drawString(x_offsets[2], y, student.contact_email)
        p.drawString(x_offsets[3], y, str(student.birth_date))
        p.drawString(x_offsets[4], y, student.student_usn)
        y -= 15
        if y < 50:
            p.showPage()
            p.setFont("Helvetica", 10)
            y = 750
            for index, header in enumerate(headers):
                p.drawString(x_offsets[index], y, header)
            y -= 15

    p.showPage()
    p.save()
    return response