
def is_substring(s1, s2):
    """这是题目提供的允许调用的方法，不需要自己实现"""
    return s1 in s2

def is_rotate_str(s1, s2):
    if len(s1) != len(s2):
        return False
    if not is_substring(s1, s2 + s2):
        return False
    return True


def check(s1, s2, exp):
    assert is_rotate_str(s1, s2) == exp, f"check rotate strings failed: {s1}, {s2} -> {exp}"


if __name__ == '__main__':
    check("waterbottle", "erbottlewat", True)
    check("yo ho", "ho yo", False)
    check("ab", "aba", False)  # 如果不检查长度，这里就坑了
    check("aba", "bab", False)
    check("hello", "world", False)
    check("", "hi", False)
    check("", "", True)
