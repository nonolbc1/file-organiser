# File Organiser - FR

Un outil simple, utilisable uniquement via le terminal (cmd), qui organise automatiquement vos fichiers dans des dossiers selon leur type (images, documents, musiques, etc.).

## 📦 Installation

1. Téléchargez le fichier `Setup_FileOrganiser.exe`.
2. Lancez l’installateur.
3. Choisissez un dossier (par défaut : `C:\Program Files\file-organiser`) et installez.

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
