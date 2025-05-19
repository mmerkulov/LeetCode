def sum_numbers(text: str) -> int:
    return sum(int(el) for el in text.split() if el.isnumeric())

def count_digits(text: str) -> int:
    return len([el for el in text if ord(el) in range(48, 58)])

x = "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
sum_numbers(text=x)
x = 'who is 1st here'
print(count_digits(x))