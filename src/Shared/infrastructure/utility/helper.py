import time

def timer(func):
    """Measures execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} executed in {time.time() - start_time:.2f}s")
        return result
    return wrapper
