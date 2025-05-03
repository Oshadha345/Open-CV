'''
This code is a simple command-line calculator 
that takes two numbers and an operation (add, subtract, multiply, divide) 
as input arguments. It performs the specified operation and prints the result. 
The code uses the argparse library to handle 
command-line arguments and provides help messages for each argument.
'''

import argparse

# step 1: Create the parser
parser = argparse.ArgumentParser(description='A simple calculator CLI.')

# step 2; add arguments
parser.add_argument('x', type=int, help='The first number')
parser.add_argument('y', type=int, help='The second number')

# adding an optional argument for the operation
parser.add_argument('--operation','-o', choices= ['add', 'subtract', 'multiply' , 'divide'],required= True, help = 'The operation to perform')


# step 3: parse the arguments
args = parser.parse_args()


# step 4: use the arguments to calculate the result
result = None
if args.operation == 'add':
    result = args.x + args.y
    
elif args.operation == 'subtract':
    result = args.x - args.y

elif args.operation == 'multiply':
    result = args.x * args.y

elif args.operation == 'divide':
    if args.y == 0:
        result = 'Error: Division by zero is not allowed.'
    else:
        result = args.x / args.y
        
print(f'The result of {args.x} {args.operation} {args.y} is: {result}')
                                            