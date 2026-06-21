---
tags: [lab, m0-linux]
aliases: [m0-linux lab]
---
> [[labs/README|⬅ Labs]] | [[HOME|Home]] | [[STUDY_PLAN|Plan]]

# Module 0 — Linux fundamentals (hands-on lab)

**Where you run this:** inside **WSL2 Ubuntu** (a real Linux box on your laptop).
**Where these notes live:** Windows side, reachable from Ubuntu at
`/mnt/c/Users/MilanGowdaJP/Documents/EXPERIMENTS/Learn/labs/m0-linux`.

Work top to bottom. For each lab: read the **Why**, run the **Do**, confirm the
**Expect**, then answer the **Checkpoint** out loud (or to me). Don't copy-paste
blindly — type it, predict the output, *then* run it. That's what makes it stick.

> Convention: `$` = a normal command. `#` after a command = a comment.
> When you see `sudo`, you're running as root; it'll ask for the password you
> set during install (nothing shows as you type — that's normal).

---

## Lab 0 — Install Ubuntu and land in the shell

**Why:** Everything in Modules 0–2 runs on Linux. WSL2 gives you a genuine
Ubuntu kernel sharing your laptop — no dual boot, no VM to babysit.

**Do (run this in Windows PowerShell, in a real terminal window — it's interactive):**
```powershell
wsl --install -d Ubuntu
```
It downloads Ubuntu, then launches it and asks you to **create a UNIX user**:
- username: something lowercase, no spaces — e.g. `milan`
- password: anything memorable; you'll type it for every `sudo`. It is hidden as you type.

When you see a green/colored prompt like `milan@MACHINE:~$`, you're in Linux.

**First commands — get your bearings:**
```bash
whoami            # your username
pwd               # where am I? -> /home/milan  (your home dir, aka ~)
id                # your user id (uid), groups
uname -a          # kernel info — confirms you're on Linux, not Windows
cat /etc/os-release   # which distro/version (Ubuntu 24.04)
```

**Expect:** `pwd` shows `/home/<you>`. `uname -a` mentions `Linux ... microsoft-standard-WSL2`.

**Update the package index once (good hygiene):**
```bash
sudo apt update && sudo apt -y upgrade
sudo apt install -y tmux htop tree nano vim curl   # tools we'll use below
```

**Checkpoint:** You can open Ubuntu, and explain that `~` = `/home/<you>` = your home directory.

---

## Lab 1 — Filesystem tour

**Why:** Linux has one tree starting at `/` (no `C:` drives). Knowing where
things live (`/etc` config, `/var` variable data/logs, `/home` users, `/bin`
programs) is half of sysadmin.

**Do:**
```bash
cd /                 # go to the root of the tree
ls -F                # list top-level dirs (trailing / marks directories)
cd /etc; ls          # system-wide config files live here
cd /var/log; ls      # logs live here
less /var/log/dpkg.log   # page through the package-install log; press q to quit
cd ~                 # back home (cd with no args also goes home)
ls -la               # long listing incl. hidden dotfiles; note . and ..
```
Reading a long listing — `-rw-r--r-- 1 milan milan 220 Jun 20 10:00 .bashrc`:
`type+perms` · `links` · `owner` · `group` · `size` · `mtime` · `name`.

**Your Windows C: drive is mounted at** `/mnt/c`. Prove it:
```bash
ls /mnt/c/Users/MilanGowdaJP/Documents/EXPERIMENTS/Learn
cd /mnt/c/Users/MilanGowdaJP/Documents/EXPERIMENTS/Learn/labs/m0-linux
ls   # you should see this README.md
```

**Checkpoint:** Name what lives in `/etc`, `/var/log`, `/home`, and where your
Windows files are inside WSL.

---

## Lab 2 — Permissions: rwx, octal, owners

**Why:** Every file has read/write/execute bits for **user / group / others**.
This is the core of Linux security (and why cloud keys must be `chmod 600`).

**The model.** Three triplets: `rwx rwx rwx` = owner, group, others.
Each triplet is a 3-bit number: `r=4, w=2, x=1`. Add them:
| Symbolic | Octal | Meaning |
|---|---|---|
| `rwx` | 7 | read+write+execute |
| `rw-` | 6 | read+write |
| `r-x` | 5 | read+execute |
| `r--` | 4 | read only |
| `---` | 0 | nothing |

So `rwxr-xr--` = `7 5 4` = `754`. `rw-------` = `600`.

**Do — a secret file only you can read:**
```bash
cd ~
echo "my cloud secret" > secret.txt
ls -l secret.txt              # default perms, e.g. -rw-r--r-- (644)
chmod 600 secret.txt          # only owner can read/write
ls -l secret.txt              # now -rw------- (600)
```

**Prove another user can't read it** (create a second user — needs sudo):
```bash
sudo adduser bob              # set any password; just hit Enter through the prompts
sudo -u bob cat ~/secret.txt  # run cat AS bob -> "Permission denied"  ✅
chmod 644 secret.txt          # open it back up
sudo -u bob cat ~/secret.txt  # now bob can read it
chmod 600 secret.txt          # lock it again
```

**Octal drill** — predict before you run:
```bash
chmod 754 secret.txt; ls -l secret.txt   # rwxr-xr-- ?
chmod 640 secret.txt; ls -l secret.txt   # rw-r----- ?
chmod 600 secret.txt; ls -l secret.txt   # rw------- ?
```
`chown` changes ownership (needs sudo): `sudo chown bob secret.txt`.

**Checkpoint:** Read `rwxr-x---` as octal instantly (= 750), and explain why an
SSH private key must be `600` (others readable = SSH refuses to use it).

---

## Lab 3 — Pipes, redirection, and the text trio (grep/find/sed/awk)

**Why:** The Unix superpower: small tools chained with `|`. You'll use this
constantly to inspect logs, find processes, and slice data.

**Redirection:** `>` overwrite, `>>` append, `<` read, `|` pipe one program's
output into another's input.
```bash
ls /etc > files.txt          # write listing to a file (overwrite)
echo "another line" >> files.txt   # append
wc -l files.txt              # count lines
cat files.txt | sort | uniq | head -5   # pipe chain: sort, dedupe, first 5
```

**grep** — search text:
```bash
grep ssh /etc/services       # lines mentioning ssh (note port 22)
grep -i error /var/log/dpkg.log    # -i = case-insensitive
ls -l /etc | grep '^d'       # only directories (lines starting with d)
```

**find** — search the filesystem:
```bash
find /etc -name "*.conf" 2>/dev/null | head    # *.conf files; hide errors
find ~ -type f -size +1k                        # files over 1KB in home
```

**sed / awk** — transform/extract:
```bash
echo "hello world" | sed 's/world/linux/'       # substitute -> hello linux
echo "a,b,c" | awk -F, '{print $2}'             # field 2 with comma sep -> b
cat /etc/passwd | awk -F: '{print $1}' | head   # all usernames (1st field)
```

**Checkpoint:** Build a one-liner that prints the 5 largest files under `/var/log`.
(Hint: `find ... -type f -printf '%s %p\n' | sort -rn | head -5`.)

---

## Lab 4 — Processes, signals, background jobs, tmux

**Why:** Servers run long-lived processes. You must be able to start them in the
background, find them, and kill them — and keep them alive after you disconnect.

**Start a process, find it, kill it:**
```bash
python3 -m http.server 8000 &     # & = run in background; prints a job + PID
jobs                               # list background jobs of this shell
ps aux | grep http.server          # find it by name -> note the PID (2nd column)
curl -s localhost:8000 | head      # prove it serves -> HTML directory listing
kill %1                            # kill background job #1  (or: kill <PID>)
```
Signals: `kill` sends `SIGTERM` (polite, default 15). `kill -9` sends `SIGKILL`
(forceful, can't be ignored). Try the polite one first.

**Survive logout with nohup:**
```bash
nohup python3 -m http.server 8001 > server.log 2>&1 &
# nohup = ignore hangup signal; >...2>&1 sends stdout+stderr to server.log
cat server.log                     # see startup line
ps aux | grep 8001
kill %1
```
`2>&1` means "send stderr (fd 2) to wherever stdout (fd 1) is going."

**tmux — detachable terminal sessions** (essential for remote/cloud work):
```bash
tmux new -s lab                    # start a named session "lab"
python3 -m http.server 8002        # runs in the foreground here
#  --- press Ctrl-b then d  to DETACH (the server keeps running) ---
tmux ls                            # see the session still alive
tmux attach -t lab                 # reattach — your server is still there
#  --- Ctrl-c to stop the server, then: exit ---
```

**System resources:**
```bash
htop      # live process viewer (q to quit); arrow keys, F9 to kill
df -h     # disk free per filesystem
du -sh ~  # total size of your home dir
free -h   # RAM usage
```

**Checkpoint:** Start a server in the background, find its PID two different ways
(`jobs` and `ps`), kill it, then run one under tmux and detach/reattach.

---

## Lab 5 — Write a bash script (`backup.sh`)

**Why:** Automation = scripts. You'll write bootstrap scripts for cloud VMs soon.

**Do — create it with nano** (`nano backup.sh`), type this, save with
`Ctrl-o Enter`, exit with `Ctrl-x`:
```bash
#!/usr/bin/env bash
# backup.sh — tar a folder into a timestamped archive
set -euo pipefail                 # fail fast: -e exit on error, -u undefined vars, -o pipefail
SRC="${1:-$HOME}"                 # 1st arg, default to home
STAMP="$(date +%Y%m%d-%H%M%S)"    # e.g. 20260620-103015
OUT="backup-$STAMP.tar.gz"
tar -czf "$OUT" -C "$(dirname "$SRC")" "$(basename "$SRC")"
echo "Created $OUT ($(du -h "$OUT" | cut -f1))"
```
Make it executable and run it:
```bash
chmod +x backup.sh           # add the execute bit
mkdir -p ~/demo && echo hi > ~/demo/a.txt
./backup.sh ~/demo           # -> Created backup-...tar.gz (4.0K)
ls -lh backup-*.tar.gz
tar -tzf backup-*.tar.gz     # list contents without extracting
```
> WSL gotcha: if you ever get `bad interpreter: /usr/bin/env^M`, the file has
> Windows line endings. Fix: `sed -i 's/\r$//' backup.sh`. (Happens when you
> edit a script on the Windows side. Editing in nano avoids it.)

**Checkpoint:** Explain `chmod +x`, what the `#!/usr/bin/env bash` shebang does,
and what `$1` / `${1:-$HOME}` mean.

---

## Lab 6 — Turn a server into a systemd service

**Why:** Production processes are managed by `systemd` — auto-start on boot,
auto-restart on crash, central logging. This is how the cloud worker will run.

**WSL prerequisite — systemd must be enabled.** Check:
```bash
ps -p 1 -o comm=        # what is PID 1?  Want: systemd
```
If it says `init` (not `systemd`), enable it:
```bash
sudo nano /etc/wsl.conf        # add the two lines below, save, exit
```
```ini
[boot]
systemd=true
```
Then from **PowerShell** (Windows): `wsl --shutdown`, wait ~10s, reopen Ubuntu,
and re-check `ps -p 1 -o comm=` → should now say `systemd`.

**Create the service** — `sudo nano /etc/systemd/system/hello.service`:
```ini
[Unit]
Description=Hello HTTP server (M0 lab)
After=network.target

[Service]
ExecStart=/usr/bin/python3 -m http.server 8003
WorkingDirectory=/home/%i
Restart=on-failure
User=%i

[Install]
WantedBy=multi-user.target
```
> Replace `%i` with your username on both lines (e.g. `milan`), or simpler: hard-code
> `WorkingDirectory=/tmp` and `User=<you>`.

**Enable, start, inspect:**
```bash
sudo systemctl daemon-reload         # re-read unit files
sudo systemctl enable --now hello    # enable (start on boot) + start now
systemctl status hello               # active (running)?  q to quit
curl -s localhost:8003 | head        # it's serving
journalctl -u hello --no-pager | tail   # its logs
sudo systemctl restart hello         # restart it
sudo systemctl stop hello            # stop
sudo systemctl disable hello         # don't start on boot
```

**Checkpoint:** Explain what `enable` vs `start` do (boot-time vs now), and how
to read a service's logs (`journalctl -u <name>`).

---

## Lab 7 — Schedule a job with cron

**Why:** Recurring tasks (nightly backups, the auto-stop kill switch in Module 6)
run on `cron`.

**WSL note:** the cron daemon may not be running. Start it:
```bash
sudo service cron start        # (or, with systemd: sudo systemctl enable --now cron)
```

**Add a job** — `crontab -e` (pick `nano` if asked). Add this line (every minute):
```cron
* * * * * echo "$(date) heartbeat" >> $HOME/heartbeat.log
```
The five stars = `minute hour day-of-month month day-of-week`. `* * * * *` = every minute.
```bash
# wait ~70 seconds, then:
cat ~/heartbeat.log            # one line per minute appears
crontab -l                     # list your jobs
crontab -e                     # delete the line to stop it (save+exit)
```
Cron syntax to recognize: `0 2 * * *` = 2:00 AM daily. `*/5 * * * *` = every 5 min.

**Checkpoint:** Read `30 3 * * 1` aloud (= 03:30 every Monday) and schedule a
job that runs every 5 minutes.

---

## Lab 8 — SSH to localhost (keys vs passwords)

**Why:** You'll SSH into every cloud VM. Practicing locally teaches keys and the
`authorized_keys` model without needing a remote box yet.

**Do:**
```bash
sudo apt install -y openssh-server
sudo service ssh start
ssh-keygen -t ed25519 -C "lab key"     # press Enter for defaults, empty passphrase OK for lab
ssh-copy-id localhost                   # installs your public key into ~/.ssh/authorized_keys
ssh localhost                           # logs in with NO password — key auth ✅
#   you're now in a nested shell on "the same machine"; type: exit
cat ~/.ssh/authorized_keys              # your public key is trusted here
ls -l ~/.ssh                            # note: private key id_ed25519 is 600
```
`scp` copies files over SSH: `scp ~/secret.txt localhost:/tmp/` then check `/tmp`.

**Checkpoint:** Explain the difference between the **private** key (stays secret,
`600`) and the **public** key (goes in `authorized_keys` on servers you log into).

---

## Lab 9 — OverTheWire "Bandit" (the best Linux practice anywhere)

**Why:** A game that teaches shell + ssh + permissions by *doing*. Levels 0→15
reinforce everything above.

**Do:** Play from your Ubuntu shell.
```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220   # password: bandit0
# read /etc/motd and the level pages at overthewire.org/wargames/bandit/
```
Each level's password unlocks the next (`bandit1`, `bandit2`, ...). Keep a notes
file. Aim for 0→15. This is homework — do a few levels per sitting.

**Checkpoint (Module 0 done):** From a fresh shell you can SSH to a host, find
what's listening, edit a file with nano, run a script as a background service,
and explain `rwxr-x---`.

---

## When you're done

Tick the **Fundamentals** boxes in `../../PROGRESS.md`, then tell me and we'll
move to **Module 1 — Networking** (ports, curl, DNS, TLS, SSH tunnels, nginx
reverse proxy in front of a FastAPI app).
