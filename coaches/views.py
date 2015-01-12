from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.core.urlresolvers import reverse_lazy
from django import forms

# Create your views here.
from coaches.models import Coach

class CoachModelForm(forms.ModelForm):
   class Meta:
        model = Coach
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'type',
        'user', 'dossier']


class Coaches(ListView):
    model = Coach

    context_object_name = 'coaches'

    template_name = 'coaches/coach_list.html'

    paginate_by = 10

    def get_queryset(self):
        qs = Coach.objects.all()
        return qs

class CoachDetail(DetailView):
    template_name = 'coaches/coach_info.html'
    model = Coach

class CoachAdd(CreateView):
    template_name = 'coaches/coach_edit.html'
    model = Coach
    form_class = CoachModelForm
    success_url = reverse_lazy('coaches_list')

    def get_context_data(self, **kwargs):
        context = super(CoachAdd, self).get_context_data(**kwargs)
        context['title'] = 'Coach add item'
        return context


class CoachEdit(UpdateView):
    template_name = 'coaches/coach_edit.html'
    model = Coach
    form_class = CoachModelForm
    success_url = reverse_lazy('coaches_list')

    def get_context_data(self, **kwargs):
        context = super(CoachEdit, self).get_context_data(**kwargs)
        context['title'] = 'Coach update item'
        return context


class CoachDelete(DeleteView):
    template_name = 'coaches/coach_delete.html'
    model = Coach
    success_url = reverse_lazy('coaches_list')

    def get_context_data(self, **kwargs):
        context = super(CoachDelete, self).get_context_data(**kwargs)
        context['title'] = 'Coach delete item'
        return context
