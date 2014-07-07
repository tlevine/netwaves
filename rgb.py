#!/usr/bin/env python3
import itertools

import alsaaudio, time, audioop

def sink(columns, rows, wav_pointer, ppm_pointer):
    try:
        pointers = [ppm_pointer, wav_pointer]
        header_str = 'P6\n%d %d\n255\n' % (columns, rows)
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
        l = [127] * (columns * rows * 3 - count)
        for pointer in pointers:
            pointer.write(bytes(l))
            pointer.flush()

def microphone():
    inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)
    inp.setchannels(1)
    inp.setrate(8000)
    inp.setformat(alsaaudio.PCM_FORMAT_S8)
    inp.setperiodsize(160)
    return inp

def main():
    try:
        s = sink(800, 600, open('sink.wav', 'wb'), open('sink.ppm', 'wb'))
        next(s)
        mic = microphone()
        while True:
            l, data = mic.read()
            if l:
                s.send(data[1:])
    except KeyboardInterrupt:
        s.close()
        raise

main()
