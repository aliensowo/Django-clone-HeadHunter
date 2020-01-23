from rest_framework import serializers
from headhot.models import Vacancy


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'title', 'description', 'state', 'owner', 'slug')