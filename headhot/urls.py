from django.urls import path
from .models import Vacancy
from .views import VacancyList


urlpatterns = [

    path(
        '',
        VacancyList,
        name = 'VacancyList'
    )
]
