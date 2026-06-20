# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_peepholer.py
# case: TestTranforms_test_make_function_doesnt_bail

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():

        def g() -> 1 + 1:
            pass
        return g
    self.assertNotInBytecode(f, 'BINARY_ADD')
    self.check_lnotab(f)
