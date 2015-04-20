#!/usr/bin/python3
import sys
import argparse
import os

def readInt(f):
    '''Reads a little endian int from a file.'''
    n = 0
    for i in range(4):
        n += f.read(1)[0] << 8*i
    return n

def readStruct(f):
    '''Reads a struct from a file.'''
    o = {}
    o['length'] = readInt(f)
    o['offset'] = readInt(f)
    o['unk1'] = readInt(f)
    o['unk2'] = readInt(f)
    return o

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extracts a .ovk file.')
    parser.add_argument('-f', '--file', help='file to extract')
    parser.add_argument('-o', '--outDir', default='.', help='where to extract')
    args = vars(parser.parse_args())

    with open(args['file'], 'rb') as f:
        numFiles = readInt(f)

        structs = []
        for i in range(numFiles):
            structs.append(readStruct(f))

        for n, i in enumerate(structs):
            with open(args['outDir'] + os.sep + str(n), 'wb') as o:
                f.seek(i['offset'])
                o.write(f.read(i['length']))
