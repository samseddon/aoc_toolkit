import parse

def line_dict(line, pattern):                                                     
    """
    When given a line and pattern returns a dictonary of keys and values

    example repeated line:  
    "1 Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\n"
    
    example corresponding pattern 
    "Card {card:d}: {winners} | {hand}\n"

    example returned dict 
    {'card': 1, 'winners': '41 48 83 86 17', 'hand': '81 87  9 41 27  4 48 52'}
    """
    pattern = parse.compile(pattern)
    match = pattern.search(line)                                               
    return match.named            


def int_array(line_dict, key, delim = " "):
    """
    Takes an extracted line dictionary, and for a given key in that dictionary
    returns a delimited (automatically space delimited string as an array of 
    ints

    example string 83 86  6 31 17  9 48 53
    returns [83, 86, 6, 31, 17, 9, 48, 53]

    naturally this would also work for any string input but you'd have to 
    put it in a dict first or edit this function. Sorry.
    """
    return [int(x) \
            for x in line_dict[key].split(delim) \
            if len(x) > 0]