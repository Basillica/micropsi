from micropsi import find_minimum

# Tests
def test_find_minimum():
    assert find_minimum([5, 4, 3, 2, 1]) == 1
    assert find_minimum([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert find_minimum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert find_minimum([1]) == 1
    assert find_minimum([2, 1]) == 1
    assert find_minimum([5, 4, 3, 2, 1, 0, -1, -2]) == -2
    assert find_minimum(['apple', 'banana', 'cherry', 'date', 'elderberry']) == 'apple'
    assert find_minimum(['banana', 'apple', 'cherry', 'date', 'elderberry']) == 'banana'
    assert find_minimum([3, 2, 1, 0, 1, 2, 3]) == 0
    assert find_minimum(['c', 'b', 'a', 'b', 'c']) == 'a'
    
    try:
        find_minimum([])
        assert False
    except ValueError:
        pass