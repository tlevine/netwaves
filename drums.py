#!/usr/bin/env python3
import operator
import itertools
import functools

def sink(columns, rows, fp):
    try:
        header_str = '''P5\n%d %d\n255\n''' % (columns, rows)
        header = header_str.encode('ascii')
        fp.write(header)
        length = columns * rows
        written = 0
        while written < length:
            fp.write(bytes([(yield)]))
            fp.flush()
            written += 1
    except GeneratorExit:
        remainder = bytes([127] * (length - written))
#       fp.write(remainder)
#       fp.close()

def press(offset, frequency, amplitude, nframes):
    bottom = -amplitude
    top = amplitude
    if frequency == None or amplitude == 0:
        for _ in range(nframes):
            yield 0 + offset
    else:
        step = round(frequency / amplitude / 2)
        atom = list(range(bottom, top, step))
        for _ in range(0,round(nframes / len(atom))):
            for a in atom:
                yield a + offset

def song():
    def drums(freq, offset):
        return itertools.chain(
             press(offset, freq, 30,  400),
             press(offset, None, 0, 1600),
        )
    return itertools.chain(
        drums(220, 0),
        drums(220, 20),
        drums(220, 0),
        drums(220, 20),
        drums(220, 0),
        drums(220, 20),
        drums(220, 0),
        drums(220, 20),
        drums(180, 0),
        drums(180, 20),
        drums(180, 0),
        drums(180, 20),
        drums(180, 0),
        drums(180, 20),
        drums(180, 0),
        drums(180, 20),
    )

def main():
    columns, rows, filename = 400, 400, '/tmp/z.ppm'
    with open(filename, 'wb') as fp:
        s = sink(columns, rows, fp)
        next(s)
        for frame in song():
            s.send(frame + 127)
        s.close()

main()
