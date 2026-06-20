# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_decompress_raw_with_dictionary

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zdict = b'abcdefghijklmnopqrstuvwxyz'
    co = zlib.compressobj(wbits=-zlib.MAX_WBITS, zdict=zdict)
    comp = co.compress(zdict) + co.flush()
    dco = zlib.decompressobj(wbits=-zlib.MAX_WBITS, zdict=zdict)
    uncomp = dco.decompress(comp) + dco.flush()
    self.assertEqual(zdict, uncomp)
