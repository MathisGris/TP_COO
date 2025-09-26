# Create your views here.

from django.views.generic import DetailView, ListView
from .models import *
from django.http import JsonResponse



class LocalListView(ListView):
    model = Local

class LocalDetailView(DetailView):
    model = Local

    def render_to_response(self, context, **response_kwargs):
        """
        
        """
        str = self.object.json()
        return JsonResponse(self.object.json())

class LocalisationListView(ListView):
    model = Localisation

class LocalisationDetailView(DetailView):
    model = Localisation

    def render_to_response(self, context, **response_kwargs):
        """
        
        """
        return JsonResponse(self.object.json())

class FabricationDetailView(DetailView):
    model = Fabrication

    def render_to_response(self, context, **response_kwargs):
        """
        
        """
        return JsonResponse(self.object.json())

class FabricationListView(ListView):
    model = Fabrication

class RessourceHumaineDetailView(DetailView):
    model = RessourceHumaine

    def render_to_response(self, context, **response_kwargs):
        """
        
        """
        return JsonResponse(self.object.json())

class RessourceHumaineListView(ListView):
    model = RessourceHumaine

class MachineDetailView(DetailView):
    model = Machine

    def render_to_response(self, context, **response_kwargs):
        """
        
        """
        return JsonResponse(self.object.json())

class MachineListView(ListView):
    model = Machine

class MetierDetailView(DetailView):
    model = Metier

    def render_to_response(self, context, **response_kwargs):
        """
        
        """
        return JsonResponse(self.object.json())

class MetierListView(ListView):
    model = Metier

class MatierePremiereDetailView(DetailView):
    model = MatierePremiere

    def render_to_response(self, context, **response_kwargs):
        """
        
        """
        return JsonResponse(self.object.json())

class MatierePremiereListView(ListView):
    model = MatierePremiere

class ApprovisionnementMatierePremiereDetailView(DetailView):
    model = ApprovisionnementMatierePremiere

    def render_to_response(self, context, **response_kwargs):
        """
        
        """
        return JsonResponse(self.object.json())

class ApprovisionnementMatierePremiereListView(ListView):
    model = ApprovisionnementMatierePremiere

class UtilisationMatierePremiereDetailView(DetailView):
    model = UtilisationMatierePremiere

    def render_to_response(self, context, **response_kwargs):
        """
        
        """
        return JsonResponse(self.object.json())

class UtilisationMatierePremiereListView(ListView):
    model = UtilisationMatierePremiere

class EnergieDetailView(DetailView):
    model = Energie

    def render_to_response(self, context, **response_kwargs):
        """
        
        """
        return JsonResponse(self.object.json())

class EnergieListView(ListView):
    model = Energie

class DebitEnergieDetailView(DetailView):
    model = DebitEnergie

    def render_to_response(self, context, **response_kwargs):
        """
        
        """
        return JsonResponse(self.object.json())

class DebitEnergieListView(ListView):
    model = DebitEnergie

class ProduitDetailView(DetailView):
    model = Produit

    def render_to_response(self, context, **response_kwargs):
        """
        
        """
        return JsonResponse(self.object.json())

class ProduitListView(ListView):
    model = Produit

