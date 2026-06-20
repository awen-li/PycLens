# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestsWithMultipleOpens_test_write_while_reading

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with zipfile.ZipFile(TESTFN2, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.writestr('ones', self.data1)
    with zipfile.ZipFile(TESTFN2, 'a', zipfile.ZIP_DEFLATED) as zipf:
        with zipf.open('ones', 'r') as r1:
            data1 = r1.read(500)
            with zipf.open('twos', 'w') as w1:
                w1.write(self.data2)
            data1 += r1.read()
    self.assertEqual(data1, self.data1)
    with zipfile.ZipFile(TESTFN2) as zipf:
        self.assertEqual(zipf.read('twos'), self.data2)
