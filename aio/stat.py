#!/usr/bin/env python3

import sys, calendar, datetime, codecs

echoareas = []

def usage_quit():
    print("Usage: stat.py -c config_file -t [stats_type] -s YYYY.MM.DD -e YYYY.MM.DD.\n\
stats_type must be \"echoareas\" or \"points\"\n")
    sys.exit(1)

def load_config():
    global echoareas, title
    lines = open(config, "r").read().split("\n")
    for line in lines:
        param = line.split(" ")
        if param[0] == "echo":
            echoareas.append(param[1])
        if param[0] == "title":
            title = " ".join(param[1:])

def parse_date(date):
    date = date.split(".")
    return calendar.timegm(datetime.date(int(date[0]), int(date[1]), int(date[2])).timetuple())

def calculate_stat():
    stat = {}
    ret = []
    for echoarea in echoareas:
        msgs = codecs.open("aio/" + echoarea + ".aio", "r", "utf-8").read().split("\n")
        for line in msgs:
            if len(line) > 20:
                msg = line.split(chr(15))
                if int(msg[2]) >= start_date and int(msg[2]) < end_date:
                    if stat_type == "points":
                        if not msg[3] in stat:
                            stat[msg[3]] = 1
                        else:
                            stat[msg[3]] += 1
                    elif stat_type == "echoareas":
                        if not echoarea in stat:
                            stat[echoarea] = 1
                        else:
                            stat[echoarea] += 1
                    elif stat_type == "subjects":
                       if not msg[6] in stat:
                           stat[msg[6]] = 1
                       else:
                           stat[msg[6]] += 1
    for item in stat:
        ret.append([item, stat[item]])
    return sorted(ret, key=lambda ret: ret[1], reverse = True)

args=sys.argv[1:]

start_on = "-s" in args
end_on = "-e" in args
type_on = "-t" in args
config_on = "-c" in args

if len(args) != 8 or not start_on or not end_on or not type_on or not config_on:
    usage_quit()

start_date = parse_date(args[args.index("-s") + 1])
end_date = parse_date(args[args.index("-e") + 1])
stat_type = args[args.index("-t") + 1]
config = args[args.index("-c") + 1]

load_config()
stat = calculate_stat()
value_of_division = round(stat[0][1] / 54 + 0.49)
total = 0
print("%-25s ▒ ≈ %s messages" % (title, value_of_division))
print("───────────────────────────────────────────────────────────────────────────────")
for item in stat:
    dots = ""
    graph = ""
    empty = ""
    for i in range(1, 25 - len(item[0]) - len(str(item[1]))):
        dots = dots + "."
    for i in range(1, round(item[1] / value_of_division + 0.49) + 1):
        graph = graph + "█"
    for i in range(1, 55 - len(graph)):
        empty = empty + "▒"
    print("%s%s%s %s%s" % (item[0], dots, item[1], graph, empty))
    total = total + item[1]
print("───────────────────────────────────────────────────────────────────────────────")

empty = ""
for i in range(1, 20 - len(str(total))):
    empty = empty + " "

print("Total", empty, total, sep="")
