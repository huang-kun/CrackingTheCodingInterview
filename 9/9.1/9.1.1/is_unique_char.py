

def is_unique_char_in_str_v1(s):
    '''蛮力算法，时间O(n²)，空间O(1)'''
    if len(s) == 0:
        return False

    for i in range(0, len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
            
    return True


def is_unique_char_in_str_v2(s):
    '''散列表缓存，时间O(n)，空间O(n)'''
    if len(s) == 0:
        return False

    cache = set()
    for c in s:
        if c in cache:
            return False
        cache.add(c)

    return True


def is_unique_char_in_str_v3(s):
    '''位向量，时间O(n)，空间O(1)，这里限制字符输入为a-z'''
    if len(s) == 0:
        return False
    
    # 为a-z设置26位比特，出现过的字符标记为1
    num = 0
    for c in s:
        i = ord(c) - 97
        if num & 1 << i:
            return False
        num |= 1 << i
    
    return True


def check(s, f):
    assert is_unique_char_in_str_v3(s) == f, f"check unique char failed: {s} -> {f}" 


if __name__ == "__main__":
    check("hello", False)
    check("hi", True)
    check("", False)
