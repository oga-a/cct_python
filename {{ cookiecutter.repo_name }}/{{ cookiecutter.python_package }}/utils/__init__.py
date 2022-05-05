def add_one(x: int) -> int:
    """1足した値を返す関数

    Args:
        x: 足したい数値

    Returns:
        int: 足された数値
    """
    return x + 1


def add_two(x: int) -> int:
    """2足した値を返す関数

    Args:
        x: 足したい数値

    Returns:
        int: 足された数値
    """
    x = add_one(x)
    x = add_one(x)
    return x
