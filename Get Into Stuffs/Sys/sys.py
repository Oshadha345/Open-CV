import sys

# This script demonstrates how to use the sys module to access command-line arguments.

# sys.argv list contains the command-line arguments passed to the script.
print(sys.argv)


# sys.exit() is used to exit the script. It can take an optional exit status code.
if len(sys.argv) < 3:
    sys.exit("❌ Usage: python myscript.py <arg>")
    
#default exit status code is 0, which indicates success.
else:
    
    data = sys.stdin.read()
    print("You entered:", data)

    first = sys.stdin.readline()
    print(first)
    
    for line in sys.stdin:
        print(line.strip())
    sys.exit(0)  # Exit with success status code
    