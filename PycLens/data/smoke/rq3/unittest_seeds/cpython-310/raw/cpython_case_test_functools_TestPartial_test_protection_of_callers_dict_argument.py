# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestPartial_test_protection_of_callers_dict_argument

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func(a=10, b=20):
        return a
    d = {'a': 3}
    p = self.partial(func, a=5)
    self.assertEqual(p(**d), 3)
    self.assertEqual(d, {'a': 3})
    p(b=7)
    self.assertEqual(d, {'a': 3})
