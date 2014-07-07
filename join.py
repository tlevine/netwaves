#!/usr/bin/env python3
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
    original_image = Image.open(ppm)
    intermediate_ppm = BytesIO()
    wav = open(wav_fn, 'rb')

    original_image.resize(new_image_size(os.path.getsize(wav), i.size, SCALE))
    original_image.save(intermediate_ppm)

    intermediate_ppm.seek(0)
    while True:
        image_pixel = intermediate_ppm.read(1)
        if image_pixel == '':
            break
        for _ in range(SCALE):
            audio_pixel = wav.read(1)
            bytes([ord(image_pixel) + ord(audio_pixel)])

    magicnumber = ppm.readline()
    dimensions = ppm.readline()
    maxcolor = ppm.readline()
    out.write(magicnumber)
    out.write(dimensions)
    out.write(maxcolor)
    columns, rows = map(int,dimensions.decode('ascii').split(' '))
    print(columns, rows)

# join(open('augustin.ppm', 'rb'), open('fms.wav', 'rb'), open('out.ppm', 'wb'))
