import numpy as np

def position_range_helper(input):
    """Args:
        position: The position of each keyword
    Returns:
        The position_range function returns a string that is either "1 to 10", "11 to 20", "21 to 30", or "31+" depending on the value of the position argument.
    """
    if input < 11:
        return "1 to 10"
    # elif input['inputs'] >= 11 and input <= 20:
    elif np.logical_and(input >= 11, input <= 20):
        return "11 to 20"
    elif  np.logical_and(input >= 21, input <= 30): 
        return "21 to 30"
    else:
        return "31+"
    
def top20_helper(input):
    if input < 21:
        return "TRUE"
    else:
        return "FALSE"


def traffic_exists_helper(input):
    if input > 0:
        return "TRUE"
    else:
        return "FALSE"