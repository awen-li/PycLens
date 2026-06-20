# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: ExtendedReadTest_test_read1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    resp = self.resp

    def r():
        res = resp.read1(4)
        self.assertLessEqual(len(res), 4)
        return res
    readliner = Readliner(r)
    self._verify_readline(readliner.readline, self.lines_expected)
