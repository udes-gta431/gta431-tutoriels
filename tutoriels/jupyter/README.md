# Jupyter Notebook et PyCharm : Comparaison et Utilisation
## Introduction
Dans ce tutoriel, nous explorerons deux environnements de développement populaires de Python : Jupyter Notebook et PyCharm. Ces environnements ont déjà été vu en classe donc nous ferons un cours résumé de leurs fonctionnalité, et de leur manière de les utiliser pour développer des projets Python. De plus, nous aborderons leurs 4 grandes différences pour bien sélectionner votre environnement de travail.  Nous finirons également par des exemples de code pour illustrer les différences.

## Partie 1: Jupyter Notebook

 **Qu'est-ce que Jupyter Notebook ?** 
 
 Jupyter Notebook est une application web open source qui permet de créer et de partager des documents contenant du code, des visualisations et du texte explicatif. Il est largement utilisé dans les domaines de la science des données, de l'apprentissage automatique, de la recherche scientifique et de l'éducation. Anciennement appelé IPython Notebooks

 **Pourquoi utiliser Jupyter Notebook ?** 
 
 * **Intégration de code et de texte**: Jupyter Notebook permet d'intégrer du code Python avec du texte narratif, ce qui facilite la création de documents interactifs et explicatifs. *Les notebooks sont des cellules de codes*.

* **Visualisation interactive**: Vous pouvez créer des visualisations de données directement dans le notebook et les rendre interactives grâce à des bibliothèques telles que Matplotlib et Plotly.

* **Facilité de partage** : Les notebooks peuvent être partagés facilement sous forme de fichiers .ipynb ou via des plateformes telles que GitHub, Google Colab, etc.

**Foctionnement de l'environnement ?**

Jupyter Notebook est une application web open-source qui vous permet de créer et de partager des documents qui contiennent à la fois du ***code en direct***, *des équations*, *des visualisations* et du *texte narratif*. 

**Voici les composantes de Jupyter Notebook** :
--

**Serveur Jupyter** : Lorsque vous lancez Jupyter Notebook, un serveur web local est démarré sur votre machine. Ce serveur est responsable de l'exécution du code, de la gestion des sessions utilisateur et de la communication avec votre navigateur web.

* **Kernel** : L'un des concepts clés de Jupyter est le kernel. Un [kernel est un programme informatique](https://www.romaglushko.com/blog/jupyter-kernel-architecture/) qui exécute du code dans un langage spécifique (par exemple, Python, R, Julia, etc.). Lorsque vous créez un nouveau notebook, vous sélectionnez un kernel associé au langage dans lequel vous voulez écrire votre code. Le kernel est responsable de l'exécution du code que vous saisissez dans les cellules du notebook.

