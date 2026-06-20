# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_super.py
# case: TestSuper_test_cell_as_self

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:

        def meth(self):
            super()

    def f():
        k = X()

        def g():
            return k
        return g
    c = f().__closure__[0]
    self.assertRaises(TypeError, X.meth, c)
