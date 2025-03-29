from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def longtime_function(*args: Any, **kwargs: Any) -> Any:
        immutable_types = (int, float, str, bool, tuple)

        for arg in args:
            if isinstance(arg, immutable_types):
                continue
            else:
                print("This is mutable!")
                break

        if args not in cache_dict.keys():
            print("Calculating new result")
            result_function = func(*args, **kwargs)
            cache_dict[args] = result_function
            return result_function
        else:
            print("Getting from cache")
            return cache_dict[args]
    return longtime_function
