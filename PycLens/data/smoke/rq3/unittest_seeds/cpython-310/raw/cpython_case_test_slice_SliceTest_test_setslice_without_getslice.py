# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_slice.py
# case: SliceTest_test_setslice_without_getslice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tmp = []

    class X(object):

        def __setitem__(self, i, k):
            tmp.append((i, k))
    x = X()
    x[1:2] = 42
    self.assertEqual(tmp, [(slice(1, 2), 42)])
