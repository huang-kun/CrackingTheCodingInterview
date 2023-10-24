
def is_palindrome(s):
    """散列表记录字符次数，时间O(n)，空间O(n)"""
    if len(s) == 0:
        return False
    
    # 记录字符次数
    d = {}
    for char in s:
        c = char.lower()
        if c == " ":
            continue
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    
    # 统计奇数字符的个数
    odd_count = 0
    for k in d:
        if d[k] % 2 != 0:
            odd_count += 1
        if odd_count > 2:
            return False
    
    return True


def check(s, f):
    assert is_palindrome(s) == f, f"check palindrome failed: {s} -> {f}"


if __name__ == '__main__':
    check("Tact Coa", True)
    check("Bat Tab", True)
    check("Was it a bar or a bat I saw", True)
    check("Hello World", False)
    check("", False)
    check("Wooooow", True)