import re
import os
import sys

def Main(file_path):
    files = os.listdir(file_path[1][:-12])

    for f in files:
        if f[(len(f)-3):] == 'mf4':
            print(f)
    
if __name__ == "__main__":
    Main(sys.argv)