#!/usr/bin/env python3

import sys, os, codecs

args = sys.argv[1:]

if not os.path.exists("ait"):
    os.makedirs("ait")

for echoarea in args:
    try:
        index = open("echo/%s" % echoarea, "r").read().split("\n")
        for msgid in index:
            if len(msgid) == 20:
                try:
                    msg = codecs.open("msg/%s" % msgid, "r", "utf8").read()
                    open("ait/%s.iat" % echoarea, "a").write("%s\n" % msgid)
                    codecs.open("ait/%s.mat" % echoarea, "a", "utf8").write("%s:%s\n" % (msgid, msg.replace("\n", chr(15))))
                    print("%s: OK" % msgid)
                except:
                    print("%s: FAIL")
    except:
        print("%s: FAIL")
