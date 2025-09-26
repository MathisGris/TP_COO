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
    path("local/<int:pk>",views.LocalDetailView.as_view(),name="Local"),
    #path("",views.LocalisationListView.as_view(),name="Localisations"),
    path("localisation/<int:pk>",views.LocalisationDetailView.as_view(),name="Localisation"),
    #path("",views.FabricationListView.as_view(),name="Fabrications"),
    path("fabrication/<int:pk>",views.FabricationDetailView.as_view(),name="Fabrication"),
    #path("",views.ProduitListView.as_view(),name="Produits"),
    path("produit/<int:pk>",views.ProduitDetailView.as_view(),name="Produit"),
    #path("",views.EnergieListView.as_view(),name="Energies"),
    path("energie/<int:pk>",views.EnergieDetailView.as_view(),name="Energie"),
    #path("",views.DebitEnergieListView.as_view(),name="DebitEnergies"),
    path("debitenergie/<int:pk>",views.DebitEnergieDetailView.as_view(),name="DebitEnergie"),
    #path("",views.MachineListView.as_view(),name="Machines"),
    path("machine/<int:pk>",views.MachineDetailView.as_view(),name="Machine"),
    #path("",views.MetierListView.as_view(),name="Metiers"),
    path("metier/<int:pk>",views.MetierDetailView.as_view(),name="Metier"),
    #path("",views.RessourceHumaineListView.as_view(),name="RessourcesHumaines"),
    path("ressourcehumaine/<int:pk>",views.RessourceHumaineDetailView.as_view(),name="RessourceHumaine"),
    #path("",views.MatierePremiereListView.as_view(),name="MatieresPremiere"),
    path("matierepremiere/<int:pk>",views.MatierePremiereDetailView.as_view(),name="MatierePremiere"),
    #path("",views.ApprovisionnementMatierePremiereListView.as_view(),name="ApprovisionnementsMatierePremiere"),
    path("approvisionnementmatierepremiere/<int:pk>",views.ApprovisionnementMatierePremiereDetailView.as_view(),name="ApprovisionnementMatierePremiere"),
    #path("",views.UtilisationMatierePremiereListView.as_view(),name="UtilisationsMatierePremiere"),
    path("utilisationmatierepremiere/<int:pk>",views.UtilisationMatierePremiereDetailView.as_view(),name="UtilisationMatierePremiere")
]
