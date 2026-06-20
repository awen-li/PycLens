# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hmac.py
# case: TestVectorsTestCase_test_md5_vectors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def md5test(key, data, digest):
        self.assert_hmac(key, data, digest, hashfunc=hashlib.md5, hashname='md5', digest_size=16, block_size=64)
    md5test(b'\x0b' * 16, b'Hi There', '9294727A3638BB1C13F48EF8158BFC9D')
    md5test(b'Jefe', b'what do ya want for nothing?', '750c783e6ab0b503eaa86e310a5db738')
    md5test(b'\xaa' * 16, b'\xdd' * 50, '56be34521d144c88dbb8c733f0e8b3f6')
    md5test(bytes(range(1, 26)), b'\xcd' * 50, '697eaf0aca3a3aea3a75164746ffaa79')
    md5test(b'\x0c' * 16, b'Test With Truncation', '56461ef2342edc00f9bab995690efd4c')
    md5test(b'\xaa' * 80, b'Test Using Larger Than Block-Size Key - Hash Key First', '6b1ab7fe4bd7bf8f0b62e6ce61b9d0cd')
    md5test(b'\xaa' * 80, b'Test Using Larger Than Block-Size Key and Larger Than One Block-Size Data', '6f630fad67cda0ee1fb1f562db3aa53e')
