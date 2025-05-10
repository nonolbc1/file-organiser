# File Organiser - US

A simple tool usable only in the cmd that automatically organizes your files into folders according to their type (images, documents, music, etc.).

## 📦 Installation

1. Download the file `Setup_FileOrganiser.exe`.
2. Run the installer.
3. Choose a folder (default: C:\Program Files\file-organiser) and install.

### 📦 How to Use

#### 🔹 Basic Usage

```bash
file-organiser <path>
```

Replace `<path>` with the folder you want to organize.

All default categories will be used: images, documents, videos, music, archives.

#### 🔹 With Specific Categories
```bash
file-organiser <path> --categories <category1> <category2> ...
```
You can choose which categories to organize by adding --categories followed by one or more of the following:
- images
- documents
- videos
- music
- archives

#### 💡 Examples
Organize everything in the Downloads folder:
```bash
file-organiser "C:\Users\YourName\Downloads"
```

Only organize images and documents:
```bash
file-organiser "C:\Users\YourName\Downloads" --categories images documents
```

📘 Read this in other languages: [Français](README.fr.md) | [English](README.md)
