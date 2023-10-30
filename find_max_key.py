def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    max1=-521032103210201
    for i in data:
        if type(i)==int or type(i)==float:
            if max1<i:
                max1=i
    return max1
data = {
    1: 'a', 
    2: 'b', 
    3: 'c'
  }
print(find_max_key(data))