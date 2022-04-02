# 66523834
"""
    Распаковывыем слова из ввода и сохраняем их в массив слов.
    Опорная точка для каждой операции распковки - наличие цифры в слове. При
    обходе слова, если встречаем цифру считаем количесво квадратных скобок для
    проверки внутрениих запакованных объектов в найденном запакованном объекте.
    Отделяем префикс и суффик и через срезы делаем замены запакованных
    элементов.
    После распаковки слов находим их общий префикс и выводим его.

    -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    Для распаковки слов потребуется O(n * k) - для каждого слова, где k -
    количество запакованных элементов в слове. Для поиска общего префикса O(2m)
    где m - длина самого коротного слова.


    -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    Потребуется O(L) - где L сумма длиг всех слов.

"""

def packed(strings):
    if len(strings) < 3:
        return strings
    for i in range(len(strings)):
        if strings[i].isdigit():
            prefix = strings[:i]
            cnt_open = 1
            cnt_close = 0
            index = i+2
            while cnt_close != cnt_open:
                if strings[index] == '[':
                    cnt_open += 1
                    index += 1
                elif strings[index] == ']':
                    cnt_close += 1
                    index += 1
                else:
                    index += 1
            pack = strings[i + 2:index-1]
            suffix = strings[index:]
            strings = prefix + int(strings[i]) * packed(pack) + packed(suffix)
            break
    return strings


def longets(strs):
    res = ''
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += strs[0][i]
    return res


if __name__ == '__main__':

    n = int(input())
    unpack_strs = [packed(input()) for i in range(n)]
    print(longets(unpack_strs))
