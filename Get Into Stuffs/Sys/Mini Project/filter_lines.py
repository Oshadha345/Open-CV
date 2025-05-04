#!/usr/bin/env python3
import sys
import re

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: filter-lines.py <pattern>")
    pattern = re.compile(sys.argv[1])
    total = matches = 0

    for line in sys.stdin:
        total += 1
        if pattern.search(line):
            sys.stdout.write(line)
            matches += 1

    sys.stderr.write(f"Scanned {total} lines, {matches} matched.\n")

if __name__ == "__main__":
    main()
