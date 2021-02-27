"""
Given a string, return how many times the word 'BALLOON' can be made
BALLXOON -> 1
BALLOONBALLOONKJH -> 2
KJHKJ -> 0
"""

def find_balloons(S):
    ballon_dict = {
            'B': 0,
            'A': 0,
            'L': 0,
            'O': 0,
            'N': 0
        }
        
    for letter in S:
        if letter in ballon_dict:
            ballon_dict[letter] += 1
            
    ballon_dict['L'] =  int(ballon_dict['L'] / 2)
    ballon_dict['O'] =  int(ballon_dict['O'] / 2)
    
    return min(ballon_dict.values()) 