# Fractran 
## Explication code fibonacci
-> la liste `fibonacci` contient le programme de l'algorithme en FRACTRAN : suite d'instruction que la machine va effectuer une par une

``Fractran(fibonacci)`` crée une machine fractran configurée avec le programme ``fibonacci``

``.suite(3, 1000)`` lance cette machine en partant du nombre n = 3, et lui demande de renvoyer les 1000 premières valeurs successives de n
le résultat, liste de 1000 nombre est stocké dans ``sortie brute``

il faut maintenant filtrer les résultats pour les rangers dans la liste ``sortie``

la condition de filtrage ne garde que les valeurs de n qui sont purement de la forme 2^a * 3^b, sans aucun autre facteur premier car ce sont les moments où la machine a terminé un cycle de calcul et affiche un vrai couple de Fibonacci.

enfin ``sortie.append(Facteur([2, 3]).décomposition(n))`` calcule à nouveau les exposants ``[a, b]`` de n (qui représentent ``(F(k), F(k+1))``) avant de les ajouter à la liste ``sortie``


