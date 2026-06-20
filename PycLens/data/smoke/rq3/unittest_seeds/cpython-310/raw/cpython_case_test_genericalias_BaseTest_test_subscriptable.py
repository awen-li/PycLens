# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericalias.py
# case: BaseTest_test_subscriptable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for t in self.generic_types:
        if t is None:
            continue
        tname = t.__name__
        with self.subTest(f'Testing {tname}'):
            alias = t[int]
            self.assertIs(alias.__origin__, t)
            self.assertEqual(alias.__args__, (int,))
            self.assertEqual(alias.__parameters__, ())
