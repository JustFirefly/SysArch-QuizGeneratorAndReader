import os
week = 3
path = f"..//PDFs_HERE//Week {week}"
n_path = f"..//Database//Week{week}"
os.chdir(n_path)
import filecmp
directory = os.listdir()
for file in directory:
    for file2 in directory:
        try:
            if filecmp.cmp(file,file2) and file != file2:
                os.remove(file)
        except:
            continue