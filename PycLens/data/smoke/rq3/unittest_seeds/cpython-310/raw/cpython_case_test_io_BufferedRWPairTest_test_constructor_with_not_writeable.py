# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRWPairTest_test_constructor_with_not_writeable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class NotWriteable(MockRawIO):

        def writable(self):
            return False
    self.assertRaises(OSError, self.tp, self.MockRawIO(), NotWriteable())
