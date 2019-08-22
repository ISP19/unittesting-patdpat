def unique(list):
    """Return a list containing only the first occurence of each distint
       element in list.  That is, all duplicates are omitted.

    Arguments:
        list: a list of elements (not modified)
    Returns:
        a new list containing only distinct elements from list

    Examples:
    >>> unique([5,5]) #test int
    [5]
    >>> unique(["b","a","a","b","b","b","a","a"]) #test string
    ['b', 'a']
    >>> unique([True, False,True]) #test booline
    [True, False]
    >>> unique([0.53,0.53]) #test float
    [0.53]
    >>> unique([[5],[5]]) #test list and check whether it's do  do a recursive scan or not
    [[5]]
    >>> unique([]) #test empty list
    []
    >>> unique(["b","a","a",0.53,0.53,5,5,True,True,[5]]) #test alltype at once
    ['b', 'a', 0.53, 5, True, [5]]
    >>> unique([777]) #test single element
    [777]
    >>> unique(4) #test input that is not a list
    Traceback (most recent call last):
     ...
    TypeError: Input must be list


    """
    if type(list) != type([]):
        raise TypeError("Input must be list")

    result = []
    for i in list:
        if i not in result:
            result.append(i)
    return result


if __name__ == "__main__":
    """Run the doctests in all methods."""
    import doctest
    doctest.testmod(verbose=True)
