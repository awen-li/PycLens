# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: AbstractWriterTests_test_write_after_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = b'content'
    with zipfile.ZipFile(TESTFN2, 'w', self.compression) as zipf:
        w = zipf.open('test', 'w')
        w.write(data)
        w.close()
        self.assertTrue(w.closed)
        self.assertRaises(ValueError, w.write, b'')
        self.assertEqual(zipf.read('test'), data)
