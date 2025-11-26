try:
    with open('Филатов М.И._у-252_vvod.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print("Содержимое файла:", lines)  # Для отладки
except FileNotFoundError:
    print("Файл не найден! Создаю пример файла...")
    with open('Филатов М.И._у-252_vvod.txt', 'w', encoding='utf-8') as file:
        file.write("3\n")
        file.write("1 2 3\n")
        file.write("4 5 6\n")
        file.write("7 8 9\n")
        file.write("3 4\n")
        file.write("10 -5 8 3\n")
        file.write("-2 15 7 1\n")
        file.write("4 6 -3 12\n")
    print("Файл создан. Запустите программу снова.")
    exit()

try:
    n = int(lines[0].strip())
    A = []

    for i in range(1, n + 1):
        row = list(map(int, lines[i].split()))
        A.append(row)

    count_positive = 0
    sum_positive = 0

    for i in range(n):
        for j in range(i + 1, n):
            if A[i][j] > 0:
                count_positive += 1
                sum_positive += A[i][j]

except (ValueError, IndexError) as e:
    print(f"Ошибка при обработке матрицы A: {e}")
    print("Проверьте формат данных в файле")
    exit()

try:
    n_b, m_b = map(int, lines[n + 1].split())
    B = []

    for i in range(n + 2, n + 2 + n_b):
        row = list(map(int, lines[i].split()))
        B.append(row)

    B_original = [row[:] for row in B]  # Сохраняем копию исходной матрицы

    for i in range(n_b):
        min_index = 0
        max_index = 0

        for j in range(1, m_b):
            if B[i][j] < B[i][min_index]:
                min_index = j
            if B[i][j] > B[i][max_index]:
                max_index = j

        B[i][0], B[i][min_index] = B[i][min_index], B[i][0]

        if max_index == 0:
            max_index = min_index

        B[i][m_b - 1], B[i][max_index] = B[i][max_index], B[i][m_b - 1]

except (ValueError, IndexError) as e:
    print(f"Ошибка при обработке матрицы B: {e}")
    print("Проверьте формат данных в файле")
    exit()

try:
    with open('Филатов М.И._у-252_vivod.txt', 'w', encoding='utf-8') as file:
        file.write("ЗАДАНИЕ 1:\n")
        file.write(f"Матрица A[{n}×{n}]:\n")
        for row in A:
            file.write(' '.join(map(str, row)) + '\n')
        file.write(f"Число положительных элементов над главной диагональю: {count_positive}\n")
        file.write(f"Сумма положительных элементов над главной диагональю: {sum_positive}\n\n")

        file.write("ЗАДАНИЕ 2:\n")
        file.write(f"Исходная матрица B[{n_b}×{m_b}]:\n")
        for row in B_original:
            file.write(' '.join(map(str, row)) + '\n')

        file.write(f"\nПреобразованная матрица B[{n_b}×{m_b}]:\n")
        for row in B:
            file.write(' '.join(map(str, row)) + '\n')

        file.write("\nПояснение:\n")
        file.write("В каждой строке минимальный элемент поменян с первым,\n")
        file.write("а максимальный элемент - с последним.\n")

    print("Результаты успешно записаны в файл 'Филатов М.И._у-252_vivod.txt'")

except Exception as e:
    print(f"Ошибка при записи в файл: {e}")