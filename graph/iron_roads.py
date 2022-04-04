# 65664290
"""
    При обработке входных данных формируем граф по принципу -
    один тип дорог яляется движением к вверх(к столице), другой тип дорог
    является движением вниз. Храним граф в виде списка смежности.
    Далее запускам стандартный обход в глубину но с поиском цикла -
    если при следовании по маршруту попадаем в уже посещенный город,
    значит цикл присутсвует и дороги не оптимальный. Данный обход совершаем
    по всему графу.

    -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
     Поскольку алгоритм обрабатывает все вершины, ему придётся пройтись по
     всем спискам смежности. В худшем случае дойдем до конца маршрута получим,
     что итоговая сложность алгоритма O(V+E). О(Е) проход по каждому ребру
     один раз.

    -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    Хранение самого графа - O(V+E), стек с вершинами - O(V), список с
    расскраской O(V)

"""


def optimal_roads(start, graph):

    stack = []
    stack.append(start)
    while stack:
        v = stack.pop()
        if color[v-1] == 0:
            color[v-1] = 1
            stack.append(v)
            for i in graph[v]:
                if color[i-1] == 0:
                    stack.append(i)
                elif color[i-1] == 1:
                    return False
        else:
            color[v-1] = 2


def main_DFS():
    for i in range(n):
        if color[i] == 0:
            if optimal_roads(i+1, roads) is False:
                return False
    return True


if __name__ == '__main__':

    n = int(input())
    roads = {}
    for i in range(1, n + 1):
        roads[i] = []
    for i in range(1, n):
        a = input()
        index = 0
        for j in range(i + 1, len(a) + i + 1):
            if a[index] == 'R':
                roads[i].append(j)
                index += 1
            else:
                roads[j].append(i)
                index += 1

    color = [0] * n
    if main_DFS() is False:
        print('NO')
    else:
        print('YES')
