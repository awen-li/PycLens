# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: DisTests_test_bug_1333982

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if not __debug__:
        self.skipTest('need asserts, run without -O')
    self.do_disassembly_test(bug1333982, dis_bug1333982)
