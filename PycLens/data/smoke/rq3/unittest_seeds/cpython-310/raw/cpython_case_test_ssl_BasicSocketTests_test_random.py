# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_random

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    v = ssl.RAND_status()
    if support.verbose:
        sys.stdout.write('\n RAND_status is %d (%s)\n' % (v, v and 'sufficient randomness' or 'insufficient randomness'))
    with warnings_helper.check_warnings():
        (data, is_cryptographic) = ssl.RAND_pseudo_bytes(16)
    self.assertEqual(len(data), 16)
    self.assertEqual(is_cryptographic, v == 1)
    if v:
        data = ssl.RAND_bytes(16)
        self.assertEqual(len(data), 16)
    else:
        self.assertRaises(ssl.SSLError, ssl.RAND_bytes, 16)
    self.assertRaises(ValueError, ssl.RAND_bytes, -5)
    with warnings_helper.check_warnings():
        self.assertRaises(ValueError, ssl.RAND_pseudo_bytes, -5)
    ssl.RAND_add('this is a random string', 75.0)
    ssl.RAND_add(b'this is a random bytes object', 75.0)
    ssl.RAND_add(bytearray(b'this is a random bytearray object'), 75.0)
