# printtopics.py: Prints the words that are most prominent in a set of
# topics.
#
# Copyright (C) 2010  Matthew D. Hoffman
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os
import re
import random
import math
# import urllib2
from urllib.request import urlopen, Request
import time
import _pickle as pickle
import numpy

import onlineldavb

def main():
    """
    Displays topics fit by onlineldavb.py. The first column gives the
    (expected) most prominent words in the topics, the second column
    gives their (expected) relative prominence.
    """

    with open(sys.argv[1]) as f:
        vocab = f.read().split()

    testlambda = numpy.loadtxt(sys.argv[2])

    for k in range(0, len(testlambda)):
        lambdak = list(testlambda[k, :])
        lambdak = lambdak / sum(lambdak)
        temp = zip(lambdak, range(0, len(lambdak)))
        temp = sorted(temp, key = lambda x: x[0], reverse=True)

        print(f'topic {k}')

        # feel free to change the "53" here to whatever fits your screen nicely.
        for i in range(0, 53):
            print(f'{vocab[temp[i][1]]}\t---\t{temp[i][0]}')
        print

if __name__ == '__main__':
    main()
