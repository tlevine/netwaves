#!/usr/bin/env python3
import itertools

def sink(columns, rows, wav_pointer, ppm_pointer):
    try:
        pointers = [ppm_pointer, wav_pointer]
        header_str = 'P6\n%d %d255\n' % (columns, rows)
        header = header_str.encode('ascii')
        ppm_pointer.write(header)
        count = 0
        while True:
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
        l = [127] * (columns * rows - count)
        for pointer in pointers:
            print(l)
            pointer.write(bytes(l))
            pointer.flush()

s = sink(800, 600, open('sink.wav', 'wb+'), open('sink.ppm', 'wb+'))
next(s)
s.send(0)
s.send([127,255])
