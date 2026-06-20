# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_univnewlines.py
# case: TestGenericUnivNewlines_test_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.open(os_helper.TESTFN, self.READMODE) as fp:
        data = fp.read()
    self.assertEqual(data, DATA_LF)
    self.assertEqual(repr(fp.newlines), repr(self.NEWLINE))
