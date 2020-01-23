from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from headhot.models import Vacancy
from .serializers import VacancySerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_vacancy(request, pk):
    try:
        vacancy = Vacancy.objects.get(pk=pk)
    except Vacancy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # get details of a single vacancy
    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)
    # update details of a single vacancy
    if request.method == 'PUT':
        serializer = VacancySerializer(vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # delete a single vacancy
    if request.method == 'DELETE':
        vacancy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def get_post_vacancies(request):
    # get all vacancies
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
    # insert a new record for a vacancy
    elif request.method == 'POST':
        data = {
            'id': int(request.data.get('id')),
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'state': request.data.get('state'),
            'owner': int(request.data.get('owner')),
            'slug': request.data.get('slug'),
        }
        serializer = VacancySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



