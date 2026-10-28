"""Synthetic Windows-style authentication log generator (ALL DATA IS FAKE).

Event 4624 = successful logon, Event 4625 = failed logon.
Every row carries a ground-truth label so detection rules can be scored.
"""
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)

START = datetime(2026, 10, 26, 0, 0, 0)
OUT_FILE = Path(__file__).parent / "logs" / "auth_logs.csv"
USERS = [f"user{i:02d}" for i in range(1, 41)]
events = []


def add(ts, ok, user, ip, host, logon_type, label, scenario):
    events.append({
        "timestamp": ts.strftime("%Y-%m-%d %H:%M:%S"),
        "event_id": 4624 if ok else 4625,
        "username": user,
        "source_ip": ip,
        "workstation": host,
        "logon_type": logon_type,
        "label": label,
        "scenario": scenario,
    })


# 1. NORMAL LOGINS
for i, user in enumerate(USERS):
    ip, host = f"10.0.1.{10 + i}", f"PC-{i:02d}"
    for day in range(3):
        t = START + timedelta(
            days=day,
            hours=random.randint(8, 10),
            minutes=random.randint(0, 59)
        )
        if random.random() < 0.10:
            add(t, False, user, ip, host, 2, "benign", "typo")
            t += timedelta(seconds=random.randint(10, 40))
        add(t, True, user, ip, host, 2, "benign", "normal")


# 2. BENIGN SHARED VPN IP
VPN_IP = "203.0.113.50"
for user in random.sample(USERS, 30):
    t = START + timedelta(
        hours=9,
        minutes=random.randint(0, 25),
        seconds=random.randint(0, 59)
    )
    if random.random() < 0.5:
        add(t, False, user, VPN_IP, "VPN-GW", 3,
            "benign", "vpn_shared_ip")
        t += timedelta(seconds=20)
    add(t, True, user, VPN_IP, "VPN-GW", 3,
        "benign", "vpn_shared_ip")


# 3. BENIGN SERVICE ACCOUNT FAILURES
t = START + timedelta(hours=13)
for _ in range(24):
    add(t, False, "svc_backup", "10.0.2.5", "BACKUP-SRV", 5,
        "benign", "service_account")
    t += timedelta(minutes=5)


# 4. BENIGN USER LOCKOUT
t = START + timedelta(hours=11)
for _ in range(8):
    add(t, False, "user07", "10.0.1.17", "PC-07", 2,
        "benign", "lockout")
    t += timedelta(seconds=20)


# 5. ATTACK A: LOUD PASSWORD SPRAY
ATTACKER_A = "198.51.100.23"
t = START + timedelta(hours=2)
for user in USERS[:25]:
    add(t, False, user, ATTACKER_A, "UNKNOWN", 3,
        "attack", "spray_loud")
    t += timedelta(seconds=20)

add(t + timedelta(minutes=2), True, "user12", ATTACKER_A,
    "UNKNOWN", 3, "attack", "spray_loud")


# 6. ATTACK B: LOW-AND-SLOW PASSWORD SPRAY
ATTACKER_B = "192.0.2.77"
t = START + timedelta(days=1, hours=1)
for user in USERS[20:40]:
    add(t, False, user, ATTACKER_B, "UNKNOWN", 3,
        "attack", "spray_slow")
    t += timedelta(minutes=15)

add(t, True, "user33", ATTACKER_B, "UNKNOWN", 3,
    "attack", "spray_slow")


# SORT AND WRITE CSV
events.sort(key=lambda e: e["timestamp"])
OUT_FILE.parent.mkdir(parents=True, exist_ok=True)

with open(OUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=events[0].keys())
    writer.writeheader()
    writer.writerows(events)


# SUMMARY
total = len(events)
attacks = sum(e["label"] == "attack" for e in events)
fails = sum(e["event_id"] == 4625 for e in events)

print(f"Wrote {total} events to {OUT_FILE}")
print(f"  attack events: {attacks} | benign events: {total - attacks}")
print(f"  failed logons (4625): {fails} | successful logons (4624): {total - fails}")