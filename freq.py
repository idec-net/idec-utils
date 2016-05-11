#!/usr/bin/env python3

import sys, urllib.request, urllib.parse

if len(sys.argv) < 3:
    print("Usage: freq.py [-c config] [-n node] [-a authkey] [-f filename].")
    quit()

node = False
authkey = False
filename = False

def load_config(filename):
    global node, authkey
    config = open(filename, "r").read().split("\n")
    for line in config:
        param = line.split(" ")
        if len(param) == 2:
            if param[0] == "node":
                node = param[1]
            elif param[0] == "auth":
                authkey = param[1]

def get_size(text):
    size = int(text)
    if size < 1024:
        return str(size) + " B"
    elif size < 1024 * 1025:
        return str(format(size / 1024, ".2f")) + " KB"
    else:
        return str(format(size / 1024 / 1024, ".2f")) + " MB"

if "-c" in sys.argv:
    load_config(sys.argv[sys.argv.index("-c") + 1])
if "-n" in sys.argv:
    node = sys.argv[sys.argv.index("-n") + 1]
if "-a" in sys.argv:
    authkey = sys.argv[sys.argv.index("-a") + 1]
if "-f" in sys.argv:
    filename = sys.argv[sys.argv.index("-f") + 1]

if not node:
    print("Node address not found.")
    quit()

if not filename:
    if authkey:
        data = urllib.parse.urlencode({"pauth": authkey}).encode("utf-8")
        request = urllib.request.Request(node + "x/filelist")
        result = urllib.request.urlopen(request, data).read().decode("utf-8")
    else:
        request = urllib.request.Request(node + "x/filelist")
        result = urllib.request.urlopen(request).read().decode("utf-8")
    filelist = result.split("\n")
    max_filename = 0
    max_size = 0
    for line in filelist:
        field = line.split(":")
        if len(field) == 3:
            if max_filename < len(field[0]):
                max_filename = len(field[0])
            if max_size < len(get_size(field[1])):
                max_size = len(get_size(field[1]))
    for line in filelist:
        field = line.split(":")
        if len(field) == 3:
            print(field[0], end="")
            for i in range(0, max_filename - len(field[0]) + 1):
                print(" ", end="")
            print("| " + get_size(field[1]), end="")
            for i in range(0, max_size - len(get_size(field[1])) + 1):
                print(" ", end="")
            print("| " + field[2])
else:
    if authkey:
        data = urllib.parse.urlencode({"pauth": authkey, "filename": filename}).encode("utf8")
        out = urllib.request.urlopen(node + "x/file", data)
    else:
        data = urllib.parse.urlencode({"filename": filename}).encode("utf8")
        out = urllib.request.urlopen(node + "x/file", data)
    file_size=0
    block_size=8192

    f = open(filename, "wb")
    while True:
        buffer = out.read(block_size)
        if not buffer:
            break
        file_size += len(buffer)
        f.write(buffer)
    f.close()
    print("Получено " + str(get_size(file_size)))
