import string
import math


def solution(n, k):
    number = str(convert_recur(n, k))
    cnt = 0

    for token in number.split('0'):
        if len(token) == 0:
            continue

        n_token = int(token)
        if is_prime_number(n_token):
            cnt += 1

    return cnt


def convert_recur(num, base):
    number = string.digits + string.ascii_uppercase
    q, r = divmod(num, base)
    return convert_recur(q, base) + number[r] if q else number[r]


def is_prime_number(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
