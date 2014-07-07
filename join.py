#!/usr/bin/env python3
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
    scale = (wav_length / (columns * rows) / scale) ** 0.5
    return round(columns * scale), round(rows * scale)

def join(ppm, wav, out):
    i = Image.open(ppm)
    i.size
    new_image_size(os.path.getsize(wav), i.size)

    magicnumber = ppm.readline()
    dimensions = ppm.readline()
    maxcolor = ppm.readline()
    out.write(magicnumber)
    out.write(dimensions)
    out.write(maxcolor)
    columns, rows = map(int,dimensions.decode('ascii').split(' '))
    print(columns, rows)

# join(open('augustin.ppm', 'rb'), open('fms.wav', 'rb'), open('out.ppm', 'wb'))
