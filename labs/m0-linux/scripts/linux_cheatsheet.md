# Linux cheatsheet (Module 0)

Quick reference. Keep it open while you do the labs.

## Navigation & files
| Command | Does |
|---|---|
| `pwd` | print working directory |
| `ls -la` | list all (incl. hidden), long format |
| `cd -` | jump to previous directory |
| `tree -L 2` | directory tree, 2 levels deep |
| `cat / less / head -n / tail -n / tail -f` | view file / page / first N / last N / follow |
| `cp -r`, `mv`, `rm -r`, `mkdir -p` | copy(recursive), move/rename, remove(recursive), make-parents |
| `find <dir> -name "*.log"` | find files by pattern |
| `du -sh <dir>` / `df -h` / `free -h` | dir size / disk free / memory |

## Permissions
| Command | Does |
|---|---|
| `chmod 600 f` | rw------- (secrets, SSH keys) |
| `chmod 755 f` | rwxr-xr-x (scripts, dirs) |
| `chmod +x f` | add execute bit |
| `chown user:group f` | change owner (needs sudo) |
| `umask` | default-permission mask |

Octal: `r=4 w=2 x=1`, per triplet **user group others**. `rwxr-x---` = `750`.

## Processes & jobs
| Command | Does |
|---|---|
| `cmd &` | run in background |
| `jobs` / `fg` / `bg` | list / foreground / background jobs |
| `ps aux \| grep x` | find a process |
| `kill PID` / `kill -9 PID` | SIGTERM (polite) / SIGKILL (force) |
| `nohup cmd &` | survive logout |
| `htop` / `top` | live process viewer |
| `ss -tlnp` | what's listening (TCP, numeric, with PID) |

## tmux (detachable sessions)
| Keys / cmd | Does |
|---|---|
| `tmux new -s name` | new named session |
| `Ctrl-b d` | detach (leaves it running) |
| `tmux ls` / `tmux attach -t name` | list / reattach |
| `Ctrl-b c` / `Ctrl-b "` / `Ctrl-b %` | new window / split horiz / split vert |

## systemd (services)
| Command | Does |
|---|---|
| `systemctl status NAME` | is it running? |
| `sudo systemctl enable --now NAME` | start now + on boot |
| `sudo systemctl restart/stop NAME` | restart / stop |
| `journalctl -u NAME -f` | follow a service's logs |
| `sudo systemctl daemon-reload` | re-read unit files after editing |

## Packages (Debian/Ubuntu)
| Command | Does |
|---|---|
| `sudo apt update` | refresh package index |
| `sudo apt install -y X` | install |
| `apt list --installed \| grep X` | is it installed? |
| `which X` / `command -v X` | where's the binary |

## Text: pipes, grep, sed, awk
| Command | Does |
|---|---|
| `a \| b` / `>` / `>>` | pipe / overwrite-redirect / append-redirect |
| `grep -i -n -r pat .` | search (ignore-case, line-no, recursive) |
| `sort \| uniq -c \| sort -rn` | frequency count (top-N idiom) |
| `sed 's/old/new/g'` | substitute |
| `awk -F: '{print $1}'` | print field 1, ':' separator |
| `cut -d, -f2` | cut field 2, ',' delimiter |
| `wc -l` | count lines |

## SSH / copy
| Command | Does |
|---|---|
| `ssh user@host` | log in |
| `ssh-keygen -t ed25519` | make a key pair |
| `ssh-copy-id user@host` | install your public key on host |
| `scp file user@host:/path` | copy over SSH |
| `ssh -L 8080:localhost:8011 user@host` | tunnel: local 8080 → remote 8011 |

## Environment
| Command | Does |
|---|---|
| `echo $PATH` / `echo $HOME` | read a variable |
| `export VAR=value` | set for this shell + children |
| `env` / `printenv VAR` | list all / print one |
| `~/.bashrc` | runs on each interactive shell (put exports here) |
