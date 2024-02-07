import parse
import string

def line_dict(line, pattern):                                                     
    """
    When given a line and pattern returns a dictonary of keys and values

    example repeated line:  
    "1 Card 1: 41 48 83 86 17 | 81 87  9 41 27  4 48 52\n"
    
    example corresponding pattern 
    "Card {card:d}: {winners} | {hand}\n"

    example returned dict 
    {'card': 1, 'winners': '41 48 83 86 17', 'hand': '81 87  9 41 27  4 48 52'}

    lines for top of file:
import os
import sys
### Get the parent directory by going one level up
current_dir = os.path.dirname(os.path.abspath(__file__))
### Add the parent directory to sys.path
parent_dir = os.path.dirname(current_dir)
uber_parent_dir = os.path.dirname(parent_dir)
sys.path.append(uber_parent_dir)
import aoc_toolkit.equations as aoc
    """
    pattern = parse.compile(pattern)
    match = pattern.search(line)                                               
    return match.named            


def int_array(line_dict, key, delim = " "):
    """
    Takes an extracted line dictionary, and for a given key in that dictionary
    returns a delimited (automatically space delimited string as an array of 
    ints

    example string 81 87  9 41 27  4 48 52
    returns [81, 87, 9, 41, 27, 4, 48, 52]

    naturally this would also work for any string input but you'd have to 
    put it in a dict first or edit this function. Sorry.
    """
    return [int(x) \
            for x in line_dict[key].split(delim) \
            if len(x) > 0]



def lowercase():
    """
    Don't judge, I just forget the commands all the time
    """
    return string.ascii_lowercase

def dict_inverter(input_dict):
    """
    I've only just met her
    {a:0, b:1} becomes {0:a, 1:b}
    """
    return {value:key for key, value in input_dict.items()}
