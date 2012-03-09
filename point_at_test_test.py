import unittest

import point_at_test


test_source = '''\
#!/usr/bin/env python

"Module docstring to make this more realistic."

class TestCaseClass(TestCase):         # Line 5

    def test_something_happens(self):  # Line 7
        make_something_happen()
        assert_something_happened()    # Line 9
                                       # Line 10
class AnotherTestCaseClass(TestCase):  # Line 11

    def test_nothing(self):            # Line 13
        pass

    def test_nothing_either(self):     # Line 16
        pass

if __name__ == '__main__':
    run()
'''


class PointAtTestTestCase(unittest.TestCase):

    def test_finds_a_class_name(self):
        test_name = point_at_test.point_at_test(test_source, 5)
        self.assertEqual('TestCaseClass', test_name)

    def test_finds_the_second_class_name(self):
        test_name = point_at_test.point_at_test(test_source, 11)
        self.assertEqual('AnotherTestCaseClass', test_name)

    def test_finds_the_first_function_name(self):
        test_name = point_at_test.point_at_test(test_source, 7)
        self.assertEqual('TestCaseClass.test_something_happens', test_name)

    def test_finds_the_second_function_name(self):
        test_name = point_at_test.point_at_test(test_source, 13)
        self.assertEqual('AnotherTestCaseClass.test_nothing', test_name)

    def test_finds_the_second_function_on_a_class(self):
        test_name = point_at_test.point_at_test(test_source, 16)
        self.assertEqual('AnotherTestCaseClass.test_nothing_either', test_name)

    def test_returns_the_empty_string_if_the_line_is_empty(self):
        test_name = point_at_test.point_at_test(test_source, 10)
        self.assertEqual('', test_name)

    def test_returns_the_empty_string_if_inside_a_method(self):
        test_name = point_at_test.point_at_test(test_source, 9)
        self.assertEqual('', test_name)


if __name__ == '__main__':
    unittest.main()
