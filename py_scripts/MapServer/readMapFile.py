#! /usr/bin/python
started = False
collected_lines = []
with open("rlayers.tpl.map", "r") as fp:
    for i, line in enumerate(fp.readlines()):
        if line.rstrip().lstrip() == "LAYER": 
            started = True
            print "started at line", i # counts from zero !
            continue
        if started and line.rstrip().lstrip()=="END":
            print "end at line", i
            # break
        # process line 
        collected_lines.append(line.rstrip())