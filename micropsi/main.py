from typing import List, TypeVar
from micropsi.util import Logger

T = TypeVar('T')
logger = Logger.get_logger()

def find_minimum(arr: List[T]) -> T:
    """
    Given an array of elements that provide a less than operator, find the minimum using as few comparisons as possible.
    The array shall be given such that the first elements are strictly monotonically decreasing,
    the remaining elements are strictly monotonically increasing.
    The less than operator be defined as the operator that works on such vectors where a < b if min(a,b) == a.

    Args:
        arr: List of elements with the less than operator defined.

    Returns:
        The minimum element in the list.
    """
    if len(arr) == 0:
        logger.info("Empty list provided")
        raise ValueError('Empty list provided')

    if len(arr) == 1:
        return arr[0]

    if arr[0] < arr[-1]:
        return arr[0]

    low, high = 0, len(arr) - 1

    while high > low:
        mid = (low + high) // 2
        if arr[mid] < arr[high]:
            high = mid
        else:
            low = mid + 1
    return arr[high]

