import sys

#using print() (writes to stdout by default)

print('Hello, world!')

#direct write
sys.stdout.write("Im writing using sys.stdout.write()")

#controlling buffering
sys.stdout.flush()

