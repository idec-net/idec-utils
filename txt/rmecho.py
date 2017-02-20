#!/usr/bin/env python3

import os, sys

if len(sys.argv) == 2:
    try:
        echo = open("echo/" + sys.argv[1], "r")
    except:
        echo = False
        print("Эхоконференция не найдена.")
    if echo:
        msgids = echo.read().split("\n")[:-1]
        for msgid in msgids:
            print("Delete: " + msgid, end=" ")
            os.remove("msg/" + msgid)
            print("OK")
        os.remove("echo/" + sys.argv[1])
else:
    print("Укажите эхоконференцию в качестве параметра.")
