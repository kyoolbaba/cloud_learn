#!/usr/bin/env bash
# processes_demo.sh — self-narrating tour of background jobs, ps, signals, nohup.
# Usage:  ./processes_demo.sh
set -euo pipefail

PORT=8009
echo "1) Start a web server in the BACKGROUND with '&' (returns control immediately):"
python3 -m http.server "$PORT" >/tmp/srv.log 2>&1 &
PID=$!                         # $! = PID of the most recent background job
echo "   Started http.server on :$PORT  (PID=$PID)"
sleep 1
echo

echo "2) Find it by name with ps + grep (the classic move):"
ps aux | grep "[h]ttp.server" | sed 's/^/   /'   # [h] trick hides grep's own line
echo

echo "3) Prove it's serving with curl:"
curl -s "localhost:$PORT" | head -3 | sed 's/^/   /'
echo

echo "4) See what's LISTENING on the port:"
ss -tlnp 2>/dev/null | grep ":$PORT" | sed 's/^/   /' || echo "   (install iproute2 for ss)"
echo

echo "5) Signals: 'kill <PID>' sends SIGTERM (polite). 'kill -9' sends SIGKILL (forceful)."
echo "   Sending SIGTERM to $PID ..."
kill "$PID"
sleep 1
if kill -0 "$PID" 2>/dev/null; then
  echo "   Still alive; escalating to SIGKILL."
  kill -9 "$PID"
else
  echo "   Process $PID is gone. ✅"
fi
echo

echo "6) nohup = survive logout. Output goes to a file since there's no terminal:"
nohup python3 -m http.server 8010 >/tmp/nohup_srv.log 2>&1 &
NPID=$!
sleep 1
echo "   nohup server PID=$NPID; log head:"
head -1 /tmp/nohup_srv.log | sed 's/^/   /' || true
kill "$NPID" 2>/dev/null || true
echo "   (cleaned up)"
echo
echo "Next: do the tmux part by hand (a script can't detach a TTY):"
echo "   tmux new -s lab   ->   run a server   ->   Ctrl-b d (detach)   ->   tmux attach -t lab"
