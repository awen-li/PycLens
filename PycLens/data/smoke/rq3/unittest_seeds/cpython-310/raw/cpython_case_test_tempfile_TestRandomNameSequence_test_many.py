# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestRandomNameSequence_test_many

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dict = {}
    r = self.r
    for i in range(TEST_FILES):
        s = next(r)
        self.nameCheck(s, '', '', '')
        self.assertNotIn(s, dict)
        dict[s] = 1
