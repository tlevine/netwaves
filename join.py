#!/usr/bin/env python3
from PIL import Image

def parser():
    p = argparse.ArgumentParser('Record sound as PPM.')
    p.add_argument('ppm', metavar = '[ppm file]', type = argparse.FileType('rb'))
    p.add_argument('wav', metavar = '[wav file]', type = argparse.FileType('rb'))
    return p

def main():
    p = parser().parse_args()

def join(ppm, wav, out):
    i = Image.open(ppm)
    i.size

    magicnumber = ppm.readline()
    dimensions = ppm.readline()
    maxcolor = ppm.readline()
    out.write(magicnumber)
    out.write(dimensions)
    out.write(maxcolor)
    columns, rows = map(int,dimensions.decode('ascii').split(' '))
    print(columns, rows)

join(open('augustin.ppm', 'rb'), open('fms.wav', 'rb'), open('out.ppm', 'wb'))
