from micropsi import find_minimum

find_minimum([5, 4, 3, 2, 1]) == 1
find_minimum([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
find_minimum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
find_minimum([1]) == 1
find_minimum([2, 1]) == 1
find_minimum([5, 4, 3, 2, 1, 0, -1, -2]) == -2
find_minimum(['apple', 'banana', 'cherry', 'date', 'elderberry']) == 'apple'
find_minimum(['banana', 'apple', 'cherry', 'date', 'elderberry']) == 'banana'
find_minimum([3, 2, 1, 0, 1, 2, 3]) == 0
find_minimum(['c', 'b', 'a', 'b', 'c']) == 'a'