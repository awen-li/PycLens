# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_if_conditional

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test_fstring(x, expected):
        flag = 0
        if f'{x}':
            flag = 1
        else:
            flag = 2
        self.assertEqual(flag, expected)

    def test_concat_empty(x, expected):
        flag = 0
        if f'{x}':
            flag = 1
        else:
            flag = 2
        self.assertEqual(flag, expected)

    def test_concat_non_empty(x, expected):
        flag = 0
        if f' {x}':
            flag = 1
        else:
            flag = 2
        self.assertEqual(flag, expected)
    test_fstring('', 2)
    test_fstring(' ', 1)
    test_concat_empty('', 2)
    test_concat_empty(' ', 1)
    test_concat_non_empty('', 1)
    test_concat_non_empty(' ', 1)
