import argparse
import os

# initialize the argument parser
parser = argparse.ArgumentParser(description='Clean up unwanted files in a folder.')

# add arguments
parser.add_argument('folder', help='Path to the folder to clean')
parser.add_argument('--extensions', nargs='+', required=True, help='List of file extensions to delete (e.g. .tmp .log)')
parser.add_argument('--dry_run', action='store_true', help ='Only preview deletions')
parser.add_argument('--recursive', action='store_true', help='Recursively clean subdirectories')
parser.add_argument('--remove_empty', action='store_true', help='Remove empty directories after cleaning')
  
# parse the arguments

args = parser.parse_args()

print('\nFolder to clean:', args.folder)  
print('Extensions to delete:', args.extensions)
print('Dry run mode:', args.dry_run)
print('----------------------------------')




# delete files with specified extensions

# convert to lowercase set for case-insensitive comparison
ext = {e.lower() for e in args.extensions} 
 
for dirpath, _, filenames in os.walk(args.folder):
    
    # check if we should clean this directory
    for fname in filenames:
        
        # check if the file extension is in the list of extensions to delete
        if os.path.splitext(fname)[1].lower() in ext:
            file_path = os.path.join(dirpath, fname)
            
            # check if we should delete this file
            if args.dry_run:
                print(f'Dry run: would delete file: {file_path}')
            
            #delete the file if not in dry run mode
            else:
                os.remove(file_path)
                print(f'Deleted file: {file_path}')


# remove empty directories

for dirpath, dirnames, filenames in os.walk(args.folder, topdown=False):
    
    # check if the directory is empty
    if not dirnames and not filenames:
        if args.dry_run:
            print(f'Dry run: would remove empty directory: {dirpath}')
        else:
            os.rmdir(dirpath)
            print(f'Removed empty directory: {dirpath}')


