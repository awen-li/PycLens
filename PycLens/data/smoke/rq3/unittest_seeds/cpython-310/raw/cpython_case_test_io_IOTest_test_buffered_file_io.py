# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_buffered_file_io

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.open(os_helper.TESTFN, 'wb') as f:
        self.assertEqual(f.readable(), False)
        self.assertEqual(f.writable(), True)
        self.assertEqual(f.seekable(), True)
        self.write_ops(f)
    with self.open(os_helper.TESTFN, 'rb') as f:
        self.assertEqual(f.readable(), True)
        self.assertEqual(f.writable(), False)
        self.assertEqual(f.seekable(), True)
        self.read_ops(f, True)
