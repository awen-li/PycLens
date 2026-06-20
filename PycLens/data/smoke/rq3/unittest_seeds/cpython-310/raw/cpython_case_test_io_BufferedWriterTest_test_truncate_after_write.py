# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedWriterTest_test_truncate_after_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    with self.open(os_helper.TESTFN, 'wb') as f:
        f.write(b'\x00' * 10000)
    buffer_sizes = [8192, 4096, 200]
    for buffer_size in buffer_sizes:
        with self.open(os_helper.TESTFN, 'r+b', buffering=buffer_size) as f:
            f.write(b'\x00' * (buffer_size + 1))
            f.read(1)
            f.truncate()
            self.assertEqual(f.tell(), buffer_size + 2)
