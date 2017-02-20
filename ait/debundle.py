#!/usr/bin/env python3

import sys, os, base64, codecs, re

def msg_filter(msgid):
    rr = re.compile(r'^[a-z0-9A-Z]{20}$')
    if rr.match(msgid): return True

if len(sys.argv) < 2:
    print("Usage: debundle.py filename.")
    quit()

if not os.path.exists("ait"):
    os.mkdir("ait")

bundle = open(sys.argv[1], "r").read().split("\n")

for msg in bundle:
    if msg:
        m = msg.split(":")
        msgid = m[0]
        if msg_filter(msgid) and m[1]:
            try:
                msgbody = base64.b64decode(m[1].encode("ascii")).decode("utf8")
                codecs.open("ait/" + msgbody.split("\n")[1] + ".iat", "a", "utf-8").write(msgid + "\n")
                codecs.open("ait/" + msgbody.split("\n")[1] + ".mat", "a", "utf-8").write(msgid + ":" + msgbody.replace("\n", chr(15)) + "\n")
                print(msgid + ": OK.")
            except:
                print(msgid + ": error.")
