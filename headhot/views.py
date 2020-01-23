from django.shortcuts import render,get_object_or_404
from .models import Vacancy


def VacancyList(request, slug=None):
    vacancy = None
    vacancies = Vacancy.objects.all()
    if slug:
        vacancy = get_object_or_404(Vacancy, slug=slug)
    return render(request, 'base.html', {
        'vacancy': vacancy,
        'vacancies': vacancies
    })