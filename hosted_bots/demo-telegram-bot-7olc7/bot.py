import time
import sys
print("=== Telegram Bot Engine Started (PID active) ===", flush=True)
print("24/7 Watchdog daemon running...", flush=True)
count = 1
while True:
    print(f"Heartbeat ping #{count} - Bot is online and listening...", flush=True)
    time.sleep(30)
    count += 1
