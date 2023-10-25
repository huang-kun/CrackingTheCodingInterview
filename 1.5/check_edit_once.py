
def check_edit_once(s1, s2):
    # 先比长度，再遍历比较。时间 O(n), 空间 O(1)
    len1 = len(s1)
    len2 = len(s2)

    if abs(len1 - len2) > 1:
        return False
    
    p, q = 0, 0
    diff_chars = 0

    while p < len1 and q < len2:
        diff = s1[p] != s2[q]
        if diff:
            diff_chars += 1
        
        if diff_chars > 1:
            return False
        
        if diff and len1 > len2:
            p += 1
        elif diff and len1 < len2:
            q += 1
        else:
            p += 1
            q += 1

    return True


def check(s1, s2, flag):
    assert check_edit_once(s1, s2) == flag, f"check edit once failed: {s1}, {s2} -> {flag}"


if __name__ == '__main__':
    check("pale", "ple", True)
    check("pales", "pale", True)
    check("pale", "bale", True)
    check("pale", "bake", False)
    check("hello", "Hello!", False)
    check("hi", "hey", False)
    check("go", "gooo", False)