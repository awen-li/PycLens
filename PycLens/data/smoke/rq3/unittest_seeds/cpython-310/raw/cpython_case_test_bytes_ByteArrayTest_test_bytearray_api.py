# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_bytearray_api

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    short_sample = b'Hello world\n'
    sample = short_sample + b'\x00' * (20 - len(short_sample))
    tfn = tempfile.mktemp()
    try:
        with open(tfn, 'wb') as f:
            f.write(short_sample)
        with open(tfn, 'rb') as f:
            b = bytearray(20)
            n = f.readinto(b)
        self.assertEqual(n, len(short_sample))
        self.assertEqual(list(b), list(sample))
        with open(tfn, 'wb') as f:
            f.write(b)
        with open(tfn, 'rb') as f:
            self.assertEqual(f.read(), sample)
    finally:
        try:
            os.remove(tfn)
        except OSError:
            pass
