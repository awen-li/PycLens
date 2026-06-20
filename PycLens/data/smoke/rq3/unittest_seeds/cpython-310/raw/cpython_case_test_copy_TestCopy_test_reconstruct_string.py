# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_reconstruct_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):

        def __reduce__(self):
            return ''
    x = C()
    y = copy.copy(x)
    self.assertIs(y, x)
    y = copy.deepcopy(x)
    self.assertIs(y, x)
