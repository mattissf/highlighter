"""
    A utility for highlighting text in a stream
    
    Author:
        Mattis Stordalen Flister
"""

import sys
import argparse
import fileinput

parser = argparse.ArgumentParser(description='Highlight words')
parser.add_argument('words_to_look_for', nargs='+', metavar="WORD", help="Word to look for")
args = parser.parse_args()

RED = '\033[91m'
END_CHARACTER = '\033[0m'

COLOR=RED

import signal
signal.signal(
    signal.SIGINT, 
    lambda *args: sys.exit(1)
)

while True:
    line = sys.stdin.readline()
    if line == '':
        break
    try:
        for word_to_look_for in args.words_to_look_for:
            line = line.replace(
                word_to_look_for, COLOR + word_to_look_for + END_CHARACTER
            )
        sys.stdout.write(line)
    except:
        pass
