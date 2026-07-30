"""
N-Queens 问题：

给定义一个正整数 n, 要求在 n x n 的棋盘上摆放 n 个 queen, 要求无论是同一行、同一列、对角线上都不能同时出现 2 个皇后

给定一个 n ， 搜索所有可能的解

"""
def solve_n_queens(n):
    res = []  # 用于存储所有找到的解

    # 用于记录皇后位置的集合
    cols = set()  # 已占用的列
    diag1 = set()  # 已占用的主对角线 (row - col = 常数)
    diag2 = set()  # 已占用的副对角线 (row + col = 常数)

    # state 记录当前解，state[i] = j 表示第 i 行的皇后放在第 j 列
    state = []

    def dfs(row):
        """深度优先搜索函数，尝试在第 row 行放置皇后"""
        if row == n:
            # 找到一个解，将其加入结果集
            res.append(state[:])
            return

        for col in range(n):
            # 检查当前列和两条对角线是否已被占用
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            # 做选择：在 (row, col) 放置皇后
            state.append(col)
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            # 递归进入下一行
            dfs(row + 1)

            # 撤销选择：回溯
            state.pop()
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    # 从第 0 行开始进行深度优先搜索
    dfs(0)
    return res


# --- 示例用法 ---
n = 4
solutions = solve_n_queens(n)
print(solutions)
print(f"找到 {len(solutions)} 个解:")
for i, solution in enumerate(solutions):
    print(f"解 {i + 1}: {solution}")
