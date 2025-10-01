def retry_on_exception(retries: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = retries

            while attempts > 0:
                try:
                    result = func(*args, **kwargs)
                    print("ok")
                    return result
                except Exception as e:
                    attempts -= 1
                    print(e.__class__.__name__)

                    if attempts == 0:
                        print(f"final {e.__class__.__name__}")
        return wrapper

    return decorator