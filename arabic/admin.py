from django.contrib import admin

from .models import Pronoun, Mood, InfinitiveForm, ConjugatedVerb

# Register your models here.

admin.site.register(Pronoun)
admin.site.register(Mood)
admin.site.register(InfinitiveForm)
admin.site.register(ConjugatedVerb)