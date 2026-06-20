# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_int.py
# case: IntTestCases_test_int_base_indexable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyIndexable(object):

        def __init__(self, value):
            self.value = value

        def __index__(self):
            return self.value
    for base in (2 ** 100, -2 ** 100, 1, 37):
        with self.assertRaises(ValueError):
            int('43', base)
    self.assertEqual(int('101', base=MyIndexable(2)), 5)
    self.assertEqual(int('101', base=MyIndexable(10)), 101)
    self.assertEqual(int('101', base=MyIndexable(36)), 1 + 36 ** 2)
