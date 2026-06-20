# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hmac.py
# case: TestVectorsTestCase_test_sha_vectors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def shatest(key, data, digest):
        self.assert_hmac(key, data, digest, hashfunc=hashlib.sha1, hashname='sha1', digest_size=20, block_size=64)
    shatest(b'\x0b' * 20, b'Hi There', 'b617318655057264e28bc0b6fb378c8ef146be00')
    shatest(b'Jefe', b'what do ya want for nothing?', 'effcdf6ae5eb2fa2d27416d5f184df9c259a7c79')
    shatest(b'\xaa' * 20, b'\xdd' * 50, '125d7342b9ac11cd91a39af48aa17b4f63f175d3')
    shatest(bytes(range(1, 26)), b'\xcd' * 50, '4c9007f4026250c6bc8414f9bf50c86c2d7235da')
    shatest(b'\x0c' * 20, b'Test With Truncation', '4c1a03424b55e07fe7f27be1d58bb9324a9a5a04')
    shatest(b'\xaa' * 80, b'Test Using Larger Than Block-Size Key - Hash Key First', 'aa4ae5e15272d00e95705637ce8a3b55ed402112')
    shatest(b'\xaa' * 80, b'Test Using Larger Than Block-Size Key and Larger Than One Block-Size Data', 'e8e99d0f45237d786d6bbaa7965c7808bbff1a91')
