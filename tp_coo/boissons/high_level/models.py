# Create your models here.

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


class MatierePremiere:
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
        return f"{self.nom}, stock : {self.remuneration} unités, emprise au sol : {self.emprise} m2"

    pass


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

    def __str__(self):
        return f"Il reste {self.quantite} de {self.matiere_premiere.nom} rangés à {self.localisation.nom} pour le prix de {self.prix_unitaire}. On pourra être réaprovisionnés sous {self.delais} jours"
        pass


class Metier:
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


class RessourceHumaine:
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


class Localisation:
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


class Energie:
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


class DebitEnergie:
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


class Local:
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


class Produit:
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
    quantité = models.IntegerField()
    emprise = models.FloatField()
    local = models.ForeignKey(
        Local,
        on_delete=models.PROTECT,
        # blank=True, null=True, related_name="+",
    )

    def __str__(self):
        return f"{self.nom}, prix de vente : {self.prix_de_vente}, quantite : {self.quantite}, emprise : {self.emprise}"


class Machine:
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


class Fabrication:
    produit = models.ForeignKey(
        Produit,
        on_delete=models.PROTECT,
        # blank=True, null=True, related_name="+",
    )
    utilisations_matiere_premiere = models.ManyToManyField(UtilisationMatierePremiere)
    machines = models.ManyToManyField(Machine)
    ressources_humaines = models.ManyToManyField(RessourceHumaine)

    def __str__(self):
        return f"{self.produit}, {self.utilisation_matiere_premiere}, {self.machines}, {self.ressources_humaines}"
