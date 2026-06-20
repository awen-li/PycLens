# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: KDFTests_test_scrypt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (password, salt, n, r, p, expected) in self.scrypt_test_vectors:
        result = hashlib.scrypt(password, salt=salt, n=n, r=r, p=p)
        self.assertEqual(result, expected)
    hashlib.scrypt(b'password', salt=b'salt', n=2, r=8, p=1)
    with self.assertRaises(TypeError):
        hashlib.scrypt('password', salt=b'salt', n=2, r=8, p=1)
    with self.assertRaises(TypeError):
        hashlib.scrypt(b'password', salt='salt', n=2, r=8, p=1)
    with self.assertRaises(TypeError):
        hashlib.scrypt(b'password')
    with self.assertRaises(TypeError):
        hashlib.scrypt(b'password', b'salt')
    with self.assertRaises(TypeError):
        hashlib.scrypt(b'password', 2, 8, 1, salt=b'salt')
    for n in [-1, 0, 1, None]:
        with self.assertRaises((ValueError, OverflowError, TypeError)):
            hashlib.scrypt(b'password', salt=b'salt', n=n, r=8, p=1)
    for r in [-1, 0, None]:
        with self.assertRaises((ValueError, OverflowError, TypeError)):
            hashlib.scrypt(b'password', salt=b'salt', n=2, r=r, p=1)
    for p in [-1, 0, None]:
        with self.assertRaises((ValueError, OverflowError, TypeError)):
            hashlib.scrypt(b'password', salt=b'salt', n=2, r=8, p=p)
    for maxmem in [-1, None]:
        with self.assertRaises((ValueError, OverflowError, TypeError)):
            hashlib.scrypt(b'password', salt=b'salt', n=2, r=8, p=1, maxmem=maxmem)
    for dklen in [-1, None]:
        with self.assertRaises((ValueError, OverflowError, TypeError)):
            hashlib.scrypt(b'password', salt=b'salt', n=2, r=8, p=1, dklen=dklen)
