# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_int.py
# case: IntTestCases_test_int_subclass_with_index

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyIndex(int):

        def __index__(self):
            return 42

    class BadIndex(int):

        def __index__(self):
            return 42.0
    my_int = MyIndex(7)
    self.assertEqual(my_int, 7)
    self.assertEqual(int(my_int), 7)
    self.assertEqual(int(BadIndex()), 0)
