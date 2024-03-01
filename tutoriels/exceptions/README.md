# Gestion des exceptions en Python

## Contexte

En programmation et en manipulation de données, différents évènement ou problématique peuvent se produire comme des fichiers manquants, des erreurs inattendues, etc. Dans ces cas, il est essentiel de savoir comment gérer de manière efficace ce type de problème, afin d’avoir un bon fonctionnement du code. Ainsi, la gestion d'exception est un concept important en programmation notamment pour le langage Python et dans de nombreux autres langages de programmation. Ce tutoriel vise à expliquer en détail ce qu'est la gestion d'exception, pourquoi elle est importante, et comment l'utiliser efficacement dans des projets Python. 

## 1. Introduction à la gestion d'exception 

La gestion d'exception permet de gérer les erreurs et les situations inhabituelles dans un programme. Elle consiste à détecter et à traiter les exceptions qui se produisent lors de l'exécution d'un code. Lorsqu'une exception se produit, Python fournit des informations détaillées sur le contexte d'une erreur, ce qui permet de rapidement trouver la cause de l’erreur et ainsi de le régler. 

Les exceptions peuvent être des erreurs ou tout autre problème imprévu qui empêche le programme de fonctionner correctement. Il est important de différencier les deux types d’erreur qui existent, qui sont les exceptions et les erreurs de syntaxe. En fait, les erreurs de syntaxe surviennent lorsqu’il y a une erreur dans la façon dont le code est écrit et c’est l’erreur la plus courante lorsque l'on apprend à utiliser Python. En revanche, les exceptions surviennent lorsqu’il y a une erreur pendant l’exécution du code malgré qu’il soit écrit correctement. Il existe plusieurs types d'exceptions.   

En effet, les raisons pour lesquelles on utilise la gestion d’exception sont qu’il permet de rendre un programme plus robuste, car la gestion appropriée des exceptions permet de détecter les erreurs inattendues et ainsi évite l’arrêt brutal du programme, si la gestion est inappropriée. 

Voici un exemple d'exception, de type NameError - la dernière ligne indique ce qui s'est passé :

 4 + spam*3

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>
  
NameError: name 'spam' is not defined


## 2. Fonctionnement de la gestion d'exception 

En Python, la gestion d'exception est réalisée à l'aide des blocs try, except et finally. Voici comment cela fonctionne : 

- Bloc try : dans le bloc try on doit mettre le code pour lequel on croit qu'il y a une exception. Si jamais il y a réellement une exception pendant l'exécution du code, le programme passe au bloc except sinon le bloc except est sautée. Également, le bloc try peut comporter plusieurs bloc except, afin de bien gérer les différents exceptions. 
  
- Bloc except : permet de gérer les erreurs, de manière appropriée, qui peuvent survenir lors de l'exécution d'un programme dans le bloc try. Ainsi, cela permet d'afficher un message d'erreur à l'utilisateur, afin de régler l'exception. Comme mentionné plus tôt, on peut avoir plusieurs blocs except pour gérer différents types d'exceptions. En effet, try et except fonctionnent ensemble. Elles permettent de tester un code qui pourrait potentiellement poser problème, dans le bloc try et de définir les actions à prendre si une exception est effectivement rencontrée, dans le bloc except.

- Bloc else : est un bloc optionnel qui vient après le bloc except. Elle est utile lorsqu'aucune exception n'est levée dans le bloc try et donc lorsqu'il n'y a aucun bloc except qui est exécuté.
  
- Bloc finally: est également un bloc optionnel qui est la dernière tâche exécutée. Si on met le bloc finally, il est toujours exécuté, qu'une exception soit levée ou non dans le bloc try. Ce bloc est utile pour gérer les opérations de nettoyage ou de fermeture dans le programme.

Voici un exemple de gestion d'exception avec try et except - Faire une division par 0 est un erreur et le type d'exception dans ce cas est ZeroDivisionError : 

try:

    x = 10 / 0
    
except ZeroDivisionError:

    print("Erreur : division par zéro")

Dans cet exemple, si une division par zéro se produit, une exception de type ZeroDivisionError est levée et le message "Erreur : division par zéro" est affiché. 

Voici un exemple avec finally - il y a une exception dans try, le fichier est introuvable, malgré ça le bloc finally sera exécuter afin de fermer le fichier : 

def lire_fichier(nom_fichier):

    try:
    
        # Code pour ouvrir et lire le fichier
        
        print("Lecture du fichier...")
        
    except FileNotFoundError:
    
        print("Fichier introuvable.")
        
    finally:
    
        # Code pour fermer le fichier (exécuté toujours)
        
        print("Fermeture du fichier...")
        

lire_fichier("mon_fichier.txt")

