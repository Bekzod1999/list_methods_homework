def main(fruits, x):
    """
    You will be given a list of fruits. Add x fruit to it from the end and return.
    Args:
        fruits(list): parameter 
        x(str): parameter
    Returns:
        list: return answer
    """
    b = fruits.extend(x)
    return b

y=main(['apple', 'banana'], 'kiwi')
print(y)


