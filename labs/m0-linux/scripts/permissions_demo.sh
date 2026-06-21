#!/usr/bin/env bash
# permissions_demo.sh — a guided, self-narrating tour of Linux file permissions.
# Run it and READ the output; it explains chmod / octal / rwx as it goes.
# Usage:  ./permissions_demo.sh
set -euo pipefail

WORK="$(mktemp -d)"          # a throwaway temp directory
cd "$WORK"
echo "Working in a scratch dir: $WORK"
echo

echo "1) Create a file and look at its default permissions:"
echo "my cloud secret" > secret.txt
ls -l secret.txt
echo "   The 10 chars '-rw-r--r--' mean: type(-) | owner(rw-) | group(r--) | others(r--)"
echo

echo "2) Octal = each rwx triplet as a number (r=4, w=2, x=1):"
echo "   rwx=7  rw-=6  r-x=5  r--=4  ---=0     so rw-r--r-- = 644"
echo

demo() {  # helper: apply a mode, then show symbolic result
  chmod "$1" secret.txt
  printf "   chmod %-4s -> %s\n" "$1" "$(ls -l secret.txt | awk '{print $1}')"
}
echo "3) Watch the bits change as we set different octal modes:"
demo 600   # rw-------
demo 644   # rw-r--r--
demo 754   # rwxr-xr--
demo 640   # rw-r-----
demo 700   # rwx------
echo

echo "4) The 'x' (execute) bit is what makes a script runnable:"
printf '#!/usr/bin/env bash\necho "I ran!"\n' > hello.sh
chmod 644 hello.sh
echo "   With 644 (no x):"
if ./hello.sh 2>/dev/null; then :; else echo "   -> Permission denied (no execute bit)"; fi
chmod +x hello.sh
echo "   After 'chmod +x' (now $(ls -l hello.sh | awk '{print $1}')):"
./hello.sh | sed 's/^/   -> /'
echo

echo "5) Why SSH keys must be 600: if others can read your private key, sshd refuses it."
echo "   Rule of thumb:  secrets 600, scripts 755, normal files 644, dirs 755."
echo
echo "Done. Scratch dir was $WORK (safe to ignore; it's in /tmp)."
