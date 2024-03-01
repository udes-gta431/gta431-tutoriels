# Tutoriel : Introduction aux gists sur GitHub 👾

## Contexte de la Problématique
Imaginez que vous avez un travail à remettre dans le cadre d'un cours de programmation universitaire. Puisque vous êtes un étudiant exemplaire, vous vous êtes pris d'avance pour ce projet. Malgré tout, vous rencontrez un obstacle et avez besoin d'aide. C'est alors que vous vous souvenez d'avoir lu le tutoriel suivant qui vous rappelle l'utilisation d'un gist sur GitHub ... 

Les gists permettent de rejoindre la communauté de programmeurs de GitHub par le biais de morceau de code spécifique. Que ce soit pour résoudre un problème ou partager des solutions, les gists sont un excellent moyen de communication entre vous et les autres utilisateurs de GitHub. Pour vulgariser, à mon avis, ceux-ci se comparent à une publication faite sur Facebook.✍🏼

## Connaissances Préalables
Afin de bien comprendre le tutoriel, assurez-vous d'avoir les connaissances de base suivantes :

- Un compte GitHub (inscription gratuite disponible💲)

- Comprendre les concepts de base de Github

  - Évidemment, plusieurs autres compétences peuvent être utiles telles qu'une compréhension des concepts de programmation, la capacité de lire et d'écrire du code dans une langue de programmation comme Python, connaître des notions de base du Markdown, etc. mais celles-ci ne sont pas nécessaire pour le simple processus de création d'un gist. Ces compétences sont davantages utiles lorsque vous aidez à résoudre le problème d'un autre programmeur par exemple.

## Qu'est-ce qu'un gist ?
Un gist sur GitHub est un moyen simple et rapide de partager des morceaux de code avec d'autres utilsateurs, des textes, des liens, prendre des notes, ou même des fichiers entiers avec d'autres personnes. Les gists sont comme des petits dépôts (il peut donc être dupliqué ou cloné), sans nécessité de créer un projet complet. Ils peuvent être publics, privés ou accessibles uniquement par une invitation de l'auteur du gist. 

## Pourquoi utiliser des gists ?
Les gists offrent une solution rapide pour partager des extraits de code avec d'autres développeurs. C'est surtout utile pour discuter de problèmes de code, demander de l'aide, partager des solutions, etc. Ils servent aussi à échanger des idées et/ou collaborer avec d'autres utilisateurs sans avoir à faire un dépôt total. Les gists peuvent aussi contenir des images, des codes, des explications pour soumettre le plus d'informations possible.

## Exemple Contextuel
Supposons que vous travaillez sur un exercice à faire sur Pycharm dans le cadre d'une formation quelconque à partir d'un Mac. Vous pourriez faire un Gist pour demander de l'aide à d'autres programmeurs afin de vous aider à distinguer la différence entre l'écriture du chemin d'un fichier sur Mac versus Windows.

### Comment créer un gist ?
Suivez ces étapes pour la création de votre gist :

#### 1. Connectez-vous à GitHub :
Assurez-vous d'être connecté à votre compte GitHub.

#### 2. Création d'un gist

- Accès à la page des gists :
   - Pour créer un gist sur GitHub, commencez par cliquer sur le "+" situé en haut à droite de la page principale de GitHub.
   - Après avoir cliqué sur le "+", choisissez l'option "Nouveau gist" dans le menu déroulant qui apparaît. Vous serez redirigé vers la page de création de gist.

- Ajout de Contenu :
  - Sur la page de création de gist, donnez un nom au fichier (optionnel mais fortement recommandé) et ajoutez une description pour contextualiser le contenu que vous partagez. C'est également à cet endroit que vous inclurez le code dans la zone de texte dédiée.
_________
**EXEMPLE**

Titre : Différences chemins de fichiers Mac/Windows - Aide pour exercice PyCharm

Description :
Bonjour à tous,
Je suis actuellement en train de travailler sur un exercice en Python dans le cadre d'une formation. Je suis sur Mac et j'utilise PyCharm, mais je rencontre des difficultés avec les chemins de fichiers. Je ne comprends pas bien la différence entre l'écriture du chemin d'un fichier sur Mac et sur Windows. Dans l'exercice, on me demande de créer un fichier et d'y écrire du texte, mais je ne sais pas comment spécifier le chemin d'accès au fichier correctement. ☹️

