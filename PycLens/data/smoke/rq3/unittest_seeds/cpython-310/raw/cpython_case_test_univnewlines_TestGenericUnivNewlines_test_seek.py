# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_univnewlines.py
# case: TestGenericUnivNewlines_test_seek

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.open(os_helper.TESTFN, self.READMODE) as fp:
        fp.readline()
        pos = fp.tell()
        data = fp.readlines()
        self.assertEqual(data, DATA_SPLIT[1:])
        fp.seek(pos)
        data = fp.readlines()
    self.assertEqual(data, DATA_SPLIT[1:])
