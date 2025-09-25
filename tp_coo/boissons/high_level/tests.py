# Create your tests here.

from django.test import TestCase
from .models import *

class MachineModelTests(TestCase):
    def test_machine_creation(self):
        self.assertEqual(Machine.objects.count(), 0)
        l = Localisation.objects.create(nom="Labège",prix_m2=2000,taxes=0)
        local = Local.objects.create(nom="salle",surface="50",localisation = l)

        travailleur = Metier.objects.create(nom="Travailleur",remuneration=1500)
        operateur1 = RessourceHumaine.objects.create(quantite=1,metier = travailleur)

        Machine.objects.create(nom="Mélangeur", prix_achat=28_000, cout_maintenance=10, debit=10,surface=100,taux_utilisation=1,local = local)
        self.assertEqual(Machine.objects.count(), 1)

class CostsTest(TestCase):
    def test_costs(self):
        l = Localisation.objects.create(nom="Labège",prix_m2=2000,taxes=0)
        local = Local.objects.create(nom="salle",surface=50,localisation = l)
        M = Machine.objects.create(nom="Mélangeur", prix_achat=2000, cout_maintenance=0, debit=10,surface=100,taux_utilisation=1,local = local)
        M = Machine.objects.create(nom="Touilleur", prix_achat=1000, cout_maintenance=0, debit=10,surface=100,taux_utilisation=1,local = local)
        stock_eau = MatierePremiere.objects.create(nom="eau",stock=50,emprise=1)
        stock_sucre = MatierePremiere.objects.create(nom="sucre",stock=1000,emprise=1)
        approvisionnement_sucre = ApprovisionnementMatierePremiere.objects.create(matiere_premiere=stock_sucre, quantite =1000,localisation = l,prix_unitaire=10,delais=1)
        approvisionnement_eau = ApprovisionnementMatierePremiere.objects.create(matiere_premiere=stock_eau, quantite=50,localisation=l,prix_unitaire=15,delais=1) 
        self.assertEqual(local.costs(), 113750)