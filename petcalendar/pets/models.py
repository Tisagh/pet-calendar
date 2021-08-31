from django.db import models

# models


class Pet(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    ANIMAL_CHOICES = (
        ('dog', 'dog'),
        ('cat', 'cat'),
        ('horse', 'horse'),
        ('rabbit', 'rabbit'),
    )

    animal = models.CharField(choices=ANIMAL_CHOICES, blank=True, null=True, max_length=9)
    date_of_birth = models.DateField(blank=True, null=True)
    breed = models.CharField(max_length=100)
    weight = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


class Visit(models.Model):
    visit_date = models.DateField()
    vet = models.CharField(max_length=255)
    next_visit = models.DateField()


class Treatment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class VisitDetail(models.Model):
    pet = models.ForeignKey(to='Pet', on_delete=models.CASCADE)
    treatment = models.ManyToManyField(to='Treatment', blank=True)
