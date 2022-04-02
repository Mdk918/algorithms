# 66655855
"""
    Создаем префиксное дерево из набора слов для проверки строки.
    При создании строки переворачиваем чтобы развенуть само дерево.
    Создаем массив равный длине строки +1, для фиксации терминальных точек и
    проверки возможности использования слов.
    После создания дерева начинаем обход строки по всей ее длине:
    Ячейки будем заполнять значениями true или false по условию того, можно ли
    составить подстроку исходной строки из имеющихся в словаре слов или нет.
    Для каждого индекса исходной строки будем проверять узлы префиксного дерева,
    и если узел терминальный и ячейка массива dp без рассматриваемого
    слова == true, то ячейка dp с текущим индексом также заполняется true.
    В конце проверяем  равен ли последний эелемент массива true.

    -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    Потребуется O(L), где L — суммарная длина слов во множестве, для построения
    дерева. Для дальнейшего выполнения обхода потребуется О(n^2), в связи с
    возможностью внутреннего цикла while из любой позиции пошагово вернуться к
    стартовой точке.

    -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    Потребуется O(N + M), где N сумма длин всех доступных слов, а M длина
    искомой строки.

"""

def add_string(root, string):
    current_node = root
    for i in range(len(string)):
        symbol = string[i]
        if symbol not in current_node:
            current_node[symbol] = {}
        current_node = current_node[symbol]
    current_node['terminal'] = True
    return current_node


def crib(text, patterns):
    stack = [False]*(len(text)+1)
    stack[0] = True
    for i in range(len(text)):
        j = i + 1
        node = patterns
        while node is not None and j > 0:
            if text[j-1] in node:
                node = node[text[j-1]]
            else:
                node = None
            j -= 1
            if node:
                if j >= 0 and 'terminal' in node and stack[j] is True:
                    stack[i+1] = True
                    break
    if stack[len(text)] is True:
        return True
    return False


if __name__ == '__main__':
    search_str = input()
    cnt_words = int(input())
    words = {}

    for i in range(cnt_words):
        cur_str = input()
        cur_str = cur_str[::-1]
        add_string(words, cur_str)

    if crib(search_str, words):
        print('YES')
    else:
        print('NO')