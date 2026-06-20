# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_clear_unconsumed_tail

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cdata = b'x\x9cKLJ\x06\x00\x02M\x01'
    dco = zlib.decompressobj()
    ddata = dco.decompress(cdata, 1)
    ddata += dco.decompress(dco.unconsumed_tail)
    self.assertEqual(dco.unconsumed_tail, b'')
