from django.test import TestCase
from headhot.models import Vacancy


class VacancyTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        Vacancy.objects.create(
            id='1', title='Vacancy 1', description='Long text', state='ARCHIVE', owner='45', slug='vacancy-1')
        Vacancy.objects.create(
            id='2', title='Vacancy 2', description='Very long text', state='ACTIVE', owner='5631', slug='vacancy-2')

    def test_vacancy_created(self):
        vacancy_first = Vacancy.objects.get(title='Vacancy 1')
        vacancy_second = Vacancy.objects.get(title='Vacancy 2')
        self.assertEqual(
            vacancy_first.get_vac(), "Vacancy 1 created.")
        self.assertEqual(
            vacancy_second.get_vac(), "Vacancy 2 created.")



