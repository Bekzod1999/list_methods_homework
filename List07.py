def main(list01):
    """
    A list of zeros and ones is given. Find how many zeros are involved and return.
    Args:
        list01(list): parameter
    Returns:
        int: return answer
    """
    k = list01.count(0)
    return k

x = main([0,1,0,0])
print(x)