from django.shortcuts import render, get_object_or_404

# Create your views here.
from courses.models import Course


def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_info(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_info.html', {'course': course})