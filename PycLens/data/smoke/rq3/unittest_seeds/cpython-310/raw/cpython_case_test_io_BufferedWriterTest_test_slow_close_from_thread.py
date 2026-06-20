# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedWriterTest_test_slow_close_from_thread

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rawio = self.SlowFlushRawIO()
    bufio = self.tp(rawio, 8)
    t = threading.Thread(target=bufio.close)
    t.start()
    rawio.in_flush.wait()
    self.assertRaises(ValueError, bufio.write, b'spam')
    self.assertTrue(bufio.closed)
    t.join()
