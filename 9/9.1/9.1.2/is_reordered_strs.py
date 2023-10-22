
def is_reordered_strs_v1(s1, s2):
    """散列表缓存，时间O(n)，空间O(n)"""

    def count_char(s):
        """记录字符出现次数，时间O(n)，空间O(n)"""
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        return d

    if len(s1) != len(s2):
        return False
    elif len(s1) == 0:
        return False
    
    d1 = count_char(s1)
    d2 = count_char(s2)

    if len(d1) != len(d2):
        return False
    
    for k in d1:
        if k not in d2:
            return False
        elif d1[k] != d2[k]:
            return False
        
    return True
    

def is_reordered_strs_v2(s1, s2):
    """排序法，时间O(nlogn)，空间O(n)"""
    
    def sorted_chars(s):
        """排序字符"""
        chars = list(s)
        # 理想系统排序时间O(nlogn)
        return sorted(chars)

    if len(s1) != len(s2):
        return False
    elif len(s1) == 0:
        return False

    cs1 = sorted_chars(s1)
    cs2 = sorted_chars(s2)

    for i in range(len(cs1)):
        if cs1[i] != cs2[i]:
            return False
    
    return True


def check(s1, s2, f):
    assert is_reordered_strs_v2(s1, s2) == f, f"check reordered strs failed: {s1}, {s2} -> {f}"


if __name__ == "__main__":
    check("hello", "elloh", True)
    check("hello", "eHllo", False)
    check("hi", "hello", False)
    check("", "", False)