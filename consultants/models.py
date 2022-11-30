from django.db import models
from django.urls import reverse

from helpers.utils import path_and_rename

class Consultant(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    middle_name = models.CharField(max_length=100, null=True, blank=True)

    SEX_CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'))
    sex = models.CharField(max_length=20, choices=SEX_CHOICES, blank=True, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to = path_and_rename('consultant/image'), blank=True, null=True)


    type = models.ForeignKey('Type', null=True, blank=True, on_delete=models.DO_NOTHING)
    competence = models.TextField(null=True, blank=True)
    education = models.TextField(null=True, blank=True)
    experience = models.TextField(null=True, blank=True)
    tasks_completed = models.TextField(null=True, blank=True) 
    
    spheres = models.ManyToManyField('Sphere')
    competences = models.ManyToManyField('Competence')
    languages = models.ManyToManyField('Language')

    daily_fee = models.PositiveIntegerField(null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)

    created = models.DateField()
    updated = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('consultants:consultant-detail', kwargs={'pk' : self.pk})
    

    class Meta:
        ordering = ['-created']
        verbose_name = 'Consultant'
        verbose_name_plural = 'Consultants'



class Sphere(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    
    created = models.DateField()
    updated = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = 'Sphere'
        verbose_name_plural = 'Spheres'



class Competence(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    
    created = models.DateField()
    updated = models.DateField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Competence'
        verbose_name_plural = 'Competences'



class Language(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    
    created = models.DateField()
    updated = models.DateField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'



class Type(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    
    created = models.DateField()
    updated = models.DateField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Type'
        verbose_name_plural = 'Types'