#!/usr/bin/env python3
from PIL import Image

def parser():
    p = argparse.ArgumentParser('Record sound as PPM.')
    p.add_argument('ppm', metavar = '[ppm file]', type = argparse.FileType('rb'))
    p.add_argument('wav', metavar = '[wav file]', type = argparse.FileType('rb'))
    return p

def main():
    p = parser().parse_args()
    Image.open(p.ppm)

def join(ppm, wav, out):

def test():
    
