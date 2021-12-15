import sys
import os
from math import sqrt

print('The command line arguments are:')
for i in sys.argv[3:5]:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')
print(os.getcwd())
print("\nSquare root of 16 is", sqrt(16))