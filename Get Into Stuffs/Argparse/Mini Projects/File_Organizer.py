import argparse 
import os
import shutil
from pathlib import Path
from datetime import datetime

# setup argument parser

parser = argparse.ArgumentParser(description ='Organize files in a folder by file type.')

# add arguments

parser.add_argument('folder',help='Path to the folder to organise')
parser.add_argument('--dry_run', action= 'store_true',help= "only show what will be moved, don't actually move files ")
parser.add_argument('--recursive',action='store_true',help='Recursively organise files in subdirectories')
parser.add_argument('--extensions', nargs='+', help="Only include files with these extensions (e.g. .jpg .pdf)")
parser.add_argument('--logfile', help='Log file to write actions to (e.g. organize.log)')

# parse the arguments

args = parser.parse_args()

# supported file types

FILE_CATEGORIES = {
    'Images' : ['.jpg' , '.jpeg', '.png', '.gif', '.webp'],
    'Documents' : ['.pdf', '.docx', '.txt', '.pptx', '.xlsx'],
    'Audio' : ['.mp3', '.wav', '.aac'],
    'Videos' : ['.mp4', '.mkv', '.mov'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Code' : ['.py', '.js', '.html', '.css', '.c', '.cpp', 'java'],
    'Other' : []
}


# ensures valid folder

folder_path = Path(args.folder)

if not folder_path.exists() or not folder_path.is_dir():
    print(f'[ERROR] The folder {args.folder} does not exist or is not a directory.')
    exit(1)



# logging function

def log(message):
    print(message)
    if args.logfile:
        
        # check if the log file exists, if not create it and write the header
        with open(args.logfile, 'a', encoding='utf-8') as f:
            f.write(f'{datetime.now()} | {message}\n')


#scan files

file_paths = folder_path.rglob('*') if args.recursive else folder_path.iterdir()

# organise logic

moved_count = 0
skipped_count = 0
preview_count = 0


#selecting a file in the folder
for file in file_paths:
    
    #checking that if its a file or not
    if file.is_file():
        #skipping the file if it is not in the specified extensions
        if args.extensions and file.suffix.lower() not in [ext.lower() for ext in args.extensions]:
            skipped_count += 1
            log(f'Skipped {file.name} (not in specified extensions)')
            continue
        
        moved = False
        
        
        for category, extensions in FILE_CATEGORIES.items():
            
            #checking whether that file extension in the extensions list or not
            if file.suffix.lower() in extensions:
                
                # create the target directory path
                target_dir = folder_path / category
                
                # create the target directory if it doesn't exist
                target_dir.mkdir(exist_ok=True)
                
                # if dry run is true, show the move action
                if args.dry_run:
                    log(f'[DRY RUN] Would move {file.name} -> {target_dir}')
                    preview_count += 1
                
                # else move the file
                else:
                    shutil.move(str(file), str(target_dir / file.name))
                    log(f'Moved {file.name} -> {target_dir}')
                    moved_count += 1
                    
                moved = True
                break
        
        # if the file type is not in any category, move it to 'Others'
        if not moved:
            
            # create the 'Others' directory path
            other_dir = folder_path / 'Others'
            
            # create the 'Others' directory if it doesn't exist
            other_dir.mkdir(exist_ok=True)
            
            if args.dry_run:
                log(f'[DRY RUN] Would move {file.name} -> {other_dir}')
                preview_count += 1
            else:
                shutil.move(str(file), str(other_dir / file.name))
                log(f'Moved {file.name} -> {other_dir}')
                moved_count += 1
                


#summary report

log(f'\n----[SUMMARY]----')
log(f'Total files moved: {moved_count}')
log(f'Total files skipped: {skipped_count}')
log(f'Total files previewed: {preview_count}')




            


