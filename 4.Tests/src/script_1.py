courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]
mentors = [
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]

courses_list = []


def create_dict(course_, mentor_, duration_):
    for title, mentor, duration in zip(course_, mentor_, duration_):
        course_dict = {'title': title, 'mentor': mentor, 'duration': duration}
        courses_list.append(course_dict)
    return courses_list


maxes = []
minis = []


def duration_courses(courses_list_):
    min_d = min(durations)
    max_d = max(durations)
    for index, duration in enumerate(durations):
        if durations[index] == max_d:
            maxes.append(index)
        elif durations[index] == min_d:
            minis.append(index)

    courses_min = []
    courses_max = []
    for id_min in minis:
        courses_min.append(courses_list_[id_min]['title'])
    for id_max in maxes:
        courses_max.append(courses_list_[id_max]['title'])

    for_print = f'Самый короткий курс(ы): {", ".join(courses_min)} - {min_d} месяца(ев)\n' \
                f'Самый длинный курс(ы): {", ".join(courses_max)} - {max_d} месяца(ев)'
    return for_print


if __name__ == '__main__':
    create_dict(courses, mentors, durations)
    print(duration_courses(courses_list))
