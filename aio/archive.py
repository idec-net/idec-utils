#!/usr/bin/env python3

import sys, calendar, datetime, base64, re

def msg_filter(msgid):
    rr = re.compile(r'^[a-z0-9A-Z]{20}$')
    if rr.match(msgid): return True

if len(sys.argv) < 3:
    print("Usage: archive.py echoarea YYYY.MM.YY.")
    quit()

date = sys.argv[2].split(".")
date = calendar.timegm(datetime.date(int(date[0]), int(date[1]), int(date[2])).timetuple())

try:
    echoarea = open("aio/" + sys.argv[1] + ".aio", "r").read().split("\n")
except:
    print("Echoarea not found.")
    quit()

bundle = ""

for line in echoarea:
    msg = line.split(":")
    if msg_filter(msg[0]):
        msg[1] = ":".join(msg[1:]).replace(chr(15), "\n")
        msgdate = int(msg[1].split("\n")[2])
        if msg and msgdate < date:
            bundle = bundle + msg[0] + ":"
            bundle = bundle + (base64.b64encode(str.encode(msg[1]))).decode("utf-8") + "\n"
            print(msg[0] + ": OK")

open(sys.argv[1] + "_" + sys.argv[2] + ".bundle", "w").write(bundle)
