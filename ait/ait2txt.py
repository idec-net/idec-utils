#!/usr/bin/env python3

import sys, os, codecs, re

def msg_filter(msgid):
    rr = re.compile(r'^[a-z0-9A-Z]{20}$')
    if rr.match(msgid): return True

args = sys.argv[1:]

if not os.path.exists("echo"):
    os.makedirs("echo")
if not os.path.exists("msg"):
    os.makedirs("msg")

for echoarea in args:
    for msg in codecs.open("ait/%s.mat" % echoarea, "r", "utf8").read().split("\n"):
        temp = msg.split(":")
        if len(temp) > 1:
            if msg_filter(temp[0]):
                msgid = temp[0]
                msgbody = ":".join(temp[1:]).replace(chr(15), "\n")
                open("echo/%s" % echoarea, "a").write(msgid + "\n")
                codecs.open("msg/%s" % msgid, "w", "utf8").write(msgbody)
                print("%s: OK" % msgid)
            else:
                print("%s: FAILED" % temp[0])
