from django.db import models
from jsonfield import JSONField

try:
    from django.utils import six
except ImportError:
    import six


class Vacancy(models.Model):
    """
    Vacancy Model

    """
    title = models.CharField(max_length=255, db_index=True)
    description = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    owner = models.IntegerField()
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['title']
        index_together = [
            ['id', 'slug']
        ]

    def get_vac(self):
        return self.title + ' created.'

    def __repr__(self):
        return 'Vacancy' + self.title + ' is added.'

    def __str__(self):
        return self.title
