# Clear the clutter
import os
path="/home/mohit/Pictures"

files = [f for f in os.listdir(path) if f.endswith(".png") or f.endswith(".jpg")or f.endswith(".jpeg")or f.endswith(".webp") or f.endswith(".avif")]
i=1

for file in files:
    old_path=os.path.join(path,file)
    extension = os.path.splitext(file)[1]
    new_path=os.path.join(path,f"pic{i}{extension}")
    os.rename(old_path,new_path)
    print(f"Renamed {file} to pic{i}{extension}")

    while os.path.exists(new_path):
        i += 1
        new_filename = f"pic{i}{extension}"
        new_path = os.path.join(path, new_filename)




