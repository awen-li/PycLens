# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_closefd_attr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.open(os_helper.TESTFN, 'wb') as f:
        f.write(b'egg\n')
    with self.open(os_helper.TESTFN, 'r', encoding='utf-8') as f:
        self.assertEqual(f.buffer.raw.closefd, True)
        file = self.open(f.fileno(), 'r', encoding='utf-8', closefd=False)
        self.assertEqual(file.buffer.raw.closefd, False)
