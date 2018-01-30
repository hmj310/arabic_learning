from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.core import serializers
import json


from .models import ConjugatedVerb, InfinitiveForm

current_verb = ""

def index(request):
    template = loader.get_template("home/home.html")
    return HttpResponse(template.render())


def verbs(request):
    arabic_verb_list = InfinitiveForm.objects.all()
    template = loader.get_template('arabic_verbs/index.html')
    context = {'arabic_verb_list': arabic_verb_list}
    return HttpResponse(template.render(context, request))


def selected_verb(request, verb):
    conjugation_list = ConjugatedVerb.objects.filter(infinitive_form__arabic_spelling=verb)
    ana_conjugation = conjugation_list.filter(pronoun__arabic_spelling='أنا')
    anta_conjugation = conjugation_list.filter(pronoun__arabic_spelling='انتَ')
    template = loader.get_template('arabic_verbs/selected_verb.html')
    context = dict(conjugation_list=conjugation_list, verb=verb, ana_conjugation=ana_conjugation,
                   anta_conjugation=anta_conjugation)
    global current_verb
    current_verb = verb
    return HttpResponse(template.render(context, request))


def nouns(request):
    arabic_verb_list = ConjugatedVerb.objects.all()
    output = ', '.join([q.arabic_spelling for q in arabic_verb_list])
    return HttpResponse(output)


def studying_verb(request):
    global current_verb
    return HttpResponse(current_verb)


def conjugations(request):
    conjugation_list = ConjugatedVerb.objects.filter(infinitive_form__arabic_spelling=current_verb)
    ana_conjugation = conjugation_list.filter(pronoun__arabic_spelling='أنا')
    output_serialized = serializers.serialize('json', ana_conjugation)

    return JsonResponse(output_serialized, safe=False)
