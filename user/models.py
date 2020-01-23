from django.db import models


class User(models.Model):
    """"
    User model
    """
    name = models.CharField(max_length=50, unique=True, db_index=True)
    own_vacancy = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


