# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_read_closed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.open(os_helper.TESTFN, 'w', encoding='utf-8') as f:
        f.write('egg\n')
    with self.open(os_helper.TESTFN, 'r', encoding='utf-8') as f:
        file = self.open(f.fileno(), 'r', encoding='utf-8', closefd=False)
        self.assertEqual(file.read(), 'egg\n')
        file.seek(0)
        file.close()
        self.assertRaises(ValueError, file.read)
    with self.open(os_helper.TESTFN, 'rb') as f:
        file = self.open(f.fileno(), 'rb', closefd=False)
        self.assertEqual(file.read()[:3], b'egg')
        file.close()
        self.assertRaises(ValueError, file.readinto, bytearray(1))
