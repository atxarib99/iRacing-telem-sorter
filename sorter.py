import os
import re
import shutil

def organize_files():
    current_dir = os.getcwd()
    file_pattern = re.compile(r"^(.+?)_(.+?) \d{4}-\d{2}-\d{2}.*")
    
    for filename in os.listdir(current_dir):
        if os.path.isfile(filename):
            match = file_pattern.match(filename)
            if match:
                car_name = match.group(1)
                track_name = match.group(2)
                
                car_dir = os.path.join(current_dir, car_name)
                track_dir = os.path.join(car_dir, track_name)
                
                os.makedirs(track_dir, exist_ok=True)
                
                shutil.move(filename, os.path.join(track_dir, filename))
                print(f"Moved: {filename} -> {track_dir}")

if __name__ == "__main__":
    organize_files()

