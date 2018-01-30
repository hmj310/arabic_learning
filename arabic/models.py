from django.db import models


# Create your models here.
class Pronoun(models.Model):
    pronoun = models.CharField(max_length=30)
    pronunciation = models.CharField(max_length=30)
    arabic_spelling = models.CharField(max_length=30)

    def __str__(self):
        return self.arabic_spelling


class Mood(models.Model):
    mood = models.CharField(max_length=30)

    def __str__(self):
        return self.mood


class InfinitiveForm(models.Model):
    en_meaning = models.CharField(max_length=30)
    pronunciation = models.CharField(max_length=30)
    arabic_spelling = models.CharField(max_length=30)

    def __str__(self):
        return self.arabic_spelling


class ConjugatedVerb(models.Model):

    en_meaning = models.CharField(max_length=30)
    pronunciation = models.CharField(max_length=30)
    arabic_spelling = models.CharField(max_length=30)
    infinitive_form = models.ForeignKey(InfinitiveForm, on_delete=models.CASCADE)
    pronoun = models.ForeignKey(Pronoun, on_delete=models.CASCADE)
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)

    def __str__(self):
        return self.arabic_spelling

