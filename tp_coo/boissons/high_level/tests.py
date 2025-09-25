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