from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from students.models import Student, Address, Dossier
from django import forms


class StudentForm(forms.Form):
    PACKAGE_CHOICES = (
        ('standart', 'Standart'),
        ('gold', 'Gold'),
        ('vip', 'VIP'),
    )
    student_name = forms.CharField(max_length=100)
    # student_package = forms.ChoiceField(choices=PACKAGE_CHOICES, widget=forms.ChoiceField, )

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'package']
        widgets = {
            'package': forms.RadioSelect
        }


def students_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html',
                  {'students': students})


def student_info(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/student_info.html', {'student': student})


def student_edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/student_edit.html', {'form': form})


def student_new(request):
    student = Student.objects.create()
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/student_new.html', {'form': form})


def student_delete(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('students_list')


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