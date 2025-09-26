# Create your models here.

import json
from django.db import models

"""
models.IntegerField()
models.CharField(max_length=100)
models.ManyToManyField(Machine)

models.ForeignKey(
    Local,
    on_delete=models.PROTECT,
    # blank=True, null=True, related_name="+",
)"""

class Localisation(models.Model):
    """
    Classe représentant la localisation

    Attributs:
        nom(str):
        prix(float): en milliers d'euros
        localisation(object):
    Methodes:

    """

    nom = models.CharField(max_length=100)
    taxes = models.CharField(max_length=100)
    prix_m2 = models.FloatField()

    def __str__(self):
        return f"{self.nom}, taxes : {self.taxes}, prix au m2 : {self.prix_m2}"

    def json(self):
        """
        
        """
        return f'"nom":{self.nom},\n "taxes":{self.taxes},\n "prix_m2":{self.prix_m2}'


class MatierePremiere(models.Model):
    """
    Classe représentant un produit

    Attributs:
        nom(str): max 100 carac
        stock(int):
        emprise (float) : en m2

    Methodes:

    """

    nom = models.CharField(max_length=100)
    stock = models.IntegerField()
    emprise = models.FloatField()

    def __str__(self):
        return f"{self.nom}, stock : {self.stock} unités, emprise au sol : {self.emprise} m2"

    def json(self):
        """
        
        """
        return f'"nom":{self.nom},\n "stock":{self.stock},\n "emprise":{self.emprise}'



class QuantiteMatierePremiere(models.Model):
    """
    Classe représentant l'approvisionnement en matiere premiere

    Attributs:
        quantite(int): quantité entière
        matiere_premiere(object):
    Methodes:
    """

    quantite = models.IntegerField()
    matiere_premiere = models.ForeignKey(
        MatierePremiere,
        on_delete=models.PROTECT,
    )

    class Meta:
        abstract = True


class UtilisationMatierePremiere(QuantiteMatierePremiere):
    """
    Classe représentant l'utilisation de matiere premiere
    Hérite de QuantiteMatierePremiere
    Attributs: hérités
    Methodes:

    """

    def __str__(self):
        return "Je suis une classe qui sert à rien"
        pass

    def json(self):
        """
        
        """
        return f'"quantite":{self.quantite},\n "matiere_premiere":{self.matiere_premiere.json()}'


class ApprovisionnementMatierePremiere(QuantiteMatierePremiere):
    """
    Classe représentant l'approvisionnement en matiere premiere

    Attributs:
        quantite(int):
        matiere_premiere(object):
        localisation(object):
        prix_unitaire(float): en euros
        delais(float): en jours
    Methodes:

    """
    localisation = models.ForeignKey(
        Localisation,
        on_delete=models.PROTECT,
    )
    prix_unitaire = models.FloatField()
    delais = models.FloatField()


    def __str__(self):
        return f"Il reste {self.quantite} de {self.matiere_premiere.nom} rangés à {self.localisation.nom} pour le prix de {self.prix_unitaire}. On pourra être réaprovisionnés sous {self.delais} jours"
        pass

    def costs(self):
        """
        
        """
        cost = self.matiere_premiere.stock * self.prix_unitaire
        return cost

    def json(self):
        """
        
        """
        return f'"localisation":{self.localisation.json()},\n "prix_unitaire":{self.prix_unitaire},\n "delais":{self.delais}'


class Metier(models.Model):
    """
    Classe représentant un metier

    Attributs:
        nom(str): max 100 carac
        remuneration(float): en euro à l'annee
    Methodes:

    """

    nom = models.CharField(max_length=100)
    remuneration = models.FloatField()

    def __str__(self):
        return f"{self.nom}, remuneration : {self.remuneration}"

    def json(self):
        """
        
        """
        return f'"nom":{self.nom},\n "remuneration":{self.remuneration}'


class RessourceHumaine(models.Model):
    """
    Classe représentant des ressources inhumaines

    Attributs:
        metier(object): la classe !
        quantite(int): en victimes
    Methodes:
    """

    metier = models.ForeignKey(
        Metier,
        on_delete=models.PROTECT,
        # blank=True, null=True, related_name="+",
    )
    quantite = models.FloatField()

    def __str__(self):
        return f"{self.metier}, quantite : {self.quantite}"

    def costs(self):
        """
        
        """
        cost = self.quantite * self.metier.remuneration
        return cost

    def json(self):
        """
        
        """
        return f'"metier":{self.metier.json()},\n "quantite":{self.quantite}'


class Energie(models.Model):
    """
    Classe représentant l'énergie

    Attributs:
        nom(str): max 100 carac
        prix(float): en milliers d'euros
        localisation(object):
    Methodes:

    """

    nom = models.CharField(max_length=100)
    prix = models.FloatField()
    localisation = models.ForeignKey(
        Localisation,
        on_delete=models.PROTECT,
        # blank=True, null=True, related_name="+",
    )

    def __str__(self):
        return f"{self.nom}, prix : {self.prix}, localisation : {self.localisation}"

    def json(self):
        """
        
        """
        return f'"nom":{self.nom},\n "prix":{self.prix},\n "localisation":{self.localisation.json()}'

