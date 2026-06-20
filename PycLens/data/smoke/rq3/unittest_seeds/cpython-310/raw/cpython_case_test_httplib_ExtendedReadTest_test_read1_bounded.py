# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: ExtendedReadTest_test_read1_bounded

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    resp = self.resp
    all = []
    while True:
        data = resp.read1(10)
        if not data:
            break
        self.assertLessEqual(len(data), 10)
        all.append(data)
    self.assertEqual(b''.join(all), self.lines_expected)
