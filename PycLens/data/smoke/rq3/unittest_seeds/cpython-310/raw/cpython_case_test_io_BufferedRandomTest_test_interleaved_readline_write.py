# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRandomTest_test_interleaved_readline_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.BytesIO(b'ab\ncdef\ng\n') as raw:
        with self.tp(raw) as f:
            f.write(b'1')
            self.assertEqual(f.readline(), b'b\n')
            f.write(b'2')
            self.assertEqual(f.readline(), b'def\n')
            f.write(b'3')
            self.assertEqual(f.readline(), b'\n')
            f.flush()
            self.assertEqual(raw.getvalue(), b'1b\n2def\n3\n')
