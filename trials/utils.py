import numpy as np


def cached(*attributes):
    """
    The decorator caches method value as long as self's attribute remains unchanged

    :param attribute a numpy array attribute name
    """
    def _cached(method):
        cache = {}
        def wrapper(*args):
            self = args[0]
            key = id(self)
            cached_item = cache.get(key)
            new_attr_vals = [getattr(self, attr) for attr in attributes]
            if cached_item:
                cached_attr_vals, cached_result = cached_item
                if all(a == b for a, b in zip(cached_attr_vals, new_attr_vals)):
                    return cached_result
                else:
                    result = method(*args)
                    cache[key] = (new_attr_vals, result)
                    return result
            else:
                result = method(*args)
                cache[key] = (new_attr_vals, result)
                return result

        return wrapper
    return _cached