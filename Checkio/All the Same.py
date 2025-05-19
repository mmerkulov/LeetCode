from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    return True if len(elements) == 0 or len(set(elements)) == 1 else False

x = []
print(all_the_same(x))

