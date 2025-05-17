# File Organiser - EN

A simple tool, usable only through the terminal (cmd), that automatically organizes your files into folders based on their type (images, documents, music, etc.).

## 📦 Installation

1. Download the `Setup_FileOrganiser.exe` file.
2. Launch the installer.
3. Choose a folder (default: `C:\Program Files (x86)\file-organiser`) and **install**.
4. If you unchecked the `Add to Path` option during installation, you will need to **add** the installation path (default: `C:\Program Files (x86)\file-organiser`) to the system **environment variables**, under the **Path** section (see next section for tutorial).

#### ⚙️ How to add file-organiser to Path?
> 1. Press `Win + R` to open the "**Run**" window.  
> 2. Type `sysdm.cpl` and press **Enter**. This opens the system properties window.  
> 3. Go to the **Advanced system settings** tab.  
> 4. Click on **Environment Variables** at the bottom.  
> 5. Under **System Variables**, find and select **Path**, then click **Edit**.  
> 6. Add the install path (default: `C:\Program Files (x86)\file-organiser`) to the list.  
> 7. Click **OK** and close all windows.

### 📦 Usage

#### 🔹 Basic usage

```bash
file-organiser <path>
```

Replace `<path>` with the folder you want to organize.

All default categories will be used: images, documents, videos, music, archives.

#### 🔹 With specific categories

```bash
file-organiser <path> --categories <category1> <category2> ...
```

You can choose which categories to organize by adding `--categories` followed by one or more of the following:
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

Organize only images and documents:
```bash
file-organiser "C:\Users\YourName\Downloads" --categories images documents
```

📘 Read this in another language: [Français](README.fr.md) | [English](README.md)
