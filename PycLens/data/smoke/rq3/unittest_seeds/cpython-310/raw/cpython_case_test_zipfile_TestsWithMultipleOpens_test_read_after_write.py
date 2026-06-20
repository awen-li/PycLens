# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestsWithMultipleOpens_test_read_after_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for f in get_files(self):
        with zipfile.ZipFile(f, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.writestr('ones', self.data1)
            zipf.writestr('twos', self.data2)
            with zipf.open('ones') as zopen1:
                data1 = zopen1.read(500)
        self.assertEqual(data1, self.data1[:500])
        with zipfile.ZipFile(f, 'r') as zipf:
            data1 = zipf.read('ones')
            data2 = zipf.read('twos')
        self.assertEqual(data1, self.data1)
        self.assertEqual(data2, self.data2)
