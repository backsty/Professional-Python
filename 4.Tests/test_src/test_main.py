# import unittest
# from unittest import TestCase
import pytest
from src.script_1 import create_dict, duration_courses


class Test_Populate_Name_Pytest:

    @pytest.mark.parametrize("courses, mentors, duration, expected", [
        (["Java-разработчик с нуля", "Fullstack-разработчик на Python"],
         [["Филипп Воронов", "Анна Юшина"], ["Евгений Шмаргунов", "Олег Булыгин"]], [14, 20], 2),
        (["Java-разработчик с нуля"], [["Филипп Воронов"]], [14], 1)
    ])
    def test_create_dict_pytest(self, courses, mentors, duration, expected):
        result = create_dict(courses, mentors, duration)
        assert len(result) == expected

    @pytest.mark.parametrize("courses_list, expected", [
        ([{'title': 'Java-разработчик с нуля', 'mentor': 'Филипп Воронов', 'duration': 14},
          {'title': 'Fullstack-разработчик на Python', 'mentor': 'Евгений Шмаргунов', 'duration': 20}],
         "Самый короткий курс(ы): Java-разработчик с нуля - 14 месяца(ев)\n"
         "Самый длинный курс(ы): Fullstack-разработчик на Python - 20 месяца(ев)"),
        ([{'title': 'Java-разработчик с нуля', 'mentor': 'Филипп Воронов', 'duration': 14}],
         "Самый короткий курс(ы): Java-разработчик с нуля - 14 месяца(ев)\n"
         "Самый длинный курс(ы): Java-разработчик с нуля - 14 месяца(ев)")
    ])
    def test_duration_courses_pytest(self, courses_list, expected):
        result = duration_courses(courses_list)
        assert result == expected


# class Test_Populate_Name_Unittest(TestCase):
#
#     def test_create_dict_unittest(self):
#         self.courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python"]
#         self.mentor = [["Филипп Воронов", "Анна Юшина"], ["Евгений Шмаргунов", "Олег Булыгин"]]
#         self.duration = [14, 20]
#         self.courses_list = create_dict(self.courses, self.mentor, self.duration)
#         self.assertEqual(len(self.courses_list), 2)
#         self.assertEqual(self.courses_list[0]['title'], "Java-разработчик с нуля")
#
#     def test_duration_courses_unittest(self):
#         result = duration_courses(self.courses_list)
#         self.assertIn(f"Самый короткий курс(ы): Java-разработчик с нуля - 14 месяца(ев)", result)
#         self.assertIn(
#             f"Самый длинный курс(ы): Fullstack-разработчик на Python, Frontend-разработчик с нуля - 20 месяца(ев)",
#             result)
#
#
# if __name__ == '__main__':
#     unittest.main()
