from django.shortcuts import render, get_object_or_404

# Create your views here.
from students.models import Student, Address, Dossier


def students_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html',
                  {'students': students})


def student_info(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/student_info.html', {'student': student})

def address_info(request, address_id):
    address = get_object_or_404(Address, id=address_id)
    return render(request, 'addresses/address_info.html', {'address': address})


def address_list(request):
    address = Address.objects.all()
    return render(request, 'addresses/address_list.html',
                  {'address': address})

def dossier_list(request):
    dossier = Dossier.objects.all()
    return render(request, 'dossier/dossier_list.html',
                  {'dossier': dossier})