from django.shortcuts import render, get_object_or_404 ,redirect
from datetime import datetime, date
# Create your views here.
from courses.models import Course
from django import forms


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        widgets = {
            'technology': forms.RadioSelect
        }


def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_info(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_info.html', {'course': course})


def course_edit(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses_list')
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/course_edit.html', {'form': form})


def course_delete(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('courses_list')

def course_new(request):
    course = Course.objects.create(start_date=date.today(), end_date=date.today())
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses_list')
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/course_new.html', {'form': form})