import os
import glob

files = glob.glob("imdb*")
for f in files:
    try:
        os.remove(f)
        print(f"Deleted: {f}")
    except Exception as e:
        print(f"Error deleting {f}: {e}")
