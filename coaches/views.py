from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

# Create your views here.
from coaches.models import Coach


# def coaches_list(request):
#     coaches = Coach.objects.all()
#     return render(request, 'coaches/coach_list.html', {'coaches': coaches})

class Coaches(ListView):
    model = Coach

    context_object_name = 'coaches'

    template_name = 'coaches/coach_list.html'

    paginate_by = 10

    def get_queryset(self):
        qs = Coach.objects.all()
        return qs


def coach_info(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    return render(request, 'coaches/coach_info.html', {'coach': coach})

class CoachDetail(DetailView):

    model = Coach

    def get_context_data(self, coach_id):
        context = super(CoachDetail, self).get_context_data()
        context['coach'] = get_object_or_404(Coach, id=coach_id)
        return context