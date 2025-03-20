### **📌 TODO (Corrigé et amélioré)**

- **Créer un objet `TemplateManager`**.
- **Utiliser la bibliothèque `ast` pour la gestion des nœuds**.
- **Valider la structure globale de l’arbre JSON**.
- **Ajouter des interfaces JSON Schema pour chaque template**.
- **Vérifier que chaque nœud correspond bien au schéma défini pour son `tag`**.
- **S’assurer que chaque template Jinja correspond au JSON Schema associé**.

- **Gérer les dépendances entre templates** : si un template dépend d’un package maison, il doit être ajouté automatiquement au projet.

- **Utiliser LangChain pour générer dynamiquement des interfaces JSON Schema**.
- **Utiliser LangChain pour générer automatiquement des templates Jinja à partir des JSON Schemas**.
- **Indexer les transducteurs (interfaces + templates) dans une base de données vectorielle sémantique** pour faciliter la recherche et la réutilisation.
- **Générer de nouveaux projets dans le DSL grâce au Retrieval-Augmented Generation (RAG)**.
- **Implémenter des mécanismes de correction d’erreurs** pour la validation JSON et la transformation.

- **Pour une interface graphique, créer une fonction qui renvoie la liste des JSON Schemas disponibles**.

- **Optimiser la génération de code avec des tests automatiques** :
  - Vérifier que le code généré avec un template et des données d’entrée **correspond à un fichier de sortie d’exemple**.
