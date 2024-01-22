from functools import wraps

def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Code to execute BEFORE calling the decorated function.

        # 2. Call the decorated unction as required, returning it`s results if need.
        return func(*args, **kwargs)
    
        # 3. Code to execute INSTEAD of calling the decorated function.
    return wrapper