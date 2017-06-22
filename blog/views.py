# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Bienvenue sur mon blog !</h1>
              <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)

def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """
    return HttpResponse(
        "Vous avez demandé les articles de {0} {1}.".format(month, year)
    )

from django.http import HttpResponse, Http404

def view_article(request, id_article):
    # Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
    if int(id_article) > 100:
        raise Http404

    return HttpResponse('<h1>Mon article ici</h1>')

from django.http import HttpResponse, Http404
from django.shortcuts import redirect

def view_article(request, id_article):
    if int(id_article) > 100:
        raise Http404

    return redirect(view_article, id_article=42)

def view_redirection(request):
    return HttpResponse("Vous avez été redirigé.")
