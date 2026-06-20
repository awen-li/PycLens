# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_getstate_exc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class EvilState(object):

        def __getstate__(self):
            raise ValueError("ain't got no stickin' state")
    self.assertRaises(ValueError, copy.copy, EvilState())
