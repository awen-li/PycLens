# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_univnewlines.py
# case: TestCRLFNewlines_test_tell

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.open(os_helper.TESTFN, self.READMODE) as fp:
        self.assertEqual(repr(fp.newlines), repr(None))
        data = fp.readline()
        pos = fp.tell()
    self.assertEqual(repr(fp.newlines), repr(self.NEWLINE))
