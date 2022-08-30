def main(numbers,i):
    """
    You are given a list of numbers. i Delete and return the number in the index.
    Args:
        numbers(list): parameter
        i(int): parameter
    Returns:
        list: return answer
    """
    k = numbers[i]
    numbers.pop(i)
    return k

x = main([1, 2, 3, 4, 5], 2)
print(x)