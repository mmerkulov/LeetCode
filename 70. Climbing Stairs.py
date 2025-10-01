"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

def clib_stairs(n: int) -> int:
    a, b = 1, 2

    if n == 1:
        return a
    if n == 2:
        return b

    for i in range(1, n):
        print(b, a + b)
        a, b = b, a + b

    return a


print(clib_stairs(n=6))
"""
n = 4
1. 1 + 1 + 1 + 1
2. 1 + 2 + 1
3. 2 + 1 + 1
4. 1 + 1 + 2
5. 2 + 2

n = 5
1. 1 1 1 1 1
2. 2 1 1 1
3. 1 2 1 1
4. 1 1 2 1
5. 1 1 1 2
6. 2 2 1
7. 1 2 2

n = 6
1.  1 1 1 1 1 1
2.  2 1 1 1 1
3.  1 2 1 1 1
4.  1 1 2 1 1
5.  1 1 1 2 1
6.  1 1 1 1 2
7.  2 2 1 1
8.  2 1 2 1
9.  2 1 1 2
10. 1 2 2 1
11. 1 1 2 2
12. 2 2 2
"""