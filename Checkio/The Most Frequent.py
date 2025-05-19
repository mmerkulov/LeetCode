def most_frequent(data: list[str]) -> str:
    d = {}
    for i in data:
        if d.get(i):
            d[i] = d[i] + 1
        else:
            d[i] = 1
    max_value = 0
    for k, v in d.items():
        if max_value < v:
            max_value = v
    result = [k for k, v in d.items() if v == max_value]
    return result[0]


most_frequent(data=["a", "b", "c", "a", "b", "a"])
# assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
# assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
data=["a", "b", "c", "a", "b", "a"]

print(max(data, key = data.count))