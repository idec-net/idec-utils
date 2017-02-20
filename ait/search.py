#!/usr/bin/env python3

import sys, os, time

full = False
argn = 1

if sys.argv[argn] == "-f":
    full = True
    argn += 1

echoarea = sys.argv[argn]
word = " ".join(sys.argv[argn+1:])

if not os.path.exists("ait/%s.mat" % echoarea):
    print("Echoarea not found.")
    quit()

for msg in open("ait/%s.mat" % echoarea, "r").read().split("\n"):
    if word.lower() in msg.lower():
        tmp = msg.split(":")
        if full:
            if len(tmp) > 1:
                m = [tmp[0]] +  ":".join(tmp[1:]).split(chr(15))
                msgid = m[0]
                date = time.strftime("%Y.%m.%d %H:%M", time.gmtime(int(m[3])))
                fr = m[4]
                addr = m[5]
                to = m[6]
                subj = m[7]
                body = "\n".join(m[9:])
                print("== %s ==============================================" % msgid)
                print("От:   %s (%s) [%s]" % (fr, addr, date))
                print("Кому: %s" % to)
                print("Тема: %s\n" % subj)
                print(body)
        else:
            print(tmp[0])
