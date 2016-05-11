#!/usr/bin/env python3

import os, sys, sqlite3

if len(sys.argv) < 2:
    print("Usage: txt2sqlite.py filename.")
    quit()

try:
    os.remove(sys.argv[1])
except:
    None

conn = sqlite3.connect(sys.argv[1])
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS msg(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
msgid TEXT,
kludges TEXT,
echoarea TEXT,
timestump INTEGER,
from_name TEXT,
address TEXT,
to_name TEXT,
subject TEXT,
body TEXT,
UNIQUE (id, msgid));""")

try:
    echoareas = sorted(os.listdir("echo/"))
except:
    print("Directory echo/ not found.")
    quit()

for echoarea in echoareas:
    if "." in echoarea:
        print("Echoarea: " + echoarea)
        msgids = open("echo/" + echoarea, "r").read().split("\n")
        for msgid in msgids[:-1]:
            print(msgid, end=": ")
            try:
                msg = open("msg/" + msgid, "r").read().split("\n")
                kludges = msg[0]
                echoarea = msg[1]
                timestump = int(msg[2])
                from_name = msg[3]
                address = msg[4]
                to_name = msg[5]
                subject = msg[6]
                body = "\n".join(msg[8:])
                c.execute("INSERT OR IGNORE INTO msg (msgid, kludges, echoarea, timestump, from_name, address, to_name, subject, body) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", (msgid, kludges, echoarea, timestump, from_name, address, to_name, subject, body))
                print("OK.")
            except:
                print()
                print(msgid + ": not found.")
        conn.commit()

conn.close()
