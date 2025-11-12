# VS Code: Python / Pylance keeps crashing (“JavaScript heap out of memory”)

This file helps you reduce Pylance memory usage in VS Code.  
You can copy–paste the config below into your **workspace** settings.

---

## 1. Where to put this

1. In VS Code open your **course / project folder** (not your whole home directory).
2. Create the folder `.vscode` in the project if it does not exist.
3. Inside it, create or edit `settings.json`.
4. Paste the config below into `.vscode/settings.json`.

---

## 2. Recommended settings (copy this)

```jsonc
{
  // ⚙️ Use lighter analysis mode
  "python.analysis.languageServerMode": "light",

  // ⚙️ Only analyze open files for errors
  "python.analysis.diagnosticMode": "openFilesOnly",

  // ⚙️ Turn off heavy indexing of all files
  "python.analysis.indexing": false,

  // ⚙️ Limit how many files Pylance tries to index
  "python.analysis.userFileIndexingLimit": 200,

  // 🚫 Tell Pylance to ignore heavy / useless folders
  "python.analysis.exclude": [
    "**/.venv/**",
    "**/env/**",
    "**/node_modules/**",
    "**/.git/**",
    "**/dist/**",
    "**/test/**",
    "**/build/**",
    "**/__pycache__/**",
    "**/.tmc/**",
    "**/tmc/**",
    "**/data/**"
  ]
}
````

After saving the file, **reload VS Code** (Command Palette → “Developer: Reload Window”).

---

## 3. What the settings do (short explanation)

* **`languageServerMode: "light"`**
  Pylance uses less memory; it focuses on the most important features.

* **`diagnosticMode: "openFilesOnly"`**
  Shows errors **only in files you have open**, not in the whole project.

* **`indexing: false` & `userFileIndexingLimit`**
  Stops Pylance from scanning thousands of files in the background.

* **`python.analysis.exclude`**
  Skips big folders like virtual environments, Git, TMC files, build folders, and large data directories that easily crash Pylance.

---



After saving the file, use **Command Palette → “Developer: Reload Window”**.

**What these do (short):**

* `languageServerMode: "light"` – lighter Pylance mode, less RAM. ([DeepWiki][2])
* `diagnosticMode: "openFilesOnly"` – errors only in open files, not the whole project. ([DeepWiki][1])
* `indexing: false` + `userFileIndexingLimit` – stops deep background scanning of thousands of files. ([DeepWiki][1])
* `python.analysis.exclude` – skips virtual envs, Git, TMC files, build and data folders that often cause memory spikes. ([DeepWiki][1])

---

## 3. Let Pylance use more Node.js memory (optional)

VS Code’s built-in Node.js is usually limited to about **4 GB heap**, which can be too small for big projects. ([GitHub][3])

Pylance has a special setting to switch to an external Node.js with a larger heap:

### 3.1 Install Node.js (if not already)

* Download and install Node.js from the official site.
* After installing, check in a terminal:

  ```bash
  node -v
  ```

  If you see a version number, Node.js is installed.

---

### 3.2 Point Pylance to an external Node (recommended)

In the same `.vscode/settings.json`, add **one** of these:

#### Option A – Let Pylance auto-manage Node

```jsonc
{
  "python.analysis.nodeExecutable": "auto"
}
```

Pylance will download/use a compatible Node and run it with a larger heap (typically 8 GB) instead of the ~4 GB limit of VS Code’s bundled Node. ([GitHub][3])

#### Option B – Give an explicit Node path

Example paths (adapt to your system):

```jsonc
{
  "python.analysis.nodeExecutable": "C:\\Program Files\\nodejs\\node.exe"
}
```

```jsonc
{
  "python.analysis.nodeExecutable": "/usr/local/bin/node"
}
```

This makes Pylance use your own Node.js, which can run with a higher `--max-old-space-size` than the default VS Code runtime, reducing “heap out of memory” crashes on large workspaces. ([GitHub][3])

> Note: some remote/devcontainer setups behave differently with this setting, but for local student projects this is usually fine. ([GitHub][4])

---

## 4. Advanced: global `NODE_OPTIONS` (usually not needed)

Only for more advanced setups (and only if you know what environment variables are).

You can globally increase the Node heap for all Node processes by setting `NODE_OPTIONS`:

### macOS / Linux (temporary for one terminal)

```bash
export NODE_OPTIONS="--max-old-space-size=8192"
code
```

### Windows PowerShell (current user)

```powershell
setx NODE_OPTIONS "--max-old-space-size=8192"
```

This gives Node processes up to **8 GB** heap instead of the default ~4 GB. ([Stack Overflow][5])

> Warning: this affects **all** Node.js apps on that machine, not just VS Code, so don’t use it on school lab computers unless allowed. ([Stack Overflow][5])

---

## 5. If it still keeps crashing

1. Check that you really opened **only** the small project/exercise folder, not a huge parent folder.
2. Try disabling Pylance just for that folder:

   * Extensions → **Pylance** → ⚙ → **Disable (Workspace)**. ([Stack Overflow][6])

You can still write and run Python code; you just lose some IntelliSense until the crashes are solved.

[1]: https://deepwiki.com/microsoft/pylance-release/2.2-analysis-settings?utm_source=chatgpt.com "Analysis Settings | microsoft/pylance-release | DeepWiki"
[2]: https://deepwiki.com/microsoft/pylance-release/2.4-performance-settings?utm_source=chatgpt.com "Performance Settings | microsoft/pylance-release | DeepWiki"
[3]: https://github.com/microsoft/pylance-release/blob/main/docs/settings/python_analysis_nodeExecutable.md?utm_source=chatgpt.com "pylance-release/docs/settings/python_analysis_nodeExecutable ... - GitHub"
[4]: https://github.com/microsoft/pylance-release/issues/5812?utm_source=chatgpt.com "Setting `python.analysis.nodeExecutable` in the user settings affects ..."
[5]: https://stackoverflow.com/questions/56982005/where-do-i-set-node-options-max-old-space-size-2048?utm_source=chatgpt.com "Where do I set 'NODE_OPTIONS=\"--max-old-space-size=2048\"'"
[6]: https://stackoverflow.com/questions/78289805/how-to-solve-pylance-crashing-in-vs-code?utm_source=chatgpt.com "How to solve Pylance crashing in VS Code? - Stack Overflow"