- exerciceGTA431.py - Le fichier Python que je suis en train de travailler. (Insérer le fichier sur lequel vous travailler, capture d'écran, etc.)

*Code :

    chemin = "chemin/vers/fichier/nom_fichier.txt" OU "../../data/source/nomdossier/nom_fichier.txt"

    #Ouvrir un fichier en écriture
    fichier = open("/Users/utilisateur/mon_fichier.txt", "w")

    #Écrire du texte dans le fichier
    fichier.write("test")

    #Fermer le fichier
    fichier.close()

Merci pour votre aide !

Noémie
_________
- Visibilité du gist :
   - Après avoir configuré le contenu du gist, choisissez la visibilité appropriée parmi les options disponibles : Public, Secret ou Gists privés. 

- Création du gist :
    - Ensuite, cliquez sur le bouton "Create public gist" ou "Create secret gist" selon vos préférences.

#### 3. Partage et Intégration

Une fois votre gist créé, vous pouvez soit le partager par  :

- Lien Direct :
  - Une fois le gist créé, copiez le lien généré pour partager directement le gist avec d'autres utilisateurs.

- Intégration sur une Page Web :
  - Si vous souhaitez intégrer le gist sur une page Web, explorez l'option "Embed" disponible sur la page du gist. Cela vous fournira un code d'intégration que vous pouvez utiliser dans le code source de votre  page.

Pour vous assurez que votre gist a bel et bien été publié, accédez à la page gists et cliquez sur le gist que vous souhaitez vérifier. S'il a bien été publié, le statut de votre gist sera *Créé il y a X minutes*. S'il est en mode Brouillon, il ne sera pas visible pour les autres utilisateurs.

## Bonnes Pratiques et Astuces

Voici quelques conseils pour améliorer la qualité de votre gist :

- **Commentez votre code** pour une meilleure compréhension d'autrui

- **Écrivez un titre de fichier clair** qui permet de comprendre le but du gist dès le départ (Par exemple, "Différences chemins de fichiers Mac/Windows" est un nom plus clair que "différences chemins".)

- **Ajoutez une description détaillée**. La description de votre gist doit fournir plus d'informations sur le contenu du gist et sur ce que vous essayez de faire. Vous pouvez également inclure des instructions, des liens et des captures d'écran. 

## Transfert de connaissance
Bien qu'ils sont majoritairement connus pour leur utilité pour les développeurs informatiques de ce monde, les gists comportent plus d'une corde à leur arc. En effet, les gists peuvent être utilisés par toutes sortes de fonctions d'une entreprise, peu importe leur rôle. En effet, une entreprise peut créer/partager des gists avec quelques personnes seulement. Dans cette optique, la direction pourrait partager les notes d'une réunion par le biais d'un gist. L'équipe marketing peut partager des idées de contenu, demander l'avis d'autres départements sur certaines publications médiatiques, etc. Bien évidemment, le service informatique peut partager des liens, codes ou guide pour aider les employés à se créer un compte sur une application quelconque par exemple. Bref, si vous cherchez un moyen simple et efficace d'améliorer la collaboration et la communication au sein de votre entreprise, les gists sont une solution à explorer.

## Limites et Prochaines Étapes

Limites :
Les gists ont pour principal but de seulement partager des petits bouts de code donc sont des dépôts légers et ne sont pas conçus pour des problèmes plus complexes. Le tutoriel se base sur les fonctionnalités de base des gists.

Prochaines étapes :
GitHub offre une [documentation officielle sur les gists](https://docs.github.com/fr/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists) au besoin . De plus, de nombreux tutoriels, articles en ligne (comme [Liquid Web](https://www.liquidweb.com/kb/what-is-a-github-gist/) par exemple) et manuels sont disponibles pour vous aider à apprendre à utiliser les gists de manière plus avancée. (Pour les *geeks* d'entre vous 🤓)

## Synthèse

En conclusion, les gists sur GitHub sont un outil puissant pour partager du code rapidement et efficacement. Que vous soyez un étudiant/professionnel travaillant sur un projet ou que vous cherchiez simplement à collaborer de manière informelle, les gists simplifient le processus de partage de code. Les gists offrent une solution à la problématique initiale, partager du code pour aider ou être aider, en facilitant la collaboration et le partage de connaissances au sein de la communauté des développeurs. En utilisant ce tutoriel, vous êtes maintenant en mesure de créer, partager et comprendre l'utilisation des gists sur GitHub ! 🎉

