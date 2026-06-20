# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_plistlib.py
# case: TestBinaryPlistlib_test_deep_nesting

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for N in [300, 100000]:
        chunks = [b'\xa1' + (i + 1).to_bytes(4, 'big') for i in range(N)]
        try:
            result = self.decode(*chunks, b'Tseed', offset_size=4, ref_size=4)
        except RecursionError:
            pass
        else:
            for i in range(N):
                self.assertIsInstance(result, list)
                self.assertEqual(len(result), 1)
                result = result[0]
            self.assertEqual(result, 'seed')
