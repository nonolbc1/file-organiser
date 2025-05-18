# File Organiser - FR
Un outil simple, utilisable uniquement via le terminal (cmd), qui organise automatiquement vos fichiers dans des dossiers selon leur type (images, documents, musiques, etc.).


## 📦 Installation
1. Téléchargez le fichier `Setup_FileOrganiser.exe`.
2. Lancez l’installateur.
3. Choisissez un dossier (par défaut : `C:\Users\VotreNom\AppData\Local\file-organizer`) et **installez**.
4. Si vous avez décoché l'option `Add to Path` lors de l'installation, vous devrez **ajouter** le chemin d'installation (par défaut: `C:\Users\VotreNom\AppData\Local\file-organizer`) dans les **variables d'environnement système**, sous la section **Path** (Tutoriel dans la section suivante).

#### ⚙️ Comment ajouter file-organiser au Path ?
> 1. Appuyez sur `Win + R` pour ouvrir la fenêtre "**Exécuter**".  
> 2. Tapez `sysdm.cpl` et appuyez sur **Entrée**. Cela ouvrira la fenêtre des propriétés système.  
> 3. Allez dans l'onglet **Paramètres système avancés**.  
> 4. Cliquez sur **Variables d'environnement** en bas de la fenêtre.  
> 5. Dans la section **Variables système**, trouvez et sélectionnez la variable **Path**, puis cliquez sur **Modifier**.  
> 6. Ajoutez le chemin d'installation (par défaut: `C:\Users\VotreNom\AppData\Local\file-organizer`) à la liste des valeurs de **Path**.  
> 7. Cliquez sur **OK** puis fermez toutes les fenêtres.


## 📦 Utilisation
### 🔹 Utilisation de base
```bash
file-organiser <chemin>
```

Organise les fichiers dans les catégories par défaut : images, documents, vidéos, musiques, archives.

### 🔹 Utiliser des catégories spécifiques
```bash
file-organiser <chemin> --categories <catégorie1> <catégorie2> ...
```

### 🔹 Ajouter des extensions à une catégorie
```bash
file-organiser --add <catégorie> .ext1 .ext2 ...
```

Ajoute des extensions à une catégorie existante, ou crée la catégorie si elle n’existe pas.

### 🔹 Retirer des extensions ou une catégorie
```bash
file-organiser --remove <catégorie> [.ext1 .ext2 ...]
```

- Si vous ne spécifiez **aucune extension**, la **catégorie entière** sera supprimée.
- Si vous spécifiez une ou plusieurs extensions, elles seront supprimées **seulement si elles existent**.


### 💡 Exemples
Organiser tout dans Téléchargements :
```bash
file-organiser "C:\Users\VotreNom\Downloads"
```

Organiser uniquement images et documents :
```bash
file-organiser "C:\Users\VotreNom\Downloads" --categories images documents
```

Ajouter `.psd` à la catégorie images :
```bash
file-organiser --add images .psd
```

Retirer `.psd` de la catégorie images :
```bash
file-organiser --remove images .psd
```

Supprimer entièrement la catégorie "archives" :
```bash
file-organiser --remove archives
```

📘 Lire dans une autre langue : [Français](README.fr.md) | [English](README.md)
