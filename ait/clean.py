#!/usr/bin/env python3

import sys, calendar, datetime, os, re

def msg_filter(msgid):
    rr = re.compile(r'^[a-z0-9A-Z]{20}$')
    if rr.match(msgid): return True

if len(sys.argv) < 3:
    print("Usage: clean.py echoarea YYYY.MM.YY.")
    quit()

date = sys.argv[2].split(".")
date = calendar.timegm(datetime.date(int(date[0]), int(date[1]), int(date[2])).timetuple())

try:
    echoarea = open("ait/" + sys.argv[1] + ".mat", "r").read().split("\n")
except:
    print("Echoarea not found.")
    quit()

clean_echoarea = []
clean_index = []

for line in echoarea:
    msg = line.split(":")
    if msg_filter(msg[0]):
        msg[1] = msg[1].replace(chr(15), "\n")
        msgdate = int(msg[1].split("\n")[2])
        if msgdate >= date:
            print(msg[0] + ": saved.")
            clean_echoarea.append(line)
            clean_index.append(msg[0])

clean_echoarea.append("")
open("ait/" + sys.argv[1] + ".iat", "w").write("\n".join(clean_index))
open("ait/" + sys.argv[1] + ".mat", "w").write("\n".join(clean_echoarea))
