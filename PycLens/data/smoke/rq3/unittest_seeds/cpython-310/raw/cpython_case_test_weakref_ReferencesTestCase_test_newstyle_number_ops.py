# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_newstyle_number_ops

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class F(float):
        pass
    f = F(2.0)
    p = weakref.proxy(f)
    self.assertEqual(p + 1.0, 3.0)
    self.assertEqual(1.0 + p, 3.0)
