from fractran import Fractran, Facteur, Fraction

# somme i + j où 1 <= i, j <= 10
somme = [Fraction(3, 2)]
facteurs = Facteur([2, 3, 5])

for i in range(1, 11):
    for j in range(1, 11):
        somme_ = Fractran(somme).run(facteurs.nombre([i, j]))
        print(f'la somme {i} + {j} vaut ' + str(facteurs.décomposition(somme_)[1]))

# produit i * j où 1 <= i, j <= 10

produit = [Fraction(455, 33),
           Fraction(11, 13),
           Fraction(1, 11),
           Fraction(3, 7),
           Fraction(11, 2),
           Fraction(1, 3)]

for i in range(1, 11):
    for j in range(1, 11):
        produit_ = Fractran(produit).run(facteurs.nombre([i, j]))
        print(f'le produit {i} * {j} vaut ' + str(facteurs.décomposition(produit_)[2]))

# suite fibonacci
print("Fibonacci rend les couples (F(n), F(n+1)) :")
fibonacci = [Fraction(23, 95),
             Fraction(57, 23),
             Fraction(17, 39),
             Fraction(130, 17),
             Fraction(11, 14),
             Fraction(35, 11),
             Fraction(19, 13),
             Fraction(1, 19),
             Fraction(35, 2),
             Fraction(13, 7),
             Fraction(7, 1)
             ]

sortie_brute = Fractran(fibonacci).suite(3, 1000)
sortie = []
for n in sortie_brute:
    if n == Facteur([2, 3]).nombre(Facteur([2, 3]).décomposition(n)):
        sortie.append(Facteur([2, 3]).décomposition(n))

print(sortie)

# nombre premier

print("Nombres premiers trouvés :")
nbs_premiers = [Fraction(17,91),
                Fraction(78,85),
                Fraction(19,51),
                Fraction(23,38),
                Fraction(29,33),
                Fraction(77,29),
                Fraction(95,23),
                Fraction(77,19),
                Fraction(1,17),
                Fraction(11,13),
                Fraction(13,11),
                Fraction(15,14),
                Fraction(15,2),
                Fraction(55,1)
                ]
sortie_brute = Fractran(nbs_premiers).suite(2, 100000)
sortie = []
for n in sortie_brute:
    exposant = Facteur([2]).décomposition(n)[0]
    if n == 2 ** exposant and exposant > 1:
        sortie.append(exposant)
print(sortie)