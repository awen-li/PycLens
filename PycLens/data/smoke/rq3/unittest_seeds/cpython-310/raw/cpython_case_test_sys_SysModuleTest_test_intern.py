# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_intern

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    global INTERN_NUMRUNS
    INTERN_NUMRUNS += 1
    self.assertRaises(TypeError, sys.intern)
    s = 'never interned before' + str(INTERN_NUMRUNS)
    self.assertTrue(sys.intern(s) is s)
    s2 = s.swapcase().swapcase()
    self.assertTrue(sys.intern(s2) is s)

    class S(str):

        def __hash__(self):
            return 123
    self.assertRaises(TypeError, sys.intern, S('abc'))
