
def str_to_url(char_list, real_len):
    """原地替换，时间O(n)，空间O(1)"""
    s = " "
    
    # 数空格数
    space_count = 0
    for i in range(0, real_len):
        c = char_list[i]
        if c == s:
            space_count += 1
    
    # 计算额外空间
    extra = space_count * 2
    
    # 放置双指针p, q
    p = real_len - 1
    q = p + extra

    # 转移字符，遇空格替换
    while p >= 0 and p < q:
        if char_list[p] != s:
            char_list[q] = char_list[p]
            p -= 1
            q -= 1
        else:
            char_list[q-2] = "%"
            char_list[q-1] = "2"
            char_list[q] = "0"
            p -= 1
            q -= 3


def check(s, real_len, result):
    char_list = list(s)
    str_to_url(char_list, real_len)
    s2 = ''.join(char_list)
    assert s2 == result, f"string percent encoding failed: f{s}, {real_len} -> {result}, actual result: {s2}"


if __name__ == '__main__':
    check("Mr John Smith    ", 13, r"Mr%20John%20Smith")
    check(" Hello  World      ", 13, r"%20Hello%20%20World")