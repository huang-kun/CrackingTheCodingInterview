
def zero_matrix(a):
    # 使用额外空间存储值为0的行列数据
    # 时间O(M*N), 空间O(M+N)
    m = len(a)
    n = len(a[0]) if m > 0 else 0

    # 如果是C语言，额外空间就可以用两个数组，下标作为行或列
    # 如果矩阵维度不会很大的话，也可以使用两个位向量，每一位表示特定的行或列
    rows = set()
    cols = set()

    for row in range(m):
        for col in range(n):
            if a[row][col] == 0:
                rows.add(row)
                cols.add(col)
    
    for row in range(m):
        for col in range(n):
            if row in rows or col in cols:
                a[row][col] = 0


def check(m1, m2):
    zero_matrix(m1)
    assert m1 == m2, f"zero matrix failed: {m1} -> {m2}"


if __name__ == '__main__':
    check([[1,2],[3,0]], [[1,0],[0,0]])

    m1 = [
        [1,2,3],
        [4,0,6],
        [7,8,9]
    ]
    m2 = [
        [1,0,3],
        [0,0,0],
        [7,0,9]
    ]
    check(m1, m2)

    m3 = [
        [ 5,  1,  9, 11],
        [ 2,  4,  0, 10],
        [ 0,  3,  6,  7],
        [15, 14, 12, 16]
    ]
    m4 = [
        [0,  1,  0, 11],
        [0,  0,  0,  0],
        [0,  0,  0,  0],
        [0, 14,  0, 16]
    ]
    check(m3, m4)