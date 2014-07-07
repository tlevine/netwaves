#!/usr/bin/env python3
from math import ceil
import itertools
import os
from io import BytesIO
from PIL import Image

def parser():
    p = argparse.ArgumentParser('Record sound as PPM.')
    p.add_argument('ppm', metavar = '[ppm file]')
    p.add_argument('wav', metavar = '[wav file]')
    return p

def main():
    p = parser().parse_args()

def new_image_size(wav_length, ppm_dimensions, scale):
    columns, rows = ppm_dimensions
    adj = wav_length / (columns * rows)
    return round(columns * adj ** 0.5 / scale), round(rows * adj ** 0.5 / scale)

def join(ppm_fn, wav_fn, out_fn):
    SCALE = 10
    ppm_fp = open(ppm_fn, 'rb')
    wav_fp = BytesIO()
    wav_fp.write(ppm_fp.readline()) # magic number
    columns, rows = map(int, ppm_fp.readline().decode('ascii').split(' '))
    wav_size = os.path.getsize(wav_fn)
    adj = (wav_size / (columns * rows)) ** 0.5
    new_columns = ceil(columns / adj)
    new_rows = ceil(rows / adj)
    dimensions = ('%d %d\n' % (new_columns, new_rows)).encode('ascii')
    wav_fp.write(dimensions)
    wav_fp.write(ppm_fp.readline()) # max color
    ppm_fp.seek(0)
    for line in open(wav_fn, 'rb'):
        wav_fp.write(line)
    remainder = (new_columns * new_rows - len(wav_fp.getvalue()))
    print(remainder)
    print(len(wav_fp.getvalue()))
    wav_fp.write(bytes([127] * remainder))
    wav_fp.seek(0)

    open('/tmp/a.ppm','wb').write(wav_fp.getvalue())

    ppm = Image.open(ppm_fp)
    wav = Image.open(wav_fp)
    Image.blend(ppm, wav, 0.8).save(out_fn)

join('augustin.ppm', 'fms.wav', 'out.ppm')
