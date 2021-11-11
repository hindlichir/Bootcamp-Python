def ft_reduce(function_to_apply, iterable):
    try:
        iter(iterable)
    except TypeError:
        print(f"TypeError: {type(iterable)} object is not iterable")
        return None
    else:
        value = iterable[0]
        for elem in iterable[1:]:
            value = function_to_apply(value, elem)
        return value
