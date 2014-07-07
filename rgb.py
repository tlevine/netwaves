#!/usr/bin/env python3
import itertools

def tone(rgb, columns, rows, basename):
    header_str = '''P6
%d %d
255
''' % (columns, rows)
    header = header_str.encode('ascii')
    body = bytes(rgb * rows * columns)
    with open('%s.wav' % basename, 'wb') as fp:
        fp.write(body)
    with open('%s.ppm' % basename, 'wb') as fp:
        fp.write(header)
        fp.write(body)

tone([0,127,255], 800, 600, 'z')
