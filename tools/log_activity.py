#!/usr/bin/env python3
"""
Simple logger: record activity events (gym, study, sleep, etc.) into activities.json
Usage:
  python tools/log_activity.py gym "Leg day 90min"
  python tools/log_activity.py study "TryHackMe: Pre-Security room1"
"""

import sys, json, os, datetime

OUT_FILE = "activities.json"

def load():
    if os.path.exists(OUT_FILE):
        return json.load(open(OUT_FILE))
    return {"activities": []}

def save(data):
    with open(OUT_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add(type_, note):
    data = load()
    entry = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "type": type_,
        "note": note
    }
    data["activities"].append(entry)
    save(data)
    print("Logged:", entry)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python tools/log_activity.py <type> \"<note>\"")
        sys.exit(1)
    t = sys.argv[1]
    n = " ".join(sys.argv[2:])
    add(t, n)
