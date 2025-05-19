def end_zero(value: int) -> int:
    amount = 0
    for el in str(value)[::-1]:
        if int(el) != 0:
            break
        else:
            amount +=1
    return amount



x = 100100
print(end_zero(x))