#!/usr/bin/env python3
import itertools

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
       #fp.write(remainder)
       #fp.close()

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
    bpm = 60
    framerate = 8000
    def beats(nbeats):
        'Return a number of frames'
        seconds = nbeats * bpm * 60
        return round(framerate / seconds)
    return itertools.chain(
        press(220, 30, beats(1)),
        press(None, 0, beats(1)),
        press(220, 30, beats(1)),
        press(None, 0, beats(1)),
        press(220, 30, beats(1)),
        press(None, 0, beats(1)),
        press(220, 30, beats(1)),
        press(None, 0, beats(1)),
    )

def main():
    columns, rows, filename = 800, 600, '/tmp/z.ppm'
    with open(filename, 'wb') as fp:
        s = sink(columns, rows, fp)
        next(s)
        for frame in song():
            s.send(frame + 127)

main()
