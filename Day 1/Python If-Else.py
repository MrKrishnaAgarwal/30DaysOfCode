#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    status = "Not Weird"
    if n % 2 != 0 or (n % 2 == 0 and 5<n<21):
        status = "Weird"
    
    print(status)
