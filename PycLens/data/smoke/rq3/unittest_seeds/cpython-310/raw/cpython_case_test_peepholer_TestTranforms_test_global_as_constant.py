# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_peepholer.py
# case: TestTranforms_test_global_as_constant

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        x = None
        x = None
        return x

    def g():
        x = True
        return x

    def h():
        x = False
        return x
    for (func, elem) in ((f, None), (g, True), (h, False)):
        self.assertNotInBytecode(func, 'LOAD_GLOBAL')
        self.assertInBytecode(func, 'LOAD_CONST', elem)
        self.check_lnotab(func)

    def f():
        """Adding a docstring made this test fail in Py2.5.0"""
        return None
    self.assertNotInBytecode(f, 'LOAD_GLOBAL')
    self.assertInBytecode(f, 'LOAD_CONST', None)
    self.check_lnotab(f)
