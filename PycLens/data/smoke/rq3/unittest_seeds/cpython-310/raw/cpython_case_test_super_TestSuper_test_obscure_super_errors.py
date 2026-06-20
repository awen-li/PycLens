# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_super.py
# case: TestSuper_test_obscure_super_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        super()
    self.assertRaises(RuntimeError, f)

    def f(x):
        del x
        super()
    self.assertRaises(RuntimeError, f, None)

    class X:

        def f(x):
            nonlocal __class__
            del __class__
            super()
    self.assertRaises(RuntimeError, X().f)
