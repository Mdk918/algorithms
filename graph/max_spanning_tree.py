# 65365296
"""
    Граф храним в матрице смежности.
    Перед началом обхода делам провеку основных условий в
    которых изначально будет известно что остов посторить невозможно.
    Прицнип обхода:
    Для построения остова, можно стартовать с любой точки, по умолчанию была
    выбрана точка 1.
    Добавляем точку в посещенные и делаем поиск всех смежных ребер. В случае
    нахождения в словаре ребра с совпадающей конечной вершиной, оставляем
    только ребро с максимальным весом. Далее находим максимальное ребро из
    доступных и повторяем процедуру пока не пройден весь граф. В случае если
    граф обойти невозможно, выдаем ошибку.

    -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
     В худшем случае временная сложность О(|V| + |E|), где Е - количество
     ребер.

    -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    Хранение самого графа - О(V^2), список посещенных вершин - O(V),
    список ребер O(E).

"""

def visit_node(node):
    added.add(node)
    for i in range(n + 1):
        if graph[node][i] is None or i in added:
            continue
        elif free_node.get(i, -1) < graph[node][i]:
            free_node[i] = graph[node][i]
    free_node[node] = -1


def find_MST():
    weight = 0
    visit_node(1)
    while len(added) != n + 1:
        node, mweight = max(free_node.items(),
                            key=lambda item: item[1])

        if mweight == -1:
            return None
        else:
            weight += mweight
            visit_node(node)
    return weight


if __name__ == '__main__':

    n, m = map(int, input().split())
    graph = [[None] * (n + 1) for _ in range(n + 1)]

    for i in range(m):
        j, k, z = map(int, input().split())
        if j == k:
            continue
        if graph[j][k] is None or graph[j][k] < z:
            graph[j][k] = z


    added = set([0])
    free_node = {}

    if n == 1 and m == 0:
        print(0)
    elif (n > 1 and m == 0) or n > m or all(any(row) for row in graph):
        print('Oops! I did it again')
    else:
        result = find_MST()
        if result is None:
            print('Oops! I did it again')
        else:
            print(result)

