from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def longtime_function(*args: Any) -> Any:

        for arg in args:
            if isinstance(arg, (int, float, str, bool, tuple)):
                continue
            else:
                print("This is mutable!")
                break

        if args not in cache_dict.keys():
            print("Calculating new result")
            result_function = func(*args)
            cache_dict[*args] = result_function
            return result_function
        else:
            print("Getting from cache")
            return cache_dict[args]
    return longtime_function
