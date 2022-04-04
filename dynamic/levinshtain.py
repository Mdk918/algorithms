# 66094931
"""
    Определяем длины строк как n и m. Заводим матрицу (n+1)(m+1). Далее
    вычисляем расстояние Левинштейна по алгоритму Вагнера-Фишера.
    Основные принципы алгоритма:
    1) D(0,0) = 0. - пустые строки и так совпадают.
    2) Также, ясны значения для:
    D(i, 0) = i;
    D(0, j) = j.
    Любая строка может получиться из пустой, добавлением нужного количества
    нужных символов, любые другие операции будут только увеличивать оценку.
    3) D(i,j) = D(i-1,j-1), если S1[i] = S2[j],
    иначе D(i,j) = min( D(i-1,j), D(i,j-1), D(i-1,j-1) ) + 1.
    В данном случае, мы выбираем, что выгоднее: удалить символ (D(i-1,j)),
    добавить (D(i,j-1)), или заменить (D(i-1,j-1)).

    -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
    Потребуется O(|S1|*|S2|) времени

    -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    Потребуется O(2*|S2|) памяти

"""


def levinstain(past_string, n, m):
    for i in range(n+1):
        current_string = [0 for i in range(m + 1)]
        for j in range(m+1):
            if i == 0 and j == 0:
                current_string[j] = 0
            elif j == 0 and i > 0:
                current_string[j] = i
            elif i == 0 and j > 0:
                current_string[j] = j
            else:
                if s1[i-1] == s2[j-1]:
                    x = 0
                else:
                    x = 1
                current_string[j] = min(current_string[j-1]+1,
                                        past_string[j]+1, past_string[j-1]+x)
        past_string = current_string
    return current_string[m]


if __name__ == '__main__':

    s1 = input()
    n = len(s1)
    s2 = input()
    m = len(s2)
    past_string = [0 for i in range(m+1)]

    print(levinstain(past_string, n, m))




