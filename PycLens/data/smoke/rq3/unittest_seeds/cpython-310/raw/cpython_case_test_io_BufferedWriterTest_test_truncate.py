# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedWriterTest_test_truncate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    with self.open(os_helper.TESTFN, self.write_mode, buffering=0) as raw:
        bufio = self.tp(raw, 8)
        bufio.write(b'abcdef')
        self.assertEqual(bufio.truncate(3), 3)
        self.assertEqual(bufio.tell(), 6)
    with self.open(os_helper.TESTFN, 'rb', buffering=0) as f:
        self.assertEqual(f.read(), b'abc')
