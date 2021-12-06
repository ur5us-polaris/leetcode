from math import floor

FIRST_BAD = 1702766719


def isBadVersion(version: int) -> bool:
    if version >= FIRST_BAD:
        return True
    return False


def firstBadVersion(n: int) -> int:
    """
    :type n: int
    :rtype: int
    """
    left = 1
    right = n
    while (right - left) > 1:
        mid = floor((right + left) / 2)
        if isBadVersion(mid):
            right = mid
            continue
        left = mid + 1
    if not isBadVersion(left):
        return right
    return left


def main():
    n = 2126753390
    res = firstBadVersion(n)
    print(res)


if __name__ == '__main__':
    main()