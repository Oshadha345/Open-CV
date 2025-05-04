import argparse
import os

# initialize the argument parser
parser = argparse.ArgumentParser(description='Clean up unwanted files in a folder.')

# add arguments
parser.add_argument('folder', help='Path to thr folder to clean')
parser.add_argument('--extensions', nargs='+', required=True, help='List of file extensions to delete (e.g. .tmp .log)')
parser.add_argument('--dry_run', action='store_true', help ='Only preview deletions')


# parse the arguments

args = parser.parse_args()

print('\nFolder to clean:', args.folder)  
print('Extensions to delete:', args.extensions)
print('Dry run mode:', args.dry_run)
print('----------------------------------')

