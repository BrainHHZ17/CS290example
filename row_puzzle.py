# Author: Hanhui Zeng
# Date: May 5, 2020
# Description: This code will check if the number in the list is able to process the index to the end of list

def row_puzzle(puzzle, pos=0):
    """This function process the actual step to reach the end of list and return True, otherwise return False"""
    step = puzzle[pos]
    if step == -1:
        return False
    if step == 0:
        return True
    puzzle[pos] = -1
    moving_left = False
    moving_right = False
    # moving left or right
    if pos + step < len(puzzle):
        #print("right", pos, "\t", step)
        moving_right = row_puzzle(puzzle, pos + step)
    if pos - step >= 0:
        #print("left", pos, "\t", step)
        moving_left = row_puzzle(puzzle, pos - step)
    if moving_left == True or moving_right == True:
        return True
    return False


