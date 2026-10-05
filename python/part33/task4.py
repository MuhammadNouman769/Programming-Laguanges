def retry(times):

    def decorator(func):

        def wrapper(*args, **kwargs):

            for attempt in range(1, times + 1):

                try:
                    return func(*args, **kwargs)

                except Exception:
                    print(f"Attempt {attempt} failed. Retrying...")

        return wrapper

    return decorator


@retry(3)
def test():

    print("Running...")

    raise ValueError("something went wrong")


test()