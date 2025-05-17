# File Organiser - EN

A simple command-line tool that automatically organizes your files into folders based on their type (images, documents, music, etc.).

## 📦 Installation

1. Download `Setup_FileOrganiser.exe`.
2. Launch the installer.
3. Choose an install path (default: `C:\Users\YourName\AppData\Local\file-organizer`) and **install**.
4. If you unchecked `Add to Path` during installation, you must manually **add the install path** (default: `C:\Users\YourName\AppData\Local\file-organizer`) to your system environment **Path** variable (see below).

#### ⚙️ How to add file-organiser to Path?
> 1. Press `Win + R` to open the "**Run**" dialog.  
> 2. Type `sysdm.cpl` and press **Enter**.  
> 3. Go to the **Advanced system settings** tab.  
> 4. Click **Environment Variables**.  
> 5. Under **System variables**, find and select **Path**, then click **Edit**.  
> 6. Add the installation path (default: `C:\Users\YourName\AppData\Local\file-organizer`).  
> 7. Click **OK** and close all windows.

### 📦 Usage

#### 🔹 Basic usage

```bash
file-organiser <path>
```

Organizes all files in the given folder using default categories: images, documents, videos, music, archives.

#### 🔹 Use specific categories

```bash
file-organiser <path> --categories <category1> <category2> ...
```

#### 🔹 Add extensions to a category

```bash
file-organiser --add <category> .ext1 .ext2 ...
```

Adds new extensions to a category or creates it if it doesn't exist.

#### 🔹 Remove extensions or entire category

```bash
file-organiser --remove <category> [.ext1 .ext2 ...]
```

- If **no extensions are provided**, the **whole category is removed**.
- If extensions are given, only those are removed **if they exist**.

#### 💡 Examples

Organize everything in Downloads:
```bash
file-organiser "C:\Users\YourName\Downloads"
```

Only organize images and documents:
```bash
file-organiser "C:\Users\YourName\Downloads" --categories images documents
```

Add `.psd` to the images category:
```bash
file-organiser --add images .psd
```

Remove `.psd` from the images category:
```bash
file-organiser --remove images .psd
```

Remove the entire "archives" category:
```bash
file-organiser --remove archives
```

📘 Read this in another language: [Français](README.fr.md) | [English](README.md)
