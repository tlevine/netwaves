#!/usr/bin/env python3
from time import sleep
from threading import Thread
import operator
import argparse
import itertools
from io import BytesIO

from getch import Getch

def sink(columns, rows, wav_pointer, ppm_pointer):
    try:
        pointers = [ppm_pointer, wav_pointer]
        header_str = 'P6\n%d %d\n255\n' % (columns, rows)
        header = header_str.encode('ascii')
        ppm_pointer.write(header)
        count = 0
        for i in itertools.count(0, 1):
            for pointer in pointers:
                raw = (yield)
                if isinstance(raw, int):
                    result = [raw]
                else:
                    result = list(raw)
                pointer.write(bytes(result))
                pointer.flush()
            count += len(result)
    except GeneratorExit:
        l = [127] * (columns * rows * 3 - count)
        for pointer in pointers:
            pointer.write(bytes(l))
            pointer.flush()

def update_color(color, key):
    if key in 'rgb':
        f = operator.sub
    elif key in 'RGB':
        f = operator.add
    else:
        return

    new_subcolor = f(color[key.lower()], 8)
    if new_subcolor >= 0 and new_subcolor <= 255:
        color[key.lower()] = new_subcolor

def work_color(state, color):
    import sys
    g = Getch()
    while state['running']:
        key = g()
        if key == 'q':
            state['running'] = False
        else:
            update_color(color, key)

def pipe(columns, rows, basename):
    try:
        s = sink(columns, rows, open('%s.wav' % basename, 'wb'), open('%s.ppm' % basename, 'wb'))
        next(s)
        color = {'r':127 - 80,'g':127,'b':127}
        state = {'running': True}
        Thread(None, target = work_color, args = (state, color,)).start()
        while state['running']:
            s.send([color['r'], color['g'], color['b']])
            sleep(0.0001)
        s.close()
    except KeyboardInterrupt:
        s.close()
        raise

def parser():
    p = argparse.ArgumentParser('Record sound as PPM.')
    p.add_argument('basename',
        help = 'Output will be written to $basename{wav,ppm}.')
    p.add_argument('-c', '--columns', type = int, default = 800,
        help = 'Number of columns in the image')
    p.add_argument('-r', '--rows', type = int, default = 450,
        help = 'Number of rows in the image')
    return p

def main():
    p = parser().parse_args()
    import os, sys
    os.system('sleep 1s && feh -D 0.1 %s.ppm %s.ppm &' % (p.basename, p.basename))
    pipe(p.columns, p.rows, p.basename)

if __name__ == '__main__':
    main()
