

def rotate_matrix(m):
    if len(m) == 0:
        return m
    
    # 数组维度
    n = len(m[0])
    # 每行或每列最后一个元素的index
    last = n - 1

    # 起始index
    start = 0
    # 结束index
    end = last

    while start < end:
        # 遍历行数组
        for i in range(start, end):
            # 每个点连续交换4次，即可完成轮转
            # 点坐标映射关系p1(x,y) = p0(-y,x) = (last-y, x)
            temp = m[start][i]
            m[start][i] = m[last-i][start]
            m[last-i][start] = m[last-start][last-i]
            m[last-start][last-i] = m[i][last-start]
            m[i][last-start] = temp
        # 进入内环
        start += 1
        end -= 1
    
    return m


def check(m1, m2):
    m3 = rotate_matrix(m1)
    assert m3 == m2, f"check rotate matrix failed: {m1} -> {m2}, actual result: {m3}"


if __name__ == '__main__':
    check([[1,2],[3,4]], [[3,1],[4,2]])

    m1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    m2 = [
        [7,4,1],
        [8,5,2],
        [9,6,3]
    ]
    check(m1, m2)

    m3 = [
        [ 5, 1, 9,11],
        [ 2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]
    ]
    m4 = [
        [15,13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7,10,11]
    ]
    check(m3, m4)