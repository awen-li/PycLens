# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SizeofTest_test_pythontypes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    size = test.support.calcobjsize
    vsize = test.support.calcvobjsize
    check = self.check_sizeof
    import _ast
    check(_ast.AST(), size('P'))
    try:
        raise TypeError
    except TypeError:
        tb = sys.exc_info()[2]
        if tb is not None:
            check(tb, size('2P2i'))
    check(sys.flags, vsize('') + self.P * len(sys.flags))
