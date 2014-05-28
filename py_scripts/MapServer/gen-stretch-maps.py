#! /usr/bin/python

import os, re



files = [
    { 'path' : '../data/bauempby15_2000.img',
      'layerName' : 'bauemp',
      'minColor' : '204,204,255',  'maxColor' : '0,0,153' },
    ];


def system(cmd):
    print cmd
    os.system(cmd)
    print "done"

for file in files:
    m = re.match(r'.*/(.+)\.img$', file['path'])
    base = m.group(1)
    if 'minColor' in file:
        system("./makestretchcmap -N 32 -a %s --rgbMin %s --rgbMax %s > cmaps/%s.cmap" % ( file['path'], file['minColor'], file['maxColor'],  base))
        system("./makestretchicon -c %s -T 0 -W 128 -h 15 -f 8 -L %s  -H %s -l low -r high cmapicons/%s.png" % (file['layerName'], file['minColor'], file['maxColor'], base))
    else:
        system("touch cmaps/%s.cmap"    % (base))
