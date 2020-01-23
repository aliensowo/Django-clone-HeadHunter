import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from headhot.models import Vacancy
from api.serializers import VacancySerializer

# initialize the APIClient app
client = Client()


class GetAllVacanciesTest(TestCase):
    """ Test module for GET all vacancies API """

    def setUp(self):
        Vacancy.objects.create(
            id='1', title='Vacancy 1', description='Long text', state='ARCHIVE', owner='45', slug='vacancy-1')
        Vacancy.objects.create(
            id='2', title='Vacancy 2', description='Very long text', state='ACTIVE', owner='5631', slug='vacancy-2')

    def test_get_all_vacancies(self):
        # get API response
        response = client.get(reverse('get_post_vacancies'))
        # get data from db
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleVacancyTest(TestCase):
    """ Test module for GET single vacancy API """
    def setUp(self):
        self.first = Vacancy.objects.create(
            id='1', title='Vacancy 1', description='Long text', state='ARCHIVE', owner='45', slug='vacancy-1')
        self.second = Vacancy.objects.create(
            id='2', title='Vacancy 2', description='Very long text', state='ACTIVE', owner='5631', slug='vacancy-2')

    def test_get_valid_single_vacancy(self):
        response = client.get(
            reverse('get_delete_update_vacancy', kwargs={'pk': self.first.pk}))
        vacancy = Vacancy.objects.get(pk=self.first.pk)
        serializer = VacancySerializer(vacancy)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_vacancy(self):
        response = client.get(
            reverse('get_delete_update_vacancy', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewVacancyTest(TestCase):
    """ Test module for inserting a new vacancy """
    def setUp(self):
        self.valid_payload = {
            'id': '1',
            'title': 'Vacancy 1',
            'description': 'Long text',
            'state': 'ARCHIVE',
            'owner': '45',
            'slug': "vacancy-1"
        }
        self.invalid_payload = {
            'id': '1',
            'title': '',
            'description': 'Long text',
            'state': 'ARCHIVE',
            'owner': '45',
            'slug': "vacancy-1"
        }

    def test_create_valid_vacancy(self):
        response = client.post(
            reverse('get_post_vacancies'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_vacancy(self):
        response = client.post(
            reverse('get_post_vacancies'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleVacancyTest(TestCase):
    """ Test module for updating an existing vacancy record """
    def setUp(self):
        self.first = Vacancy.objects.create(
            id='1', title='Vacancy 1', description='Long text', state='ARCHIVE', owner='45', slug='vacancy-1')
        self.second = Vacancy.objects.create(
            id='2', title='Vacancy 2', description='Very long text', state='ACTIVE', owner='5631', slug='vacancy-2')
        self.valid_payload = {
            'id': '1',
            'title': 'Vacancy 1',
            'description': 'Long text',
            'state': 'ARCHIVE',
            'owner': '45',
            'slug': "vacancy-1"
        }
        self.invalid_payload = {
            'id': '1',
            'title': '',
            'description': 'Long text',
            'state': 'ARCHIVE',
            'owner': '45',
            'slug': "vacancy-1"
        }

    def test_valid_update_vacancy(self):
        response = client.put(
            reverse('get_delete_update_vacancy', kwargs={'pk': self.first.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_vacancy(self):
        response = client.put(
            reverse('get_delete_update_vacancy', kwargs={'pk': self.first.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleVacancyTest(TestCase):
    """ Test module for deleting an existing vacancy record """
    def setUp(self):
        self.first = Vacancy.objects.create(
            id='1', title='Vacancy 1', description='Long text', state='ARCHIVE', owner='45', slug='vacancy-1')
        self.second = Vacancy.objects.create(
            id='2', title='Vacancy 2', description='Very long text', state='ACTIVE', owner='5631', slug='vacancy-2')

    def test_valid_delete_vacancy(self):
        response = client.delete(
            reverse('get_delete_update_vacancy', kwargs={'pk': self.second.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_vacancy(self):
        response = client.delete(
            reverse('get_delete_update_vacancy', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)