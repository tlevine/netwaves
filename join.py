#!/usr/bin/env python3
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
    original_image = Image.open(ppm_fn)
    intermediate_ppm = BytesIO()
    wav = open(wav_fn, 'rb')
    out = open(out_fn, 'wb')

    size = new_image_size(os.path.getsize(wav_fn), original_image.size, SCALE)
    columns, rows = size
    original_image.resize(size)
    original_image.save(intermediate_ppm, format = 'ppm')

    intermediate_ppm.seek(0)
    magicnumber = intermediate_ppm.readline()
    dimensions = intermediate_ppm.readline()
    maxcolor = intermediate_ppm.readline()
    out.write(magicnumber)
    out.write(dimensions)
    out.write(maxcolor)
    intermediate_ppm.seek(0)

    while True:
        half = lambda x: round(x / 2)
        image_row = list(map(half, intermediate_ppm.read(columns)))
        if len(image_row) < columns:
            break

        audio_row = itertools.chain(*[[half(ord(wav.read(1)))] * SCALE for _ in range(round(columns/SCALE))])
        print(image_row, audio_row)

        # Adjust them, and write it a few times
        # out.write(bytes([a + b for a, b in zip(image_row, audio_row)] * SCALE))
        # out.write(bytes([a + b for a, b in zip(image_row, audio_row)]))
        out.write(bytes(image_row))

join('augustin.ppm', 'fms.wav', 'out.ppm')
