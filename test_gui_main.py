import unittest
from gui_main import *


class MyTestCase(unittest.TestCase):
    def test_student_name(self):
        self.assertEqual(student_name("Abby"), "Abby")  # add assertion here
        self.assertEqual(student_name("Beth"), "Beth")

        self.assertNotEqual(student_name("Abby!"), "Abby")
        self.assertNotEqual(student_name("123"), "Beth")

    def test_student_score(self):
        self.assertEqual(student_score("50"), 50.0)
        self.assertEqual(student_score("100"), 100.0)

        self.assertNotEqual(student_score("1000"), 1000)
        self.assertNotEqual(student_score("-5"), -5)
        self.assertNotEqual(student_score("hi"), 100)

    def test_letter_grade(self):
        self.assertEqual(student_score("50"), "F")
        self.assertEqual(student_score("100"), "A")

        self.assertNotEqual(student_score("1000"), "A")
        self.assertNotEqual(student_score("-5"), "F")
        self.assertNotEqual(student_score("hi"), "F")
        self.assertNotEqual(student_score("50"), "A")


if __name__ == '__main__':
    unittest.main()
