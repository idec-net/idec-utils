#!/usr/bin/env python3

import sys, calendar, datetime, os

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

clean_echoarea = []

for msgid in echoarea:
    if len(msgid) == 20:
        try:
            msgdate = int(open("msg/" + msgid, "r").read().split("\n")[2])
        except:
            print(msgid + ": not found.")
            msgdate = 0
        if msgdate >= date:
            print(msgid + ": saved.")
            clean_echoarea.append(msgid)
        else:
            print(msgid + ": deleted.")
            os.remove("msg/" + msgid)

clean_echoarea.append("")
open("echo/" + sys.argv[1], "w").write("\n".join(clean_echoarea))
