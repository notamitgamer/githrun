# Pyrgo

> The Swiss Army Knife for Remote Python Execution.

Pyrgo is a powerful CLI tool and Python library that lets you run, explore, and install Python code directly from GitHub and Gists. It handles dependencies, private repositories, and even turns remote scripts into local command-line tools.

[![PyPI version](https://badge.fury.io/py/pyrgo.svg)](https://badge.fury.io/py/pyrgo)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

* **Remote Execution**: Run scripts from GitHub or Gist URLs instantly.
* **Auto-Dependency Management**: Automatically creates temporary virtual environments and installs missing packages using the `--auto-install` flag.
* **Private Repo Access**: Authenticate securely with GitHub tokens to access private code and increase API rate limits.
* **Bookmarks**: Save long URLs as short aliases (e.g., `pyrgo run clean-db`).
* **Tool Installation**: Install remote scripts as permanent local CLI commands available in your system path.
* **Recursive Downloads**: Download entire folders or specific sub-directories from a repository.
* **Interactive Search**: Search for files in a repo and run them immediately from the results.
* **Smart Caching**: Caches API responses to speed up repeated searches and reduce API usage.

---

## Installation

```bash
pip install pyrgo
```

---

## CLI Usage

### 1. Run Remote Code
Execute a script directly from a URL.

**Basic Execution:**
```bash
pyrgo run [https://github.com/user/repo/blob/main/script.py](https://github.com/user/repo/blob/main/script.py)
```

**Run Gists:**
```bash
pyrgo run [https://gist.github.com/user/1234567890abcdef](https://gist.github.com/user/1234567890abcdef)
```

**Auto-Install Dependencies:**
If a remote script requires packages you do not have installed (e.g., pandas, requests), use this flag to run it in an isolated environment:
```bash
pyrgo run [https://github.com/user/repo/blob/main/data.py](https://github.com/user/repo/blob/main/data.py) --auto-install
```

**Inspect Code:**
View the source code with syntax highlighting before running it (Safety Check):
```bash
pyrgo run [https://github.com/user/repo/blob/main/script.py](https://github.com/user/repo/blob/main/script.py) --inspect
```

### 2. Authentication (Private Repos & Rate Limits)
GitHub limits unauthenticated requests to 60 per hour. Login to increase this limit to 5,000 and access private repositories.

```bash
pyrgo login ghp_YourPersonalAccessToken...
```
*The token is stored securely in `~/.pyrgo/config.json`.*

### 3. Bookmarks
Stop copy-pasting long URLs. Save them once, run them anywhere.

**Add a Bookmark:**
```bash
pyrgo bookmark add clean-db [https://github.com/user/repo/blob/main/utils/cleanup.py](https://github.com/user/repo/blob/main/utils/cleanup.py)
```

**Run a Bookmark:**
```bash
pyrgo run clean-db
```

**List Bookmarks:**
```bash
pyrgo bookmark list
```

### 4. Install as a Tool
Turn a remote Python script into a command you can run from anywhere in your terminal.

```bash
pyrgo install [https://github.com/user/repo/blob/main/my-tool.py](https://github.com/user/repo/blob/main/my-tool.py) --name mytool
```

* **Windows:** Creates a `.bat` file in `~/.pyrgo/bin`.
* **Linux/Mac:** Creates an executable shim in `~/.pyrgo/bin`.
* *Note: You must add `~/.pyrgo/bin` to your system PATH.*

### 5. Find & Search
Search for files inside a remote repository without cloning it.

```bash
# Search for files containing "config"
pyrgo find [https://github.com/user/repo](https://github.com/user/repo) "config"
```
*This command is interactive. You can select a result number to run it immediately.*

### 6. Download Files & Folders
Download artifacts to your local machine.

**Download a single file:**
```bash
pyrgo download [https://github.com/user/repo/blob/main/script.py](https://github.com/user/repo/blob/main/script.py)
```

**Download a specific folder (Recursive):**
```bash
pyrgo download [https://github.com/user/repo/tree/main/src/utils](https://github.com/user/repo/tree/main/src/utils) --output ./local_utils
```

### 7. Show Folder Contents
List files in a remote directory to understand the structure.

```bash
pyrgo show [https://github.com/user/repo/tree/main/src](https://github.com/user/repo/tree/main/src)
```

---

## Python API Usage

You can use Pyrgo inside your own Python scripts.

```python
import pyrgo

# 1. Search a repository
results = pyrgo.search_repository("[https://github.com/user/repo](https://github.com/user/repo)", "test")
for item in results:
    print(item['path'], item['raw_url'])

# 2. Download a file
pyrgo.download_file("[https://github.com/user/repo/blob/main/script.py](https://github.com/user/repo/blob/main/script.py)", output_path="script.py")

# 3. Download a full folder
pyrgo.download_folder("[https://github.com/user/repo/tree/main/src](https://github.com/user/repo/tree/main/src)")

# 4. Execute code programmatically
exit_code = pyrgo.execute_remote_code("[https://github.com/user/repo/blob/main/script.py](https://github.com/user/repo/blob/main/script.py)", args=["--verbose"])
```

## Configuration

Pyrgo stores configuration and cache files in your home directory:

* **Config:** `~/.pyrgo/config.json` (Tokens, Bookmarks)
* **Cache:** `~/.pyrgo/cache/` (API responses)
* **Binaries:** `~/.pyrgo/bin/` (Installed tools)

## License

This project is licensed under the MIT License.