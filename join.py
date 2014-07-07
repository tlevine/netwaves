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
    dimensions = ('%d %d\n' % (columns, rows)).encode('ascii')
    wav_fp.write(dimensions)
    wav_fp.write(ppm_fp.readline()) # max color
    header_length = wav_fp.tell()
    print(header_length)
    ppm_fp.seek(0)
    print('--')
    wav_bytes = open(wav_fn, 'rb').read()
    print('--')
   #wav_fp.write(bytes(itertools.chain(*[[b] * 3 for b in wav_bytes])))
    wav_fp.write(wav_bytes)
    print('--')
    remainder = (columns * rows * 3 - header_length - len(wav_fp.getvalue()))
    remainder += 34 # why !????
    print(remainder)
    print(len(wav_fp.getvalue()))
    wav_fp.write(bytes([127] * remainder))
    wav_fp.seek(0)

    open('/tmp/a.ppm','wb').write(wav_fp.getvalue())

    ppm = Image.open(ppm_fp)
    wav = Image.open(wav_fp)
    Image.blend(ppm, wav, 0.2).save(out_fn)

join('augustin.ppm', 'fms.wav', 'out.ppm')
