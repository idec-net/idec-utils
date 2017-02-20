#!/usr/bin/env python3

import sys, os, codecs

args = sys.argv[1:]

if not os.path.exists("aio"):
    os.makedirs("aio")

for echoarea in args:
    try:
        index = open("echo/%s" % echoarea, "r").read().split("\n")
        for msgid in index:
            if len(msgid) == 20:
                try:
                    msg = codecs.open("msg/%s" % msgid, "r", "utf8").read()
                    codecs.open("aio/%s.aio" % echoarea, "a", "utf8").write("%s:%s\n" % (msgid, msg.replace("\n", chr(15))))
                    print("%s: OK" % msgid)
                except:
                    print("%s: FAIL")
    except:
        print("%s: FAIL")
