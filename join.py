#!/usr/bin/env python3
from math import ceil
import itertools
import os
from io import BytesIO
from PIL import Image

def join(ppm_fn, wav_fn, out_fn):
    ppm_fp = open(ppm_fn, 'rb')
    wav_fp = BytesIO()
    wav_fp.write(ppm_fp.readline()) # magic number
    columns, rows = map(int, ppm_fp.readline().decode('ascii').split(' '))
    wav_size = os.path.getsize(wav_fn)
    dimensions = ('%d %d\n' % (columns, rows)).encode('ascii')
    wav_fp.write(dimensions)
    wav_fp.write(ppm_fp.readline()) # max color
    header_length = wav_fp.tell()
    print(header_length)
    ppm_fp.seek(0)
    wav_bytes = open(wav_fn, 'rb').read()
    wav_fp.write(wav_bytes)
    remainder = (columns * rows * 3 - header_length - len(wav_fp.getvalue()))
    remainder += 34 # why !????
    wav_fp.write(bytes([127] * remainder))
    wav_fp.seek(0)

    open('%s.ppm' % wav_fn,'wb').write(wav_fp.getvalue())

    ppm = Image.open(ppm_fp)
    wav = Image.open(wav_fp)
    Image.blend(ppm, wav, 0.4).save(out_fn)

join('augustin.ppm', 'fms.wav', 'out.ppm')
