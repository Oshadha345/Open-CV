
import sys
import re

'''
 This script filters lines from standard input based on a regex pattern provided as a command-line argument.
 it writes the matching lines to standard output and prints a summary of the number of lines scanned and matched to standard error.
'''

def main():
    
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        sys.exit("Usage: filter-lines.py <pattern>")
    
    # Compile the regex pattern from the command-line argument
    ''' re.compile is use to compile this in our case pattern we looking is "ap" into a object, 
        so later we can call methods like .search(), .match(), or .findall() on it.
    '''
    pattern = re.compile(sys.argv[1], re.IGNORECASE)
    
    total = matches = 0

    # read lines from standard input until EOF
    for line in sys.stdin:
        total += 1
        
        # Check if the line matches the regex pattern
        # calling search on pattern object
        if pattern.search(line):
            sys.stdout.write(line)
            matches += 1

    sys.stderr.write(f"Scanned {total} lines, {matches} matched.\n")

if __name__ == "__main__":
    main()
