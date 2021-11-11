def ft_map(function_to_apply, iterable):
    try:
        iter(iterable)
    except TypeError:
        print(f"TypeError: {type(iterable)} object is not iterable")
        return None
    try:
        for elem in iterable:
            function_to_apply(elem)
    except Exception:
        print("The function cannot be applied to the iterable")
        return None
    else:
        for elem in iterable:
            yield function_to_apply(elem)
