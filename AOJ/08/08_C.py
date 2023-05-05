import sys

str = sys.stdin.read().lower()
for chr in "abcdefghijklmnopqrstuvwxyz":
    char_c = str.count(chr)
    print(f'{chr} : {char_c}')