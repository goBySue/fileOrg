import os 
import shutil

# Define the source directory and destination directory
source_dir = '/Users/jisuk/Desktop'
destination_dir = '/Users/jisuk/Desktop/applications'

# Create destination directory if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Iterate over each file in the source directory
for filename in os.listdir(source_dir):
    # Check if 'JK' is in the filename
    if 'JK' in filename or 'JisuKim' in filename or 'Jisu Kim' in filename:
        # Construct full file path
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)
        
        # Move the file
        shutil.move(source_file, destination_file)
        print(f"Moved: {filename}")

print("File organizing completed.")
