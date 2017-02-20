#!/usr/bin/env python3

import sys, calendar, datetime, base64

if len(sys.argv) < 3:
    print("Usage: archive.py echoarea YYYY.MM.YY.")
    quit()

date = sys.argv[2].split(".")
date = calendar.timegm(datetime.date(int(date[0]), int(date[1]), int(date[2])).timetuple())

try:
    echoarea = open("echo/" + sys.argv[1], "r").read().split("\n")
except:
    print("Echoarea not found.")
    quit()

bundle = ""

for msgid in echoarea:
    if len(msgid) == 20:
        try:
            msgdate = int(open("msg/" + msgid, "r").read().split("\n")[2])
            msg = str.encode(open("msg/" + msgid, "r").read())
        except:
            msg = False
            print(msgid + ": not found.")
        if msg and msgdate < date:
            bundle = bundle + msgid + ":"
            bundle = bundle + (base64.b64encode(msg)).decode("utf-8") + "\n"
            print(msgid + ": OK")

open(sys.argv[1] + "_" + sys.argv[2] + ".bundle", "w").write(bundle)
