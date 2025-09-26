"""
URL configuration for boissons project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from high_level import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("local/",views.LocalListView.as_view(),name="Locals"),
    path("local/",views.LocalDetailView.as_view(),name="Local"),
    path("",views.LocalisationListView.as_view(),name="Localisations"),
    path("",views.LocalisationDetailView.as_view(),name="Localisation"),
    path("",views.FabricationListView.as_view(),name="Fabrications"),
    path("",views.FabricationDetailView.as_view(),name="Fabrication"),
    path("",views.ProduitListView.as_view(),name="Produits"),
    path("",views.ProduitDetailView.as_view(),name="Produit"),
    path("",views.EnergieListView.as_view(),name="Energies"),
    path("",views.EnergieDetailView.as_view(),name="Energie"),
    path("",views.DebitEnergieListView.as_view(),name="DebitEnergies"),
    path("",views.DebitEnergieDetailView.as_view(),name="DebitEnergie"),
    path("",views.MachineListView.as_view(),name="Machines"),
    path("",views.MachineDetailView.as_view(),name="Machine"),
    path("",views.MetierListView.as_view(),name="Metiers"),
    path("",views.MetierDetailView.as_view(),name="Metier"),
    path("",views.RessourceHumaineListView.as_view(),name="RessourcesHumaines"),
    path("",views.RessourceHumaineDetailView.as_view(),name="RessourceHumaine"),
    path("",views.MatierePremiereListView.as_view(),name="MatieresPremiere"),
    path("",views.MatierePremiereDetailView.as_view(),name="MatierePremiere"),
    path("",views.ApprovisionnementMatierePremiereListView.as_view(),name="ApprovisionnementsMatierePremiere"),
    path("",views.ApprovisionnementMatierePremiereDetailView.as_view(),name="ApprovisionnementMatierePremiere"),
    path("",views.UtilisationMatierePremiereListView.as_view(),name="UtilisationsMatierePremiere"),
    path("",views.UtilisationMatierePremiereDetailView.as_view(),name="UtilisationMatierePremiere")
]
