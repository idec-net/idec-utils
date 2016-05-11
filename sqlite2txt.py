#!/usr/bin/env python3

import os, sys, sqlite3
from shutil import rmtree

if len(sys.argv) < 2:
    print("Usage: sqlite2txt.py filename.")
    quit()

if os.path.exists("echo/"):
    rmtree("echo/")
if os.path.exists("msg/"):
    rmtree("msg/")
os.mkdir("echo/")
os.mkdir("msg/")

if not os.path.exists(sys.argv[1]):
    print("Database not found.")
    quit()

conn = sqlite3.connect(sys.argv[1])
c = conn.cursor()

echoareas = []
for row in c.execute("SELECT echoarea FROM msg GROUP BY echoarea;"):
    echoareas.append(row[0])

for echoarea in echoareas:
    print("Echoarea: " + echoarea)
    echo = open("echo/" + echoarea, "w")
    msgids = []
    for msg in c.execute("SELECT * FROM msg WHERE echoarea = '" + echoarea + "' ORDER BY id;"):
        print (msg[1], end=": ")
        echo.write(msg[1] + "\n")
        msgf = open("msg/" + msg[1], "w")
        msgf.write(msg[2] + "\n" + msg[3] + "\n" + str(msg[4]) + "\n" + msg[5] + "\n" + msg[6] + "\n" + msg[7] + "\n" + msg[8] + "\n\n" + msg[9])
        msgf.close()
        print("OK.")
    echo.close()

conn.close()
