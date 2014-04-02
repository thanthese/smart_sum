from unittest import TestCase

from smart_sum import smart_sum


class TestSmart_sum(TestCase):
    def test_ints(self):
        expected = "1001339"
        actual = smart_sum("""
            10
            100 hello world
            $1,000 test LKJDF (*&)@
            -10
            1,000,000
            234
            -14 3 4
            nonsense 12""")
        self.assertEqual(expected, actual, msg="Expected {} but got {}".format(expected, actual))

    def test_floats(self):
        expected = "1001340.5434"
        actual = smart_sum("""
            10.2
            100.3 hello world
            $1,000.4 test LKJDF (*&)@
            -10.6
            1,000,000.1234
            234.02
            -14.1 3.3 4.4
            nonsense 12.5""")
        self.assertEqual(expected, actual, msg="Expected {} but got {}".format(expected, actual))


    def test_money(self):
        expected = "312.95"
        actual = smart_sum("$12.43 $100.42 $200.10")
        self.assertEqual(expected, actual, msg="Expected {} but got {}".format(expected, actual))


    def test_mix(self):
        expected = "30.2"
        actual = smart_sum("10.2 20")
        self.assertEqual(expected, actual, msg="Expected {} but got {}".format(expected, actual))

    def test_possible_gotcha_examples(self):
        expected = "1.00"
        actual = smart_sum("1 000 000.00")
        self.assertEqual(expected, actual, msg="Expected {} but got {}".format(expected, actual))

        expected = "123456789"
        actual = smart_sum("123,456,789")
        self.assertEqual(expected, actual, msg="Expected {} but got {}".format(expected, actual))

