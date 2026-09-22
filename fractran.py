import math

class Fraction:
    def __init__(self, numérateur, dénominateur):

        self.numérateur = numérateur
        self.dénominateur = dénominateur

    def est_entier(self, n):
        return n % self.dénominateur == 0

    def valeur(self, n):
        return self.numérateur * (n // self.dénominateur)

    def __repr__(self):
        return f"Fraction(num={self.numérateur}, den={self.dénominateur})"

    #code de la méthode __eq__ pour le test du constructeur de Fractran
    def __eq__(self, other):
        return self.numérateur == other.numérateur and self.dénominateur == other.dénominateur


class Facteur:
    def __init__(self, nombres_premier):
        self.facteurs = nombres_premier

    def nombre(self, coeffs):
        return math.prod(self.facteurs[i]**coeffs[i] for i in range(len(coeffs)))

    def décomposition(self, n):
        décomp = [0]*len(self.facteurs)
        i = 0
        while n != 1 and i <= len(self.facteurs)-1 and n != 0:
            if n % self.facteurs[i] == 0:
                n = n // self.facteurs[i]
                décomp[i] += 1
            else:
                i += 1
        return décomp


class Fractran:
    def __init__(self, fractions):
        self.programme = fractions
        self.liste = []
    def run(self, n, N = None):
        i = 0
        self.liste.append(n)
        while i < len(self.programme):
            if N is not None and len(self.liste) >= N:
                break
            if self.programme[i].est_entier(n):
                n = self.programme[i].valeur(n)
                self.liste.append(n)
                i = 0
            else:
                i += 1
        return n
    def suite(self, n, N):
        self.run(n,N)
        return self.liste[:N]