class DebitEnergie(models.Model):
    """
    Classe représentant le débit d'énergie

    Attributs:
        debit(float): en KW
        energie(object):Type d'énergie
    Methodes:

    """

    debit = models.FloatField()
    energie = models.ForeignKey(
        Energie,
        on_delete=models.PROTECT,
        # blank=True, null=True, related_name="+",
    )

    def __str__(self):
        return f"debit : {self.debit}, {self.energie}"

    def costs(self):
        """
        
        """
        cost = self.debit * self.energie.prix
        return cost

    def json(self):
        """
        
        """
        return f'"debit":{self.debit},\n "energie":{self.energie.json()}'

class Local(models.Model):
    """
    Classe représentant un lieu de travail
    Attributs:
        nom(str): max 100 carac
        localisation(object):
        surface(float): surface en m2
    Methodes:

    """

    nom = models.CharField(max_length=100)
    localisation = models.ForeignKey(
        Localisation,
        on_delete=models.PROTECT,
        # blank=True, null=True, related_name="+",
    )
    surface = models.FloatField()

    def __str__(self):
        return f"{self.nom}, {self.localisation}, surface : {self.surface}"

    def costs(self):
        """
        
        """
        cost = self.surface * self.localisation.prix_m2
        for m in self.machine_set.all():
            cost += m.costs()
        for am in self.localisation.approvisionnementmatierepremiere_set.all():
            cost += am.costs()
        return cost

    def json(self):
        """
        
        """
        return f'"nom":{self.nom},\n "localisation":{self.localisation.json()},\n "surface":{self.surface}'

class Produit(models.Model):
    """
    Classe représentant un produit

    Attributs:
        nom(str): max 100 carac
        prix_de_vente(float): en euro à l'unité'
        quantité(int):
        emprise (float) : en m2
        local(object): lieu de résidence du produit

    Methodes:

    """

    nom = models.CharField(max_length=100)
    prix_de_vente = models.FloatField()
    quantite = models.IntegerField()
    emprise = models.FloatField()
    local = models.ForeignKey(
        Local,
        on_delete=models.PROTECT,
        # blank=True, null=True, related_name="+",
    )

    def __str__(self):
        return f"{self.nom}, prix de vente : {self.prix_de_vente}, quantite : {self.quantite}, emprise : {self.emprise}"

    def json(self):
        """
        
        """
        return f'["nom":{self.nom},\n "prix_de_vente":{self.prix_de_vente},\n "quantite":{self.quantite},\n "emprise":{self.emprise},\n "local":{self.local.json()}]'

class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix_achat = models.FloatField()
    cout_maintenance = models.FloatField()
    debit = models.FloatField()
    surface = models.IntegerField()
    taux_utilisation = models.FloatField()
    local = models.ForeignKey(
        Local,
        on_delete=models.PROTECT,
        # blank=True, null=True, related_name="+",
    )
    operateurs = models.ManyToManyField(RessourceHumaine)

    def __str__(self):
        return f"{self.nom}, prix d'achat : {self.prix_achat}, cout de maintenance : {self.cout_maintenance}, debit : {self.debit}, surface : {self.surface}, taux d utilisation : {self.taux_utilisation}, local : {self.local}, operateurs : {self.operateurs}"

    def costs(self):
        """
        
        """
        cost = self.prix_achat + self.cout_maintenance 
        return cost

    def json(self):
        """
        
        """
        for op in self.operateurs:
            operateurs_tot += op.json()
    
        return  f'["nom":{self.nom},\n "prix_achat":{self.prix_achat},\n "cout_maintenance":{self.cout_maintenance},\n "debit":{self.debit},\n "surface":{self.surface},\n "taux_utilisation":{self.taux_utilisation},\n "local":{self.local.json()},\n "operateurs":[{operateurs_tot}]]'

class Fabrication(models.Model):
    produit = models.ForeignKey(
        Produit,
        on_delete=models.PROTECT,
        # blank=True, null=True, related_name="+",
    )
    utilisation_matiere_premiere = models.ManyToManyField(UtilisationMatierePremiere)
    machines = models.ManyToManyField(Machine)
    ressources_humaines = models.ManyToManyField(RessourceHumaine)

    def __str__(self):
        return f"{self.produit}, {self.utilisation_matiere_premiere}, {self.machines}, {self.ressources_humaines}"

    def json(self):
        """
        
        """
        produit_json = produit.json()
        for ump in utilisation_matiere_premiere:
            ump_json_tot += ump.json()    
        for m in machines:
            m_json_tot += m.json()
        for rh in ressources_humaines:
            rh_json_tot += rh.json()    
        return f'[{produit_json}\n,{rh_json_tot}\n,{m_json_tot}\n,{ump_json_tot}]'


        