"""环线检测模块。

识别公交站点序列中的重复循环模式，用于区分环形线路和普通线路。

典型用法::

    from BusNetPynew.find_cycle import find_cycle

    stops = ["A", "B", "C", "D", "A", "B", "C", "D"]
    cycle = find_cycle(stops)  # ["A", "B", "C", "D"]
"""

from typing import List, TypeVar

T = TypeVar('T')


def find_cycle(sequence: List[T]) -> List[T]:
    """检测序列中的最短重复循环模式。

    从序列开头开始，尝试找到一个最短子序列，使得整个序列是该子序列的重复。
    如果找不到重复模式，返回原始序列。

    Args:
        sequence: 待检测的元素序列（如站点名称列表）。

    Returns:
        最短循环子序列。若序列无重复模式，返回原序列。

    Examples:
        >>> find_cycle(["A", "B", "C", "A", "B", "C"])
        ['A', 'B', 'C']
        >>> find_cycle(["A", "B", "C", "D"])
        ['A', 'B', 'C', 'D']
        >>> find_cycle([1, 2, 1, 2, 1, 2])
        [1, 2]
    """
    n = len(sequence)
    for cycle_length in range(1, n // 2 + 1):
        cycle = sequence[:cycle_length]
        repeated = True
        for i in range(cycle_length, n, cycle_length):
            if sequence[i:i + cycle_length] != cycle:
                repeated = False
                break
        if repeated:
            return cycle
    return sequence
