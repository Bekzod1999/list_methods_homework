def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    i = 0
    list1 = []
    while i < len(fruits):
        if fruits[i] != 'apple':
            list1.append(fruits[i])
        i+=1
    return list1

x =main(['app', 's', 'apple', 'df'])
print(x)