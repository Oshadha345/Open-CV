import sys

lines = []
print('Type text. Enter a blank line to finish:')

# Read lines until a blank line is entered
for line in sys.stdin:
    
    # Check for a blank line
    if line.strip() == '':
        break
    
    # Append the line to the list, removing the newline character
    lines.append(line.rstrip("\n"))
    

print("You entered:")
print("\n".join(lines))

