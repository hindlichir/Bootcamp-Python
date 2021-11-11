def ft_filter(function_to_apply, iterable):
    try:
        iter(iterable)
    except TypeError:
        print(f"TypeError: {type(iterable)} object is not iterable")
        return None
    else:
        for elem in iterable:
            if function_to_apply(elem):
                yield elem
