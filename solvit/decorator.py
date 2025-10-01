def retry_on_exception(retries: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            amount = retries
            while amount > 0:
                try:
                    print('ok')
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    amount = amount - 1
                    print(e.__class__.__name__)
                    if amount == 0:
                        print(f'final {e.__class__.__name__}')
                        raise
        return wrapper
    return decorator


# @retry_on_exception(retries=3)
# def m1():
#     return print('Hallo')

# @retry_on_exception(retries=3)
# def m2():
#     raise ValueError


# m2()

error_counter_success = 0

@retry_on_exception(retries=3)
def test_success_after_one_fail():
    global error_counter_success
    if error_counter_success < 2:
        error_counter_success += 1
        raise ValueError
    return "Success after fail!"


test_success_after_one_fail()