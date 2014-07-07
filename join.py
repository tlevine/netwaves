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
    ppm_fp = open(ppm_fn, 'rb')
    wav_fp = BytesIO()
    for _ in range(3):
        wav_fp.write(ppm_fp.readline())
    ppm_fp.seek(0)
    for line in open(wav_fn, 'rb'):
        wav_fp.write(line)
    wav_fp.seek(0)

    ppm = Image.open(ppm_fp)
    wav = Image.open(wav_fp)

join('augustin.ppm', 'fms.wav', 'out.ppm')
