# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_flush_with_freed_input

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    input1 = b'abcdefghijklmnopqrstuvwxyz'
    input2 = b'QWERTYUIOPASDFGHJKLZXCVBNM'
    data = zlib.compress(input1)
    dco = zlib.decompressobj()
    dco.decompress(data, 1)
    del data
    data = zlib.compress(input2)
    self.assertEqual(dco.flush(), input1[1:])
