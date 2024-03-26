from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("Test1")
        self.student_with_courses = Student("Test2", {"math": ["x + y = z"]})

    def test_correct_init(self):
        self.assertEqual("Test1", self.student.name)
        self.assertEqual("Test2", self.student_with_courses.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({"math": ["x + y = z"]}, self.student_with_courses.courses)

    def test_enroll_with_the_same_course_appends_new_notes(self):
        result = self.student_with_courses.enroll("math", ["1 + 2 = 3"], "3 + 4 = 7")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"math": ["x + y = z", "1 + 2 = 3"]}, self.student_with_courses.courses)

    def test_enroll_with_new_course(self):
        result = self.student_with_courses.enroll("english", ["x + y = z"])
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"english": ["x + y = z"], "math": ["x + y = z"]}, self.student_with_courses.courses)

    def test_enroll_with_new_course_notes(self):
        result = self.student_with_courses.enroll("english", ["x + y = z"], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"english": ["x + y = z"], "math": ["x + y = z"]}, self.student_with_courses.courses)

    def test_enroll_with_invalid_course_notes(self):
        result = self.student_with_courses.enroll("english", ["x + y = z"], "n")
        self.assertEqual("Course has been added.", result)
        self.assertEqual({"english": [], "math": ["x + y = z"]}, self.student_with_courses.courses)

    def test_add_notes_to_existing_course_expect_success(self):
        result = self.student_with_courses.add_notes("math", "x + y = z")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual({"math": ["x + y = z", "x + y = z"]}, self.student_with_courses.courses)

    def test_add_notes_to_non_existing_course_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_courses.add_notes("english", "x + y = z")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
        self.assertEqual({"math": ["x + y = z"]}, self.student_with_courses.courses)

    def test_leave_course_expect_success(self):
        result = self.student_with_courses.leave_course("math")
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student_with_courses.courses)

    def test_leave_course_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_courses.leave_course("english")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
        self.assertEqual({"math": ["x + y = z"]}, self.student_with_courses.courses)


if __name__ == "__main__":
    main()
