import argparse 

parser = argparse.ArgumentParser()

parser.add_argument('name', help='Your Name')
parser.add_argument('--shout', action='store_true')

args = parser.parse_args()


if args.shout:
    print(args.name.upper())
else:
    print(args.name)
    
    