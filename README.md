### This toolkit is designed by Sam Seddon and Alina Bendt, and designed to aide
### common advent of code requirements. 

# Install
### Assuming you have some directory structure like so 
___
AOC_2023/day_n/day_n.py

### then git clone this repo when in directory AOC_2023 and add the following lines
### to the top of your day_n.py code

___

import os                                                                         
import sys
### Get the parent directory by going one level up
current_dir = os.path.dirname(os.path.abspath(__file__))
### Add the parent directory to sys.path
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)                                                    
import aoc_toolkit.equations as aoc            

____



