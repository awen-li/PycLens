# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: CTextIOWrapperTest_test_rwpair_cleared_before_textio

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in range(1000):
        b1 = self.BufferedRWPair(self.MockRawIO(), self.MockRawIO())
        t1 = self.TextIOWrapper(b1, encoding='ascii')
        b2 = self.BufferedRWPair(self.MockRawIO(), self.MockRawIO())
        t2 = self.TextIOWrapper(b2, encoding='ascii')
        t1.buddy = t2
        t2.buddy = t1
    support.gc_collect()
