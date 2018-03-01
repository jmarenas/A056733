#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''Generates the sequence of numbers that are the sum of the cubes of its 3 sections.

This program must be used from the command line
passing at least 1 argument:
1: number of digits of the sections.
2: (optional) The number of subprocess to run. Default 8.
   this argument should match the number of cpu of the executing computer
   for maximium performance.

example:
  > python a056733.py 3 8
  output:
  1 166500333
  2 296584415
  3 333667000
  4 333667001
  5 334000667
  6 710656413
  7 828538472
  
  The example above generates the numbers that are
  the sum of the cubes of its 3 sections of 3 digits
  using 8 subprocess.
  Executing with parameter 4 generates the next
  elements of the sequence.
'''
import math
from multiprocessing import Pool

__author__ = "José M. Arenas"
__copyright__ = "Copyright (c) 2017 José M. Arenas"


class SumSecCube:
    def __init__(self, secd: int):
        self.end = 10**secd
        self.cubes = [i * i * i for i in range(self.end)]

    def run(self, i):
        nssc = []
        iend2 = i * self.end * self.end
        for j in range(self.end):
            jend = j * self.end
            a = (jend + iend2) - self.cubes[i] - self.cubes[j]
            if a < 0:
                break
            else:
                a = math.ceil(a**(1 / 3))
            for k in range(a, self.end):
                b = self.cubes[i] + self.cubes[j] + self.cubes[k]
                c = (k + jend + iend2)
                if b > c:
                    break
                if c == b:
                    nssc.append(b)
        return nssc


def f(a):
    if a != []:
        return True
    return False


if __name__ == '__main__':
    import sys
    try:
        secd = int(sys.argv[1])
        if len(sys.argv) > 2:
            proc = int(sys.argv[2])
        else:
            proc = 8
    except:
        print("Input must be a positive number.")
        exit()
    if secd < 0:
        print("Input must be a positive number.")
        exit()
    end = 10**secd
    a = SumSecCube(secd)
    with Pool(processes=proc) as pool:
        p = filter(f, pool.map(a.run, range(end // 10, end)))
    d = 1
    for i in p:
        for j in i:
            print(d, j)
            d += 1
