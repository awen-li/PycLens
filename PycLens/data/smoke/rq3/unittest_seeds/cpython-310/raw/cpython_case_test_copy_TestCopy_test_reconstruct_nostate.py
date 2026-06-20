# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_reconstruct_nostate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):

        def __reduce__(self):
            return (C, ())
    x = C()
    x.foo = 42
    y = copy.copy(x)
    self.assertIs(y.__class__, x.__class__)
    y = copy.deepcopy(x)
    self.assertIs(y.__class__, x.__class__)
