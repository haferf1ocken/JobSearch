"""
Definition of models.
"""

from django.db import models


class User(models.Model):
    fullname = models.CharField(max_length=50, verbose_name='fullname')
    education = models.CharField(max_length=50, verbose_name='education')
    experience = models.CharField(max_length=50, verbose_name='experience')
    summary = models.FileField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'users'

    def __str__(self):
        return self.fullname


class Employer(models.Model):
    name = models.CharField(max_length=50, verbose_name='name company')
    address = models.CharField(max_length=50, verbose_name='address')

    class Meta:
        verbose_name_plural = 'employers'

    def __str__(self):
        return self.name


class Intership(models.Model):
    name = models.CharField(max_length=50, verbose_name='name intership')
    experience = models.CharField(max_length=50, verbose_name='experience')
    company = models.ForeignKey(Employer, null=True, on_delete=models.CASCADE, verbose_name='employer id')
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='user id')

    class Meta:
        verbose_name_plural = 'interships'

    def __str__(self):
        return self.name
