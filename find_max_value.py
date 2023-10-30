def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    max1=-65210321032
    for i in data:
        if type(data.get(i))==int or type(data.get(i))==float:
            if data.get(i)>max1:
                max1=data.get(i)
    return max1
data = {
    'a' : -10, 
    'b' : -2, 
    'c' : 0
  }
print(find_max_value(data))