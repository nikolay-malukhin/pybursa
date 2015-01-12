# coding=utf-8
from django.shortcuts import render, get_object_or_404 ,redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
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

class Courses(ListView):
    model = Course

    context_object_name = 'courses'

    template_name = 'courses/course_list.html'

    paginate_by = 10

    def get_queryset(self):
        qs = Course.objects.all()
        return qs


class CourseDetail(DetailView):
    template_name = 'courses/course_info.html'
    model = Course


class CourseEdit(UpdateView):
    template_name = 'courses/course_edit.html'
    model = Course
    form_class = CourseModelForm
    success_url = reverse_lazy('course_list')

    def get_context_data(self, **kwargs):
        context = super(CourseEdit, self).get_context_data(**kwargs)
        context['title'] = 'Course update item'
        return context


class CourseDelete(DeleteView):
    template_name = 'courses/course_delete.html'
    model = Course
    success_url = reverse_lazy('courses_list')

    def get_context_data(self, **kwargs):
        context = super(CourseDelete, self).get_context_data(**kwargs)
        context['title'] = 'Course delete item'
        return context

#
# def course_new(request):
#     course = Course.objects.create(start_date=date.today(), end_date=date.today())
#     if request.method == 'POST':
#         form = CourseModelForm(request.POST, instance=course)
#         if form.is_valid():
#             form.save()
#             return redirect('courses_list')
#     else:
#         form = CourseModelForm(instance=course)
#     return render(request, 'courses/course_new.html', {'form': form}


class CourseAdd(CreateView):
    template_name = 'courses/course_edit.html'
    model = Course
    form_class = CourseModelForm
    success_url = reverse_lazy('course_list')

    def get_context_data(self, **kwargs):
        context = super(CourseAdd, self).get_context_data(**kwargs)
        context['title'] = 'Course add item'
        return context