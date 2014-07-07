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

def press(frequency, amplitude, nframes):
    bottom = -amplitude
    top = amplitude
    if frequency == None or amplitude == 0:
        for _ in range(nframes):
            yield 0
    else:
        step = round(frequency / amplitude / 2)
        atom = list(range(bottom, top, step))
        for _ in range(0,round(nframes / len(atom))):
            yield from atom

def song():
    drums = lambda freq: list(itertools.chain(
        press(freq, 30,  400),
        press(None, 0, 1600),
    ))
    phrase = lambda atom: functools.reduce(operator.add, itertools.repeat(atom, 8))
    return itertools.chain(
        phrase(drums(220)),
        phrase(drums(180)),
        phrase(drums(220)),
        phrase(drums(180)),
        map(lambda x: x + 10, phrase(drums(220))),
        map(lambda x: x + 10, phrase(drums(180))),
        map(lambda x: x + 10, phrase(drums(220))),
        map(lambda x: x + 10, phrase(drums(180))),
    )

def main():
    columns, rows, filename = 400, 300, '/tmp/z.ppm'
    with open(filename, 'wb') as fp:
        s = sink(columns, rows, fp)
        next(s)
        for frame in song():
            s.send(frame + 127)
        s.close()

main()
