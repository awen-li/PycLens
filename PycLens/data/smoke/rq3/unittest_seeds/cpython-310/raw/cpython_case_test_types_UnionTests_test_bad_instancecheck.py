# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: UnionTests_test_bad_instancecheck

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BadMeta(type):

        def __instancecheck__(cls, inst):
            1 / 0
    x = int | BadMeta('A', (), {})
    self.assertTrue(isinstance(1, x))
    self.assertRaises(ZeroDivisionError, isinstance, [], x)
