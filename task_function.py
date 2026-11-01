# ДЗ Функии
#
# В `Corp_Summary.csv` лежит выгрузка по сотрудникам: ФИО, департамент, команда, должность, оценка, оклад. Колонки разделены `;`.
#
# Напишите программу, которая читает файл и по выбранному в аргументах варианту готовит отчёт. На экран выводите так, как вам удобно читать.
#
# Варианты отчётов такие. Основная функция должна принимать на вход int - номер варианта. остальные параметры - по желанию:
#
# 1. Иерархия: для каждого департамента показать, какие команды в него входят.
# 2. Сводка по департаментам: название, сколько человек, минимальная и максимальная зарплата, средняя по каждому департаменту.
# 3. То же самое, что в "2", но записанное в csv-файл. Имя выходного файла можно захардкодить(например, константой в начале файла) или передавать опциональным параметром в эту же функцию.
#
# Чтение файла и каждый отчёт вынесите в отдельные функции.
#

import csv

def read_file(filename: str)-> list[list[str]]:

    with open(filename, 'r', encoding='utf-8-sig', newline='' ) as f:
        reader = csv.reader(f, delimiter=';')
        return list(reader)

def task1(data) -> dict:
    hierarchy = {}

    for s in data[1:]:
        department = s[1]
        team = s[2]

        if department not in hierarchy:
            hierarchy[department] = set()

        hierarchy[department].add(team)

    return hierarchy

def show_task1(hierarchy) -> None:
    print('Вывелось задание 1')

    for department, team in hierarchy.items():
        print(f'{department}: {', '.join(team)}')

def task2(data) -> dict:
    summary = {}

    for s in data[1:]:
        department = s[1]
        salary = float(s[5])

        if department not in summary:
            summary[department] = {'employee_count': 0,
                      'min_salary': salary,
                      'max_salary': salary,
                      'average_salary': 0}

        summary[department]['employee_count'] += 1
        summary[department]['average_salary'] += salary

        if salary < summary[department]['min_salary']:
            summary[department]['min_salary'] = salary

        if salary > summary[department]['max_salary']:
            summary[department]['max_salary'] = salary

    for department in summary:
        summary[department]['average_salary'] = round(
            summary[department]['average_salary']
            /summary[department]['employee_count'], 2)

    return summary

def show_task2(summary) -> None:
    print('Вывелось задание 2')

    for department in summary:
        print(f"Департамент: {department}\n"
              f"Количество сотрудников: {summary[department]['employee_count']}\n"
              f"Минимальная зарплата: {summary[department]['min_salary']}\n"
              f"Максимальная зарплата: {summary[department]['max_salary']}\n"
              f"Средняя зарплата: {summary[department]['average_salary']}\n")


def task3(data) -> None:
    department_summary = task2(data)
    department_stats = list(department_summary.values())

    with open('department_summary.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['department'] + (list(department_stats[0].keys())))

        for department, stats in department_summary.items():
            writer.writerow([department] + list(stats.values()))
    # читаем что получилось
    with open('department_summary.csv', 'r', encoding='utf-8') as file:
       print(file.read())
    print('Задание 3 выполнилось')


def main(number_task: int) -> None:

    if number_task not in (1, 2, 3):
        print("Некорректный номер отчёта")
        return

    data = read_file('Corp_Summary.csv')

    if number_task == 1:
        show_task1(task1(data))

    elif number_task == 2:
        show_task2(task2(data))

    else:
        task3(data)


if __name__ == "__main__":

    number_task =  int(input('Введите номер задания: '))
    main(number_task)