![Image and Preview Themes on the toolbar](https://www.romaglushko.com/blog/jupyter-kernel-architecture/jupyter-kernel-overview.png) 

* **Environnement d'exécution** : Chaque notebook s'exécute dans son propre environnement d'exécution, qui est contrôlé par le kernel associé. Cela signifie que les variables et les fonctions que vous définissez dans une cellule sont accessibles aux autres cellules dans le même notebook, mais pas nécessairement à d'autres notebooks ou environnements d'exécution.

* **Communication avec le navigateur** : Une fois que le serveur Jupyter est en cours d'exécution, vous pouvez interagir avec votre notebook via votre navigateur web. Le navigateur envoie des requêtes au serveur pour obtenir des mises à jour sur l'état du notebook, pour exécuter du code dans les cellules, et pour afficher les résultats.

* **Structure du notebook** : Le notebook est divisé en cellules, qui peuvent être de différents types, tels que code, texte, ou encore des cellules contenant des équations mathématiques. Vous pouvez exécuter chaque cellule individuellement, ce qui permet une exploration interactive et incrémentielle des données et du code.

En somme , Jupyter Notebook combine un serveur local, des kernels pour exécuter du code dans différents langages, et une interface utilisateur basée sur le navigateur pour créer un environnement interactif et collaboratif pour l'analyse de données, la visualisation, l'apprentissage machine, etc. 

![Image and Preview Themes on the toolbar](https://global.discourse-cdn.com/standard11/uploads/jupyter/original/2X/d/db350abab5848c85709675265441573e32aaf9c0.png) 
## Partie 2: PyCharm

 **Qu'est-ce que PyCharm ?** 

[PyCharm](https://realpython.com/pycharm-guide/) est un environnement de développement intégré (IDE) pour Python, développé par JetBrains. Il offre des fonctionnalités avancées pour le développement Python, y compris un éditeur de code puissant, un débogueur, et une intégration avec des outils de gestion de versions.

**Pourquoi utiliser PyCharm ?**

* **Fonctionnalités avancées**: PyCharm offre un ensemble complet d'outils pour le développement Python, y compris un débogueur, un éditeur de code avancé, et des fonctionnalités de refactoring.

* **Gestion de projet intégrée** : PyCharm facilite la gestion de projets Python complexes avec son support pour les environnements virtuels, les gestionnaires de paquets, et les systèmes de contrôle de version.

* **Support pour les tests unitaires**: PyCharm offre un support intégré pour l'écriture et l'exécution de tests unitaires Python.

## Partie 3: Les 4 plus grandes différences


Jupyter Notebook et PyCharm sont deux environnements de développement populaires pour Python, mais ils diffèrent dans leur conception, leurs fonctionnalités et leur utilisation. Voici quatre grandes différences entre les deux :


### Mode interactif vs Environnement de développement intégré (IDE):
------
Jupyter Notebook est principalement utilisé pour le développement interactif et l'exploration des données. Il permet d'écrire et d'exécuter du code Python par sections, ce qui est idéal pour l'analyse exploratoire, la visualisation de données et le prototypage rapide.

PyCharm, en revanche, est un environnement de développement intégré (IDE) plus traditionnel, conçu pour le développement de projets Python complexes. Il offre un ensemble complet d'outils de développement, y compris un éditeur de code avancé, un débogueur, un gestionnaire de projets, et des fonctionnalités de refactoring.

### Types de projets:
-----

Jupyter Notebook est souvent utilisé pour des tâches telles que l'analyse de données, l'apprentissage automatique, la recherche scientifique, et l'enseignement. Il est particulièrement adapté pour créer des documents interactifs et des rapports.

PyCharm est plus adapté pour le développement de projets Python de grande envergure, y compris les applications web, les applications de bureau, les bibliothèques, et les projets d'équipe. Il offre des fonctionnalités avancées pour la gestion de projets et la collaboration.

### Interface utilisateur:
-----

Jupyter Notebook a une interface utilisateur basée sur un navigateur web, ce qui le rend facile à utiliser et à partager. Les cellules de code et de texte peuvent être organisées dans un document interactif, avec la possibilité d'exécuter et de modifier le code à la volée.

PyCharm a une interface utilisateur basée sur une application de bureau, avec une disposition plus traditionnelle des fenêtres et des onglets. Il offre une expérience de développement plus complète avec des fonctionnalités telles que la coloration syntaxique, la complétion automatique, et le débogage intégré.

### Flexibilité et polyvalence:
-----

Jupyter Notebook est particulièrement flexible et polyvalent, car il permet d'intégrer du code, du texte explicatif, des visualisations, et même des équations mathématiques dans un seul document interactif. Il est largement utilisé dans les domaines de la science des données, de l'apprentissage automatique, et de la recherche scientifique.

PyCharm offre une expérience de développement plus structurée et ciblée, avec des fonctionnalités spécifiques pour le développement de logiciels Python de grande envergure. Il est mieux adapté pour les projets de développement de logiciels plus traditionnels et pour les développeurs qui préfèrent une interface de développement plus classique.

En somme, Jupyter Notebook est idéal pour l'exploration des données et la création de documents interactifs, tandis que PyCharm est mieux adapté pour le développement de projets Python de grande envergure avec un ensemble complet d'outils de développement. Le choix entre les deux dépendra des besoins spécifiques du projet et des préférences personnelles du développeur.

***Consulter cette source pour encore plus d'éléments de comparaison***: [Geeks fo Geeks](https://www.geeksforgeeks.org/difference-between-jupyter-and-pycharm/) :-)



# Conclusion
Dans ce tutoriel, nous avons exploré deux environnements de développement populaires pour Python : Jupyter Notebook et PyCharm. Nous avons discuté de leurs fonctionnalités, de leurs avantages et inconvénients, et de la manière de les utiliser pour développer des projets Python. Jupyter Notebook est idéal pour créer des documents interactifs et exploratoires, tandis que PyCharm est plus adapté pour le développement de projets Python complexes avec un ensemble complet d'outils de développement. En fonction de vos besoins et préférences, vous pouvez choisir l'outil qui convient le mieux à votre projet.



---

### Exemple de Code  


````markdown
# Code spécifique à PyCharm
name = input("Entrez votre nom : ")
print("Bonjour,", name, "! Bienvenue dans PyCharm.")
````
Dans cet exemple, nous utilisons la fonction input() pour demander à l'utilisateur d'entrer son nom. Une fois que l'utilisateur a entré son nom, nous affichons un message de salutation personnalisé dans la console.

Ce code est spécifique à PyCharm car il utilise la fonction input(), qui lit l'entrée de l'utilisateur à partir de la console. Cette fonctionnalité est couramment utilisée dans les scripts Python exécutés dans un environnement de développement intégré (IDE) comme PyCharm, où l'interaction avec l'utilisateur se fait via la console. Dans un notebook Jupyter, cette fonctionnalité n'est pas adaptée car l'interaction avec l'utilisateur se fait généralement à l'intérieur du notebook lui-même, pas à travers la console.

````markdown
# Code spécifique à Jupyter notebook
import matplotlib.pyplot as plt
import numpy as np

# Générer des données aléatoires
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Afficher un graphique dans le notebook
plt.plot(x, y)
plt.title('Graphique de la fonction sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()
````
Dans cet exemple, nous utilisons la bibliothèque matplotlib pour tracer un graphique de la fonction sinus dans l'intervalle [0, 10]. L'utilisation de plt.show() affichera le graphique directement dans le notebook lorsque vous exécutez cette cellule.

Ce code est spécifique à Jupyter Notebook car il utilise une fonctionnalité intégrée de Jupyter pour afficher des graphiques directement dans le notebook, ce qui n'est pas possible de manière native dans un script Python exécuté dans un environnement tel que PyCharm.

Autres environnements de travail
--
* Spyder: https://docs.spyder-ide.org/3/index.html
* IDLE : https://docs.python.org/3/library/idle.html
## Sources
---
* https://jupyter.org/
* https://www.youtube.com/watch?v=HW29067qVWk
* https://www.jetbrains.com/pycharm/
* https://www.youtube.com/watch?v=bcYWaDD2FuE
* https://jupyter-notebook.readthedocs.io/en/stable/notebook.html 
* https://medium.com/@think-data/pycharm-vs-jupyter-notebooks-choosing-the-right-python-programming-environment-ca235b06431c#:~:text=PyCharm%20excels%20in%20providing%20a,%2C%20data%20analysis%2C%20and%20documentation.
* https://www.reddit.com/r/learnpython/comments/wirpqi/pycharm_vs_jupyter_notebook/?rdt=45912
