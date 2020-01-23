from django.urls import path
from headhot.models import Vacancy
from .views import get_post_vacancies, get_delete_update_vacancy


urlpatterns = [

    path(
        'api/v1/vacancies/<int:pk>/',
        get_delete_update_vacancy,
        name='get_delete_update_vacancy'
    ),
    path(
        'api/v1/vacancies/',
        get_post_vacancies,
        name='get_post_vacancies'
    )
]
