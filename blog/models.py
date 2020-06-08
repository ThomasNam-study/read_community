from django.db import models


class Post(models.Model):
    title = models.CharField('TITLE', max_length=50),

