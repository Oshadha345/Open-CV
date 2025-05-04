import os

print("👣 Current directory:", os.getcwd())

print("\n📂 All files & folders here:")



for item in os.listdir():
    
    # get the full path of the item( direcrtory path(os.getcwd()) + file name(item))
    path = os.path.join(os.getcwd(),item)
    
    #check if the item is  file
    if os.path.isfile(path):
        print(f"  📄 {item}")
        
    #check if the item is a directory
    elif os.path.isdir(path):
        print(f"  📁 {item}")
        
    # check if the item is a symbolic link
    else:
        print(f"  ❓ {item}")


# check if a specific file exists
# os.path.exists() returns True if the file exists, otherwise False
print("\n 🔍 Does 'README.md' exist?", os.path.exists('README.md'))

