# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRandomTest_test_write_after_readahead

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for overwrite_size in [1, 5]:
        raw = self.BytesIO(b'A' * 10)
        bufio = self.tp(raw, 4)
        self.assertEqual(bufio.read(1), b'A')
        self.assertEqual(bufio.tell(), 1)
        bufio.write(b'B' * overwrite_size)
        self.assertEqual(bufio.tell(), overwrite_size + 1)
        bufio.flush()
        self.assertEqual(bufio.tell(), overwrite_size + 1)
        s = raw.getvalue()
        self.assertEqual(s, b'A' + b'B' * overwrite_size + b'A' * (9 - overwrite_size))
