import unittest

from function_composition import compose


class FunctionCompositionTests(unittest.TestCase):

    def test_compose_1_arg_funcs(self):
        def plus_2(x):
            return x + 2

        def times_3(x):
            return 3 * x

        self.assertEqual(compose(times_3, plus_2)(1), 9)
        self.assertEqual(compose(times_3, plus_2)(2), 12)
        self.assertEqual(compose(times_3, plus_2)(3), 15)
        self.assertEqual(map(compose(times_3, plus_2), [1, 2, 3]), [9, 12, 15])

    def test_compose_string_funcs(self):
        self.assertEqual(compose(str.strip, str.upper)(' hello '), 'HELLO')
        self.assertEqual(compose(str.strip, str.upper)(' goodbye '), 'GOODBYE')

    def test_compose_2_arg_funcs(self):
        def plus_2(x, y):
            return (x + 2, y + 2)

        def times_3(x, y):
            return (3 * x, 3 * y)

        self.assertEqual(compose(times_3, plus_2)(1, 2), (9, 12))
        self.assertEqual(compose(times_3, plus_2)(2, 3), (12, 15))
        self.assertEqual(compose(times_3, plus_2)(3, 4), (15, 18))
