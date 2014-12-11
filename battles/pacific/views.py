from django.shortcuts import render
from django.views import generic
from . import models

# Create your views here.
class MainView(generic.TemplateView):
    """ Loads the main page"""
    template_name = 'main.html'

class CampaignMapView(generic.TemplateView):
    """ Loads the main page"""
    template_name = 'base_map_page.html'

class HistoryView(generic.TemplateView):
    """ Loads the main page"""
    template_name = 'history.html'

class BattleMapView(generic.DetailView):
    """Load the Guadalcanal map."""
    model = models.Battle
    template_name = 'battle_map.html'
    context_object_name = "battle"

class LinkView(generic.TemplateView):
    """ Loads the links page"""
    template_name = 'links.html'