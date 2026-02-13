# Githrun

Githrun is a versatile command-line tool and VS Code extension that enables you to execute, explore, and install Python scripts directly from GitHub and Gists. It streamlines remote execution by handling dependencies, private repositories, and local tool installation.

[![PyPI version](https://img.shields.io/pypi/v/githrun.svg)](https://pypi.org/project/githrun/) [![Python](https://img.shields.io/pypi/pyversions/githrun.svg)](https://pypi.org/project/githrun/) [![License](https://img.shields.io/github/license/notamitgamer/githrun)](https://github.com/notamitgamer/githrun/blob/main/LICENSE) [![Downloads](https://pepy.tech/badge/githrun)](https://pepy.tech/project/githrun) [![Last Commit](https://img.shields.io/github/last-commit/notamitgamer/githrun)](https://github.com/notamitgamer/githrun/commits/main) [![Contributors](https://img.shields.io/github/contributors/notamitgamer/githrun)](https://github.com/notamitgamer/githrun/graphs/contributors)

<a href="https://www.producthunt.com/products/githrun?embed=true&amp;utm_source=badge-featured&amp;utm_medium=badge&amp;utm_campaign=badge-githrun" target="_blank" rel="noopener noreferrer"><img alt="Githrun - Execute remote Python scripts directly from GitHub. | Product Hunt" width="250" height="54" src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1078250&amp;theme=light&amp;t=1770971505390"></a>
<a href="https://www.producthunt.com/products/githrun/reviews/new?utm_source=badge-product_review&utm_medium=badge&utm_source=badge-githrun" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/product_review.svg?product_id=1163407&theme=light" alt="Githrun - Execute&#0032;remote&#0032;Python&#0032;scripts&#0032;directly&#0032;from&#0032;GitHub&#0046; | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a>
<a href="https://www.producthunt.com/products/githrun?utm_source=badge-follow&utm_medium=badge&utm_source=badge-githrun" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/follow.svg?product_id=1163407&theme=light" alt="Githrun - Execute&#0032;remote&#0032;Python&#0032;scripts&#0032;directly&#0032;from&#0032;GitHub&#0046; | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a>
---

# VS Code Extension

## Extension Installation & Setup

### 1. Install the Extension
* **Marketplace:** Search for "Githrun" in the VS Code Extensions view and click Install.
* **Manual:** If installing from a VSIX file, go to Extensions -> ... -> Install from VSIX.

### 2. Install the Core CLI (Required)
This extension acts as a bridge to the Githrun command-line tool. You **must** have the Githrun CLI installed on your system.

Open your terminal and run:

```bash
pip install githrun
```

## Extension Features & Usage

### CodeLens Integration
The extension automatically scans Markdown, Python, and Text files for GitHub or Gist URLs.
* **Action:** Look for the "Run with Githrun" link appearing above any detected URL.
* **Click:** Clicking the link opens a terminal and executes the script immediately.

### Context Menu
* **Action:** Highlight any GitHub URL in your editor.
* **Click:** Right-click the selection and choose **Githrun: Run Selected Text**.

### Command Palette
* **Action:** Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac).
* **Command:** Type `Githrun: Run from URL...` and paste your target link into the input box.

## Extension Settings
The extension attempts to automatically detect your Githrun installation.
* It first checks for `githrun` in your global PATH.
* If not found, it tries `python -m githrun` (or `python3` on Mac/Linux).

---

## Features

* **Remote Execution**: Run scripts from GitHub or Gist URLs instantly.
* **Auto-Dependency Management**: Automatically creates temporary virtual environments and installs missing packages using the `--auto-install` flag.
* **Private Repo Access**: Authenticate securely with GitHub tokens to access private code and increase API rate limits.
* **Bookmarks**: Save long URLs as short aliases (e.g., `githrun run clean-db`).
* **Tool Installation**: Install remote scripts as permanent local CLI commands available in your system path.
* **Recursive Downloads**: Download entire folders or specific sub-directories from a repository.
* **Interactive Search**: Search for files in a repo and run them immediately from the results.
* **Smart Caching**: Caches API responses to speed up repeated searches and reduce API usage.

---

## CLI Usage

### 1. Run Remote Code
Execute a script directly from a URL.

**Basic Execution:**
```bash
githrun run [https://github.com/user/repo/blob/main/script.py](https://github.com/user/repo/blob/main/script.py)
```

**Run Gists:**
```bash
githrun run [https://gist.github.com/user/1234567890abcdef](https://gist.github.com/user/1234567890abcdef)
```

**Auto-Install Dependencies:**
If a remote script requires packages you do not have installed (e.g., pandas, requests), use this flag to run it in an isolated environment:
```bash
githrun run [https://github.com/user/repo/blob/main/data.py](https://github.com/user/repo/blob/main/data.py) --auto-install
```

**Inspect Code:**
View the source code with syntax highlighting before running it (Safety Check):
```bash
githrun run [https://github.com/user/repo/blob/main/script.py](https://github.com/user/repo/blob/main/script.py) --inspect
```

### 2. Authentication (Private Repos & Rate Limits)
GitHub limits unauthenticated requests to 60 per hour. Login to increase this limit to 5,000 and access private repositories.

```bash
githrun login ghp_YourPersonalAccessToken...
```
*The token is stored securely in `~/.githrun/config.json`.*

### 3. Bookmarks
Stop copy-pasting long URLs. Save them once, run them anywhere.

**Add a Bookmark:**
```bash
githrun bookmark add clean-db [https://github.com/user/repo/blob/main/utils/cleanup.py](https://github.com/user/repo/blob/main/utils/cleanup.py)
```

**Run a Bookmark:**
```bash
githrun run clean-db
```

**List Bookmarks:**
```bash
githrun bookmark list
```

### 4. Install as a Tool
Turn a remote Python script into a command you can run from anywhere in your terminal.

```bash
githrun install [https://github.com/user/repo/blob/main/my-tool.py](https://github.com/user/repo/blob/main/my-tool.py) --name mytool
```

* **Windows:** Creates a `.bat` file in `~/.githrun/bin`.
* **Linux/Mac:** Creates an executable shim in `~/.githrun/bin`.
* *Note: You must add `~/.githrun/bin` to your system PATH.*

### 5. Find & Search
Search for files inside a remote repository without cloning it.

```bash
# Search for files containing "config"
githrun find [https://github.com/user/repo](https://github.com/user/repo) "config"
```
*This command is interactive. You can select a result number to run it immediately.*

### 6. Download Files & Folders
Download artifacts to your local machine.

**Download a single file:**
```bash
githrun download [https://github.com/user/repo/blob/main/script.py](https://github.com/user/repo/blob/main/script.py)
```

**Download a specific folder (Recursive):**
```bash
githrun download [https://github.com/user/repo/tree/main/src/utils](https://github.com/user/repo/tree/main/src/utils) --output ./local_utils
```

### 7. Show Folder Contents
List files in a remote directory to understand the structure.

```bash
githrun show [https://github.com/user/repo/tree/main/src](https://github.com/user/repo/tree/main/src)
```

---

## Python API Usage

You can use Githrun inside your own Python scripts.

```python
import githrun

# 1. Search a repository
results = githrun.search_repository("[https://github.com/user/repo](https://github.com/user/repo)", "test")
for item in results:
    print(item['path'], item['raw_url'])

# 2. Download a file
githrun.download_file("[https://github.com/user/repo/blob/main/script.py](https://github.com/user/repo/blob/main/script.py)", output_path="script.py")

# 3. Download a full folder
githrun.download_folder("[https://github.com/user/repo/tree/main/src](https://github.com/user/repo/tree/main/src)")

# 4. Execute code programmatically
exit_code = githrun.execute_remote_code("[https://github.com/user/repo/blob/main/script.py](https://github.com/user/repo/blob/main/script.py)", args=["--verbose"])
```

---

## Configuration

Githrun stores configuration and cache files in your home directory:

* **Config:** `~/.githrun/config.json` (Tokens, Bookmarks)
* **Cache:** `~/.githrun/cache/` (API responses)
* **Binaries:** `~/.githrun/bin/` (Installed tools)

## License

This project is licensed under the MIT License.
