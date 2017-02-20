#!/usr/bin/env python3

import sys, os, base64, codecs

if len(sys.argv) < 2:
    print("Usage: debundle.py filename.")
    quit()

if not os.path.exists("echo"):
    os.mkdir("echo")
if not os.path.exists("msg"):
    os.mkdir("msg")

bundle = open(sys.argv[1], "r").read().split("\n")

for msg in bundle:
    if msg:
        m = msg.split(":")
        msgid = m[0]
        if len(msgid) == 20 and m[1]:
            try:
                msgbody = base64.b64decode(m[1].encode("ascii")).decode("utf8")
                codecs.open("msg/" + msgid, "w", "utf-8").write(msgbody)
                codecs.open("echo/" + msgbody.split("\n")[1], "a", "utf-8").write(msgid + "\n")
                print(msgid + ": OK.")
            except:
                print(msgid + ": error.")
