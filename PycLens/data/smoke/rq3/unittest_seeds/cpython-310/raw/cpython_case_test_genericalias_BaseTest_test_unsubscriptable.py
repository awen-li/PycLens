# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericalias.py
# case: BaseTest_test_unsubscriptable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for t in (int, str, float, Sized, Hashable):
        tname = t.__name__
        with self.subTest(f'Testing {tname}'):
            with self.assertRaises(TypeError):
                t[int]
