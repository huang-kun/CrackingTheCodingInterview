
def compress_str(s):
    # 1.6 字符串压缩：一次遍历，时间O(n)，空间O(n)
    # 由于python没有StringBuilder，所以每次字符串的整合耗时暂时没有考虑
    cs = ""
    last_char = None
    counter = 0
    len_s = 0
    len_cs = 0

    for char in s:
        len_s += 1
        if last_char and last_char != char:
            cs += last_char
            cs += str(counter)
            len_cs += 2
            last_char = char
            counter = 1
        else:
            last_char = char
            counter += 1
    
    if last_char and counter > 0:
        cs += last_char
        cs += str(counter)
        len_cs += 2
    
    if len_cs < len_s:
        return cs
    else:
        return s


def check(s, exp):
    cs = compress_str(s)
    assert cs == exp, f"compress string failed: {s} -> {exp}, actual result: {cs}"


if __name__ == '__main__':
    check("aabcccccaaa", "a2b1c5a3")
    check("hello", "hello")
    check("aa", "aa")
    check("", "")
    check("AaAAAAbAAAA", "A1a1A4b1A4")
    check("AaAAABbAAAA", "AaAAABbAAAA")