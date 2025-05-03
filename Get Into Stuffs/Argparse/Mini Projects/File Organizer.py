import argparse 
import os
import shutil
from pathlib import Path

# setup argument parser

parser = argparse.ArgumentParser(description ='Organize files in a folder by file type.')

# add arguments

parser.add_argument('folder',help='Path to the folder to organise')
parser.add_argument('--dry_run', action= 'store_true',help= "only show what will be moved, don't actually move files ")


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


# organise logic


#selecting a file in the folder
for file in folder_path.iterdir():
    
    #checking that if its a file or not
    if file.is_file():
        
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
                    print(f'[DRY RUN] Would move {file.name} -> {target_dir}')
                
                # else move the file
                else:
                    shutil.move(str(file), str(target_dir / file.name))
                    print(f'Moved {file.name} -> {target_dir}')
                moved = True
                break
        
        # if the file type is not in any category, move it to 'Others'
        if not moved:
            
            # create the 'Others' directory path
            other_dir = folder_path / 'Others'
            
            # create the 'Others' directory if it doesn't exist
            other_dir.mkdir(exist_ok=True)
            
            if args.dry_run:
                print(f'[DRY RUN] Would move {file.name} -> {other_dir}')
            else:
                shutil.move(str(file), str(other_dir / file.name))
                print(f'Moved {file.name} -> {other_dir}')



            