## 3. Utilisation de la gestion d'exception

Comme mentionné plus haut, la gestion d'exception est utile pour anticiper et gérer les erreurs dans un code. Elle permet de détecter les problèmes potentiels et de prendre des mesures appropriées pour les gérer. Par exemple, on peut utiliser la gestion d'exception pour vérifier si un fichier existe avant de l'ouvrir, pour valider des entrées utilisateur, ou pour gérer des erreurs de connexion à une base de données.

Voici un exemple qui montre l'utilisation de la gestion d'exception pour gérer des erreurs lors de l'ouverture d'un fichier :

try:

    fichier = open("exemple.txt", "r")
    
    contenu = fichier.read()
    
    fichier.close()
    
except FileNotFoundError:

    print("Erreur : le fichier n'existe pas")
    
except IOError:

    print("Erreur : impossible de lire le fichier")

Dans cet exemple, si le fichier "exemple.txt" n'existe pas ou s'il est impossible à lire, une exception est levée et un message d'erreur approprié est affiché.

De plus, il est possible de signaler une exception grâce au mot-clé **raise**. Ce mot-clé permet de déclencher manuellement une exception, ce qui veut dire qu'on peut spécifiez le type d'exception à lever. Il est également possible d'utiliser ce mot-clé pour relancer une exception dans un bloc except.

Voici un exemple dans un bloc except : 

try:

    numerateur = int(input("Entrez un numérateur : "))
    
    denominateur = int(input("Entrez un dénominateur : "))
    
    resultat = numerateur / denominateur
    
    print("Le resultat de la division est", resultat)
    
except (ValueError, ZeroDivisionError):

    print("Désolé, quelque chose ne s'est pas bien passé.")
    
    raise

## 4. Bonne pratique 

Voici une bonne pratique à suivre lors de l'utilisation de la gestion d'exception, afin d'écrire un code qui gère les exceptions de manière efficace :

- Il est très important d'être **précis** dans les types d'exceptions que l'on veut traiter, tout en laissant les erreurs imprévues se propager telles quelles.

## 5. Limites et prochaines étapes d'apprentissage

Les limites pour la gestion d'exception sont : 

- La gestion d'exception ne doit pas être trop utilisée, car cela peut rendre un code plus complexe et difficile à lire.
- Il est également important de se rappeler qu'avec la gestion d'exception on ne peut pas trouver ou règler tout les problèmes, il y a d'autres méthodes qui peuvent être plus efficace, dépendant de l'erreur ou de la problématique.


Prochaines étapes d'apprentissage:

- On peut utiliser la **journalisation** ou logging, afin d'avoir un historique et une documentation concernant les erreurs dans un code. L'utilité d'utiliser la journalisation avec la gestion d'exception est que cela permet de retracer facilement les erreurs survenues et facilite le déboguage, car on dispose d'un historique détaillé.  
  
  Voici un exemple du cours :
  
  import logging

Configuration de la journalisation dans un fichier
 
logging.basicConfig(filename='journal.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    # Code pouvant générer une erreur
    
    résultat = 10 / 0
    
except Exception as e:

    # Enregistrement de l'erreur
    
    logging.error("Une erreur s'est produite : %s", str(e))

- Un autre mot-clé intéressant que l'on peut utiliser avec la gestion d'exception est **pass** qui permet d'ignorer une exception. La même chose peut être fait pour le bloc try où pass nous permet de ne pas produire de bloc expect.

Voici le même exemple vu plus haut, mais cette fois-ci avec le mot-clé pass :

try:

    # Bloc de code où une exception pourrait se produire
    
    resultat = 10 / 0
    
except ZeroDivisionError:

    # Gestion de l'exception, mais dans ce cas, nous ne faisons rien
    
    pass


## 6. Conclusion

Pour conclure, la gestion d'exception est un outil très utile en Python qui permet de rendre l'exécution d'un code plus robuste et fiable. En utilisant des blocs try, except et finally, on peut anticiper les erreurs et définir des actions à prendre en cas d'exception. Cependant, il est important de ne pas abuser de la gestion d'exception, car cela peut rendre le code complexe et difficile à lire. 

# Bibliographie 

Python (s.d.). _Erreurs et exceptions_. Document téléaccessible à l’adresse <https://docs.python.org/fr/3/tutorial/errors.html>. Consulté le 13 février 2024.

Python 3.X (s.d.). _Les exceptions et la gestion des erreurs_. Document téléaccessible à l’adresse <https://gayerie.dev/docs/python/python3/exception.html>. Consulté le 15 février 2024.

OpenAI. "ChatGPT". Version GPT-3.5. <https://openai.com/chatgpt>. Consulté le 13 février 2024. 




 
