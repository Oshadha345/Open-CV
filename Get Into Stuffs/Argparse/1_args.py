import argparse

# step 1: create the parser

parser = argparse.ArgumentParser(description='Say hello to someone.')

#step 2: add arguments

parser.add_argument('name', help="The person's name")

#step 3: parse the arguments

args = parser.parse_args()

#step 4: use the arguments

print(f'Hello, {args.name}!!!')
                    
                    
                    
                    