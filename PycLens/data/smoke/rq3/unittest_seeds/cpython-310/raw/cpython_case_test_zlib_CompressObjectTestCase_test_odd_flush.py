# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_odd_flush

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import random
    co = zlib.compressobj(zlib.Z_BEST_COMPRESSION)
    dco = zlib.decompressobj()
    try:
        gen = random.WichmannHill()
    except AttributeError:
        try:
            gen = random.Random()
        except AttributeError:
            gen = random
    gen.seed(1)
    data = gen.randbytes(17 * 1024)
    first = co.compress(data)
    second = co.flush(zlib.Z_SYNC_FLUSH)
    expanded = dco.decompress(first + second)
    self.assertEqual(expanded, data, "17K random source doesn't match")
