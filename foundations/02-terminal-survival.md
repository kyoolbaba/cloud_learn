---
tags: [foundations, beginner, terminal]
aliases: [Terminal Survival, Terminal Basics, Command Line Basics]
---
> [[01-absolute-basics|◀ Absolute basics]] · [[START-HERE|Start here]] · [[03-glossary|Glossary ▶]]

# 02 · Terminal survival (open it, don't fear it)

The **terminal** is just a window where you *type* instructions to the computer instead of
clicking. Think of it as **texting your computer**: you type a command, press Enter, it replies.
Every cloud tool (AWS CLI, Docker, git, Python) is driven from here. You only need ~10 commands
to be dangerous. Go slow; nothing here can hurt if you don't delete things.

## What "terminal" / "shell" / "command line" mean
- **Terminal** = the window. **Shell** = the program inside it that understands your typing.
- On **Windows** your shell is **PowerShell**. On **Linux/Mac** (and WSL) it's **bash**.
- You'll use **both**: PowerShell for Windows + AWS, and bash once you install WSL Ubuntu (Module 0).
  Most ideas are identical; only a few command *names* differ (table below).

## Open one right now
- **PowerShell:** press `Win`, type **PowerShell**, hit Enter. (Or install **Windows Terminal** from the Microsoft Store — nicer, tabs.)
- **WSL/Ubuntu bash (later):** after `wsl --install -d Ubuntu`, type **Ubuntu** in Start.

You'll see a **prompt** — a line ending in `>` (PowerShell) or `$` (bash) waiting for you. That's it asking "what next?"

## The 10 commands that get you everywhere
| Goal | PowerShell (Windows) | bash (Linux/WSL/Mac) |
|---|---|---|
| Where am I? | `pwd` (or `Get-Location`) | `pwd` |
| List files here | `ls` (or `dir`) | `ls` |
| Go into a folder | `cd foldername` | `cd foldername` |
| Go up one folder | `cd ..` | `cd ..` |
| Go to my home | `cd ~` | `cd ~` |
| Make a folder | `mkdir name` | `mkdir name` |
| Show a file's contents | `cat file.txt` (or `Get-Content`) | `cat file.txt` |
| Clear the screen | `clear` (or `cls`) | `clear` |
| Stop a running command | `Ctrl + C` | `Ctrl + C` |
| Run a Python file | `python script.py` | `python3 script.py` |

> `cd` = **c**hange **d**irectory. "Directory" is just the old word for "folder."

## Paths — the address of a file
- **Windows:** `C:\Users\Milan\Documents\EXPERIMENTS\Learn` (back-slashes, starts with a drive letter).
- **Linux:** `/home/milan/learn` (forward-slashes, starts at `/`).
- **Absolute path** = the full address from the top. **Relative path** = from where you're standing now.
- Shorthand: `.` = "here", `..` = "the folder above me", `~` = "my home folder".

**Try it (safe):**
```powershell
cd C:\Users\MilanGowdaJP\Documents\EXPERIMENTS\Learn
ls          # see HOME.md, certs, labs, projects...
cd certs
ls          # the cert folders
cd ..       # back up to Learn
```

## Three tricks that save your sanity
1. **Tab completion** — type the first few letters of a file/folder and press **Tab**; the shell finishes it. (Stops typos.)
2. **Up-arrow** — recalls your last command so you can re-run or edit it. Press it a few times to scroll history.
3. **`Ctrl + C`** — the universal "stop!" If something runs forever or you're stuck, this gets you back to the prompt.

## Errors are normal — read the *last* line
A red wall of text looks scary but the **last line** usually tells you the real problem in plain-ish English:
- `command not found` / `is not recognized` → the tool isn't installed or isn't on your `PATH` (see [[03-glossary#PATH]]).
- `No such file or directory` / `cannot find path` → you're in the wrong folder, or mistyped the name (use Tab).
- `Access is denied` / `Permission denied` → you lack rights, or the file is in use.

Copy that last line to me and I'll explain it. There are no dumb errors.

## Running things you'll actually run
```powershell
# set which AWS account to use for the lab session (you'll do this a lot)
$env:AWS_PROFILE = "learn"
# check a tool is installed (prints its version)
aws --version
python --version
git --version
```
If one says "not recognized," the tool just isn't installed yet — that's a setup step, not a failure.

## ⚠️ The only dangerous commands (handle with care)
- `Remove-Item` / `rm` **deletes** files (no recycle bin in the terminal). Double-check the path first.
- `rm -r foldername` / `Remove-Item -Recurse` deletes a whole folder tree. Be sure.
- When in doubt, `ls` first to confirm what's there before you delete.

## You're ready when you can…
- Open PowerShell, `cd` into the `Learn` folder, `ls` its contents, `cat HOME.md`, and stop a command with `Ctrl+C` — without looking anything up.

Next: keep [[03-glossary]] open in a tab and look up any word that stumps you. Then head to
[[START-HERE]] step 4 (set up your AWS account).
