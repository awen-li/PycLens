# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRandomTest_test_interleaved_read_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.BytesIO(b'abcdefgh') as raw:
        with self.tp(raw, 100) as f:
            f.write(b'1')
            self.assertEqual(f.read(1), b'b')
            f.write(b'2')
            self.assertEqual(f.read1(1), b'd')
            f.write(b'3')
            buf = bytearray(1)
            f.readinto(buf)
            self.assertEqual(buf, b'f')
            f.write(b'4')
            self.assertEqual(f.peek(1), b'h')
            f.flush()
            self.assertEqual(raw.getvalue(), b'1b2d3f4h')
    with self.BytesIO(b'abc') as raw:
        with self.tp(raw, 100) as f:
            self.assertEqual(f.read(1), b'a')
            f.write(b'2')
            self.assertEqual(f.read(1), b'c')
            f.flush()
            self.assertEqual(raw.getvalue(), b'a2c')
