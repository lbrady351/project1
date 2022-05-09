import unittest
from gui_main import *


class MyTestCase(unittest.TestCase):
    def test_student_name(self):
        self.assertEqual(student_name("Abby"), "ABBY")  # add assertion here
        self.assertEqual(student_name("Beth"), "BETH")

        self.assertNotEqual(student_name("Abby!"), "ABBY!")
        self.assertNotEqual(student_name("123"), "BETH")

    def test_student_score(self):
        self.assertEqual(student_score("50"), 50.0)
        self.assertEqual(student_score("100"), 100.0)

        self.assertNotEqual(student_score("1000"), 1000)
        self.assertNotEqual(student_score("-5"), -5)
        self.assertNotEqual(student_score("hi"), 100)

    def test_letter_grade(self):
        self.assertEqual(letter_grade("50"), "F")
        self.assertEqual(letter_grade("100"), "A")

        self.assertNotEqual(letter_grade("1000"), "A")
        self.assertNotEqual(letter_grade("-5"), "F")
        self.assertNotEqual(letter_grade("hi"), "F")
        self.assertNotEqual(letter_grade("50"), "A")


if __name__ == '__main__':
    unittest.main()
