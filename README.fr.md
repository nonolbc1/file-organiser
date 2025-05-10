# File Organiser - FR

Un outil simple, utilisable uniquement via le terminal (cmd), qui organise automatiquement vos fichiers dans des dossiers selon leur type (images, documents, musiques, etc.).

## 📦 Installation

1. Téléchargez le fichier `Setup_FileOrganiser.exe`.
2. Lancez l’installateur.
3. Choisissez un dossier (par défaut : `C:\Program Files\file-organiser`) et installez.
4. Si vous avez décoché `Add to Path`, vous devrez ajouter le chemin d'installation (par défaut: `C:\Program Files\file-organiser`) dans les variables d'environnement système, sous la section Path:
### > Comment l'ajouter dans le Path
    1. Appuyez sur `Win + R` pour ouvrir la fenêtre "Exécuter"
    2. Tapez `sysdm.cpl` et appuyez sur **Entrée**. Cela ouvrira la fenêtre des propriétés système.
    3. Allez dans l'onglet **Paramètres système avancés**.
    4. Cliquez sur **Variables d'environnement** en bas de la fenêtre.
    5. Dans la section **Variables système**, trouvez et sélectionnez la variable **Path**, puis cliquez sur **Modifier**.
    6. Ajoutez `C:\Program Files\file-organiser` à la liste des valeurs de **Path**.
    7. Cliquez sur **OK** pour fermer toutes les fenêtres.

### 📦 Utilisation

#### 🔹 Utilisation de base

```bash
file-organiser <chemin>
```

Remplacez `<chemin>` par le dossier que vous souhaitez organiser.

Toutes les catégories par défaut seront utilisées : images, documents, vidéos, musiques, archives.

#### 🔹 Avec des catégories spécifiques
```bash
file-organiser <chemin> --categories <catégorie1> <catégorie2> ...
```
Vous pouvez choisir les catégories à organiser en ajoutant --categories suivi d’une ou plusieurs des catégories suivantes :
- images
- documents
- videos
- music
- archives

#### 💡 Exemples
Organiser tout dans le dossier Téléchargements :
```bash
file-organiser "C:\Users\VotreNom\Downloads"
```

Organiser uniquement les images et documents :
```bash
file-organiser "C:\Users\VotreNom\Downloads" --categories images documents
```

📘 Lire cela dans une autre langue: [Français](README.fr.md) | [English](README.md)
