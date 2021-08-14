from ..utils import add as _add


def add_loop(start: int, times: int) -> int:
    for i in range(times):
        start = _add(start, 1)

    return start
